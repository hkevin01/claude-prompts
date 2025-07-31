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

   - Create appropriate subfolders for different code categories: 

     - `/src` or `/lib` for main source code 

     - `/components` for reusable components 

     - `/utils` or `/helpers` for utility functions 

     - `/config` for configuration files 

     - `/tests` for test files 

     - `/docs` for documentation 

     - `/assets` for static resources 

     - Any framework-specific folders 

  

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

   - Clean up unused variables and parameters 

  

6. **Code Consolidation** 

   - Merge duplicate functions and extract common patterns 

   - Create shared utility modules for repeated code 

   - Consolidate similar configuration files 

   - Optimize import statements 

  

## IMPROVEMENT PHASE 

7. **Fix Missing Elements** 

   - Add missing imports and dependencies 

   - Create missing configuration files (package.json, requirements.txt, etc.) 

   - Add proper entry points and index files 

   - Ensure all modules are properly connected 

  

8. **Code Quality Improvements** 

   - Standardize naming conventions throughout the project 

   - Add proper error handling where missing 

   - Improve function and variable names for clarity 

   - Add basic documentation comments for complex functions 

  

## FINAL DELIVERABLES 

Provide me with: 

- A detailed summary of all changes made 

- The new directory structure with explanations 

- List of files moved, renamed, or deleted 

- List of unused code removed 

- Any issues found and how they were resolved 

- Recommendations for further improvements 

  

## IMPORTANT REQUIREMENTS 

- Preserve all functional code and maintain backward compatibility 

- Update all import paths and references after moving files 

- Ensure the project still works after reorganization 

- Follow the specific conventions of the detected framework/language 

- Create a backup strategy or change log for rollback if needed 

- Prioritize maintainability and scalability in the new structure 

  

Please start by asking me to share the project files or codebase you'll be working with, then proceed systematically through each phase. 
