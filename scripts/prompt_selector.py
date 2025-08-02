#!/usr/bin/env python3
"""
Modern Claude AI Prompt Selector
A comprehensive prompt management tool with enhanced features
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Configure rich console
console = Console()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PromptSelector:
    """Modern prompt selection tool with enhanced features"""

    def __init__(self, prompts_dir: Path = None):
        self.prompts_dir = prompts_dir or Path(".github/prompts")
        self.src_prompts_dir = Path("src/prompts")
        self.categories = self._discover_categories()

    def _discover_categories(self) -> Dict[str, str]:
        """Discover available prompt categories"""
        categories = {}

        # Check .github/prompts structure
        if self.prompts_dir.exists():
            for category_dir in self.prompts_dir.iterdir():
                if (category_dir.is_dir() and
                    not category_dir.name.startswith('.')):
                    categories[category_dir.name] = str(category_dir)

        # Check src/prompts structure
        if self.src_prompts_dir.exists():
            for category_dir in self.src_prompts_dir.iterdir():
                if (category_dir.is_dir() and
                    not category_dir.name.startswith('.')):
                    categories[category_dir.name] = str(category_dir)

        return categories

    def show_usage(self):
        """Display usage information with rich formatting"""
        console.print("\n[bold green]Claude AI Prompt Selector[/bold green]")
        console.print("A modern tool for browsing and selecting Claude prompts\n")

        console.print("[bold]Usage:[/bold]")
        console.print("  python prompt_selector.py [category] [prompt-name]")
        console.print("  python prompt_selector.py --list-categories")
        console.print("  python prompt_selector.py --search <term>\n")

        if self.categories:
            table = Table(title="Available Categories")
            table.add_column("Category", style="cyan")
            table.add_column("Description", style="green")

            descriptions = {
                "code-review": "Code review and quality analysis",
                "development": "Debugging and development assistance",
                "architecture": "System and API design",
                "optimization": "Performance and algorithm optimization",
                "testing": "Test-driven development and automation",
                "generation": "Code generation from specifications",
                "legacy": "Legacy code modernization",
                "api": "API development and design",
                "coding": "Programming and development prompts",
                "creative": "Creative writing and content prompts",
                "business": "Business and professional prompts",
                "analysis": "Data analysis and research prompts",
                "educational": "Learning and teaching prompts",
                "personal": "Personal productivity prompts"
            }

            for category in sorted(self.categories.keys()):
                desc = descriptions.get(category, "Various prompts")
                table.add_row(category, desc)

            console.print(table)

        console.print("\n[bold]Examples:[/bold]")
        console.print("  python prompt_selector.py coding code-review-assistant")
        console.print("  python prompt_selector.py personal task-prioritizer")
        console.print("  python prompt_selector.py --search 'testing'")

    def list_prompts(self, category: str) -> List[Dict[str, str]]:
        """List all prompts in a category"""
        if category not in self.categories:
            console.print(f"[red]❌ Unknown category: {category}[/red]")
            return []

        category_path = Path(self.categories[category])
        prompts = []

        if category_path.exists():
            for prompt_file in category_path.glob("*.md"):
                if prompt_file.name != "README.md":
                    prompts.append({
                        "name": prompt_file.stem,
                        "file": str(prompt_file),
                        "title": self._extract_title(prompt_file)
                    })

        return sorted(prompts, key=lambda x: x["name"])

    def _extract_title(self, prompt_file: Path) -> str:
        """Extract title from prompt file frontmatter"""
        try:
            content = prompt_file.read_text(encoding='utf-8')
            if content.startswith('---'):
                # Extract YAML frontmatter
                parts = content.split('---', 2)
                if len(parts) >= 2:
                    import yaml
                    frontmatter = yaml.safe_load(parts[1])
                    return frontmatter.get('title', prompt_file.stem)
        except Exception:
            pass
        return prompt_file.stem.replace('-', ' ').title()

    def display_prompts_table(self, category: str):
        """Display prompts in a category as a table"""
        prompts = self.list_prompts(category)

        if not prompts:
            console.print(f"[yellow]No prompts found in category: {category}[/yellow]")
            return

        table = Table(title=f"Prompts in '{category}' Category")
        table.add_column("Name", style="cyan")
        table.add_column("Title", style="green")

        for prompt in prompts:
            table.add_row(prompt["name"], prompt["title"])

        console.print(table)

    def display_prompt(self, category: str, prompt_name: str):
        """Display a specific prompt with rich formatting"""
        if category not in self.categories:
            console.print(f"[red]❌ Unknown category: {category}[/red]")
            return False

        category_path = Path(self.categories[category])
        prompt_file = category_path / f"{prompt_name}.md"

        if not prompt_file.exists():
            console.print(f"[red]❌ Prompt not found: {prompt_file}[/red]")
            console.print(f"[yellow]Available prompts in {category}:[/yellow]")
            self.display_prompts_table(category)
            return False

        try:
            content = prompt_file.read_text(encoding='utf-8')

            # Create a panel with the prompt content
            panel = Panel(
                content,
                title="🤖 Claude AI Prompt",
                subtitle="💡 Copy and paste into Claude AI",
                border_style="green"
            )

            console.print(panel)
            console.print(f"\n[dim]Source: {prompt_file}[/dim]")
            return True

        except Exception as e:
            console.print(f"[red]❌ Error reading prompt file: {e}[/red]")
            return False

    def search_prompts(self, search_term: str) -> List[Dict[str, str]]:
        """Search for prompts containing the search term"""
        results = []

        for category, category_path in self.categories.items():
            for prompt_file in Path(category_path).glob("*.md"):
                if prompt_file.name == "README.md":
                    continue

                try:
                    content = prompt_file.read_text(encoding='utf-8').lower()
                    if search_term.lower() in content:
                        results.append({
                            "category": category,
                            "name": prompt_file.stem,
                            "title": self._extract_title(prompt_file),
                            "file": str(prompt_file)
                        })
                except Exception:
                    continue

        return results

    def display_search_results(self, search_term: str):
        """Display search results in a table"""
        results = self.search_prompts(search_term)

        if not results:
            console.print(f"[yellow]No prompts found matching '{search_term}'[/yellow]")
            return

        table = Table(title=f"Search Results for '{search_term}'")
        table.add_column("Category", style="blue")
        table.add_column("Name", style="cyan")
        table.add_column("Title", style="green")

        for result in results:
            table.add_row(result["category"], result["name"], result["title"])

        console.print(table)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Modern Claude AI Prompt Selector",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("category", nargs="?", help="Prompt category")
    parser.add_argument("prompt", nargs="?", help="Specific prompt name")
    parser.add_argument("--list-categories", action="store_true",
                       help="List all available categories")
    parser.add_argument("--search", metavar="TERM",
                       help="Search for prompts containing the term")
    parser.add_argument("--prompts-dir", type=Path,
                       help="Custom prompts directory")

    args = parser.parse_args()

    # Initialize selector
    selector = PromptSelector(args.prompts_dir)

    # Handle different modes
    if args.list_categories:
        console.print("\n[bold]Available Categories:[/bold]")
        for category in sorted(selector.categories.keys()):
            console.print(f"  • {category}")
        return

    if args.search:
        selector.display_search_results(args.search)
        return

    if not args.category:
        selector.show_usage()
        return

    if not args.prompt:
        selector.display_prompts_table(args.category)
        return

    # Display specific prompt
    success = selector.display_prompt(args.category, args.prompt)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
