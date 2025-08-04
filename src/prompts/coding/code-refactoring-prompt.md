---
title: "Code Refactoring Prompt"
category: "coding"
tags: ['documentation', 'architecture', 'refactoring', 'development']
difficulty: "intermediate"
description: "Professional development assistant for code refactoring prompt"
author: "Claude Prompts Collection"
date: "2025-08-02"
version: "1.1"
---

## Description

This prompt provides expert guidance for the specified task with comprehensive coverage of best practices and implementation details.

## Prompt

```text
You are an expert software architect and code refactoring specialist. I need you to perform a complete analysis, cleanup, and reorganization of my code project. Please follow this systematic approach:

## ANALYSIS PHASE
1. **Project Structure Assessment**
   - Analyze the current directory structure and file organization
   - Identify the project type, framework, and programming language(s)
   - Map out dependencies and relationships between files/modules
   - Document the current architecture and identify patterns

2. **Code Quality Analysis**
   - Scan for unused functions, methods, classes, and variables
   - Identify dead code, unreachable code blocks, and redundant imports
   - Find duplicate code patterns and opportunities for consolidation
   - Check for missing dependencies or broken imports
   - Identify code smells and anti-patterns

## REORGANIZATION PHASE
3. **Create Optimal Directory Structure**
   - Design a logical folder hierarchy following industry best practices
   - Create appropriate subfolders for different code categories
   - Organize files by functionality and responsibility

4. **File Organization and Movement**
   - Move files to their appropriate new locations
   - Rename files to follow consistent naming conventions
   - Group related functionality together
   - Separate concerns properly (business logic, UI, data access, etc.)

## CLEANUP PHASE
5. **Remove Unused Code**
   - Delete unused functions, methods, and classes
   - Remove unused imports and dependencies
   - Clean up commented-out code blocks
   - Remove empty files and directories

6. **Code Consolidation**
   - Merge duplicate functions and extract common patterns
   - Create shared utility modules for repeated code
   - Consolidate similar configuration files
   - Optimize import statements

Provide detailed documentation of all changes made.
```

## Variables to Customize

- **Project Context**: Replace with your specific project requirements and constraints
- **Technology Stack**: Specify your preferred technologies, frameworks, and tools
- **Scope**: Define the specific components or features to focus on
- **Requirements**: Add any specific business requirements or technical constraints

## Example Usage

Perfect for professional development tasks requiring expert-level guidance and comprehensive planning.

## Tips

- Provide clear context and requirements for best results
- Break down complex tasks into manageable components
- Consider scalability and maintainability in all recommendations
