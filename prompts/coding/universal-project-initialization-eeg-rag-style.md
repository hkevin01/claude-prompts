---
title: "Universal Project Initialization (EEG-RAG Style)"
category: "coding"
tags: ['project-initialization', 'architecture', 'folder-structure', 'documentation', 'pipelines']
difficulty: "advanced"
description: "Generate a complete project bootstrap plan, modular folder structure, pipeline framework, and rigorous documentation standards modeled after EEG-RAG"
author: "hkevin01"
date: "2026-04-01"
version: "1.0"
---

## Description

A reusable meta-prompt for generating production-grade project initialization plans with EEG-RAG-inspired structure, module boundaries, pipeline design, deployment layout, and strict documentation/requirement traceability standards.

## Prompt

```text
You are an expert software architect.
Given the following project description:

[INSERT PROJECT DESCRIPTION HERE]

Generate a complete project initialization plan modeled after the structure and design philosophy of the EEG-RAG repository.

Your output must include:

1. Full Folder Structure (EEG-RAG Style)
Produce a complete directory tree that includes:

Core Modules
- /src/ — main application logic
- /src/modules/ — modular components
- /src/pipelines/ — processing or workflow pipelines
- /src/utils/ — shared utilities
- /src/config/ — configuration files
- /src/services/ — external integrations

Data & Assets
- /data/raw/
- /data/processed/
- /data/examples/
- /assets/

Models / Checkpoints (if applicable)
- /models/
- /models/checkpoints/

Documentation
- /docs/
- /docs/architecture/
- /docs/diagrams/
- /docs/usage/

Scripts
- /scripts/
- /scripts/setup/
- /scripts/evaluation/

Environment & Config
- .env.example
- config.yaml
- settings.json

Testing
- /tests/
- /tests/unit/
- /tests/integration/

Deployment
- /deploy/
- /deploy/docker/
- /deploy/k8s/

2. Project Initialization Steps
Provide a detailed setup flow:
- Environment creation
- Dependency installation
- Directory bootstrapping
- Data download instructions
- Model download instructions (if applicable)
- How to run the first pipeline
- How to validate installation

3. Module-by-Module Explanation
For each folder in the structure:
- What belongs in it
- Why it exists
- How it interacts with other modules
- Example files that would live there

4. Pipeline Framework (EEG-RAG Inspired)
Create a reusable pipeline pattern:
- Input → Preprocessing → Core Processing → Postprocessing → Output
- Describe how pipelines should be registered
- Describe how they should be executed
- Provide a template pipeline file

5. Configuration Philosophy
Explain:
- How configs should be structured
- How environment variables should be used
- How to override configs for dev/prod
- How EEG-RAG’s config style maps to this project

6. Recommended Tech Stack
Provide:
- Languages
- Frameworks
- Libraries
- Tooling
- Rationale for each choice

7. Example Initialization Commands
Provide commands such as:
make setup
make run
python scripts/setup/init_project.py
python src/pipelines/run_pipeline.py --config config.yaml

8. Optional Enhancements
Include optional modules such as:
- Agents
- Retrieval systems
- Evaluation frameworks
- Visualization dashboards
- Data ingestion pipelines
- Monitoring & logging

9. Documentation & Function Commenting Standard (Required)
Define a high-level documentation standard and a per-function requirement contract.

9.1 Requirement ID & Traceability Standard
- Every requirement must have a unique ID (e.g., REQ-ARCH-001, REQ-FUNC-014, REQ-SEC-003).
- Each function must reference one or more requirement IDs.
- Add cross-references to related requirements and upstream/downstream dependencies.

9.2 Per-Function Documentation Template
For every function, include:
- ID
- Requirement(s)
- Purpose
- Rationale
- Inputs
- Outputs
- Preconditions
- Postconditions
- Assumptions
- Side effects
- Standard output behavior
- Failure modes
- Error handling strategy
- Constraints
- Verification approach (unit/integration/property tests)
- References to other requirements

9.3 Process-Wide Documentation Rules
- Apply the same standard consistently across modules, pipelines, services, and scripts.
- Ensure comments are technically precise and auditable.
- Include explicit invariants and non-functional constraints where relevant.
- Include examples of “good” function comments and anti-patterns to avoid.

STYLE REQUIREMENTS
The output must:
- Follow the same structural clarity as EEG-RAG
- Be modular, extensible, and clean
- Include diagrams when helpful
- Use tables for clarity
- Be deeply technical and precise
- Avoid generic boilerplate
- Tailor the structure to the specific project description
```

## Variables to Customize

- **Project Description**: Replace `[INSERT PROJECT DESCRIPTION HERE]` with your concrete system idea and constraints.

## Example Usage

Use this when you want an end-to-end initialization blueprint (structure + setup + architecture + documentation standard) for a new repository.

## Tips

- Include domain constraints (performance, security, compliance) in your project description.
- Ask for requirement traceability tables when working in regulated or safety-critical contexts.
- Request language-specific commenting templates to enforce consistency in CI checks.
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
