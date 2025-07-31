Part 1: Analyze and Restructure the Project 

Prompt: 

"Analyze the project structure and reorganize it to adhere to modern development standards. Perform the following steps: 

Organize code into logical directories and subdirectories (e.g., src, tests, docs, etc.). 

Move misplaced or loose files into appropriate folders, and create subfolders where necessary for better modularity. 

Ensure the directory structure is clean, logical, and easy to navigate." 

 

 

Part 2: Modernize the Code 

Prompt: 

"Review the codebase thoroughly and update it to follow modern coding standards and best practices. Perform the following: 

Refactor outdated or deprecated code to use modern equivalents (e.g., ES6+ for JavaScript, Python 3.x for Python, etc.). 

Remove unused or redundant code. 

Ensure the code is modular, readable, and maintainable. 

Add comments and docstrings where necessary." 

 

 

Part 3: Generate Core Documentation 

Prompt: 

"Create core documentation for the project, including: 

A README.md file with:  

Project overview. 

Installation instructions. 

Usage examples. 

Contribution guidelines. 

License information (default to MIT if none exists). 

A WORKFLOW.md file that explains the development workflow, including branching strategies, CI/CD pipelines, and code review processes. 

A PROJECT_GOALS.md file outlining:  

The purpose of the project. 

Short-term and long-term goals. 

The intended audience." 

 

 

Part 4: Add GitHub Workflow Files 

Prompt: 

"Set up a .github folder with the following content: 

Workflow files for CI/CD pipelines (e.g., build.yml, test.yml, deploy.yml). 

Issue and pull request templates. 

A CODEOWNERS file if applicable. 

A CONTRIBUTING.md file with guidelines on how to contribute to the project. 

A SECURITY.md file for reporting vulnerabilities." 

 

 

Part 5: Add Copilot-Specific Files 

Prompt: 

"Create a .copilot folder and include: 

A configuration file for Copilot behavior and preferences (if supported). 

Any custom Copilot prompts or settings that are relevant to this project." 

 

 

Part 6: Enhance Tooling and Configuration 

Prompt: 

"Add or update the following configuration files: 

.editorconfig for consistent coding styles across editors. 

.gitignore to exclude unnecessary files from version control. 

.prettierrc or .eslintrc for code formatting and linting (if applicable). 

Dependency management files like package.json, requirements.txt, or Pipfile. 

Verify that all dependencies are up to date." 

 

 

Part 7: Add Supporting Directories and Files 

Prompt: 

"Create additional directories and files to support the project: 

A docs folder for detailed project documentation. 

A tests folder for unit tests and integration tests. 

A CHANGELOG.md file to track changes in the project over time. 

Add boilerplate or example code where missing." 

 

 

Part 8: Automate and Finalize 

Prompt: 

"Add automation and finalize the project update: 

Set up scripts for automating repetitive tasks (e.g., build, test, and deployment scripts). 

Integrate CI/CD tools like GitHub Actions, CircleCI, or Travis CI to automate testing and deployment. 

Ensure all changes are well-documented and the project works as intended. 

Commit changes with clear, descriptive commit messages." 

 

 

By breaking the tasks into these manageable chunks, you can keep Copilot focused on one aspect of the project at a time, ensuring higher quality and precision in the outputs. 

 

improve project layout , use src layout create .gitignore and docs folder and scripts fodler and create in docs a project plan.md  in the project plan have category phases with at least 5 bulets and for bullets have checkboxes ; example phase 1 topic with 5 checkboxes and detailed actioni items with options for solutions, and then phase 2 topic with 5 checkboxes and detailed action ; create .github folder and .copilot folder with necessary files in them and common files.  

 

Create .vscode folder use https://github.com/antfu/vscode-settings/tree/main/.vscode 

 

Do not create readme.md in .github ;; also examine the project prior and determine what it is doing and include that in project plan .md and readme.md files  

 

Create also a data and assets folder  

 

The vs code settings.json should also have rules for keeping to standards and practices for java, c++ and python for naming, method names, filenames etc.  

 

Update .gitignore as needed.  

 

Create .vscode folder and settings.json with "chat.tools.autoApprove": true, 

"chat.agent.maxRequests": 100, 

 

 

Create a virtual environment if using python and if there isn't already a venv and make sure to add the venv to .gitignore  
