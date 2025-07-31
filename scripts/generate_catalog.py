#!/usr/bin/env python3
"""
Generate catalog from prompt files
"""

import sys
from datetime import datetime
from pathlib import Path


def generate_catalog():
    """Generate CATALOG.md from existing prompts"""
    base_path = Path(".")

    # Find all prompt files
    prompt_dirs = [
        base_path / "src" / "prompts",
        base_path / "prompts"
    ]

    prompts = []
    for prompt_dir in prompt_dirs:
        if prompt_dir.exists():
            for prompt_file in prompt_dir.rglob("*.md"):
                if prompt_file.name != "README.md":
                    try:
                        content = prompt_file.read_text(encoding='utf-8')
                        # Extract title from first heading
                        lines = content.split('\n')
                        title = "Unknown"
                        for line in lines:
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break

                        relative_path = prompt_file.relative_to(base_path)
                        prompts.append({
                            'title': title,
                            'path': str(relative_path),
                            'category': prompt_file.parent.name
                        })
                    except Exception:
                        continue

    # Generate catalog content
    catalog_content = f"""# Prompts Catalog

Auto-generated catalog of Claude prompts.

## 📊 Quick Stats

- **Total Prompts**: {len(prompts)}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 📋 All Prompts

"""

    # Group by category
    by_category = {}
    for prompt in prompts:
        category = prompt['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(prompt)

    for category, category_prompts in sorted(by_category.items()):
        catalog_content += f"\n### {category.title()}\n\n"
        for prompt in sorted(category_prompts, key=lambda x: x['title']):
            catalog_content += f"- [{prompt['title']}]({prompt['path']})\n"

    # Write catalog
    catalog_file = base_path / "CATALOG.md"
    catalog_file.write_text(catalog_content, encoding='utf-8')

    print(f"✅ Generated catalog with {len(prompts)} prompts")
    return 0


if __name__ == "__main__":
    sys.exit(generate_catalog())
