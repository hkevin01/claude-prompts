---
title: "Repository Cleanup and Organization"
category: "coding"
tags: ["cleanup", "organization", "project-structure", "best-practices"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Comprehensive guide for cleaning up and organizing GitHub repositories with modern structure"
use_cases:
  - "Repository restructuring"
  - "Legacy project modernization"
  - "Clean project setup"
  - "Code organization improvement"
variables:
  - name: "project_type"
    description: "Type of project (web app, API, library, etc.)"
    example: "React web application"
  - name: "current_issues"
    description: "Main organization problems in the current repository"
    example: "files scattered in root, no clear structure, mixed concerns"
  - name: "target_structure"
    description: "Desired organization goals"
    example: "modern src/ structure, separate docs and tests, clean root"
---

# Repository Cleanup and Organization

## Description
A systematic approach to cleaning up and reorganizing GitHub repositories to follow modern development standards with logical directory structures and clean organization.

## Prompt

```
I need help cleaning up and organizing my GitHub repository. Help me transform it into a well-structured, modern project.

**Project Type:** {project_type}
**Current Issues:** {current_issues}
**Target Structure:** {target_structure}

## CLEANUP AND ORGANIZATION PROCESS:

### Phase 1: Root Folder Analysis and Cleanup

**Keep Only Essential Root-Level Items:**
- README.md, LICENSE, .gitignore, .env.example
- Package/dependency files (package.json, requirements.txt, Cargo.toml, etc.)
- Configuration files (.prettierrc, .eslintrc, tsconfig.json, etc.)
- CI/CD files (.github/, .gitlab-ci.yml, etc.)
- Build/deployment files (Dockerfile, docker-compose.yml, Makefile, etc.)
- Documentation entry points (CHANGELOG.md, CONTRIBUTING.md, SECURITY.md)

**Move Everything Else to Organized Subfolders:**

### Phase 2: Source Code Organization

**Create `src/` directory with logical subdirectories:**
- `src/components/` - Reusable UI components
- `src/pages/` or `src/views/` - Page-level components
- `src/services/` - API calls and external service integrations
- `src/utils/` or `src/helpers/` - Utility functions and helpers
- `src/hooks/` - Custom hooks (React/Vue)
- `src/stores/` or `src/state/` - State management
- `src/types/` - Type definitions (TypeScript)
- `src/constants/` - Application constants
- `src/models/` - Data models and schemas

### Phase 3: Supporting Directories

**Create organized support structure:**
- `docs/` - Detailed documentation, guides, architecture docs
- `tests/` or `__tests__/` - Test files organized by feature/component
- `public/` or `static/` - Static assets, images, icons
- `scripts/` - Build scripts, utilities, automation tools
- `config/` - Configuration files for different environments
- `assets/` - Design files, images, media resources

### Phase 4: File Organization Rules

**Apply consistent organization:**
1. **Group by Feature/Domain** (preferred for larger apps)
   ```
   src/
   ├── user-management/
   │   ├── components/
   │   ├── services/
   │   ├── types/
   │   └── utils/
   ├── billing/
   │   ├── components/
   │   ├── services/
   │   └── types/
   ```

2. **Group by Type** (for smaller projects)
   ```
   src/
   ├── components/
   ├── services/
   ├── utils/
   ├── types/
   └── constants/
   ```

### Phase 5: File Naming Conventions

**Establish consistent naming:**
- Use kebab-case for files and folders: `user-profile.component.js`
- Use PascalCase for component files: `UserProfile.jsx`
- Use camelCase for utility files: `dateUtils.js`
- Use UPPER_CASE for constants: `API_ENDPOINTS.js`
- Be descriptive: `calculateTotalPrice.js` not `calc.js`

### Phase 6: Cleanup Actions

**Remove and Clean:**
1. Delete unused files, empty directories
2. Remove commented-out code blocks
3. Clean up duplicate files
4. Remove old build artifacts
5. Consolidate similar configuration files
6. Update imports after moving files
7. Remove unused dependencies

### Phase 7: Documentation Updates

**Update key files:**
- README.md with new structure explanation
- Update import paths in code
- Create index files for easier imports
- Add .gitignore rules for new structure
- Document the organization rationale

## DELIVERABLES:
✅ Clean root directory with only essential files
✅ Logical src/ directory structure
✅ Organized supporting directories (docs, tests, etc.)
✅ Consistent file naming conventions
✅ Updated documentation reflecting new structure
✅ Working code with updated import paths
✅ Comprehensive .gitignore file

Provide a before/after directory structure comparison and migration plan.
```

## Variables to Customize

- **{project_type}**: Specify the type of project for appropriate structure recommendations
- **{current_issues}**: Describe current organizational problems to address
- **{target_structure}**: Define the desired end state and organization goals

## Usage Examples

### Example 1: React Web Application
**Input Variables:**
- project_type: "React web application with TypeScript"
- current_issues: "components mixed with utilities in root, no clear folder structure"
- target_structure: "modern src/ layout with feature-based organization"

**Expected Output:**
Complete reorganization plan with React-specific folder structure, TypeScript organization, and component architecture.

### Example 2: Node.js API
**Input Variables:**
- project_type: "Node.js REST API with Express"
- current_issues: "routes, models, and controllers all in root directory"
- target_structure: "MVC pattern with clear separation of concerns"

**Expected Output:**
API-focused structure with controllers, models, routes, middleware, and services properly organized.

## Tips for Best Results

- Start with a backup of your current repository
- Move files in small batches to avoid breaking imports
- Update import statements as you move files
- Test the application after each major reorganization step
- Consider the size and complexity of your project when choosing organization patterns
- Document the new structure for team members
- Use this prompt iteratively for different parts of large projects

## Related Prompts

- [Code Refactoring](../development/refactoring.md)
- [Project Setup Assistant](project-setup-assistant.md)
- [Documentation Generator](../business/documentation-generator.md)

## Changelog

- **v1.0** (2025-07-31): Initial version with comprehensive cleanup and organization strategy
