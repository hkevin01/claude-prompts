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
