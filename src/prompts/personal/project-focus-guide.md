---
title: "Project Focus and Context Guide"
category: "personal"
tags: ["focus", "context", "project-management", "development-guidance"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Create focused context guides for AI assistants working on specific projects"
use_cases:
  - "AI assistant context setting"
  - "Project onboarding"
  - "Development focus maintenance"
  - "Team collaboration guidance"
variables:
  - name: "project_name"
    description: "Name of the project"
    example: "E-commerce Platform Redesign"
  - name: "project_purpose"
    description: "Main purpose and goals of the project"
    example: "Modernize legacy e-commerce system with improved UX and performance"
  - name: "key_technologies"
    description: "Main technologies and frameworks used"
    example: "React, Node.js, PostgreSQL, Docker"
  - name: "current_phase"
    description: "Current development phase or sprint"
    example: "Phase 2: Frontend component development"
---

# Project Focus and Context Guide

## Description
Create comprehensive focus guides that help AI assistants and team members maintain context and direction while working on specific projects.

## Prompt

```
Create a comprehensive focus guide for my project that will help AI assistants stay on track and provide relevant assistance.

**Project Name:** {project_name}
**Project Purpose:** {project_purpose}
**Key Technologies:** {key_technologies}
**Current Phase:** {current_phase}

## CREATE FOCUS GUIDE:

### Project Overview Section
Create a clear, concise overview that includes:

**Project Summary:**
- Main goals and objectives
- Target audience or users
- Key success metrics
- Timeline and milestones

**Technical Context:**
- Technology stack and architecture
- Development environment setup
- Key dependencies and integrations
- Database schema and data models

### Current State and Objectives
Document the current development state:

**Current Phase Details:**
- What we're working on now
- Immediate priorities and deadlines
- Blockers or challenges
- Next milestones

**Key Objectives:**
1. Primary goal for this phase
2. Secondary objectives
3. Success criteria
4. Quality standards to maintain

### Guidelines for AI Assistance
Provide specific guidance for AI helpers:

**Focus Areas:**
- Prioritize suggestions related to current phase objectives
- Maintain consistency with established patterns and conventions
- Consider performance and scalability implications
- Ensure security best practices

**Code Standards:**
- Naming conventions and style guidelines
- Testing requirements and coverage expectations
- Documentation standards
- Error handling patterns

**What to Prioritize:**
- Features that support main user workflows
- Code quality and maintainability improvements
- Performance optimizations for identified bottlenecks
- Security enhancements and vulnerability fixes

**What to Avoid:**
- Premature optimization in non-critical areas
- Over-engineering for hypothetical future requirements
- Breaking changes without clear migration paths
- Adding complexity without clear benefits

### Useful Context and Notes
Include project-specific information:

**Architecture Decisions:**
- Key design patterns being used
- Why certain technologies were chosen
- Trade-offs and compromises made
- Areas marked for future refactoring

**Domain Knowledge:**
- Business rules and constraints
- User personas and use cases
- Integration requirements
- Compliance or regulatory considerations

**Development Workflow:**
- Branching strategy and release process
- Code review requirements
- Testing and deployment procedures
- Documentation maintenance

### Quick Reference
Provide easy access to:

**Important Files and Directories:**
- Configuration files
- Main entry points
- Key documentation
- Test directories

**Useful Commands:**
- Build and development commands
- Testing and linting commands
- Deployment procedures
- Debugging tools

**External Resources:**
- API documentation
- Design systems or style guides
- Third-party service documentation
- Team communication channels

## OUTPUT FORMAT:
Create a well-structured markdown file that can be saved as `.copilot/focus.md` or similar, containing:

1. **Project Overview** - Clear summary and context
2. **Current Objectives** - What we're working on now
3. **Development Guidelines** - How to approach tasks
4. **Technical Context** - Architecture and technology details
5. **Quality Standards** - Code quality and testing expectations
6. **Quick Reference** - Useful commands and resources

The guide should be:
- Scannable and easy to reference quickly
- Updated regularly as the project evolves
- Specific enough to guide decision-making
- Comprehensive enough to onboard new team members

This focus guide will help maintain consistency and direction throughout the development process.
```

## Variables to Customize

- **{project_name}**: The specific name or identifier for your project
- **{project_purpose}**: High-level goals and purpose of the project
- **{key_technologies}**: Main technologies, frameworks, and tools being used
- **{current_phase}**: Current development phase, sprint, or focus area

## Usage Examples

### Example 1: Web Application Project
**Input Variables:**
- project_name: "Customer Portal Redesign"
- project_purpose: "Create modern, responsive customer portal with improved UX"
- key_technologies: "Vue.js, Express.js, MongoDB, Tailwind CSS"
- current_phase: "Phase 1: User authentication and dashboard components"

**Expected Output:**
Comprehensive focus guide with Vue.js specific guidelines, authentication context, and dashboard development priorities.

### Example 2: API Development
**Input Variables:**
- project_name: "Inventory Management API"
- project_purpose: "Build scalable REST API for multi-tenant inventory system"
- key_technologies: "Python, FastAPI, PostgreSQL, Redis, Docker"
- current_phase: "Sprint 3: Product catalog endpoints and caching layer"

**Expected Output:**
API-focused guide with FastAPI patterns, database optimization context, and caching implementation guidelines.

## Tips for Best Results

- Update the focus guide regularly as the project evolves
- Include specific examples of current challenges or decisions
- Reference existing documentation and architectural decision records
- Include team-specific conventions and preferences
- Make it actionable with clear do's and don'ts
- Consider creating separate focus guides for different project phases

## Related Prompts

- [Project Planning Assistant](../business/project-planning.md)
- [Documentation Generator](../business/documentation-generator.md)
- [Development Workflow](../personal/development-workflow.md)

## Changelog

- **v1.0** (2025-07-31): Initial version with comprehensive focus guide creation
