---
title: "Universal README Generator & Updater"
category: "workflow"
tags: ['documentation', 'readme', 'architecture', 'technical-writing', 'mermaid', 'badges', 'github']
difficulty: "intermediate"
description: "Generate showcase-grade README documentation using every GitHub-supported visual element: Mermaid diagrams, shields.io badges, collapsible sections, anchor TOC, Gantt roadmap, mindmaps, and more."
author: "hkevin01"
date: "2026-04-01"
version: "2.0"
---

## Description

A production-grade meta-prompt for generating or updating project README files to the highest visual and structural standard supported by GitHub Flavored Markdown. Output leverages every available GitHub rendering feature: Mermaid diagram suite, shields.io badges, collapsible sections, keyboard shortcuts, GitHub Alerts, anchor navigation, contributor grids, and richly structured tables.

---

## Prompt

```text
You are an expert technical writer, developer advocate, and open-source maintainer.

Given the following GitHub repository:

[INSERT GITHUB URL HERE]

Analyze the entire project and generate a COMPLETE, showcase-quality README.md that uses every relevant GitHub-supported visual and structural element.

====================================================================
SECTION A — REQUIRED VISUAL ELEMENTS
====================================================================

1. BANNER HEADER (HTML centered block)
   Use HTML for the banner — GitHub renders this correctly in markdown:

   <div align="center">
     <h1>🚀 Project Name</h1>
     <p><em>One-sentence tagline that captures the essence of the project.</em></p>
   </div>

2. BADGES ROW (shields.io)
   Place immediately below the banner. Use real, dynamic shields.io badge URLs.
   Required badge types (adapt slug/color to project):

   [![License](https://img.shields.io/github/license/USER/REPO?style=flat-square)](LICENSE)
   [![GitHub Stars](https://img.shields.io/github/stars/USER/REPO?style=flat-square)](https://github.com/USER/REPO/stargazers)
   [![GitHub Forks](https://img.shields.io/github/forks/USER/REPO?style=flat-square)](https://github.com/USER/REPO/network)
   [![Last Commit](https://img.shields.io/github/last-commit/USER/REPO?style=flat-square)](https://github.com/USER/REPO/commits/main)
   [![Repo Size](https://img.shields.io/github/repo-size/USER/REPO?style=flat-square)](https://github.com/USER/REPO)
   [![Issues](https://img.shields.io/github/issues/USER/REPO?style=flat-square)](https://github.com/USER/REPO/issues)

   Add technology-specific badges where relevant:
   [![Python](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square&logo=python)](https://python.org)
   [![Node](https://img.shields.io/badge/node-20%2B-green?style=flat-square&logo=node.js)](https://nodejs.org)
   [![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-74aa9c?style=flat-square&logo=openai)](https://openai.com)

3. TABLE OF CONTENTS
   Full anchor-linked TOC covering every major section.
   Format:

   ## Table of Contents
   - [Overview](#overview)
   - [Key Features](#key-features)
   - [Architecture](#architecture)
   - [Technology Stack](#technology-stack)
   - [Setup & Installation](#setup--installation)
   - [Usage](#usage)
   - [Roadmap](#roadmap)
   - [Contributing](#contributing)
   - [License](#license)

   Rules:
   - Anchor text must be lowercase, spaces replaced with hyphens, special chars removed.
   - Use nested list items for subsections.

4. GITHUB ALERTS (callout blocks)
   Use GitHub's native alert syntax for important callouts:

   > [!NOTE]
   > Use this for informational notes that are helpful but not critical.

   > [!TIP]
   > Use this for pro tips and best practices.

   > [!IMPORTANT]
   > Use this section for critical information the reader must not miss.

   > [!WARNING]
   > Use this for actions or states that can cause problems.

   > [!CAUTION]
   > Use this for dangerous actions that can cause irreversible harm.

5. MERMAID DIAGRAMS
   GitHub renders Mermaid natively using fenced code blocks with "mermaid" language tag.
   REQUIRED: Include a minimum of THREE distinct Mermaid diagram types. Choose the types
   most appropriate for the project from the following supported set:

   a) FLOWCHART — Architecture or data flow:
   ```mermaid
   flowchart TD
     A[Input] --> B[Processing]
     B --> C{Decision}
     C -->|Yes| D[Output A]
     C -->|No| E[Output B]
   ```

   b) SEQUENCE DIAGRAM — Usage or API interaction flow:
   ```mermaid
   sequenceDiagram
     participant User
     participant API
     participant DB
     User->>API: POST /request
     API->>DB: query()
     DB-->>API: result
     API-->>User: 200 OK
   ```

   c) PIE CHART — Distribution breakdown:
   ```mermaid
   pie title Category Distribution
     "Category A" : 60
     "Category B" : 25
     "Category C" : 15
   ```

   d) GANTT CHART — Project roadmap:
   ```mermaid
   gantt
     title Project Roadmap
     dateFormat  YYYY-MM-DD
     section Phase 1
       Foundation     :done,    f1, 2024-01-01, 2024-03-01
       Core Features  :active,  f2, 2024-03-01, 2024-06-01
     section Phase 2
       Advanced       :         f3, 2024-06-01, 2024-09-01
   ```

   e) CLASS DIAGRAM — Object model (when applicable):
   ```mermaid
   classDiagram
     class ComponentA {
       +string name
       +process()
     }
     ComponentA --> ComponentB : uses
   ```

   f) MINDMAP — Domain taxonomy:
   ```mermaid
   mindmap
     root((Project))
       Module A
         Feature 1
         Feature 2
       Module B
         Feature 3
   ```

   g) QUADRANT CHART — Priority / impact matrix:
   ```mermaid
   quadrantChart
     title Feature Priority Matrix
     x-axis Low Effort --> High Effort
     y-axis Low Impact --> High Impact
     quadrant-1 Plan carefully
     quadrant-2 Ship first
     quadrant-3 Skip for now
     quadrant-4 Consider later
     Feature A: [0.2, 0.8]
     Feature B: [0.7, 0.6]
   ```

   h) TIMELINE — Release or milestone history:
   ```mermaid
   timeline
     title Release History
     2024-Q1 : v1.0 - Initial release
     2024-Q2 : v1.5 - Performance upgrade
     2024-Q3 : v2.0 - Major feature drop
   ```

   i) GIT GRAPH — Branching strategy:
   ```mermaid
   gitGraph
     commit id: "Init"
     branch feature
     checkout feature
     commit id: "Feature work"
     checkout main
     merge feature id: "Merge"
   ```

   j) XY CHART — Trend data:
   ```mermaid
   xychart-beta
     title "Performance Over Releases"
     x-axis ["v1.0", "v1.5", "v2.0"]
     y-axis "Requests/sec" 0 --> 1000
     bar [200, 500, 900]
   ```

6. COLLAPSIBLE SECTIONS
   Use HTML <details>/<summary> for long content that would otherwise dominate the page:

   <details>
   <summary>📋 Full Feature List</summary>

   Put the long content here — tables, code blocks, lists, etc.

   </details>

   Use collapsible sections for: full API docs, exhaustive configuration lists,
   complete changelog, advanced usage examples, full dependency lists.

7. KEYBOARD SHORTCUTS
   Use <kbd> tags for keyboard shortcut documentation:
   Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop the server.

8. FEATURE TABLE (with Status column)
   | Icon | Feature | Description | Impact | Status |
   |------|---------|-------------|--------|--------|
   | 🔍 | Feature Name | What it does and why it matters | High | ✅ Stable |

9. TECHNOLOGY STACK TABLE (with Rationale column)
   | Technology | Purpose | Why Chosen | Alternatives |
   |------------|---------|------------|--------------|
   | Tool | Role in system | Key reason for selection | What was rejected |

10. BACK-TO-TOP LINKS
    End every major section with:
    <p align="right">(<a href="#top">back to top ↑</a>)</p>

====================================================================
SECTION B — REQUIRED CONTENT SECTIONS
====================================================================

Generate content for all of the following sections. Populate every section
with project-specific facts, not generic placeholders.

11. PROJECT OVERVIEW
    - One-paragraph high-level description
    - What specific problem this solves
    - Category/domain context (e.g., "AI tooling", "DevOps automation")
    - Who it is for (specific persona: solo devs, teams, enterprise, etc.)

12. KEY FEATURES
    Feature table (Section A item 8) plus:
    - 3–5 bullet points expanding on the most impactful features
    - Performance metrics or benchmarks if available

13. ARCHITECTURE OVERVIEW
    - Mermaid flowchart (Section A item 5a) showing main components
    - Component responsibility summary
    - External service integration points
    - Data flow narrative (1–2 paragraphs)

14. USAGE FLOW
    - Mermaid sequence diagram (Section A item 5b) showing user interaction
    - Step-by-step usage instructions
    - CLI examples in fenced bash blocks with realistic inputs/outputs

15. CATEGORY / DISTRIBUTION BREAKDOWN (where applicable)
    - Mermaid pie chart (Section A item 5c) showing breakdown
    - Table with count and percentage per category

16. TECHNOLOGY STACK
    Tech stack table (Section A item 9) with full rationale.

17. SETUP & INSTALLATION
    Step-by-step with fenced code blocks:
    - Prerequisites
    - Clone instructions
    - Dependency installation
    - Environment variable setup (reference .env.example)
    - Verification step

18. CORE CAPABILITIES
    Subsections per capability area. Use emoji section headers.
    Use GitHub Alerts (Section A item 4) to call out tips and warnings.

19. PROJECT ROADMAP
    - Mermaid Gantt chart (Section A item 5d) for visual timeline
    - Table version: Phase | Goals | Target | Status

20. DEVELOPMENT STATUS
    Table showing: Version | Stability | Coverage | Known Limitations

21. CONTRIBUTING
    - Fork → Branch → Commit → PR workflow
    - Collapsible section (Section A item 6) for detailed guidelines
    - Code style, testing requirements

22. LICENSE & ACKNOWLEDGEMENTS
    - License summary in plain language
    - Credits: inspiration, referenced work, contributors

====================================================================
SECTION C — QUALITY & STYLE REQUIREMENTS
====================================================================

MUST meet all of the following:

- Use emoji section headers to aid navigation and visual hierarchy
- Every section must contain project-specific content — zero generic placeholders
- All Mermaid diagram node/label text must reference actual project components
- All badge URLs must use the actual GitHub repo slug (USER/REPO)
- All code examples must be realistic and runnable
- Tables must be properly aligned and use GitHub Markdown pipe syntax
- Use GitHub Alerts (NOTE/TIP/IMPORTANT/WARNING/CAUTION) at least 2 times
- Include at least 3 collapsible <details> sections
- Include at least one back-to-top link per major section
- The README must be scannable in 30 seconds and deeply readable in 5 minutes
- No filler content, no lorem ipsum, no vague statements
- Total length: aim for 400–700 lines of Markdown for a comprehensive project
- Do NOT include HTML comments in the final output
```

---

## Variables to Customize

| Variable | Description | Example |
|----------|-------------|---------|
| `[INSERT GITHUB URL HERE]` | Target GitHub repository URL | `https://github.com/owner/repo` |
| `USER/REPO` | GitHub owner/repo slug for badge URLs | `hkevin01/claude-prompts` |
| Diagram types | Choose 3+ from the supported Mermaid set | flowchart + pie + gantt |
| Collapsible content | Long lists, full API docs, changelogs | dependency tree, full config |

---

## Example Usage

Point this prompt at any repository and it will produce a fully visualized, standards-compliant README. Use it:

- When creating a README from scratch
- When upgrading an outdated README
- When a project grows to need better documentation structure
- To standardize README format across an organization

---

## Tips

- Provide the full repository URL including README, source files, and structure
- For large repos, also provide `ls -R` output or a file tree
- Request strict project-specificity — generic content defeats the purpose
- When updating existing READMEs, supply the current README and ask for a "diff-aware upgrade"
- The Mermaid pie chart for prompt/feature distribution is especially effective for library projects
- Run through the GitHub rendering preview to verify all Mermaid diagrams render correctly

---

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
