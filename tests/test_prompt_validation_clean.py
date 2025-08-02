#!/usr/bin/env python3
"""
Comprehensive Test Suite for Claude Prompts Collection
Modern pytest-based testing with coverage and property-based testing
"""

import json
import sys
import tempfile
from pathlib import Path

import pytest
from hypothesis import given
from hypothesis import strategies as st

# Import modules to test
sys.path.append(str(Path(__file__).parent.parent / "scripts"))

from validate_prompts import PromptValidator  # noqa: E402


class TestPromptValidator:
    """Test cases for prompt validation"""

    @pytest.fixture
    def validator(self):
        """Create a validator instance for testing"""
        return PromptValidator()

    @pytest.fixture
    def valid_prompt_content(self):
        """Valid prompt content for testing"""
        return """---
title: "Test Prompt"
category: "coding"
tags: ["test", "example"]
difficulty: "beginner"
description: "A test prompt for validation"
author: "Test Author"
date: "2025-07-31"
version: "1.0"
---

# Test Prompt

This is a test prompt for validation.

## Prompt

```
Test prompt content here
```
"""

    @pytest.fixture
    def invalid_prompt_content(self):
        """Invalid prompt content for testing"""
        return """---
title: "Test Prompt"
# Missing required fields
---

# Incomplete Prompt
"""

    def test_validator_initialization(self, validator):
        """Test validator initializes correctly"""
        assert isinstance(validator, PromptValidator)
        assert hasattr(validator, 'errors')
        assert hasattr(validator, 'warnings')
        assert hasattr(validator, 'schema')

    def test_parse_frontmatter_valid(self, validator, valid_prompt_content):
        """Test parsing valid YAML frontmatter"""
        result = validator.parse_frontmatter(valid_prompt_content)
        frontmatter, content = result

        assert frontmatter is not None
        assert frontmatter['title'] == "Test Prompt"
        assert frontmatter['category'] == "coding"
        assert "test" in frontmatter['tags']
        assert content.strip().startswith("# Test Prompt")

    def test_parse_frontmatter_invalid(self, validator):
        """Test parsing invalid YAML frontmatter"""
        invalid_yaml = """---
title: "Test
invalid: yaml: content
---

Content here"""

        frontmatter, content = validator.parse_frontmatter(invalid_yaml)
        assert frontmatter is None
        assert len(validator.errors) > 0

    def test_validate_required_fields(self, validator):
        """Test validation of required fields"""
        # Missing required fields
        incomplete_frontmatter = {
            'title': 'Test',
            # Missing category, tags, difficulty, description
        }

        validator.validate_frontmatter_schema(incomplete_frontmatter)

        # Should have errors for missing required fields
        assert len(validator.errors) > 0
        assert any('category' in error for error in validator.errors)

    @given(st.text(min_size=1, max_size=100))
    def test_title_validation_property(self, validator, title):
        """Property-based test for title validation"""
        frontmatter = {
            'title': title,
            'category': 'coding',
            'tags': ['test'],
            'difficulty': 'beginner',
            'description': 'Test description'
        }

        # Clear previous errors
        validator.errors = []
        validator.validate_frontmatter_schema(frontmatter)

        # Title should always be valid if it's a non-empty string
        title_errors = [e for e in validator.errors if 'title' in e.lower()]
        assert len(title_errors) == 0

    def test_category_validation(self, validator):
        """Test category field validation"""
        valid_categories = [
            'coding', 'creative', 'business', 'analysis',
            'educational', 'personal'
        ]

        for category in valid_categories:
            validator.errors = []
            frontmatter = {
                'title': 'Test',
                'category': category,
                'tags': ['test'],
                'difficulty': 'beginner',
                'description': 'Test'
            }

            validator.validate_frontmatter_schema(frontmatter)
            category_errors = [
                e for e in validator.errors if 'category' in e
            ]
            msg = f"Category '{category}' should be valid"
            assert len(category_errors) == 0, msg

    def test_difficulty_validation(self, validator):
        """Test difficulty field validation"""
        valid_difficulties = ['beginner', 'intermediate', 'advanced']

        for difficulty in valid_difficulties:
            validator.errors = []
            frontmatter = {
                'title': 'Test',
                'category': 'coding',
                'tags': ['test'],
                'difficulty': difficulty,
                'description': 'Test'
            }

            validator.validate_frontmatter_schema(frontmatter)
            errors = [e for e in validator.errors if 'difficulty' in e]
            msg = f"Difficulty '{difficulty}' should be valid"
            assert len(errors) == 0, msg

    def test_tags_validation(self, validator):
        """Test tags field validation"""
        test_cases = [
            (['single-tag'], True),
            (['tag1', 'tag2', 'tag3'], True),
            ([], False),  # Empty tags should be invalid
            ('not-a-list', False),  # Non-list should be invalid
        ]

        for tags, should_be_valid in test_cases:
            validator.errors = []
            frontmatter = {
                'title': 'Test',
                'category': 'coding',
                'tags': tags,
                'difficulty': 'beginner',
                'description': 'Test'
            }

            validator.validate_frontmatter_schema(frontmatter)
            tags_errors = [e for e in validator.errors if 'tags' in e.lower()]

            if should_be_valid:
                msg = f"Tags {tags} should be valid"
                assert len(tags_errors) == 0, msg
            else:
                msg = f"Tags {tags} should be invalid"
                assert len(tags_errors) > 0, msg

    def test_validate_file_with_temp_file(self, validator,
                                          valid_prompt_content):
        """Test file validation with temporary file"""
        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.md', delete=False
        ) as f:
            f.write(valid_prompt_content)
            temp_path = Path(f.name)

        try:
            result = validator.validate_file(temp_path)
            assert result is True
            assert len(validator.errors) == 0
        finally:
            temp_path.unlink()  # Clean up

    def test_validate_nonexistent_file(self, validator):
        """Test validation of non-existent file"""
        nonexistent_path = Path("/nonexistent/file.md")
        result = validator.validate_file(nonexistent_path)

        assert result is False
        assert len(validator.errors) > 0
        error_found = any(
            'not found' in error.lower() for error in validator.errors
        )
        assert error_found

    def test_content_validation(self, validator):
        """Test content structure validation"""
        test_cases = [
            ("# Valid Title\n\nContent here", True),
            ("No title content", False),
            ("", False),
        ]

        for content, should_be_valid in test_cases:
            validator.errors = []
            validator.warnings = []
            validator.validate_content_structure(content)

            if should_be_valid:
                assert len(validator.errors) == 0
            else:
                has_issues = (
                    len(validator.errors) > 0 or
                    len(validator.warnings) > 0
                )
                assert has_issues

    @pytest.mark.parametrize("date_string,expected_valid", [
        ("2025-07-31", True),
        ("2025-12-01", True),
        ("invalid-date", False),
        ("25-07-31", False),
        ("2025-13-01", False),  # Invalid month
    ])
    def test_date_validation(self, validator, date_string, expected_valid):
        """Test date format validation"""
        frontmatter = {
            'title': 'Test',
            'category': 'coding',
            'tags': ['test'],
            'difficulty': 'beginner',
            'description': 'Test',
            'date': date_string
        }

        validator.errors = []
        validator.validate_frontmatter_schema(frontmatter)

        date_errors = [e for e in validator.errors if 'date' in e.lower()]

        if expected_valid:
            msg = f"Date '{date_string}' should be valid"
            assert len(date_errors) == 0, msg
        else:
            msg = f"Date '{date_string}' should be invalid"
            assert len(date_errors) > 0, msg


class TestIntegration:
    """Integration tests for the complete validation workflow"""

    def test_validate_directory_structure(self):
        """Test validation of directory structure"""
        src_prompts = Path("src/prompts")
        if src_prompts.exists():
            categories = [d.name for d in src_prompts.iterdir()
                          if d.is_dir()]
            expected_categories = [
                'coding', 'creative', 'business',
                'analysis', 'educational', 'personal'
            ]

            for category in expected_categories:
                msg = f"Category '{category}' directory should exist"
                assert category in categories, msg

    def test_schema_file_exists(self):
        """Test that schema file exists and is valid"""
        schema_path = Path("src/schemas/prompt-schema.json")
        assert schema_path.exists(), "Schema file should exist"

        with open(schema_path) as f:
            schema = json.load(f)

        assert 'required' in schema
        assert 'properties' in schema
        assert 'title' in schema['required']

    @pytest.mark.slow
    def test_all_existing_prompts_valid(self):
        """Test that all existing prompts are valid"""
        validator = PromptValidator()
        src_prompts = Path("src/prompts")

        if not src_prompts.exists():
            pytest.skip("No src/prompts directory found")

        failed_files = []

        for prompt_file in src_prompts.rglob("*.md"):
            validator.errors = []
            validator.warnings = []

            result = validator.validate_file(prompt_file)
            if not result:
                failed_files.append({
                    'file': str(prompt_file),
                    'errors': validator.errors.copy(),
                    'warnings': validator.warnings.copy()
                })

        if failed_files:
            error_msg = "The following prompts failed validation:\n"
            for failed in failed_files:
                error_msg += f"\n{failed['file']}:\n"
                for error in failed['errors']:
                    error_msg += f"  ERROR: {error}\n"
                for warning in failed['warnings']:
                    error_msg += f"  WARNING: {warning}\n"

            pytest.fail(error_msg)


class TestPerformance:
    """Performance and stress tests"""

    @pytest.mark.slow
    def test_large_file_validation(self):
        """Test validation performance with large files"""
        validator = PromptValidator()

        # Create a large valid prompt content
        large_content = """---
title: "Large Test Prompt"
category: "coding"
tags: ["test", "performance"]
difficulty: "advanced"
description: "A large prompt for performance testing"
---

# Large Test Prompt

""" + "This is repeated content. " * 10000

        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.md', delete=False
        ) as f:
            f.write(large_content)
            temp_path = Path(f.name)

        try:
            import time
            start_time = time.time()
            result = validator.validate_file(temp_path)
            end_time = time.time()

            assert result is True
            msg = "Validation should complete within 5 seconds"
            assert end_time - start_time < 5.0, msg

        finally:
            temp_path.unlink()


# Fixtures for test data
@pytest.fixture
def sample_prompt_data():
    """Sample prompt data for testing"""
    return {
        'title': 'Sample Test Prompt',
        'category': 'coding',
        'tags': ['testing', 'validation'],
        'difficulty': 'intermediate',
        'description': 'A sample prompt for testing purposes',
        'author': 'Test Suite',
        'date': '2025-07-31',
        'version': '1.0'
    }


# Marks for different test categories
pytestmark = [
    pytest.mark.unit,  # Mark all tests in this file as unit tests
]


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])
