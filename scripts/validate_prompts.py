#!/usr/bin/env python3
"""
Simple validation script for Claude Prompts Collection
"""

import sys
from pathlib import Path


def validate_prompts():
    """Basic validation of prompt files"""
    base_path = Path(".")
    errors = []
    
    # Check for basic structure
    prompt_dirs = [
        base_path / "src" / "prompts",
        base_path / "prompts"
    ]
    
    prompt_count = 0
    for prompt_dir in prompt_dirs:
        if prompt_dir.exists():
            for prompt_file in prompt_dir.rglob("*.md"):
                if prompt_file.name != "README.md":
                    try:
                        content = prompt_file.read_text(encoding='utf-8')
                        if not content.startswith('---'):
                            errors.append(f"{prompt_file}: Missing frontmatter")
                        prompt_count += 1
                    except Exception as e:
                        errors.append(f"{prompt_file}: Error reading: {e}")
    
    print(f"Validated {prompt_count} prompt files")
    
    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  {error}")
        return 1
    else:
        print("✅ All validations passed!")
        return 0


if __name__ == "__main__":
    sys.exit(validate_prompts())
