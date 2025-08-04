#!/usr/bin/env bash

# Setup script for local development environment
set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Setting up Claude Prompts development environment...${NC}\n"

# Check prerequisites
check_prerequisite() {
    if ! command -v $1 &> /dev/null; then
        echo -e "${RED}Error: $1 is required but not installed.${NC}"
        echo "Please install $1 and try again."
        exit 1
    fi
}

check_prerequisite "node"
check_prerequisite "npm"
check_prerequisite "python3"
check_prerequisite "git"

# Install Node.js dependencies
echo -e "\n${YELLOW}Installing Node.js dependencies...${NC}"
npm install

# Install Python dependencies
echo -e "\n${YELLOW}Installing Python dependencies...${NC}"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Set up Git hooks
echo -e "\n${YELLOW}Setting up Git hooks...${NC}"
cat > .git/hooks/pre-commit << 'EOL'
#!/bin/bash
set -e

echo "Running pre-commit checks..."

# Run TypeScript compilation
echo "Checking TypeScript compilation..."
npm run compile

# Run linting
echo "Running linters..."
npm run lint
npx markdownlint-cli "**/*.md" -c .markdownlint.json

# Validate prompts
echo "Validating prompts..."
python3 scripts/validate_prompts.py

# Check links
echo "Checking links..."
python3 scripts/check_links.py
EOL

chmod +x .git/hooks/pre-commit

# Set up VS Code settings
echo -e "\n${YELLOW}Configuring VS Code settings...${NC}"
mkdir -p .vscode
cat > .vscode/settings.json << 'EOL'
{
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "[typescript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[markdown]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "typescript.tsdk": "node_modules/typescript/lib",
    "search.exclude": {
        "**/node_modules": true,
        "**/dist": true,
        "**/.vscode-test": true
    },
    "files.exclude": {
        "**/.git": true,
        "**/node_modules": true,
        "**/dist": true,
        "**/.vscode-test": true
    }
}
EOL

# Create VS Code launch configuration
cat > .vscode/launch.json << 'EOL'
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Extension",
            "type": "extensionHost",
            "request": "launch",
            "args": [
                "--extensionDevelopmentPath=${workspaceFolder}"
            ],
            "outFiles": [
                "${workspaceFolder}/dist/**/*.js"
            ],
            "preLaunchTask": "npm: compile"
        },
        {
            "name": "Extension Tests",
            "type": "extensionHost",
            "request": "launch",
            "args": [
                "--extensionDevelopmentPath=${workspaceFolder}",
                "--extensionTestsPath=${workspaceFolder}/dist/test/suite"
            ],
            "outFiles": [
                "${workspaceFolder}/dist/test/**/*.js"
            ],
            "preLaunchTask": "npm: compile"
        }
    ]
}
EOL

# Create default environment file
cat > .env.example << 'EOL'
# VS Code Extension Settings
VSCE_PAT=your_vscode_marketplace_token_here
GITHUB_TOKEN=your_github_token_here

# Testing Settings
TEST_WORKSPACE_PATH=/path/to/test/workspace

# Security Settings
ENCRYPTION_KEY=generate_a_secure_key_here
TELEMETRY_ENABLED=false

# Cloud Integration (Future)
CLAUDE_API_KEY=your_claude_api_key_here
EOL

# Generate encryption key for local development
ENCRYPTION_KEY=$(openssl rand -base64 32)
cp .env.example .env
sed -i "s/generate_a_secure_key_here/$ENCRYPTION_KEY/" .env

# Create data directory for user settings
mkdir -p data/user-data

echo -e "\n${GREEN}Development environment setup complete!${NC}"
echo -e "\nNext steps:"
echo -e "1. Copy .env.example to .env and configure your environment variables"
echo -e "2. Install recommended VS Code extensions:"
echo -e "   - ESLint"
echo -e "   - Prettier"
echo -e "   - Python"
echo -e "   - markdownlint"
echo -e "3. Run 'npm run watch' to start development"
echo -e "4. Press F5 in VS Code to launch the extension in debug mode"
