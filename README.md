# Claude Prompts Collection

A software-focused prompt library for coding execution and full SDLC delivery.

## Scope

This repository is intentionally limited to engineering prompts only:

- `coding`: implementation, architecture, APIs, refactoring, testing, debugging
- `workflow`: SDLC orchestration, phase execution, audits, operational standards
- `priority`: project execution and progress control prompts

Non-software categories are intentionally excluded.

## Repository Layout

```text
claude-prompts/
├── prompts/
│   ├── coding/             # Coding and architecture prompts
│   ├── workflow/           # SDLC and execution workflow prompts
│   └── priority/           # Project control and planning prompts
├── templates/              # Prompt authoring template
├── CATALOG.md              # Prompt index
├── CHANGELOG.md            # Version history
└── README.md
```

## Current Inventory

- Total prompts: 54
- Coding prompts: 42
- Workflow prompts: 9
- Priority prompts: 3

## Quick Start

1. Open `CATALOG.md` and select a prompt by objective.
2. Fill prompt variables with project context (goals, stack, constraints).
3. Run the prompt in GitHub Copilot Chat / Claude.
4. Execute outputs phase-by-phase and collect verification evidence.

## Recommended SDLC Flow

1. Start with `prompts/workflow/universal-project-initialization.md`.
2. Build execution plan with `prompts/priority/project-plan-executor.md`.
3. Track status using `prompts/priority/progress-tracker-plan-comparison.md`.
4. Implement with targeted coding prompts from `prompts/coding/`.
5. Validate quality via `prompts/workflow/phased-test-strategy.md` and `prompts/workflow/project-completion-audit.md`.
6. Update repository docs with `prompts/workflow/universal-readme-generator.md`.

## Engineering Rigor Baseline

All software prompts include:

- Guard-first function construction
- Explicit setup and loop discipline rules
- Clean return shape requirements
- Guard-linked, actionable error messages
- SDLC gates for scope, build, test, quality, security, docs, and release

## Contributing

1. Use `templates/prompt-template.md` for new prompts.
2. Add prompts only to `coding`, `workflow`, or `priority`.
3. Keep prompt instructions implementation-oriented and testable.
4. Update `CATALOG.md` for any additions, removals, or renames.

## License

MIT License.
