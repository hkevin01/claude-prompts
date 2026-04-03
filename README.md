# Claude Prompts Collection

A software-engineering prompt library for coding delivery and full SDLC execution in GitHub Copilot and Claude workflows.

## Project Overview

This repository curates high-rigor prompts that help teams move from idea to production with consistent quality gates.

- What it solves: inconsistent prompt quality, weak execution discipline, and missing SDLC structure
- Why it exists: to provide reusable prompts with engineering rigor, traceability, and delivery checklists
- Who it is for: developers, technical leads, and teams using AI-assisted software development

The repository is intentionally scoped to software work only.

## Key Features

| Feature | Description | Impact | Status |
|---|---|---|---|
| SDLC-Oriented Prompt Categories | Organized into `coding`, `workflow`, and `priority` | Clear separation between implementation and orchestration | Active |
| Engineering Rigor Baseline | Prompts include guard-first rules, setup/loop discipline, clean return patterns, and error taxonomy | More reliable, auditable outputs | Active |
| Cataloged Prompt Inventory | Central index in `CATALOG.md` | Faster discovery and prompt selection | Active |
| Reusable Prompt Template | Standardized authoring via `templates/prompt-template.md` | Consistency across new prompts | Active |
| Project Documentation Updater | Dedicated workflow prompt to update README with structured quality | Maintains docs fidelity as prompts evolve | Active |

## Architecture Overview

```text
						+-----------------------------+
						|        README.md            |
						|  (entrypoint + guidance)    |
						+-------------+---------------+
										  |
										  v
						+-----------------------------+
						|         CATALOG.md          |
						|  (prompt inventory index)   |
						+-------------+---------------+
										  |
		  +-----------------------+------------------------+
		  |                       |                        |
		  v                       v                        v
+---------------+      +----------------+      +----------------+
| prompts/coding|      |prompts/workflow|      |prompts/priority|
| implementation|      | SDLC orchestration     | execution ctrl |
| + technical   |      | + quality gates |      | + tracking     |
+---------------+      +----------------+      +----------------+
		  |
		  v
+------------------------+
| templates/prompt-template.md |
| standardized prompt schema   |
+------------------------+
```

### Component Breakdown

- `prompts/coding`: implementation-focused prompts (architecture, API, testing, debugging, optimization)
- `prompts/workflow`: process-focused prompts (phase execution, audits, iterative improvement, quality rules)
- `prompts/priority`: project-control prompts (execution and progress tracking)
- `CATALOG.md`: machine-readable/human-readable inventory surface
- `README.md`: project contract and onboarding guide

## Technology Stack (With Rationale)

| Technology | Why It Is Used | Alternatives Considered | Tradeoffs |
|---|---|---|---|
| Markdown (`.md`) | Portable, versionable prompt and doc format | JSON, YAML-only content stores | Less strict schema enforcement without extra tooling |
| YAML frontmatter | Lightweight metadata for prompt indexing | JSON sidecar files | Requires format discipline |
| Git + GitHub | Change history, reviewability, collaboration | Local-only storage | Requires branch hygiene |
| Copilot/Claude prompt execution | Operational target for prompt consumers | Other LLM tooling | Prompt behavior can vary by model/runtime |

## Repository Layout

```text
claude-prompts/
├── prompts/
│   ├── coding/             # 42 coding prompts
│   ├── workflow/           # 9 SDLC workflow prompts
│   └── priority/           # 3 execution-control prompts
├── templates/              # Prompt authoring template
├── CATALOG.md              # Prompt index
├── CHANGELOG.md            # Version history
└── README.md               # This file
```

## Setup & Installation Flow

### Prerequisites

- Git
- VS Code with GitHub Copilot Chat (or another Claude-compatible environment)

### Steps

1. Clone the repository.
2. Open the repository in VS Code.
3. Read `README.md` and `CATALOG.md`.
4. Choose a prompt category by intent:
	- coding task -> `prompts/coding`
	- SDLC orchestration -> `prompts/workflow`
	- execution tracking -> `prompts/priority`
5. Fill variables in selected prompt(s) using project goals, constraints, and tech stack.

No runtime build pipeline is required for core prompt usage.

## Usage Flow Diagram

```text
Project Brief
	|
	v
Select Prompt Category
	|
	+--> coding    -> implement feature/fix -> verify tests
	|
	+--> workflow  -> define phases/gates   -> enforce SDLC checks
	|
	+--> priority  -> track execution       -> compare plan vs actual
	|
	v
Update Docs and Catalog
	|
	v
Repeat Iteratively Until Release-Ready
```

## Core Capabilities

- Architecture planning and modernization
- API design and code generation scaffolding
- Refactoring and optimization support
- Test strategy definition and validation flows
- Debugging and failure-analysis workflows
- SDLC phase control, completion audits, and progress reporting
- README and project documentation updating

## API Overview

This is a prompt library repository and does not expose runtime API endpoints.

## Project Roadmap

| Phase | Timeline | Goals | Status |
|---|---|---|---|
| Scope Hardening | Current | Keep only software-focused prompt categories | In Progress |
| Prompt Rigor Standardization | Current | Enforce shared engineering rigor sections across prompts | In Progress |
| Prompt Consolidation | Next | Reduce duplicate legacy prompt variants | Planned |
| Validation Automation | Next | Add/update lightweight checks for metadata and links | Planned |
| Continuous Prompt QA | Ongoing | Maintain consistency as library evolves | Ongoing |

## Development Status

- Total prompts: 54
- Coding prompts: 42
- Workflow prompts: 9
- Priority prompts: 3
- Stability: active curation with ongoing cleanup
- Known limitations:
  - Some legacy duplicate prompt variants still exist in `prompts/coding`
  - Catalog and README must be refreshed after structural edits

## Why This Project Matters

AI-assisted development often fails at process discipline, not code generation capability. This repository addresses that gap by combining implementation prompts with SDLC orchestration prompts and explicit quality gates. The result is more predictable delivery and easier project handoff.

## Example Workflows

### 1. New Project Bootstrap

1. Use `prompts/workflow/universal-project-initialization.md`.
2. Generate phased plan with `prompts/priority/project-plan-executor.md`.
3. Run implementation tasks with selected `prompts/coding/*` prompts.

### 2. Ongoing Project Improvement

1. Use `prompts/workflow/iterative-improvement-workflow.md`.
2. Track gaps using `prompts/priority/progress-tracker-plan-comparison.md`.
3. Execute focused coding prompt updates and run quality gates.

### 3. Documentation Refresh

1. Use `prompts/workflow/universal-readme-generator.md` as the README updater.
2. Reconcile architecture, setup, and roadmap sections against actual repository state.

## Contributing Guide

1. Start from `templates/prompt-template.md`.
2. Add prompts only under `prompts/coding`, `prompts/workflow`, or `prompts/priority`.
3. Keep prompts specific, testable, and execution-oriented.
4. Preserve engineering rigor sections and SDLC gates.
5. Update `CATALOG.md` for any additions, removals, or renames.

## License

MIT License. You can use, modify, and distribute this prompt library with attribution under the license terms.
