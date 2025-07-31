#!/usr/bin/env python3
"""
Comprehensive link checker for markdown files
Validates internal links, external URLs, and image references
"""

import argparse
import logging
import re
import sys
# from urllib.parse import urlparse  # Reserved for future use
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("requests not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class LinkChecker:
    """Comprehensive link validation for markdown files"""

    def __init__(self, timeout: int = 10, max_workers: int = 10):
        self.timeout = timeout
        self.max_workers = max_workers
        self.errors = []
        self.warnings = []
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Create a requests session with retry strategy"""
        session = requests.Session()

        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Set user agent
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Claude Prompts Link Checker)'
        })

        return session

    def extract_links(self, content: str, file_path: Path) -> dict:
        """Extract all links from markdown content"""
        links = {
            'markdown': [],  # [text](url)
            'html': [],      # <a href="url">
            'images': [],    # ![alt](src)
            'references': []  # [text][ref]
        }

        # Markdown links: [text](url)
        md_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(md_pattern, content):
            text, url = match.groups()
            links['markdown'].append({
                'text': text,
                'url': url.strip(),
                'line': content[:match.start()].count('\n') + 1
            })

        # HTML links: <a href="url">
        html_pattern = r'<a\s+href=["\']([^"\']+)["\'][^>]*>'
        for match in re.finditer(html_pattern, content, re.IGNORECASE):
            url = match.group(1)
            links['html'].append({
                'url': url.strip(),
                'line': content[:match.start()].count('\n') + 1
            })

        # Images: ![alt](src)
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(img_pattern, content):
            alt, src = match.groups()
            links['images'].append({
                'alt': alt,
                'src': src.strip(),
                'line': content[:match.start()].count('\n') + 1
            })

        # Reference links: [text][ref]
        ref_pattern = r'\[([^\]]+)\]\[([^\]]+)\]'
        for match in re.finditer(ref_pattern, content):
            text, ref = match.groups()
            links['references'].append({
                'text': text,
                'ref': ref.strip(),
                'line': content[:match.start()].count('\n') + 1
            })

        return links

    def check_internal_link(self, url: str, file_path: Path) -> bool:
        """Check if internal link exists"""
        if url.startswith('#'):
            # Fragment link - would need content parsing to validate
            return True

        # Resolve relative path
        if url.startswith('./') or url.startswith('../'):
            target_path = (file_path.parent / url).resolve()
        else:
            # Relative to project root
            target_path = Path('.').resolve() / url

        if target_path.exists():
            return True

        # Try with .md extension if not present
        if not target_path.suffix and not target_path.exists():
            target_path = target_path.with_suffix('.md')
            return target_path.exists()

        return False

    def check_external_link(self, url: str) -> bool:
        """Check if external URL is accessible"""
        try:
            response = self.session.head(
                url,
                timeout=self.timeout,
                allow_redirects=True
            )

            # If HEAD fails, try GET
            if response.status_code == 405:
                response = self.session.get(
                    url,
                    timeout=self.timeout,
                    allow_redirects=True
                )

            return response.status_code < 400

        except requests.exceptions.RequestException:
            return False

    def validate_file_links(self, file_path: Path) -> bool:
        """Validate all links in a file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            links = self.extract_links(content, file_path)

            file_valid = True

            # Check markdown links
            for link in links['markdown']:
                url = link['url']
                line = link['line']

                if url.startswith('http://') or url.startswith('https://'):
                    if not self.check_external_link(url):
                        msg = f"{file_path}:{line}: External link failed: {url}"
                        self.errors.append(msg)
                        file_valid = False
                else:
                    if not self.check_internal_link(url, file_path):
                        msg = f"{file_path}:{line}: Internal link not found: {url}"
                        self.errors.append(msg)
                        file_valid = False

            # Check HTML links
            for link in links['html']:
                url = link['url']
                line = link['line']

                if url.startswith('http://') or url.startswith('https://'):
                    if not self.check_external_link(url):
                        msg = f"{file_path}:{line}: HTML link failed: {url}"
                        self.errors.append(msg)
                        file_valid = False

            # Check images
            for img in links['images']:
                src = img['src']
                line = img['line']

                if src.startswith('http://') or src.startswith('https://'):
                    if not self.check_external_link(src):
                        msg = f"{file_path}:{line}: Image link failed: {src}"
                        self.warnings.append(msg)
                else:
                    if not self.check_internal_link(src, file_path):
                        msg = f"{file_path}:{line}: Image not found: {src}"
                        self.errors.append(msg)
                        file_valid = False

            return file_valid

        except Exception as e:
            self.errors.append(f"{file_path}: Error reading file: {e}")
            return False

    def check_links(self, base_path: Path = None) -> int:
        """Check links in all markdown files"""
        if base_path is None:
            base_path = Path(".")

        # Find all markdown files
        md_files = list(base_path.rglob("*.md"))

        logger.info(f"Checking links in {len(md_files)} markdown files...")

        valid_files = 0

        # Process files in parallel for external links
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_file = {
                executor.submit(self.validate_file_links, md_file): md_file
                for md_file in md_files
            }

            for future in as_completed(future_to_file):
                md_file = future_to_file[future]
                try:
                    if future.result():
                        valid_files += 1
                except Exception as e:
                    self.errors.append(f"{md_file}: Processing error: {e}")

        # Print results
        print(f"\n🔗 Link Check Results:")
        print(f"   Total markdown files: {len(md_files)}")
        print(f"   Files without link errors: {valid_files}")
        print(f"   Files with link errors: {len(md_files) - valid_files}")
        print(f"   Warnings: {len(self.warnings)}")
        print(f"   Errors: {len(self.errors)}")

        if self.warnings:
            print(f"\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"   {warning}")

        if self.errors:
            print(f"\n❌ Errors:")
            for error in self.errors:
                print(f"   {error}")
            return 1
        else:
            print(f"\n✅ All links are valid!")
            return 0


def main():
    """Main entry point with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Check links in markdown files"
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Base path to check",
        default=Path(".")
    )
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout for external links (seconds)",
        default=10
    )
    parser.add_argument(
        "--workers",
        type=int,
        help="Number of worker threads",
        default=10
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    checker = LinkChecker(timeout=args.timeout, max_workers=args.workers)
    return checker.check_links(args.path)


if __name__ == "__main__":
    sys.exit(main())
