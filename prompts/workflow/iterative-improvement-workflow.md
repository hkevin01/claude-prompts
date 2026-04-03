---
title: "Iterative Improvement Workflow"
category: "workflow"
tags: ["iterative", "improvement", "refactoring", "continuous-improvement", "workflow"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2026-04-02"
version: "2.0"
description: "A continuous improvement framework for evolving a working project — refining features, expanding coverage, and increasing quality iteratively without breaking what already works."
use_cases:
  - "Ongoing project maintenance and enhancement"
  - "Post-launch improvement cycles"
  - "Incorporating user feedback into the codebase"
  - "Technical debt reduction"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "API Gateway Service"
  - name: "improvement_focus"
    description: "The specific area to improve in this cycle"
    example: "performance, error handling, test coverage, documentation"
  - name: "plan_file"
    description: "Path to project_plan.md or equivalent"
    example: "docs/project_plan.md"
---

# Iterative Improvement Workflow

## Description
An iterative mode for projects that are already working but need ongoing refinement. Each improvement cycle follows a structured pattern: assess → plan → implement → test → document → update the plan. Designed to keep a project healthy and evolving without regression.

## Prompt

```
You are running an improvement cycle on **{project_name}**.

Focus area this cycle: {improvement_focus}
Plan file: `{plan_file}`

---

## IMPROVEMENT CYCLE RULES

1. **Complete one cycle fully** before starting another — partial improvements compound technical debt
2. **Never break existing tests** — if an improvement causes a test failure, fix it before continuing
3. **Update `{plan_file}` continuously** — mark completed items, add newly discovered tasks
4. **Document every change** — code comments for implementation decisions, docs for user-facing changes
5. **Refactor only for readability, not "reusability"** — extract functions when it makes code clearer, not for hypothetical future use

---

## IMPROVEMENT CYCLE STRUCTURE

### Phase A — Assessment
Before changing anything:
1. **Current state audit**
   - Read all files relevant to the focus area
   - List what works correctly
   - List what is fragile, slow, undocumented, or poorly tested
   - Identify the top 3 highest-impact improvements

2. **Risk assessment**
   - Which changes could break existing functionality?
   - What needs a rollback plan?
   - What can be changed safely without side effects?

3. **Improvement prioritization**
   | Improvement | Impact | Risk | Effort | Priority |
   |---|---|---|---|---|
   | Fix X | High | Low | Small | 🔴 Do first |
   | Refactor Y | Medium | Medium | Large | 🟡 Later |

### Phase B — Planning
For each prioritized improvement:
- Write the specific change in one sentence
- Identify which files will change
- Define what "done" looks like (acceptance criteria)
- Estimate: small (< 1hr) / medium (1-4hr) / large (> 4hr)

### Phase C — Implement
For each improvement:
1. Make the change
2. Preserve backward compatibility unless a breaking change is explicitly intended
3. Add/update comments and docstrings
4. If refactoring existing code: do not change behavior, only structure

### Phase D — Test
- Run the full existing test suite first — zero failures should remain after improvements
- Add new tests for any new behavior introduced
- Specifically test any code paths that were modified
- For performance improvements: add a benchmark before/after measurement

### Phase E — Document
- Update inline comments for changed logic
- Update `README.md` if the user-facing behavior changed
- Update `{plan_file}`:
  - Check off completed items
  - Add newly discovered improvements as future tasks
  - Update the "last improved" date

### Phase F — Review
Before closing the cycle:
- [ ] All planned improvements implemented
- [ ] All existing tests still pass
- [ ] New tests added for new behavior
- [ ] No regressions introduced
- [ ] Documentation updated
- [ ] `{plan_file}` updated

---

## CONTINUOUS IMPROVEMENT BACKLOG

Maintain a rolling backlog in `{plan_file}` with this structure:

```markdown
## Improvement Backlog

### High Priority
- [ ] [perf] Cache database query results in UserService
- [ ] [reliability] Add retry logic to external API calls

### Medium Priority
- [ ] [quality] Increase test coverage for auth module to >80%
- [ ] [docs] Document all public API endpoints with examples

### Low Priority / Future
- [ ] [refactor] Extract email template logic to separate module
```

---

## DELIVERABLES EACH CYCLE

1. Implemented improvements with documentation
2. Updated test suite (all passing)
3. Updated `{plan_file}` with completed items and new discoveries
4. A brief cycle summary:
   - What was improved
   - Metrics (test count, coverage, performance delta if applicable)
   - What was discovered and added to backlog
```

## Variables to Customize

- **project_name**: Project display name
- **improvement_focus**: The theme of this improvement cycle (e.g., "performance", "security", "test coverage")
- **plan_file**: Path to your plan/roadmap file so the AI keeps it updated

## Tips

- Run one improvement cycle per session — don't try to improve everything at once
- Start with "high impact, low risk" items (Phase A prioritization matrix)
- The "never break existing tests" rule is the most important — treat it as a hard constraint
- Commit after each completed improvement cycle with a descriptive commit message
