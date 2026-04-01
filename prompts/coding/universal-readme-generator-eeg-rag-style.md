---
title: "Universal README Generator (EEG-RAG Style)"
category: "coding"
tags: ['documentation', 'readme', 'architecture', 'api', 'technical-writing']
difficulty: "intermediate"
description: "Generate production-grade README documentation with deep structure, diagrams, tables, and project-specific rationale"
author: "hkevin01"
date: "2026-04-01"
version: "1.0"
---

## Description

A reusable meta-prompt for generating comprehensive, project-specific README files with the same depth and structure as a high-quality technical reference.

## Prompt

```text
You are an expert technical writer, architect, and developer advocate.
Given the following GitHub repository:

[INSERT GITHUB URL HERE]

Analyze the entire project and generate a complete, production-grade README with the same depth, structure, and sophistication as the EEG-RAG README.

Your README must include all of the following sections, written with clarity, precision, and technical depth:

1. Project Overview
- High-level description
- What problem it solves
- Why it exists
- Who it is for

2. Key Features (Table + Descriptions)
Create a table with columns:
| Feature | Description | Impact | Status |

3. Architecture Overview
Provide:
- High-level architecture diagram (ASCII)
- Component breakdown
- Data flow explanation
- How modules interact
- Where external services integrate

4. Technology Stack (With Rationale)
For each technology:
- What it is
- Why it was chosen
- Alternatives considered
- Tradeoffs

5. Setup & Installation Flow
Include:
- Prerequisites
- Environment variables
- Step-by-step installation
- Development vs production setup
- Optional components

6. Usage Flow Diagram
ASCII diagram showing:
- Inputs
- Processing stages
- Outputs
- Optional branches

7. Core Capabilities
Break down the system into capabilities such as:
- Retrieval
- Processing
- APIs
- UI
- Agents
- Pipelines
- Automation
- Evaluation

8. API Overview (If applicable)
List:
- Endpoints
- Methods
- Parameters
- Example requests
- Example responses

9. Project Roadmap (Gantt-Style Table)
Example format:
|Phase|Timeline|Goals|Status|
|---|---|---|---|

10. Development Status
Include:
- Version
- Stability
- Test coverage
- Lines of code
- Known limitations

11. Why This Project Matters
Explain:
- Industry context
- Research context
- Practical benefits
- Who gains the most

12. Example Workflows
Provide:
- CLI examples
- API examples
- UI examples
- End-to-end usage

13. Contributing Guide
Include:
- Branching strategy
- Code style
- Testing instructions
- How to submit PRs

14. License
Summarize the license in plain language.

15. Optional Enhancements
If the project supports them:
- Multi-agent systems
- Retrieval pipelines
- Evaluation frameworks
- Benchmarking
- Visualization dashboards
- Data ingestion pipelines

STYLE REQUIREMENTS
The README must:
- Be as detailed as the EEG-RAG README
- Use tables, diagrams, and structured sections
- Include ASCII architecture diagrams
- Provide deep technical explanations
- Be engaging, readable, and professional
- Include clear examples
- Avoid filler content
- Be project-specific, not generic
```

## Variables to Customize

- **Repository URL**: Replace `[INSERT GITHUB URL HERE]` with the target repository.

## Example Usage

Use this when you want a full, high-quality README generated from an existing project codebase.

## Tips

- Point the model to the full repository and key source files.
- Ask for strict project specificity to avoid generic output.
- Request updates iteratively when architecture or scope changes.