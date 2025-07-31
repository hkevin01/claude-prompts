---
title: "Task Prioritizer"
category: "personal"
tags: ["productivity", "planning", "organization", "time-management"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Prioritize tasks based on importance, urgency, and available resources"
use_cases:
  - "Daily task planning"
  - "Project management"
  - "Workflow optimization"
  - "Decision making"
variables:
  - name: "tasks"
    description: "List of tasks to prioritize"
    example: "Write proposal, Answer emails, Team meeting, Budget review, Client call"
  - name: "constraints"
    description: "Time, resource, or other limitations"
    example: "Only 4 hours available today, need proposal done by Friday"
  - name: "goals"
    description: "Current priorities or objectives"
    example: "Close Q4 deals, improve team efficiency"
---

# Task Prioritizer

## Description
Analyze and prioritize your tasks using proven productivity frameworks. Get a clear action plan that maximizes your effectiveness and helps you focus on what matters most.

## Prompt

```
Please help me prioritize the following tasks and create an action plan:

**Tasks to Prioritize:**
{tasks}

**Current Constraints:**
{constraints}

**Primary Goals:**
{goals}

Please analyze these tasks using multiple prioritization frameworks:

1. **Eisenhower Matrix** (Urgent vs Important):
   - Quadrant 1: Urgent + Important (Do First)
   - Quadrant 2: Important, Not Urgent (Schedule)
   - Quadrant 3: Urgent, Not Important (Delegate)
   - Quadrant 4: Neither Urgent nor Important (Eliminate)

2. **Impact vs Effort Analysis**:
   - High Impact, Low Effort (Quick Wins)
   - High Impact, High Effort (Major Projects)
   - Low Impact, Low Effort (Fill-in Tasks)
   - Low Impact, High Effort (Avoid/Minimize)

3. **Goal Alignment Score** (1-10):
   Rate how well each task supports your primary goals

**Output Format:**
- **Today's Top 3**: Most critical tasks for immediate action
- **This Week**: Important tasks to schedule
- **Delegate/Defer**: Tasks to handle differently
- **Consider Eliminating**: Low-value activities

For each prioritized task, include:
- Priority rank and rationale
- Estimated time needed
- Best time of day to tackle it
- Any dependencies or prerequisites
- Success metrics

End with a recommended daily schedule and productivity tips based on the analysis.
```

## Variables to Customize

- **{tasks}**: List all tasks, projects, or activities you need to prioritize
- **{constraints}**: Time limits, resource constraints, deadlines, energy levels
- **{goals}**: Short-term and long-term objectives, key priorities

## Usage Examples

### Example 1: Daily Work Planning
**Input Variables:**
- tasks: "Write proposal, Answer emails, Team meeting, Budget review, Client call"
- constraints: "Only 4 hours available today, need proposal done by Friday"
- goals: "Close Q4 deals, improve team efficiency"

**Expected Output:**
Prioritized task list with time blocks, rationale for each priority, and a structured daily schedule.

### Example 2: Personal Life Organization
**Input Variables:**
- tasks: "Grocery shopping, Exercise, Pay bills, Call family, Home repairs, Book vacation"
- constraints: "Weekend only, limited budget this month"
- goals: "Better work-life balance, save money for vacation"

**Expected Output:**
Balanced priority list considering personal well-being, financial constraints, and life goals.

## Tips for Best Results

- Be honest about time constraints and energy levels
- Include both work and personal tasks if relevant
- Specify deadlines and dependencies between tasks
- Mention your peak productivity times (morning person, night owl, etc.)
- Include the context of your current workload and stress level
- Ask for follow-up advice on maintaining the prioritization system

## Related Prompts

- [Goal Setting Framework](goal-setting-framework.md)
- [Time Blocking Assistant](time-blocking-assistant.md)
- [Energy Management Guide](../educational/energy-management-guide.md)

## Changelog

- **v1.0** (2025-07-31): Initial version with multiple prioritization frameworks
