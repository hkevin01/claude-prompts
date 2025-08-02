#!/usr/bin/env python3
"""
Fix migrated prompts by adding main headings.
"""

import os
import re
from pathlib import Path


def fix_prompt_heading(file_path):
    """Add main heading to a prompt file if missing."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if there's YAML frontmatter
    if not content.startswith('---'):
        return False

    # Find the end of frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    body = parts[2]

    # Extract title from frontmatter
    title_match = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', frontmatter)
    if not title_match:
        return False

    title = title_match.group(1).strip()

    # Check if main heading already exists
    if re.match(r'^\s*#\s+', body.strip()):
        return False

    # Add main heading
    new_body = f"\n\n# {title}" + body
    new_content = f"---{frontmatter}---{new_body}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Fixed: {file_path}")
    return True

def main():
    """Fix all prompt files in src/prompts/coding/."""
    src_dir = Path("src/prompts/coding")

    if not src_dir.exists():
        print("❌ src/prompts/coding directory not found")
        return

    fixed_count = 0
    for md_file in src_dir.glob("*.md"):
        if fix_prompt_heading(md_file):
            fixed_count += 1

    print(f"\n🎉 Fixed {fixed_count} prompt files")

if __name__ == "__main__":
    main()
