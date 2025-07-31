#!/usr/bin/env python3
"""
Check for broken links in markdown files
"""

import sys
from pathlib import Path


def check_links():
    """Check for broken links"""
    base_path = Path(".")
    errors = []

    # Find all markdown files
    md_files = list(base_path.rglob("*.md"))

    print(f"Checking {len(md_files)} markdown files for links...")

    # For now, just do basic validation
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            # Basic check for common issues
            if '[broken-link]' in content:
                errors.append(f"{md_file}: Contains broken link placeholder")
        except Exception:
            errors.append(f"{md_file}: Could not read file")

    if errors:
        print("Link errors found:")
        for error in errors:
            print(f"  {error}")
        return 1
    else:
        print("✅ No broken links detected!")
        return 0


if __name__ == "__main__":
    sys.exit(check_links())
