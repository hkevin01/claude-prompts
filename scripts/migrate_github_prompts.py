#!/usr/bin/env python3
"""
GitHub Prompts Migration Script
Migrates prompts from .github/prompts to src/prompts with proper metadata
"""

import os
import re
from pathlib import Path
from typing import Dict, List

# Category mapping from directory names to our schema
CATEGORY_MAPPING = {
    'code-review': 'coding',
    'development': 'coding',
    'architecture': 'coding',
    'optimization': 'coding',
    'testing': 'coding',
    'generation': 'coding',
    'legacy': 'coding',
    'api': 'coding'
}

# Difficulty mapping based on content complexity
DIFFICULTY_MAPPING = {
    'basic': 'beginner',
    'simple': 'beginner',
    'comprehensive': 'intermediate',
    'advanced': 'advanced',
    'expert': 'advanced',
    'complex': 'advanced'
}

def extract_title_from_content(content: str) -> str:
    """Extract title from markdown content"""
    lines = content.strip().split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "Untitled Prompt"

def determine_difficulty(content: str, title: str) -> str:
    """Determine difficulty based on content analysis"""
    content_lower = content.lower()
    title_lower = title.lower()

    # Check for complexity indicators
    advanced_indicators = [
        'architecture', 'microservices', 'performance', 'optimization',
        'security', 'scalability', 'enterprise', 'distributed'
    ]

    intermediate_indicators = [
        'comprehensive', 'integration', 'testing', 'automation',
        'workflow', 'pipeline', 'strategy'
    ]

    # Count indicators
    advanced_count = sum(1 for indicator in advanced_indicators
                        if indicator in content_lower or indicator in title_lower)
    intermediate_count = sum(1 for indicator in intermediate_indicators
                           if indicator in content_lower or indicator in title_lower)

    if advanced_count >= 2:
        return 'advanced'
    elif intermediate_count >= 1 or advanced_count >= 1:
        return 'intermediate'
    else:
        return 'beginner'

def extract_tags_from_content(content: str, directory: str) -> List[str]:
    """Extract relevant tags from content and directory"""
    base_tags = [directory.replace('-', ' ').replace('_', ' ')]

    # Common tag patterns in content
    tag_patterns = {
        'testing': ['test', 'testing', 'tdd', 'automation'],
        'api': ['api', 'rest', 'graphql', 'endpoint'],
        'database': ['database', 'sql', 'query', 'optimization'],
        'security': ['security', 'authentication', 'authorization'],
        'performance': ['performance', 'optimization', 'speed'],
        'documentation': ['documentation', 'docs', 'readme'],
        'architecture': ['architecture', 'design', 'system'],
        'deployment': ['deployment', 'ci/cd', 'pipeline'],
        'refactoring': ['refactor', 'cleanup', 'modernization'],
        'debugging': ['debug', 'troubleshoot', 'fix']
    }

    content_lower = content.lower()
    found_tags = set(base_tags)

    for tag_category, keywords in tag_patterns.items():
        if any(keyword in content_lower for keyword in keywords):
            found_tags.add(tag_category)

    return list(found_tags)[:6]  # Limit to 6 tags

def create_frontmatter(title: str, directory: str, content: str) -> str:
    """Create YAML frontmatter for the prompt"""
    category = CATEGORY_MAPPING.get(directory, 'coding')
    difficulty = determine_difficulty(content, title)
    tags = extract_tags_from_content(content, directory)

    # Clean title for filename
    clean_title = re.sub(r'[^\w\s-]', '', title).strip()
    clean_title = re.sub(r'[-\s]+', '-', clean_title).lower()

    description = f"Professional {directory.replace('-', ' ')} assistant for {title.lower()}"

    return f"""---
title: "{title}"
category: "{category}"
tags: {tags}
difficulty: "{difficulty}"
description: "{description}"
author: "Claude Prompts Collection"
date: "2025-08-02"
version: "1.1"
---"""

def convert_prompt_content(content: str) -> str:
    """Convert raw prompt to our standard format"""
    lines = content.strip().split('\n')

    # Remove the title line
    if lines and lines[0].startswith('# '):
        lines = lines[1:]

    # Remove empty lines at the start
    while lines and not lines[0].strip():
        lines.pop(0)

    prompt_content = '\n'.join(lines).strip()

    return f"""## Description

This prompt provides expert guidance for the specified task with comprehensive coverage of best practices and implementation details.

## Prompt

```text
{prompt_content}
```

## Variables to Customize

- **Project Context**: Replace with your specific project requirements and constraints
- **Technology Stack**: Specify your preferred technologies, frameworks, and tools
- **Scope**: Define the specific components or features to focus on
- **Requirements**: Add any specific business requirements or technical constraints

## Example Usage

Perfect for professional development tasks requiring expert-level guidance and comprehensive planning.

## Tips

- Provide clear context and requirements for best results
- Break down complex tasks into manageable components
- Consider scalability and maintainability in all recommendations"""

def migrate_prompts():
    """Migrate all prompts from .github/prompts to src/prompts"""
    github_prompts_dir = Path('.github/prompts')
    src_prompts_dir = Path('src/prompts')

    if not github_prompts_dir.exists():
        print("❌ .github/prompts directory not found")
        return

    migrated_count = 0

    # Process each prompt file
    for prompt_file in github_prompts_dir.rglob('*.md'):
        if prompt_file.name == 'README.md':
            continue

        try:
            # Read original content
            with open(prompt_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract metadata
            directory = prompt_file.parent.name
            title = extract_title_from_content(content)

            # Create new filename
            clean_title = re.sub(r'[^\w\s-]', '', title).strip()
            clean_filename = re.sub(r'[-\s]+', '-', clean_title).lower() + '.md'

            # Create frontmatter and new content
            frontmatter = create_frontmatter(title, directory, content)
            new_content = convert_prompt_content(content)

            # Combine frontmatter and content
            full_content = f"{frontmatter}\n\n{new_content}\n"

            # Determine output category directory
            output_category = CATEGORY_MAPPING.get(directory, 'coding')
            output_dir = src_prompts_dir / output_category
            output_dir.mkdir(parents=True, exist_ok=True)

            # Write new file
            output_path = output_dir / clean_filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_content)

            print(f"✅ Migrated: {prompt_file} -> {output_path}")
            migrated_count += 1

        except Exception as e:
            print(f"❌ Error migrating {prompt_file}: {e}")

    print(f"\n🎉 Migration completed! {migrated_count} prompts migrated successfully.")

if __name__ == "__main__":
    migrate_prompts()
