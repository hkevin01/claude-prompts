#!/usr/bin/env python3
"""
Comprehensive test runner for the Claude Prompts project
Orchestrates all testing phases with proper reporting
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table


class TestRunner:
    """Orchestrates comprehensive testing workflow"""

    def __init__(self, verbose: bool = False):
        self.console = Console()
        self.verbose = verbose
        self.results = {
            'validation': None,
            'unit_tests': None,
            'integration_tests': None,
            'lint': None,
            'type_check': None,
            'security': None,
            'links': None,
            'coverage': None
        }

    def run_command(self, cmd: List[str], description: str) -> bool:
        """Run a command and capture results"""
        try:
            if self.verbose:
                self.console.print(f"[blue]Running: {' '.join(cmd)}[/blue]")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False
            )

            if result.returncode == 0:
                if self.verbose:
                    self.console.print(
                        f"[green]✓ {description} passed[/green]"
                    )
                return True
            else:
                self.console.print(f"[red]✗ {description} failed[/red]")
                if self.verbose and result.stderr:
                    self.console.print(f"Error: {result.stderr}")
                return False

        except FileNotFoundError:
            self.console.print(f"[red]✗ Command not found: {cmd[0]}[/red]")
            return False
        except Exception as e:
            self.console.print(f"[red]✗ {description} error: {e}[/red]")
            return False

    def validate_prompts(self) -> bool:
        """Validate all prompt files"""
        self.console.print("\n[bold cyan]Phase 1: Prompt Validation[/bold cyan]")

        # Check if validation script exists
        validator_path = Path("scripts/validate_prompts.py")
        if not validator_path.exists():
            self.console.print("[yellow]⚠ Validation script not found[/yellow]")
            return False

        return self.run_command(
            ["python", "scripts/validate_prompts.py"],
            "Prompt validation"
        )

    def run_unit_tests(self) -> bool:
        """Run unit tests with pytest"""
        self.console.print("\n[bold cyan]Phase 2: Unit Tests[/bold cyan]")

        # Check if pytest is available
        try:
            subprocess.run(["pytest", "--version"], capture_output=True)
        except FileNotFoundError:
            self.console.print("[yellow]⚠ pytest not installed[/yellow]")
            return False

        return self.run_command(
            ["pytest", "tests/", "-v", "--tb=short"],
            "Unit tests"
        )

    def run_integration_tests(self) -> bool:
        """Run integration tests"""
        self.console.print("\n[bold cyan]Phase 3: Integration Tests[/bold cyan]")

        return self.run_command(
            ["pytest", "tests/", "-m", "integration", "-v"],
            "Integration tests"
        )

    def run_lint_checks(self) -> bool:
        """Run linting and code style checks"""
        self.console.print("\n[bold cyan]Phase 4: Code Quality[/bold cyan]")

        checks = [
            (["python", "-m", "flake8", "scripts/"], "Flake8 linting"),
            (["python", "-m", "black", "--check", "."], "Black formatting"),
            (["python", "-m", "isort", "--check-only", "."], "Import sorting"),
        ]

        all_passed = True
        for cmd, description in checks:
            if not self.run_command(cmd, description):
                all_passed = False

        return all_passed

    def run_type_checks(self) -> bool:
        """Run type checking with mypy"""
        self.console.print("\n[bold cyan]Phase 5: Type Checking[/bold cyan]")

        try:
            subprocess.run(["mypy", "--version"], capture_output=True)
        except FileNotFoundError:
            self.console.print("[yellow]⚠ mypy not installed[/yellow]")
            return False

        return self.run_command(
            ["mypy", "scripts/"],
            "Type checking"
        )

    def run_security_checks(self) -> bool:
        """Run security analysis"""
        self.console.print("\n[bold cyan]Phase 6: Security Analysis[/bold cyan]")

        checks = []

        # Check for bandit
        try:
            subprocess.run(["bandit", "--version"], capture_output=True)
            checks.append((["bandit", "-r", "scripts/"], "Bandit security scan"))
        except FileNotFoundError:
            self.console.print("[yellow]⚠ bandit not installed[/yellow]")

        # Check for safety
        try:
            subprocess.run(["safety", "--version"], capture_output=True)
            checks.append((["safety", "check"], "Safety dependency check"))
        except FileNotFoundError:
            self.console.print("[yellow]⚠ safety not installed[/yellow]")

        if not checks:
            return False

        all_passed = True
        for cmd, description in checks:
            if not self.run_command(cmd, description):
                all_passed = False

        return all_passed

    def check_links(self) -> bool:
        """Check links in markdown files"""
        self.console.print("\n[bold cyan]Phase 7: Link Validation[/bold cyan]")

        # Check for async link checker
        checker_path = Path("scripts/async_link_checker_clean.py")
        if not checker_path.exists():
            self.console.print("[yellow]⚠ Link checker not found[/yellow]")
            return False

        return self.run_command(
            ["python", "scripts/async_link_checker_clean.py"],
            "Link validation"
        )

    def generate_coverage_report(self) -> bool:
        """Generate test coverage report"""
        self.console.print("\n[bold cyan]Phase 8: Coverage Analysis[/bold cyan]")

        return self.run_command(
            ["pytest", "tests/", "--cov=scripts", "--cov-report=term-missing"],
            "Coverage analysis"
        )

    def run_all_tests(self) -> Dict[str, bool]:
        """Run all test phases"""
        phases = [
            ("validation", self.validate_prompts),
            ("unit_tests", self.run_unit_tests),
            ("integration_tests", self.run_integration_tests),
            ("lint", self.run_lint_checks),
            ("type_check", self.run_type_checks),
            ("security", self.run_security_checks),
            ("links", self.check_links),
            ("coverage", self.generate_coverage_report),
        ]

        for phase_name, phase_func in phases:
            self.results[phase_name] = phase_func()

        return self.results

    def display_summary(self):
        """Display test results summary"""
        self.console.print("\n" + "=" * 60)
        self.console.print("[bold]Test Summary[/bold]")
        self.console.print("=" * 60)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Phase", style="cyan", no_wrap=True)
        table.add_column("Status", justify="center")
        table.add_column("Description", style="dim")

        phase_descriptions = {
            'validation': 'Prompt schema and structure validation',
            'unit_tests': 'Unit test execution',
            'integration_tests': 'Integration test execution',
            'lint': 'Code style and linting',
            'type_check': 'Static type checking',
            'security': 'Security vulnerability scanning',
            'links': 'Markdown link validation',
            'coverage': 'Test coverage analysis'
        }

        for phase, result in self.results.items():
            if result is True:
                status = "[green]✓ PASS[/green]"
            elif result is False:
                status = "[red]✗ FAIL[/red]"
            else:
                status = "[yellow]⚠ SKIP[/yellow]"

            table.add_row(
                phase.replace('_', ' ').title(),
                status,
                phase_descriptions.get(phase, "")
            )

        self.console.print(table)

        # Overall status
        passed = sum(1 for r in self.results.values() if r is True)
        total = len([r for r in self.results.values() if r is not None])

        if total == 0:
            self.console.print("\n[yellow]No tests were run[/yellow]")
        elif passed == total:
            self.console.print("\n[green]🎉 All tests passed![/green]")
        else:
            failed = total - passed
            self.console.print(
                f"\n[red]{failed} of {total} test phases failed[/red]"
            )

        return passed == total and total > 0


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Comprehensive test runner for Claude Prompts project"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--phase",
        choices=[
            "validation", "unit", "integration", "lint",
            "type", "security", "links", "coverage"
        ],
        help="Run only a specific test phase"
    )

    args = parser.parse_args()

    runner = TestRunner(verbose=args.verbose)

    try:
        if args.phase:
            # Run specific phase
            phase_map = {
                "validation": runner.validate_prompts,
                "unit": runner.run_unit_tests,
                "integration": runner.run_integration_tests,
                "lint": runner.run_lint_checks,
                "type": runner.run_type_checks,
                "security": runner.run_security_checks,
                "links": runner.check_links,
                "coverage": runner.generate_coverage_report,
            }

            if args.phase in phase_map:
                success = phase_map[args.phase]()
                sys.exit(0 if success else 1)
        else:
            # Run all phases
            runner.run_all_tests()
            success = runner.display_summary()
            sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\nTesting interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error during testing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
