---
title: "Project Setup & Modernizer"
category: "coding"
tags: ["project-setup", "modernization", "github", "configuration", "scaffolding"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "Analyze an existing project and fully modernize it — directory structure, config files, GitHub workflow files, Copilot config, VS Code settings, documentation, and more — all in one pass."
use_cases:
  - "Setting up a brand-new project from scratch"
  - "Modernizing an old project to current standards"
  - "Adding GitHub Actions, templates, and .vscode config"
  - "Establishing documentation structure"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "Signal Analytics API"
  - name: "project_description"
    description: "What the project does"
    example: "A FastAPI backend for processing and visualizing sensor data"
  - name: "tech_stack"
    description: "Primary language(s) and frameworks"
    example: "Python 3.11, FastAPI, PostgreSQL, Docker"
  - name: "team_size"
    description: "Number of developers"
    example: "1 (solo), 3, 10+"
---

# Project Setup & Modernizer

## Description
A comprehensive setup prompt that analyzes your project and produces a fully modernized structure — proper directories, config files, GitHub workflow templates, Copilot files, `.vscode` settings, documentation foundation, and a phased project plan. Run this once at project start or to rescue a messy legacy repo.

## Prompt

```
Analyze and modernize the project **{project_name}**.

Project description: {project_description}
Tech stack: {tech_stack}
Team size: {team_size}

First, examine any existing files to understand what the project is currently doing. Then apply each part below.

---

## PART 1: Directory Structure

Create a clean, logical layout:
```
{project_name}/
├── src/                    # All source code
│   ├── components/         # Reusable components (UI projects)
│   ├── services/           # Business logic and external integrations
│   ├── utils/              # Pure utility functions
│   ├── models/             # Data models and schemas
│   ├── routes/ or api/     # API routes / controllers
│   └── constants/          # App-wide constants
├── tests/                  # All tests (mirrors src/ structure)
├── docs/                   # All documentation
│   ├── project_plan.md     # Phased project plan with checkboxes
│   ├── api/                # API reference docs
│   └── architecture/       # Architecture decision records
├── scripts/                # Build, deploy, and dev helper scripts
├── config/                 # Environment-specific configuration
├── assets/ or data/        # Static files and data
└── [framework-specific dirs]
```

Move any misplaced files to their correct location. Document restructuring in CHANGELOG.md.

---

## PART 2: Core Configuration Files

Create or update:

- **`.gitignore`** — comprehensive for {tech_stack}; include virtualenv, build outputs, IDE files, secrets
- **`.editorconfig`** — consistent indentation and line endings for all file types
- **`.prettierrc`** or **`.eslintrc`** (if JS/TS) — enforce code style
- **`pyproject.toml`** / **`package.json`** / equivalent — verified, pinned dependencies
- **`.env.example`** — all required env vars with placeholder values and comments
- **`Makefile`** or **`scripts/`** — `make install`, `make test`, `make run`, `make build`

---

## PART 3: GitHub Files

Create `.github/` with:

**Workflow files:**
- `workflows/test.yml` — run tests on every push and PR
- `workflows/lint.yml` — run linting on every push
- `workflows/build.yml` — build and validate on main branch pushes

**Issue & PR templates:**
- `ISSUE_TEMPLATE/bug-report.yml` — structured bug report
- `ISSUE_TEMPLATE/feature-request.yml` — structured feature request
- `pull_request_template.md` — checklist for PRs

**Other:**
- `CONTRIBUTING.md` — branch naming, commit format, PR process
- `SECURITY.md` — how to report vulnerabilities

---

## PART 4: VS Code Configuration

Create `.vscode/` with:

**`settings.json`** including:
```json
{
  "chat.tools.autoApprove": true,
  "chat.agent.maxRequests": 100,
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "files.trimTrailingWhitespace": true,
  "[python]": { "editor.defaultFormatter": "ms-python.black-formatter" },
  "[typescript]": { "editor.defaultFormatter": "esbenp.prettier-vscode" },
  "python.analysis.typeCheckingMode": "strict",
  "typescript.preferences.strictNullChecks": true
}
```

Add naming convention enforcement rules for: Python (snake_case), TypeScript (camelCase/PascalCase), C++ (PascalCase classes, camelCase methods), Java (camelCase methods, PascalCase classes).

**`extensions.json`** — recommended extensions for {tech_stack}

**`launch.json`** — debug configurations for the main entry point

**`tasks.json`** — `Run Tests`, `Build`, `Lint` tasks

---

## PART 5: Copilot Configuration

Create `.copilot/` with:
- `focus.md` — project overview, current phase, AI assistant guidelines
- `prompts.md` — recurring prompts for common tasks in this project

---

## PART 6: Documentation Foundation

Create `docs/project_plan.md` with:
- Project goal and target users
- At least 5 phases, each with:
  - Phase title and objective
  - At least 5 detailed tasks with `[ ]` checkboxes
  - Dependencies on prior phases
  - Definition of done

Create `README.md` with:
- Project overview (what it does, who it's for)
- Quick start (install + run in under 5 commands)
- Directory structure overview
- Development setup instructions
- How to run tests
- Contributing guide link

---

## PART 7: Python-Specific Setup (if Python in stack)

- Create `venv/` virtual environment and add to `.gitignore`
- Create `requirements.txt` (pinned versions) and `requirements-dev.txt`
- Set up `pytest.ini` with coverage config
- Add `pyproject.toml` with Black + isort config

---

## PART 8: Finalize

- Update `.gitignore` for any new files/directories created
- Verify all imports and paths work
- Add a `CHANGELOG.md` entry for this modernization
- Check that `README.md` quick-start actually works step-by-step
```

## Variables to Customize

- **project_name**: Used in all documentation headers
- **project_description**: Drives README content and docs/project_plan.md goal section
- **tech_stack**: Determines which config files to create and which naming conventions to enforce
- **team_size**: Affects strictness of branching strategy and PR template requirements

## Tips

- Run "examine existing files first" — Claude shouldn't overwrite working code, only wrap it in structure
- For solo developers: skip `CONTRIBUTING.md` detail and simplify the PR template
- The `docs/project_plan.md` created here becomes the input for `project-plan-executor.md`
- Add `.vscode/` to `.gitignore` if you don't want to share settings with collaborators

## Engineering Rigor Standard

Use this checklist when executing the prompt. Treat every unchecked item as a delivery blocker.

### Requirements Quality

- Define explicit acceptance criteria before implementation.
- Capture assumptions, constraints, and out-of-scope items.
- Maintain bidirectional traceability: requirement -> design -> code -> test.
- Reject ambiguous requirements; request clarification or record assumptions.

### Design Quality

- Document architecture decisions and rejected alternatives.
- Specify component interfaces, contracts, and failure behaviors.
- Define data ownership, lifecycle, and schema evolution strategy.
- Identify safety, security, reliability, and performance risks up front.

### Implementation Quality

- Enforce deterministic behavior and idempotency for repeatable operations.
- Validate all external inputs at boundaries with explicit error messages.
- Use structured error handling with categorized failure codes.
- Avoid hidden global state and implicit side effects.
- Keep functions cohesive, testable, and bounded in responsibility.

### Function Construction Standard

- Guards first: validate preconditions at function entry and fail fast on invalid state.
- Setup phase: initialize required local state, dependencies, and defaults before core logic.
- Loop discipline (when needed): define loop invariants, explicit termination conditions, and max-iteration/time guards for unbounded workloads.
- Clean returns: return one well-defined result shape per success path; avoid ambiguous or partial return values.
- Guard-linked errors: each guard must emit a precise, actionable error message that names the failed condition and expected input/state.
- Error taxonomy: distinguish validation errors, domain errors, and system errors with consistent codes/messages.

### Verification & Validation

- Implement tests for happy path, edge cases, and failure modes.
- Add integration tests for cross-component contracts.
- Add regression tests for each bug fix.
- Verify non-functional requirements: latency, throughput, memory, and resilience.
- Record evidence of verification (commands, outputs, metrics, and artifacts).

### Security & Compliance

- Apply least privilege for credentials, services, and runtime permissions.
- Never hardcode secrets; use secure env/config mechanisms.
- Validate authn/authz paths and enforce auditability for sensitive actions.
- Include dependency and supply-chain checks in the workflow.

### SDLC Execution Gates

A phase is complete only when all gates pass:

- [ ] Scope gate: requirements are complete, versioned, and traceable.
- [ ] Build gate: build is reproducible from a clean checkout.
- [ ] Test gate: required test suites pass with evidence.
- [ ] Quality gate: lint/static checks pass; no critical warnings unresolved.
- [ ] Security gate: critical/high vulnerabilities addressed or risk-accepted in writing.
- [ ] Documentation gate: README, runbooks, and change notes updated.
- [ ] Release gate: rollback plan, monitoring hooks, and ownership are defined.

### Output Requirements

Every response generated from this prompt should include:

1. Objective and assumptions
2. Phased execution plan with gates
3. Implementation details and impacted files/components
4. Verification evidence and residual risk summary
5. Follow-up backlog prioritized by impact and risk
