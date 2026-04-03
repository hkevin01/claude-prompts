---
title: "Repository Cleanup & Organizer"
category: "coding"
tags: ["cleanup", "organization", "repository", "structure", "maintenance"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "A comprehensive repository cleanup prompt — analyze the current state, move misplaced files, eliminate dead code, consolidate duplicates, and produce a clean industry-standard layout with documentation."
use_cases:
  - "Cleaning up an inherited messy codebase"
  - "Pre-release organization pass"
  - "Removing legacy cruft from an old repo"
  - "Consolidating scattered files into proper structure"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "Legacy Payment System"
  - name: "tech_stack"
    description: "Language(s) and framework(s)"
    example: "Python, Django, PostgreSQL"
  - name: "target_standard"
    description: "Organizational standard to follow"
    example: "src-layout, feature-based, domain-driven"
---

# Repository Cleanup & Organizer

## Description
A thorough, systematic repository cleanup — from root folder to the deepest nested file. Covers analysis, reorganization, dead code removal, code consolidation, import path updates, and documentation. Produces a final summary of every change made.

## Prompt

```
Perform a comprehensive repository cleanup for **{project_name}**.

Tech stack: {tech_stack}
Target layout: {target_standard}

Start by examining every file and directory before making any changes. Build a complete picture first.

---

## PHASE 1: Assessment

### 1.1 Project Structure Audit
- Map the current directory tree
- Identify the project type and framework
- List all dependencies and which files import them
- Document the current architecture and identify patterns used

### 1.2 Problem Identification
List every issue found:
- Files in wrong locations
- Unused functions, classes, variables
- Dead code and unreachable blocks
- Duplicate code (identical or near-identical)
- Broken or missing imports
- Empty files or directories
- Docs that contradict the code

---

## PHASE 2: Target Structure

Design the clean target layout following {target_standard}:

```
{project_name}/
├── src/                    # Main source code
│   ├── [feature folders]
│   ├── utils/              # Shared utility functions
│   ├── models/             # Data models and types
│   └── constants/          # App-wide constants
├── tests/                  # All tests mirroring src/ structure
├── docs/                   # Documentation
├── scripts/                # Automation scripts
├── config/                 # Configuration files
└── [root configs]          # .gitignore, README, package files
```

Document the mapping: **old path → new path** for every file being moved.

---

## PHASE 3: Root Folder Cleanup

**Keep only essential root-level files:**
- README.md, LICENSE, .gitignore, .env.example
- Package/dependency files (package.json, requirements.txt, pyproject.toml, etc.)
- Configuration files (.prettierrc, .eslintrc, tsconfig.json, etc.)
- CI/CD entry points (.github/, .gitlab-ci.yml, Makefile)
- CHANGELOG.md, CONTRIBUTING.md, SECURITY.md

**Move everything else** to the appropriate subdirectory.

---

## PHASE 4: Code Reorganization

1. **Move files** to their target locations
2. **Rename files** to follow consistent naming conventions:
   - Python: `snake_case.py`
   - JS/TS: `kebab-case.ts` for files, `PascalCase.tsx` for components
   - CSS: `kebab-case.css`
3. **Update all import paths** throughout the codebase after every move
4. **Verify imports resolve** after every batch of moves

---

## PHASE 5: Dead Code Removal

Remove:
- [ ] Unused functions and methods (verify with grep/search before deleting)
- [ ] Unused imports and dependencies
- [ ] Commented-out code blocks older than the last release
- [ ] Empty files (add `.gitkeep` if the directory must remain)
- [ ] Orphaned test files for code that no longer exists

For each deletion, note: **what was removed and why**

---

## PHASE 6: Code Consolidation

- Merge duplicate functions into shared utilities
- Consolidate similar config files
- Create barrel exports (`index.js/ts`) where beneficial for cleaner imports
- Extract repeated inline logic into named utility functions

---

## PHASE 7: Docs Consolidation

If a `docs/` folder exists:
- Identify which plan/tracker files are outdated vs. current
- Archive outdated files to `docs/archive/`
- Consolidate scattered doc files into logical categories
- Verify no broken links in documentation

---

## PHASE 8: Final Validation

Run the following checks:
- [ ] Project builds/runs from a clean checkout
- [ ] All tests pass
- [ ] All imports resolve without error
- [ ] No files remain at incorrect paths
- [ ] .gitignore updated for any new build artifacts
- [ ] README.md still accurate after reorganization

---

## DELIVERABLES

1. **Reorganized project** with all files in correct locations
2. **Change log** — every file moved, renamed, or deleted
3. **Updated import paths** throughout the codebase
4. **Cleaned docs/** with archive of outdated files
5. **CHANGELOG.md entry** documenting this cleanup
6. **Summary report:**
   - Files moved: X
   - Files deleted: X
   - Duplicate code consolidated: X occurrences
   - Broken imports fixed: X
   - Test results after cleanup: X/X passed
```

## Variables to Customize

- **project_name**: Used in reports and change logs
- **tech_stack**: Determines naming conventions and which files to look for
- **target_standard**: The organizational pattern to apply (`src-layout`, `feature-based`, `flat`)

## Tips

- ALWAYS read files before moving them — don't move based on filenames alone
- Fix import paths IMMEDIATELY after each move — don't batch them at the end
- Keep a running "moved files" list as you go — it's easy to lose track
- Run tests after every phase, not just at the end
- Never delete code without first searching if it's imported anywhere

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
