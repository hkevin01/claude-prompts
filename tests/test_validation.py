#!/usr/bin/env python3
"""
Comprehensive test suite for prompt validation system
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import yaml

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

try:
    from check_links import LinkChecker
    from validate_prompts import PromptValidator
except ImportError as e:
    print(f"Failed to import modules: {e}")
    sys.exit(1)


class TestPromptValidator(unittest.TestCase):
    """Test cases for prompt validation"""

    def setUp(self):
        """Set up test environment"""
        self.validator = PromptValidator()
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_test_prompt(self, content: str, filename: str = "test.md") -> Path:
        """Create a test prompt file"""
        file_path = self.temp_dir / filename
        file_path.write_text(content, encoding='utf-8')
        return file_path

    def test_valid_prompt(self):
        """Test validation of a valid prompt"""
        content = """---
title: "Test Prompt"
description: "A test prompt for validation"
author: "Test Author"
version: "1.0.0"
category: "testing"
tags: ["test", "validation"]
difficulty: "beginner"
language: "en"
license: "MIT"
---

# Test Prompt

This is a test prompt with valid frontmatter.

## Usage

Use this prompt for testing validation.
"""
        file_path = self.create_test_prompt(content)
        result = self.validator.validate_file(file_path)
        self.assertTrue(result)
        self.assertEqual(len(self.validator.errors), 0)

    def test_missing_frontmatter(self):
        """Test prompt without frontmatter"""
        content = """# Test Prompt

This prompt has no frontmatter.
"""
        file_path = self.create_test_prompt(content)
        result = self.validator.validate_file(file_path)
        self.assertFalse(result)
        self.assertGreater(len(self.validator.errors), 0)

    def test_invalid_yaml(self):
        """Test prompt with invalid YAML frontmatter"""
        content = """---
title: "Test Prompt
description: Missing quote
---

# Test Prompt
"""
        file_path = self.create_test_prompt(content)
        result = self.validator.validate_file(file_path)
        self.assertFalse(result)

    def test_missing_required_fields(self):
        """Test prompt missing required fields"""
        content = """---
title: "Test Prompt"
# Missing required fields
---

# Test Prompt
"""
        file_path = self.create_test_prompt(content)
        result = self.validator.validate_file(file_path)
        self.assertFalse(result)

    def test_invalid_field_values(self):
        """Test prompt with invalid field values"""
        content = """---
title: "Test Prompt"
description: "Test description"
author: "Test Author"
version: "1.0.0"
category: "invalid-category"  # Invalid category
tags: ["test"]
difficulty: "invalid-difficulty"  # Invalid difficulty
language: "en"
license: "MIT"
---

# Test Prompt
"""
        file_path = self.create_test_prompt(content)
        result = self.validator.validate_file(file_path)
        self.assertFalse(result)

    def test_schema_validation(self):
        """Test JSON schema validation"""
        valid_metadata = {
            "title": "Test Prompt",
            "description": "Test description",
            "author": "Test Author",
            "version": "1.0.0",
            "category": "testing",
            "tags": ["test"],
            "difficulty": "beginner",
            "language": "en",
            "license": "MIT"
        }
        result = self.validator.validate_schema(valid_metadata)
        self.assertTrue(result)

        # Test with missing required field
        invalid_metadata = valid_metadata.copy()
        del invalid_metadata["title"]
        result = self.validator.validate_schema(invalid_metadata)
        self.assertFalse(result)


class TestLinkChecker(unittest.TestCase):
    """Test cases for link checking"""

    def setUp(self):
        """Set up test environment"""
        self.checker = LinkChecker()
        self.temp_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def create_test_file(self, content: str, filename: str = "test.md") -> Path:
        """Create a test markdown file"""
        file_path = self.temp_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding='utf-8')
        return file_path

    def test_extract_markdown_links(self):
        """Test extraction of markdown links"""
        content = """
# Test Document

[Valid Link](https://example.com)
[Internal Link](./other.md)
![Image](./image.png)
"""
        file_path = self.create_test_file(content)
        links = self.checker.extract_links(content, file_path)

        self.assertEqual(len(links['markdown']), 2)
        self.assertEqual(len(links['images']), 1)

        # Check link details
        self.assertEqual(links['markdown'][0]['url'], 'https://example.com')
        self.assertEqual(links['markdown'][1]['url'], './other.md')
        self.assertEqual(links['images'][0]['src'], './image.png')

    def test_internal_link_validation(self):
        """Test internal link validation"""
        # Create target file
        target_file = self.create_test_file("# Target", "target.md")

        # Test valid internal link
        source_content = "[Link to target](./target.md)"
        source_file = self.create_test_file(source_content, "source.md")

        result = self.checker.check_internal_link("./target.md", source_file)
        self.assertTrue(result)

        # Test invalid internal link
        result = self.checker.check_internal_link("./nonexistent.md", source_file)
        self.assertFalse(result)

    @patch('requests.Session.head')
    def test_external_link_validation(self, mock_head):
        """Test external link validation with mocked requests"""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_head.return_value = mock_response

        result = self.checker.check_external_link("https://example.com")
        self.assertTrue(result)

        # Mock failed response
        mock_response.status_code = 404
        result = self.checker.check_external_link("https://nonexistent.com")
        self.assertFalse(result)

    def test_file_validation(self):
        """Test complete file validation"""
        # Create a file with mixed link types
        content = """# Test File

[Valid external](https://example.com)
[Valid internal](./target.md)
[Invalid internal](./nonexistent.md)
"""

        # Create target file for internal link
        self.create_test_file("# Target", "target.md")

        # Create source file
        source_file = self.create_test_file(content, "source.md")

        # Mock external link checker
        with patch.object(self.checker, 'check_external_link', return_value=True):
            result = self.checker.validate_file_links(source_file)
            # Should fail due to invalid internal link
            self.assertFalse(result)
            self.assertGreater(len(self.checker.errors), 0)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""

    def setUp(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.validator = PromptValidator()
        self.checker = LinkChecker()

    def tearDown(self):
        """Clean up test environment"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_complete_validation_workflow(self):
        """Test the complete validation workflow"""
        # Create a valid prompt with internal links
        prompt_content = """---
title: "Integration Test Prompt"
description: "A prompt for integration testing"
author: "Test Suite"
version: "1.0.0"
category: "testing"
tags: ["integration", "test"]
difficulty: "intermediate"
language: "en"
license: "MIT"
---

# Integration Test Prompt

This prompt links to [another prompt](./other-prompt.md) and
includes an image ![test image](./assets/test.png).

## External Resources

See [documentation](https://example.com/docs) for more info.
"""

        # Create referenced files
        other_prompt = """---
title: "Other Prompt"
description: "Referenced prompt"
author: "Test Suite"
version: "1.0.0"
category: "testing"
tags: ["test"]
difficulty: "beginner"
language: "en"
license: "MIT"
---

# Other Prompt

This is the referenced prompt.
"""

        # Set up file structure
        prompt_file = self.temp_dir / "test-prompt.md"
        other_file = self.temp_dir / "other-prompt.md"
        assets_dir = self.temp_dir / "assets"
        assets_dir.mkdir()
        image_file = assets_dir / "test.png"

        prompt_file.write_text(prompt_content, encoding='utf-8')
        other_file.write_text(other_prompt, encoding='utf-8')
        image_file.write_text("fake image content")  # Placeholder

        # Test prompt validation
        result = self.validator.validate_file(prompt_file)
        self.assertTrue(result, f"Validation errors: {self.validator.errors}")

        # Test link checking (mock external links)
        with patch.object(self.checker, 'check_external_link', return_value=True):
            result = self.checker.validate_file_links(prompt_file)
            self.assertTrue(result, f"Link errors: {self.checker.errors}")


def main():
    """Run all tests"""
    # Configure test discovery
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])

    # Run tests with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        buffer=True
    )

    result = runner.run(suite)

    # Return appropriate exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
