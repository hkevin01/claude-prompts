---
title: "Phase-by-Phase Implementation Guide"
category: "workflow"
tags: ["implementation", "phases", "planning", "workflow", "delivery"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "A disciplined phase-by-phase implementation framework that enforces complete delivery of each phase before advancing, with mandatory testing, error handling, and documentation at every step."
use_cases:
  - "Starting a new project from a plan"
  - "Onboarding an AI to an existing phased roadmap"
  - "Ensuring consistent quality across phases"
  - "Team handoff between development phases"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "REST API Backend"
  - name: "tech_stack"
    description: "Languages and frameworks"
    example: "Node.js, Express, MongoDB"
  - name: "phase_list"
    description: "List of phase names"
    example: "Phase 1: Setup, Phase 2: Core API, Phase 3: Auth, Phase 4: Tests"
---

# Phase-by-Phase Implementation Guide

## Description
Gives an AI assistant clear rules for working through a phased project plan — one phase at a time, with clean code, proper testing, and documentation updates baked into the workflow. Prevents the common failure mode of skipping phases or delivering incomplete work.

## Prompt

```
You are implementing **{project_name}** using the following tech stack: {tech_stack}

Phases to execute: {phase_list}

Follow every instruction below for every phase, without skipping steps.

---

## GENERAL RULES

- **Complete each phase fully** before moving to the next — no partial phases
- **Write modular code** — functions should do one thing and be reusable
- **Document as you go** — every non-trivial function needs a comment or docstring
- **Handle errors** — wrap all I/O, network calls, and external services in proper error handling
- **Update .gitignore** every time you add build artifacts, secrets, or generated files
- **No hardcoded credentials** — use environment variables; add them to `.env.example`

---

## PER-PHASE WORKFLOW

### Step 1 — Phase Kickoff
State:
- Phase name and goal
- Complete task list for this phase
- Dependencies on prior phases
- Any ambiguities you need to clarify before starting

### Step 2 — Implement Each Task
For each task in the phase:
1. Break it into sub-tasks
2. Implement each sub-task
3. Add inline documentation
4. Add configuration flexibility where relevant (no magic numbers/strings)

### Step 3 — Error Handling Pass
After implementing:
- Wrap all external calls with try/catch (or equivalent)
- Add meaningful error messages that tell the user what went wrong and how to fix it
- Validate inputs at function boundaries

### Step 4 — Test the Phase
- Write unit tests for new functions
- Write integration tests for component interactions
- Run all tests; fix every failure before marking the phase complete

### Step 5 — Document the Phase
- Add usage instructions for any new feature or CLI command
- Update `README.md` if this phase adds user-facing functionality
- Add a brief comment at the top of new files explaining their purpose

### Step 6 — Phase Wrap-up
Confirm:
- [ ] All tasks implemented
- [ ] All tests pass
- [ ] Documentation updated
- [ ] .gitignore updated
- [ ] No hardcoded secrets
- [ ] No TODO/FIXME left in new code

---

## FINAL PHASE

When all phases are complete:

1. **End-to-end test** — run the complete project from entry to output
2. **README audit** — verify every example in README still works
3. **Dependency cleanup** — remove unused packages
4. **Release prep** — update CHANGELOG.md, bump version in package/config file

---

## DELIVERABLES

At completion:
- Fully working project organized by phases
- All source code, configs, and tests
- Updated documentation
- CHANGELOG entry with what was built
```

## Variables to Customize

- **project_name**: Project display name
- **tech_stack**: Specify language + framework + database so Claude uses the right idioms
- **phase_list**: Comma-separated phase names matching your plan document

## Tips

- Paste your actual phase task lists after this prompt for maximum context
- If a phase is taking too long in one session, save state and use `project-plan-executor.md` to resume
- The error handling pass (Step 3) is often skipped — don't skip it
