---
title: "Project Plan Executor"
category: "priority"
tags: ["project-management", "execution", "phases", "workflow", "delivery"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "Drive systematic phase-by-phase execution of a project plan with built-in validation, documentation, and error handling at every step."
use_cases:
  - "Executing multi-phase project plans"
  - "Ensuring nothing is skipped between phases"
  - "Generating phase completion reports"
  - "Keeping AI assistants on-track during long sessions"
  - "Driving autonomous implementation"
variables:
  - name: "project_name"
    description: "Name of the project being executed"
    example: "Signal Analytics Dashboard"
  - name: "plan_file"
    description: "Path to the project plan markdown file"
    example: "docs/project_plan.md"
  - name: "current_phase"
    description: "Phase number or name to start execution from"
    example: "Phase 2"
  - name: "tech_stack"
    description: "Technologies and languages used in the project"
    example: "Python 3.11, FastAPI, PostgreSQL, Docker"
---

# Project Plan Executor

## Description
A structured execution prompt that drives a systematic, phase-by-phase delivery of any project plan. Enforces validation gates between phases, ensures documentation is updated after each step, and produces clean modular code throughout. Use this when you want an AI agent to *actually execute* your plan rather than just discuss it.

## Prompt

```
You are executing the project plan for **{project_name}**.

Reference plan: `{plan_file}`
Tech stack: {tech_stack}
Starting at: {current_phase}

Follow these execution rules strictly from start to finish.

---

## EXECUTION RULES

### Rule 1 — Phase Gate Discipline
- Complete 100% of the current phase before advancing
- At the end of each phase, run a gate check (see Phase Gate section below)
- Only proceed after the gate check passes
- If it fails, fix all issues before moving on

### Rule 2 — Code Quality Non-Negotiables
- Write modular, reusable, well-documented code
- Every function must have a docstring or inline comment explaining its purpose
- Add error handling (try/catch, input validation) for all I/O and network operations
- No hardcoded secrets — use environment variables
- No TODO comments left in delivered code

### Rule 3 — Documentation First
- Update `docs/project_plan.md` as each task completes (check the checkbox)
- Update `.gitignore` whenever new build artifacts or secrets are introduced
- Write a brief implementation note for each major component created

### Rule 4 — Test Before Declaring Done
- Test every feature as you build it — don't batch testing to the end
- For every function: test the happy path, one edge case, and one error condition
- Run the full test suite before closing any phase

---

## PHASE EXECUTION WORKFLOW

For each phase in `{plan_file}`, follow this sequence:

### Step 1 — Phase Briefing
- State the phase name, goal, and list of tasks
- Identify dependencies on prior phases
- Flag any ambiguities or missing information before starting

### Step 2 — Sub-task Breakdown
- Break each task into atomic sub-tasks (no sub-task should take more than ~30 min)
- Sequence sub-tasks by dependency order
- Identify which sub-tasks can be parallelized

### Step 3 — Implementation
For each sub-task:
1. Implement the feature/file/config
2. Add inline documentation
3. Write and run the test
4. Update `project_plan.md` checkbox
5. Note any discovered edge cases or follow-up items

### Step 4 — Phase Gate Check

Before closing the phase, verify ALL of the following:

```
PHASE GATE CHECKLIST — {current_phase}
[ ] All phase tasks checked off in project_plan.md
[ ] All new code has docstrings/comments
[ ] All tests pass (unit + integration)
[ ] No hardcoded credentials or secrets
[ ] .gitignore updated for any new artifacts
[ ] Documentation updated (README if user-facing changes)
[ ] No TODO or FIXME comments remaining
[ ] All imports resolve without errors
[ ] Build/run succeeds from a clean state
```

If any box is unchecked → fix it before calling the phase complete.

---

## FINAL PHASE PROTOCOL

When all phases are complete:

1. **End-to-End Test** — Run the full project workflow from entry point to output
2. **Documentation Audit** — Verify README, docs/, and inline comments are accurate
3. **Dependency Audit** — Confirm all packages in requirements.txt/package.json are used
4. **Clean Build** — Confirm the project builds/runs from a fresh clone with documented steps
5. **Release Prep** — Update CHANGELOG.md, bump version, tag the release

---

## DELIVERABLES

At completion you must provide:

1. Fully functional implementation organized by phases
2. All source files, configs, and tests
3. Updated `docs/project_plan.md` with all checkboxes checked
4. `CHANGELOG.md` entry for this delivery
5. A **Execution Summary** with:
   - Tasks completed vs. planned
   - Any scope changes made and why
   - Known limitations or follow-up items
   - Instructions for the next developer or session
```

## Variables to Customize

- **project_name**: The display name of your project
- **plan_file**: Path to your plan markdown (e.g., `docs/project_plan.md`, `ROADMAP.md`)
- **current_phase**: Phase to begin execution from (use "Phase 1" for a fresh start)
- **tech_stack**: Technologies so Claude picks the right idioms and tooling

## Example Usage

Use this at the start of a coding session when you want Claude to autonomously execute your project plan. Pair with Beast Mode for maximum autonomy. Point it at your actual plan file so it populates the phase tasks automatically.

## Tips

- Keep your `project_plan.md` broken into clearly named `## Phase N` sections with `- [ ]` checkboxes
- Use this prompt alongside `progress-tracker-plan-comparison.md` — run the tracker weekly, run this executor per session
- If the session runs long, add "Resume from Phase N, task X" to the {current_phase} variable
- The Phase Gate Checklist is the most valuable part — don't skip it

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
