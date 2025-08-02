#!/usr/bin/env python3
"""
Asynchronous Link Checker for Markdown Files
High-performance link validation with rich reporting
"""

import argparse
import asyncio
import logging
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import aiohttp
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AsyncLinkChecker:
    """High-performance asynchronous link checker"""

    def __init__(self, timeout: int = 10, max_concurrent: int = 50):
        """Initialize the link checker"""
        self.timeout = timeout
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.console = Console()
        self.session = None
        self.results = {
            'total_files': 0,
            'total_links': 0,
            'broken_links': [],
            'valid_links': 0,
            'errors': []
        }

    async def create_session(self) -> aiohttp.ClientSession:
        """Create an aiohttp session with proper configuration"""
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Linux; Link Checker) '
                'AppleWebKit/537.36 Chrome/91.0.4472.124'
            )
        }
        return aiohttp.ClientSession(
            timeout=timeout,
            headers=headers,
            connector=aiohttp.TCPConnector(limit=100)
        )

    async def read_file(self, file_path: Path) -> str:
        """Read file content asynchronously"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            error_msg = f"Error reading {file_path}: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            return ""

    def extract_links_from_content(self, content: str,
                                   file_path: Path) -> List[Dict]:
        """Extract all links from markdown content"""
        links = []

        # Markdown link pattern: [text](url)
        markdown_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(markdown_pattern, content):
            text, url = match.groups()
            links.append({
                'text': text.strip(),
                'url': url.strip(),
                'type': 'markdown',
                'file': file_path,
                'line': content[:match.start()].count('\n') + 1
            })

        # Reference link pattern: [text][ref]
        ref_pattern = r'\[([^\]]*)\]\[([^\]]+)\]'
        ref_definitions = {}

        # Extract reference definitions: [ref]: url
        ref_def_pattern = r'^\s*\[([^\]]+)\]:\s*(.+)$'
        for line_num, line in enumerate(content.split('\n'), 1):
            match = re.match(ref_def_pattern, line)
            if match:
                ref_id, url = match.groups()
                ref_definitions[ref_id.strip()] = url.strip()

        # Find reference links
        for match in re.finditer(ref_pattern, content):
            text, ref_id = match.groups()
            if ref_id in ref_definitions:
                links.append({
                    'text': text.strip(),
                    'url': ref_definitions[ref_id],
                    'type': 'reference',
                    'file': file_path,
                    'line': content[:match.start()].count('\n') + 1
                })

        # HTML anchor pattern: <a href="url">
        html_pattern = r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>'
        for match in re.finditer(html_pattern, content, re.IGNORECASE):
            url = match.group(1)
            links.append({
                'text': 'HTML link',
                'url': url.strip(),
                'type': 'html',
                'file': file_path,
                'line': content[:match.start()].count('\n') + 1
            })

        return links

    def is_valid_url(self, url: str) -> bool:
        """Check if URL format is valid"""
        if not url or url.startswith('#'):
            return False
        if url.startswith(('http://', 'https://')):
            return True
        if url.startswith(('mailto:', 'ftp:', 'ftps:')):
            return False  # Skip these for HTTP checking
        return False

    async def check_url(self, url: str) -> Tuple[str, int, str]:
        """Check a single URL and return status"""
        async with self.semaphore:
            try:
                if not self.session:
                    self.session = await self.create_session()

                async with self.session.get(url) as response:
                    return url, response.status, str(response.reason)

            except asyncio.TimeoutError:
                return url, 408, "Request Timeout"
            except aiohttp.ClientError as e:
                return url, 0, f"Client Error: {str(e)}"
            except Exception as e:
                return url, 0, f"Unknown Error: {str(e)}"

    def validate_link(self, link: Dict, file_path: Path):
        """Validate a link and categorize it"""
        url = link['url']

        # Skip certain URL types
        if url.startswith('#'):
            # Fragment links - would need local validation
            return
        elif url.startswith('mailto:'):
            # Email links - skip validation
            return
        elif url.startswith(('http://', 'https://')):
            # HTTP links - add to validation queue
            return link
        else:
            # Relative or other links - could add file existence check
            return

    async def check_file(self, file_path: Path,
                         progress: Progress,
                         task_id: TaskID) -> List[Dict]:
        """Check all links in a single file"""
        try:
            content = await self.read_file(file_path)
            if not content:
                return []

            links = self.extract_links_from_content(content, file_path)
            progress.update(task_id, advance=1)

            return [link for link in links
                    if self.validate_link(link, file_path)]

        except Exception as e:
            error_msg = f"Error processing {file_path}: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            return []

    async def check_all_files(self, directory: Path) -> Dict:
        """Check all markdown files in directory"""
        markdown_files = list(directory.rglob("*.md"))
        self.results['total_files'] = len(markdown_files)

        if not markdown_files:
            self.console.print("[yellow]No markdown files found[/yellow]")
            return self.results

        all_links = []

        with Progress() as progress:
            task_id = progress.add_task(
                "[green]Processing files...",
                total=len(markdown_files)
            )

            # Process files concurrently
            tasks = [
                self.check_file(file_path, progress, task_id)
                for file_path in markdown_files
            ]

            file_results = await asyncio.gather(*tasks)
            for links in file_results:
                all_links.extend(links)

        # Filter HTTP/HTTPS links for validation
        http_links = [
            link for link in all_links
            if link and link['url'].startswith(('http://', 'https://'))
        ]

        self.results['total_links'] = len(all_links)

        if not http_links:
            self.console.print("[yellow]No HTTP links found to validate[/yellow]")
            return self.results

        # Check HTTP links
        await self.check_http_links(http_links)

        return self.results

    async def check_http_links(self, links: List[Dict]):
        """Check HTTP/HTTPS links concurrently"""
        unique_urls = list(set(link['url'] for link in links))

        with Progress() as progress:
            task_id = progress.add_task(
                "[blue]Checking links...",
                total=len(unique_urls)
            )

            # Check URLs concurrently
            check_tasks = [self.check_url(url) for url in unique_urls]
            url_results = await asyncio.gather(*check_tasks)

            # Create URL status mapping
            url_status = {url: (status, reason)
                          for url, status, reason in url_results}

            # Process results
            for link in links:
                url = link['url']
                status, reason = url_status.get(url, (0, "Unknown"))

                if 200 <= status < 400:
                    self.results['valid_links'] += 1
                else:
                    self.results['broken_links'].append({
                        'file': str(link['file']),
                        'line': link['line'],
                        'url': url,
                        'text': link['text'],
                        'status': status,
                        'reason': reason
                    })

                progress.update(task_id, advance=1)

    def display_results(self):
        """Display validation results in a formatted table"""
        self.console.print(f"\n[bold]Link Validation Results[/bold]")
        self.console.print(f"Files processed: {self.results['total_files']}")
        self.console.print(f"Total links found: {self.results['total_links']}")
        self.console.print(f"Valid links: {self.results['valid_links']}")
        self.console.print(f"Broken links: {len(self.results['broken_links'])}")

        if self.results['broken_links']:
            self.console.print("\n[red]Broken Links:[/red]")
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("File", style="cyan", no_wrap=True)
            table.add_column("Line", justify="right", style="green")
            table.add_column("URL", style="yellow")
            table.add_column("Status", justify="center")
            table.add_column("Error", style="red")

            for broken in self.results['broken_links']:
                table.add_row(
                    str(broken['file']),
                    str(broken['line']),
                    broken['url'][:50] + "..." if len(broken['url']) > 50
                    else broken['url'],
                    str(broken['status']),
                    broken['reason'][:30] + "..." if len(broken['reason']) > 30
                    else broken['reason']
                )

            self.console.print(table)

        if self.results['errors']:
            self.console.print(f"\n[red]Errors: {len(self.results['errors'])}")
            for error in self.results['errors']:
                self.console.print(f"  • {error}")

    async def close(self):
        """Clean up resources"""
        if self.session:
            await self.session.close()


async def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Check links in markdown files"
    )
    parser.add_argument(
        "directory",
        type=Path,
        nargs="?",
        default=Path("."),
        help="Directory to scan for markdown files"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Request timeout in seconds"
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=50,
        help="Maximum concurrent requests"
    )

    args = parser.parse_args()

    if not args.directory.exists():
        print(f"Error: Directory {args.directory} does not exist")
        sys.exit(1)

    checker = AsyncLinkChecker(
        timeout=args.timeout,
        max_concurrent=args.max_concurrent
    )

    try:
        results = await checker.check_all_files(args.directory)
        checker.display_results()

        # Exit with error code if broken links found
        if results['broken_links']:
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        await checker.close()


if __name__ == "__main__":
    asyncio.run(main())
