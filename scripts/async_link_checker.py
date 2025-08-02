#!/usr/bin/env python3
"""
Asynchronous Link Checker for Markdown Files
High-performance link validation with rich reporting
"""

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse

import aiohttp
from rich.console import Console
from rich.progress import Progress, TaskID, track
from rich.table import Table

# Configure rich console
console = Console()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AsyncLinkChecker:
    """High-performance async link checker"""

    def __init__(self,
                 timeout: int = 10,
                 max_concurrent: int = 50,
                 max_retries: int = 3):
        self.timeout = timeout
        self.max_concurrent = max_concurrent
        self.max_retries = max_retries
        self.session: aiohttp.ClientSession = None
        self.semaphore = asyncio.Semaphore(max_concurrent)

        # Results tracking
        self.results = {
            'valid_links': [],
            'broken_links': [],
            'warnings': [],
            'skipped': []
        }

    async def __aenter__(self):
        """Async context manager entry"""
        connector = aiohttp.TCPConnector(
            limit=self.max_concurrent,
            limit_per_host=10,
            ttl_dns_cache=300,
            use_dns_cache=True
        )

        timeout = aiohttp.ClientTimeout(total=self.timeout)

        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers={
                'User-Agent': 'Mozilla/5.0 (Claude Prompts Link Checker)'
            }
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()

    async def extract_links_from_file(self, file_path: Path) -> List[Dict]:
        """Extract all links from a markdown file"""
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()

            return self.extract_links_from_content(content, file_path)

        except Exception as e:
            logger.error(f"Error reading {file_path}: {e}")
            return []

    def extract_links_from_content(self, content: str,
                                  file_path: Path) -> List[Dict]:
        """Extract links from markdown content"""
        links = []

        # Markdown links: [text](url)
        md_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(md_pattern, content):
            text, url = match.groups()
            links.append({
                'type': 'markdown',
                'text': text,
                'url': url.strip(),
                'line': content[:match.start()].count('\n') + 1,
                'file': str(file_path)
            })

        # HTML links: <a href="url">
        html_pattern = r'<a\s+href=["\']([^"\']+)["\'][^>]*>'
        for match in re.finditer(html_pattern, content, re.IGNORECASE):
            url = match.group(1)
            links.append({
                'type': 'html',
                'url': url.strip(),
                'line': content[:match.start()].count('\n') + 1,
                'file': str(file_path)
            })

        # Images: ![alt](src)
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(img_pattern, content):
            alt, src = match.groups()
            links.append({
                'type': 'image',
                'alt': alt,
                'url': src.strip(),
                'line': content[:match.start()].count('\n') + 1,
                'file': str(file_path)
            })

        return links

    def is_external_url(self, url: str) -> bool:
        """Check if URL is external"""
        parsed = urlparse(url)
        return bool(parsed.scheme and parsed.netloc)

    def is_valid_internal_path(self, url: str, base_path: Path) -> bool:
        """Check if internal path exists"""
        if url.startswith('#'):
            return True  # Fragment links are assumed valid

        # Handle relative paths
        if not url.startswith('/'):
            target_path = base_path.parent / url
        else:
            target_path = base_path.parent / url.lstrip('/')

        # Remove URL fragments and query parameters
        clean_path = str(target_path).split('#')[0].split('?')[0]
        return Path(clean_path).exists()

    async def check_external_url(self, url: str) -> Tuple[bool, str]:
        """Check if external URL is accessible"""
        async with self.semaphore:
            for attempt in range(self.max_retries):
                try:
                    async with self.session.head(url) as response:
                        if response.status < 400:
                            return True, f"OK ({response.status})"
                        elif response.status == 405:
                            # HEAD not allowed, try GET
                            async with self.session.get(url) as get_response:
                                if get_response.status < 400:
                                    return True, f"OK ({get_response.status})"
                                return False, f"HTTP {get_response.status}"
                        else:
                            return False, f"HTTP {response.status}"

                except asyncio.TimeoutError:
                    if attempt == self.max_retries - 1:
                        return False, "Timeout"
                    await asyncio.sleep(2 ** attempt)

                except Exception as e:
                    if attempt == self.max_retries - 1:
                        return False, f"Error: {str(e)[:50]}"
                    await asyncio.sleep(2 ** attempt)

        return False, "Max retries exceeded"

    async def validate_link(self, link: Dict, base_path: Path) -> Dict:
        """Validate a single link"""
        url = link['url']
        result = link.copy()

        # Skip certain URLs
        if any(skip in url.lower() for skip in [
            'mailto:', 'tel:', 'javascript:', 'data:', 'ftp:'
        ]):
            result['status'] = 'skipped'
            result['message'] = 'Skipped URL type'
            return result

        if self.is_external_url(url):
            is_valid, message = await self.check_external_url(url)
            result['status'] = 'valid' if is_valid else 'broken'
            result['message'] = message
        else:
            # Internal link
            if self.is_valid_internal_path(url, base_path):
                result['status'] = 'valid'
                result['message'] = 'Internal path exists'
            else:
                result['status'] = 'broken'
                result['message'] = 'Internal path not found'

        return result

    async def check_file(self, file_path: Path,
                        progress: Progress,
                        task_id: TaskID) -> List[Dict]:
        """Check all links in a file"""
        links = await self.extract_links_from_file(file_path)

        if not links:
            progress.advance(task_id, 1)
            return []

        # Validate all links concurrently
        tasks = [
            self.validate_link(link, file_path)
            for link in links
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        valid_results = []
        for result in results:
            if isinstance(result, Exception):
                logger.error(f"Error validating link: {result}")
            else:
                valid_results.append(result)

        progress.advance(task_id, 1)
        return valid_results

    async def check_directory(self, directory: Path) -> Dict:
        """Check all markdown files in directory"""
        md_files = list(directory.rglob("*.md"))

        if not md_files:
            console.print("[yellow]No markdown files found[/yellow]")
            return self.results

        console.print(f"Found {len(md_files)} markdown files to check")

        with Progress() as progress:
            task = progress.add_task(
                "[green]Checking links...",
                total=len(md_files)
            )

            # Process files concurrently
            tasks = [
                self.check_file(file_path, progress, task)
                for file_path in md_files
            ]

            all_results = await asyncio.gather(*tasks)

        # Aggregate results
        for file_results in all_results:
            for result in file_results:
                status = result.get('status', 'unknown')
                if status == 'valid':
                    self.results['valid_links'].append(result)
                elif status == 'broken':
                    self.results['broken_links'].append(result)
                elif status == 'skipped':
                    self.results['skipped'].append(result)
                else:
                    self.results['warnings'].append(result)

        return self.results

    def generate_report(self) -> None:
        """Generate a comprehensive report"""
        console.print("\n[bold green]Link Check Report[/bold green]")

        # Summary table
        summary_table = Table(title="Summary")
        summary_table.add_column("Status", style="bold")
        summary_table.add_column("Count", justify="right")

        summary_table.add_row("✅ Valid Links",
                             str(len(self.results['valid_links'])))
        summary_table.add_row("❌ Broken Links",
                             str(len(self.results['broken_links'])))
        summary_table.add_row("⚠️  Warnings",
                             str(len(self.results['warnings'])))
        summary_table.add_row("⏭️  Skipped",
                             str(len(self.results['skipped'])))

        console.print(summary_table)

        # Broken links details
        if self.results['broken_links']:
            console.print("\n[bold red]Broken Links:[/bold red]")
            broken_table = Table()
            broken_table.add_column("File", style="blue")
            broken_table.add_column("Line", justify="right")
            broken_table.add_column("URL", style="red")
            broken_table.add_column("Error", style="yellow")

            for link in self.results['broken_links']:
                broken_table.add_row(
                    Path(link['file']).name,
                    str(link['line']),
                    link['url'][:60] + "..." if len(link['url']) > 60 else link['url'],
                    link['message']
                )

            console.print(broken_table)


async def main():
    """Main async entry point"""
    parser = argparse.ArgumentParser(
        description="Modern async link checker for markdown files"
    )
    parser.add_argument("directory", nargs="?", default=".",
                       help="Directory to check (default: current)")
    parser.add_argument("--timeout", type=int, default=10,
                       help="Request timeout in seconds")
    parser.add_argument("--max-concurrent", type=int, default=50,
                       help="Maximum concurrent requests")
    parser.add_argument("--max-retries", type=int, default=3,
                       help="Maximum retries per URL")

    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.exists():
        console.print(f"[red]Directory not found: {directory}[/red]")
        sys.exit(1)

    console.print(f"[green]Starting link check in: {directory}[/green]")

    async with AsyncLinkChecker(
        timeout=args.timeout,
        max_concurrent=args.max_concurrent,
        max_retries=args.max_retries
    ) as checker:
        results = await checker.check_directory(directory)
        checker.generate_report()

        # Exit with error if broken links found
        if results['broken_links']:
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
