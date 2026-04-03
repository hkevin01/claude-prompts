---
title: "Copilot Focus & Context Configuration"
category: "workflow"
tags: ["copilot", "focus", "context", "configuration", "ai-setup"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "Generate a complete .copilot/ directory with focus guide, prompt examples, and project-specific Copilot configuration files to keep AI assistants on-task throughout the project lifecycle."
use_cases:
  - "Setting up Copilot context for a new project"
  - "Documenting AI assistance preferences"
  - "Creating reusable prompt files for recurring tasks"
  - "Onboarding Copilot to an existing codebase"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "E-commerce Platform"
  - name: "project_purpose"
    description: "What the project does"
    example: "A React + Node.js e-commerce platform with Stripe payments"
  - name: "tech_stack"
    description: "Technologies used"
    example: "React 18, Node.js, PostgreSQL, Docker"
  - name: "current_phase"
    description: "Current development phase"
    example: "Phase 2: Backend API development"
  - name: "standards"
    description: "Key coding standards to enforce"
    example: "TypeScript strict mode, ESLint Airbnb config, 80% test coverage"
---

# Copilot Focus & Context Configuration

## Description
Creates a complete `.copilot/` directory structure with configuration files that keep GitHub Copilot and other AI assistants focused and context-aware. Includes a focus guide, example prompt library, and project config — all customized to your project's specifics.

## Prompt

```
Create a `.copilot/` directory for **{project_name}** with the following three files:

---

### File 1: `.copilot/focus.md`

```markdown
# Focus Guide — {project_name}

## Project Overview
{project_purpose}

## Tech Stack
{tech_stack}

## Current Phase
{current_phase}

## Key Objectives
1. [Objective 1 — define from project context]
2. [Objective 2]
3. [Objective 3]

## Coding Standards
{standards}

## Guidelines for AI Assistants
- Assume this is a production project unless told otherwise
- Prefer simple, direct solutions — avoid over-engineering
- Check existing patterns before introducing new ones
- Every function needs error handling and a docstring
- Update .gitignore when adding new file types or build artifacts
- Never suggest deprecated APIs without flagging them as deprecated

## File Structure Reference
[Describe the src/ layout and key entry points]

## Out of Scope
- Infrastructure provisioning (handled separately)
- UI design decisions (use existing component library)
- [Add other out-of-scope areas]

## Useful Context
- Main entry point: [file]
- Config loaded from: [file or env vars]
- Tests run with: [command]
- Build with: [command]

*Refer to this file at the start of each session to stay on track.*
```

---

### File 2: `.copilot/prompts.md`

```markdown
# Project Prompt Library — {project_name}

A collection of recurring prompts tailored to this project.

## Setup & Initialization
- "Create a new [component/service/module] following the patterns in [existing file]."
- "Set up a virtual environment / node_modules and install all dependencies."
- "Add [feature] to the project, following the existing code style."

## Implementing Features
- "Implement [feature name] in {tech_stack} with error handling and tests."
- "Add a new REST endpoint for [resource] following the patterns in [existing route file]."
- "Create a new database migration for [change]."

## Refactoring
- "Refactor [file/function] for clarity — don't change behavior, only structure."
- "Extract the [logic] from [file] into a reusable utility in utils/."

## Testing
- "Write unit tests for [module] covering happy path, edge cases, and error conditions."
- "Generate integration tests for the [endpoint/service]."
- "Find untested code paths in [file] and write tests for them."

## Documentation
- "Update README.md to reflect the new [feature]."
- "Add JSDoc/docstrings to all public functions in [file]."
- "Generate an API reference for all endpoints in [router file]."

## Debugging
- "Diagnose why [symptom] happens. Check [suspected area] first."
- "Add logging to [component] to trace the data flow for [operation]."
```

---

### File 3: `.copilot/config.json`

```json
{
  "project": "{project_name}",
  "version": "1.0.0",
  "lastUpdated": "2026-04-02",
  "phase": "{current_phase}",
  "techStack": ["{tech_stack}"],
  "goals": [
    "Implement all phases in project_plan.md",
    "Maintain test coverage above 80%",
    "Keep documentation up to date"
  ],
  "focusAreas": [
    "Code readability and maintainability",
    "Error handling and resilience",
    "Test coverage",
    "Documentation accuracy"
  ],
  "conventions": {
    "naming": "camelCase for variables/functions, PascalCase for classes/components",
    "files": "kebab-case for filenames",
    "tests": "tests/ mirrors src/ structure",
    "commits": "conventional commits (feat:, fix:, docs:, chore:)"
  },
  "excludedFromSuggestions": [
    "node_modules",
    "dist",
    "build",
    ".env",
    "*.log"
  ]
}
```

After creating these files, add `.copilot/` to tracking in `.gitignore` exceptions so it IS committed (it's documentation, not a secret).
```

## Variables to Customize

- **project_name**: Used as the header in all three files
- **project_purpose**: One paragraph description for the focus guide
- **tech_stack**: Comma-separated list; used in focus guide and config.json
- **current_phase**: Updated each time you start a new development phase
- **standards**: Your linting rules, coverage requirements, TypeScript config level

## Tips

- Regenerate `.copilot/focus.md` at the start of each phase to update "current_phase"
- Commit changes to `.copilot/` after each phase — it serves as project documentation
- Copy prompts from `prompts.md` into your AI chat when starting recurring tasks
- The `config.json` is machine-readable — you can use it in scripts to auto-configure tooling

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
