#!/usr/bin/env python3
"""
Comprehensive validation script for Claude Prompts Collection
Validates YAML frontmatter, content structure, and schema compliance
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Dict, Tuple

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PromptValidator:
    """Comprehensive prompt validation with schema checking"""

    def __init__(self, schema_path: Path = None):
        self.errors = []
        self.warnings = []
        self.schema = self._load_schema(schema_path)

    def _load_schema(self, schema_path: Path = None) -> Dict[str, Any]:
        """Load validation schema"""
        if schema_path and schema_path.exists():
            try:
                with open(schema_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load schema: {e}")

        # Default schema if none provided
        return {
            "required": [
                "title", "category", "tags", "difficulty", "description"
            ],
            "categories": [
                "coding", "creative", "business",
                "analysis", "educational", "personal"
            ],
            "difficulties": ["beginner", "intermediate", "advanced"]
        }

    def validate_frontmatter(self, content: str,
                           file_path: Path) -> Tuple[Dict[str, Any], bool]:
        """Validate YAML frontmatter"""
        if not content.startswith('---'):
            self.errors.append(f"{file_path}: Missing YAML frontmatter")
            return {}, False

        try:
            # Extract frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.errors.append(f"{file_path}: Malformed frontmatter")
                return {}, False

            frontmatter = yaml.safe_load(parts[1])
            if not isinstance(frontmatter, dict):
                msg = f"{file_path}: Frontmatter must be a dictionary"
                self.errors.append(msg)
                return {}, False

            # Validate required fields
            for field in self.schema.get("required", []):
                if field not in frontmatter:
                    msg = f"{file_path}: Missing required field '{field}'"
                    self.errors.append(msg)
                elif not frontmatter[field]:
                    msg = f"{file_path}: Field '{field}' cannot be empty"
                    self.errors.append(msg)

            # Validate category
            if "category" in frontmatter:
                valid_cats = self.schema.get("categories", [])
                if frontmatter["category"] not in valid_cats:
                    cat = frontmatter['category']
                    msg = f"{file_path}: Invalid category '{cat}'"
                    self.errors.append(msg)

            # Validate difficulty
            if "difficulty" in frontmatter:
                valid_diffs = self.schema.get("difficulties", [])
                if frontmatter["difficulty"] not in valid_diffs:
                    diff = frontmatter['difficulty']
                    msg = f"{file_path}: Invalid difficulty '{diff}'"
                    self.errors.append(msg)

            # Validate tags
            if "tags" in frontmatter:
                if not isinstance(frontmatter["tags"], list):
                    self.errors.append(f"{file_path}: Tags must be a list")
                elif not frontmatter["tags"]:
                    self.warnings.append(f"{file_path}: No tags specified")

            # Validate date format
            if "date" in frontmatter:
                date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                if not re.match(date_pattern, str(frontmatter["date"])):
                    msg = f"{file_path}: Date must be in YYYY-MM-DD format"
                    self.errors.append(msg)

            return frontmatter, True

        except yaml.YAMLError as e:
            self.errors.append(f"{file_path}: YAML parsing error: {e}")
            return {}, False
        except Exception as e:
            msg = f"{file_path}: Unexpected error parsing frontmatter: {e}"
            self.errors.append(msg)
            return {}, False

    def validate_content_structure(self, content: str, file_path: Path,
                                 frontmatter: Dict[str, Any]) -> bool:
        """Validate content structure and format"""
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False

        main_content = parts[2].strip()

        # Check for main heading
        if not main_content.startswith('# '):
            self.errors.append(f"{file_path}: Missing main heading (# Title)")

        # Check for required sections
        required_sections = [
            "## Description", "## Prompt", "## Variables to Customize"
        ]
        for section in required_sections:
            if section not in main_content:
                msg = f"{file_path}: Missing section '{section}'"
                self.warnings.append(msg)

        # Check for prompt block
        if "```" not in main_content:
            msg = f"{file_path}: No code blocks found"
            self.warnings.append(msg)

        # Check for variables in prompt if variables are defined
        if "variables" in frontmatter and frontmatter["variables"]:
            for var in frontmatter["variables"]:
                var_name = var.get("name", "")
                if var_name and f"{{{var_name}}}" not in main_content:
                    msg = f"{file_path}: Variable '{var_name}' defined but not used"
                    self.warnings.append(msg)

        return True

    def validate_file(self, file_path: Path) -> bool:
        """Validate a single prompt file"""
        try:
            content = file_path.read_text(encoding='utf-8')

            # Validate frontmatter
            frontmatter, fm_valid = self.validate_frontmatter(
                content, file_path
            )

            # Validate content structure
            if fm_valid:
                self.validate_content_structure(
                    content, file_path, frontmatter
                )

            return fm_valid

        except Exception as e:
            self.errors.append(f"{file_path}: Error reading file: {e}")
            return False

    def validate_prompts(self, base_path: Path = None) -> int:
        """Validate all prompt files"""
        if base_path is None:
            base_path = Path(".")

        # Find prompt directories
        prompt_dirs = [
            base_path / "src" / "prompts",
            base_path / "prompts"
        ]

        prompt_count = 0
        valid_count = 0

        logger.info("Starting prompt validation...")

        for prompt_dir in prompt_dirs:
            if prompt_dir.exists():
                logger.info(f"Checking directory: {prompt_dir}")
                for prompt_file in prompt_dir.rglob("*.md"):
                    if prompt_file.name != "README.md":
                        prompt_count += 1
                        if self.validate_file(prompt_file):
                            valid_count += 1

        # Print results
        print(f"\n📊 Validation Results:")
        print(f"   Total prompt files: {prompt_count}")
        print(f"   Valid files: {valid_count}")
        print(f"   Files with errors: {prompt_count - valid_count}")
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
            print(f"\n✅ All validations passed!")
            return 0


def main():
    """Main entry point with argument parsing"""
    parser = argparse.ArgumentParser(description="Validate Claude prompt files")
    parser.add_argument(
        "--schema",
        type=Path,
        help="Path to JSON schema file",
        default=Path("src/schemas/prompt-schema.json")
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Base path to validate",
        default=Path(".")
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    validator = PromptValidator(args.schema)
    return validator.validate_prompts(args.path)


if __name__ == "__main__":
    sys.exit(main())
