---
title: "Project Progress Tracker & Plan Comparison"
category: "priority"
tags: ["project-management", "progress-tracking", "planning", "reporting", "milestones"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "Analyze project plan files and generate a comprehensive progress tracking document with status indicators, gap analysis, and actionable recommendations."
use_cases:
  - "Project status reporting"
  - "Sprint retrospectives"
  - "Multi-plan consolidation"
  - "Progress dashboard creation"
  - "Stakeholder communication"
variables:
  - name: "plan_files"
    description: "Paths to plan files to analyze (e.g., plan.md, plan_part1.md, plan_part2.md)"
    example: "docs/plan.md, docs/plan_part2.md"
  - name: "project_name"
    description: "Name of the project"
    example: "EEG Signal Processing Platform"
  - name: "report_date"
    description: "Date for the progress report"
    example: "2026-04-02"
  - name: "owner"
    description: "Project owner or team name"
    example: "Development Team"
---

# Project Progress Tracker & Plan Comparison

## Description
Analyze all project plan files and generate a master progress tracking document that consolidates tasks, exposes gaps, and provides an actionable dashboard. Ideal for solo developers and small teams who need a single source of truth across multiple planning documents.

## Prompt

```
Please analyze all project plan files ({plan_files}) and create a comprehensive progress tracking document for **{project_name}** as of {report_date}.

---

## Part 1: Plan Analysis & Consolidation

- Extract every task, milestone, and deliverable from each plan file
- Organize items by phase, category, or timeline
- Flag any overlapping or duplicate items across plan files
- Assign each unique task a short identifier (e.g., TCH-001, DOC-002)
- Note the source file for every item

---

## Part 2: Progress Status Master Table

For each task, populate the following columns:

| ID | Task | Phase | Priority | Status | Planned Date | Actual Date | Variance | Owner | Blockers | Notes |
|----|------|--------|----------|--------|-------------|------------|----------|-------|----------|-------|

**Status key:**
- ✅ Complete
- 🟡 In Progress
- ⭕ Not Started
- ❌ Blocked
- 🔄 Needs Review

**Priority key:**
- 🔴 Critical
- 🟠 High
- 🟡 Medium
- 🟢 Low

---

## Part 3: Visual Progress Dashboard

Generate summary metrics:

```
OVERALL COMPLETION: [X]%
━━━━━━━━━━━━━━━━━━━━ [██████████░░░░░░░░░░]

BY PHASE:
  Phase 1 - Setup:      [X]% ██████████
  Phase 2 - Core:       [X]% ████░░░░░░
  Phase 3 - Testing:    [X]% ██░░░░░░░░

HEALTH INDICATORS:
  ✅ Complete:        [X] tasks
  🟡 In Progress:    [X] tasks
  ⭕ Not Started:    [X] tasks
  ❌ Blocked:        [X] tasks
  ⏰ Overdue:        [X] tasks
  📅 Due this week:  [X] tasks
```

---

## Part 4: Comparison Matrix

Show planned vs. actual for key deliverables:

| Planned Item | Source File | Planned Date | Status | Actual Date | Variance | Notes |
|---|---|---|---|---|---|---|

---

## Part 5: Gap Analysis

Identify and report:

1. **Scope Additions** — Work completed that was never in the original plans
2. **Dropped Items** — Planned items that were cancelled or deprioritized (with reason)
3. **Missing Prerequisites** — Dependencies that must be resolved before blocked items can proceed
4. **Resource Gaps** — Areas with insufficient capacity or skill coverage

---

## Part 6: Actionable Recommendations

Provide a prioritized action list:

1. **Immediate (this week):** Blocked items that need resolution NOW
2. **Short-term (2 weeks):** Upcoming deadlines at risk
3. **Medium-term (1 month):** Plan adjustments recommended based on actual velocity
4. **Strategic:** Resource reallocation or scope changes to consider

---

## Format Requirements

- Use markdown with clear numbered headers
- Include `[ ]` checkboxes for all actionable items
- Timestamp every section: `*Last updated: {report_date} by {owner}*`
- Make the document easy to update weekly — leave update instructions at the top
- Add a "Quick Links" section at the top linking to each major section

---

## Example Task Entry

### [Phase 2] — API Integration Layer

- **ID**: TCH-007
- **Status**: 🟡 In Progress (45% complete)
- **Priority**: 🔴 Critical
- **Planned**: March 15 – March 28, 2026
- **Actual Start**: March 18, 2026 | **Est. Completion**: April 5, 2026
- **Variance**: +8 days delay
- **Blocker**: Waiting for third-party API credentials from vendor
- **Owner**: {owner}
- **Depends On**: TCH-005 (Database schema finalized)
- **Notes**: OAuth flow implemented; data mapping 60% done; blocked on credentials
```

## Variables to Customize

- **plan_files**: Comma-separated paths to all plan/tracker markdown files in your project
- **project_name**: Your project's full name for report headers
- **report_date**: ISO date of the report (YYYY-MM-DD)
- **owner**: Your name or team name for audit trail

## Example Usage

Paste this prompt at the start of a session and point Claude at your `/docs` folder. Works best with `plan.md`, `ROADMAP.md`, `project_plan.md`, or any phase-based planning documents.

## Tips

- Run this weekly and commit the output as `docs/progress-YYYY-MM-DD.md`
- Use the Comparison Matrix to catch scope creep early
- Keep the dashboard section at the top so it's instantly visible in GitHub
- Link blocked items directly to the relevant GitHub Issue numbers
