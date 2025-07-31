Create a .copilot Directory and Files 

1. Add a .copilot/focus.md File 

This file can act as a guide for Copilot, summarizing the purpose of the project and providing specific instructions. For example: 

# Focus Guide for Copilot 
 
## Project Overview 
This project is a modernized version of an older codebase. The goal is to restructure, update, and document the project to meet current best practices. 
 
## Key Objectives 
1. Restructure the project into a clean and modular directory structure. 
2. Update code to modern standards (e.g., ES6+ for JavaScript, Python 3.x for Python). 
3. Provide detailed documentation in `README.md`, `WORKFLOW.md`, and `PROJECT_GOALS.md`. 
4. Integrate automation tools like CI/CD pipelines and add necessary configuration files. 
 
## Guidelines for Copilot 
- Focus on maintaining readability and modularity in the code. 
- Prioritize modern coding standards and remove deprecated practices. 
- Ensure all changes are well-documented and tested. 
 
## Useful Notes 
- Use `.github` for workflows, templates, and GitHub-specific files. 
- Use `.editorconfig`, `.prettierrc`, `.eslintrc` for consistency in code formatting. 
- Add a `tests` folder with unit and integration tests. 
 
Refer to this file whenever needed to stay focused on the project goals. 
  

 

2. Add a .copilot/prompts.md File 

This file can include example prompts or tasks you frequently ask Copilot to perform. For example: 

# Example Prompts for Copilot 
 
## Restructure the Project 
- "Organize the project files into `src`, `tests`, and `docs` folders." 
- "Move all utility functions into a `utils` subfolder." 
 
## Modernize the Code 
- "Refactor this function to use modern ES6+ syntax." 
- "Convert this class-based component to a functional component with React Hooks." 
 
## Add Documentation 
- "Create a `README.md` file with an overview, installation instructions, and usage examples." 
- "Write a `WORKFLOW.md` file explaining the development workflow." 
 
## Automate Tasks 
- "Create a GitHub Actions workflow to run tests on every pull request." 
- "Add a script to automate code formatting with Prettier." 
 
  

 

3. Add a .copilot/config.json File 

While Copilot doesn't natively support configuration files, you can define your own structure for organizational purposes. For example: 

{ 
  "projectGoals": [ 
    "Modernize the codebase", 
    "Restructure the project for modularity", 
    "Add comprehensive documentation", 
    "Automate testing and deployment" 
  ], 
  "focusAreas": [ 
    "Code readability", 
    "Best practices", 
    "Automation integration", 
    "Documentation clarity" 
  ], 
  "excludedFiles": [ 
    "node_modules", 
    "build", 
    ".env" 
  ] 
} 
  

 

How This Helps 

While Copilot doesn't "read" these files directly, they can help you stay consistent and focused. By keeping these files in the project, you can refer to them as you work and even copy-paste their contents into prompts for Copilot when needed. 

 

 

Pro Tip 

For more immediate focus, add comments at the top of individual files while working with Copilot. For example: 

# This script calculates user statistics. Refactor to use Python 3.x best practices. 
# Key tasks: 
# 1. Replace outdated `print` statements with `logging`. 
# 2. Optimize the performance of the `calculate_stats` function. 
  

This approach ensures Copilot understands the immediate context and your expectations for the file at hand. 

 