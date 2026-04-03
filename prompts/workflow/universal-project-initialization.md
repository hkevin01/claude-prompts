---
title: "Universal Project Initialization Blueprint"
category: "coding"
tags: ['project-initialization', 'architecture', 'folder-structure', 'documentation', 'pipelines']
difficulty: "advanced"
description: "Generate a complete project bootstrap plan, modular folder structure, pipeline framework, and rigorous documentation standards"
author: "hkevin01"
date: "2026-04-01"
version: "1.0"
---

## Description

A reusable meta-prompt for generating production-grade project initialization plans with clear structure, module boundaries, pipeline design, deployment layout, and strict documentation/requirement traceability standards.

## Prompt

```text
You are an expert software architect.
Given the following project description:

[INSERT PROJECT DESCRIPTION HERE]

Generate a complete project initialization plan modeled after production-grade repository structure and design principles.

Your output must include:

1. Full Folder Structure (Production Blueprint)
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

4. Pipeline Framework (Reusable Pattern)
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
- How this configuration style maps to this project

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
- Follow a clear, modular, production-ready structure
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
