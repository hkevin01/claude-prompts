---
title: "Phased Test Strategy & Infrastructure"
category: "workflow"
tags: ["testing", "phased", "automation", "ci", "infrastructure"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "Set up a comprehensive, phased test infrastructure — from unit to integration to E2E to performance — with CI pipeline integration, log output, and coverage reporting."
use_cases:
  - "Building a test suite from scratch"
  - "Scaling testing as a project grows"
  - "Adding CI pipeline test automation"
  - "Establishing test coverage baselines"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "Payment Processor API"
  - name: "tech_stack"
    description: "Language and test framework"
    example: "Python 3.11 + pytest, Node.js + jest, Go + testing"
  - name: "phases"
    description: "Development phases to create tests for"
    example: "Phase 1: Auth, Phase 2: Core API, Phase 3: Integrations"
---

# Phased Test Strategy & Infrastructure

## Description
Establishes a complete, phased test infrastructure aligned to your project's development phases. Covers all test types (unit, integration, regression, performance, fault tolerance), CI pipeline integration, log folders, and coverage reporting. Built to grow alongside the project.

## Prompt

```
Set up a comprehensive test infrastructure for **{project_name}**.

Tech stack: {tech_stack}
Phases to cover: {phases}

---

## SETUP PHASE — Test Infrastructure

### 1. Directory Structure
Create the following test layout:
```
tests/
├── unit/                   # Unit tests mirroring src/ structure
├── integration/            # Tests for component interactions
├── e2e/                    # End-to-end workflow tests
├── performance/            # Benchmarks and load tests
├── fixtures/               # Test data, seeds, and mock payloads
├── mocks/                  # Mock implementations of external services
├── helpers/                # Shared test utilities
├── setup/                  # Global test configuration and hooks
└── logs/                   # Test run logs (gitignored)
```

### 2. Configuration Files
Create:
- Test runner config (jest.config.js / pytest.ini / etc.) with:
  - Coverage threshold: minimum 70% overall, 80% for critical paths
  - Test timeout: appropriate for the stack
  - Auto-discover test files
  - Output logs to `tests/logs/`
- `tests/setup/global-setup.{ext}` — database seeding, env vars, mock initialization
- `tests/setup/global-teardown.{ext}` — cleanup after test runs
- `.env.test` — test-specific environment variables (never use production secrets)

### 3. Single-Command Execution
Create `scripts/run-tests.sh` that:
- Runs all test types in order: unit → integration → e2e → performance
- Shows coverage summary
- Saves full output to `tests/logs/run-YYYY-MM-DD.log`
- Returns exit code 0 only if ALL tests pass

---

## PHASED TESTING ROADMAP

For each phase in: {phases}

### Unit Tests (Phase Objectives)
For each function/class in this phase:
- **Happy path**: normal input → expected output
- **Edge cases**: empty, null, boundaries, zero, negative
- **Error conditions**: invalid input, missing required fields, type mismatches
- **Naming convention**: `test_[function]_[condition]_[expected_result]`

### Integration Tests
For each component interaction:
- Verify data flows correctly between modules
- Test with real database (test instance, not production)
- Mock only external APIs and third-party services
- Test the full HTTP request-response cycle for API endpoints

### Regression Tests
- After each bug fix, add a regression test that would have caught it
- Store in `tests/integration/regression/` with a comment linking to the bug

### Performance Tests
- Benchmark any function with documented performance requirements
- Test against the limits stated in README (e.g., "handles 1000 requests/sec")
- Store baseline metrics in `tests/performance/baselines.json`

### Fault Tolerance Tests
- Simulate: database connection failure, external API timeout, corrupted input data
- Assert: graceful error message, no data corruption, safe state after failure

---

## TEST QUALITY STANDARDS

Every test must follow:
- **Descriptive name**: explains the scenario, not just the function
- **Real assertions**: verify actual values, not just "no exception raised"
- **Independent**: each test can run in isolation without depending on test order
- **Fast**: unit tests < 100ms, integration tests < 5s each
- **Deterministic**: same input → same result every time
- **Self-cleaning**: create and destroy its own test data

---

## CI INTEGRATION

Create `.github/workflows/test.yml` (or equivalent):
```yaml
# Runs on every PR and push to main
# Steps:
# 1. Install dependencies
# 2. Set up test database
# 3. Run: scripts/run-tests.sh
# 4. Upload coverage report to artifact
# 5. Comment coverage delta on PR
# 6. Fail the build if coverage drops below threshold
```

---

## DELIVERABLES

1. Full test directory structure with config files
2. `tests/setup/` initialization files
3. `scripts/run-tests.sh` single-command runner
4. Test suite for all specified phases
5. CI workflow file
6. `tests/logs/` directory (gitignored except `.gitkeep`)
7. Initial coverage report in `tests/logs/coverage-baseline.txt`
```

## Variables to Customize

- **project_name**: Used in test file headers and CI comments
- **tech_stack**: Determines test framework, config format, and test syntax
- **phases**: Phases from your plan to generate tests for (add more later)

## Tips

- Start with unit tests — they're fastest to write and run
- The `tests/logs/` folder is gold — examine every test run output, don't just look at pass/fail
- Set coverage thresholds conservatively at first (70%) and raise them as you add more tests
- Regression tests are the most valuable long-term investment in your test suite
