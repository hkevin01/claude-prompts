# Claude Prompts Collection

![Claude Prompts Extension Icon](images/icon.png)

Professional Claude AI Prompts for Developers - instant access to expert-crafted prompts right in VS Code!

[![Version](https://img.shields.io/visual-studio-marketplace/v/hkevin01.claude-prompts)](https://marketplace.visualstudio.com/items?itemName=hkevin01.claude-prompts)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/hkevin01.claude-prompts)](https://marketplace.visualstudio.com/items?itemName=hkevin01.claude-prompts)
[![Rating](https://img.shields.io/visual-studio-marketplace/r/hkevin01.claude-prompts)](https://marketplace.visualstudio.com/items?itemName=hkevin01.claude-prompts)
[![License](https://img.shields.io/github/license/hkevin01/claude-prompts)](https://github.com/hkevin01/claude-prompts/blob/main/LICENSE)

🚀 **Boost your development workflow with professionally curated Claude AI prompts**

## ✨ Features

- **50+ Professional Prompts**: Expert-crafted prompts with comprehensive coding assistance
- **Smart Search**: Quickly find prompts by title, tags, or description
- **Category Organization**: Browse prompts by development, architecture, testing, and more
- **Instant Insert**: Click to insert prompts directly into your active editor
- **Difficulty Indicators**: Color-coded difficulty levels (🟢 Beginner, 🟡 Intermediate, 🔴
  Advanced)
- **Rich Preview**: View prompt details before using them
- **Custom Prompts**: Add your own prompt collections

## 🎯 Available Prompts

### 💻 Development & Architecture
- **System Architecture**: Microservices design, system architecture planning
- **API Development**: REST API and GraphQL API design
- **Code Generation**: API implementation, specification to code conversion
- **Refactoring**: Code modernization and cleanup strategies
- **Debugging**: Systematic debugging approaches

### 🔍 Code Review & Quality
- **Security Review**: Security-focused code analysis
- **Performance Review**: Performance optimization analysis
- **Comprehensive Review**: Complete code quality assessment
- **Legacy Code**: Modernization and dependency upgrades
- **Best Practices**: Coding standards and patterns

### ⚡ Optimization & Testing
- **Database Optimization**: Query and schema optimization
- **Algorithm Optimization**: Performance improvements
- **Test Automation**: Testing strategy and implementation
- **TDD Development**: Test-driven development guidance
- **Quality Assurance**: Comprehensive testing approaches

## 🎯 Available Prompt Categories

### 🔧 Coding (25+ prompts)

- **Architecture**: System design, microservices planning
- **Testing**: TDD, test automation, comprehensive testing strategies
- **Code Review**: Security, performance, and quality reviews
- **Legacy**: Modernization strategies, dependency upgrades
- **API Development**: REST and GraphQL design
- **Optimization**: Algorithm and database performance
- **Generation**: Code generation from specifications

### 🎨 Creative (3+ prompts)

- Story generation and creative writing
- Content creation assistance

### 💼 Business (2+ prompts)

- Email composition and professional communication
- Business process optimization

### 📊 Analysis & More

- Task prioritization and project planning
- Educational content development

## 🚀 Quick Start

### Installation

1. **From VS Code Marketplace** (Coming Soon)
   - Open VS Code
   - Go to Extensions (`Ctrl+Shift+X`)
   - Search for "Claude Prompts Collection"
   - Click Install

2. **From Source** (Development)
   ```bash
   git clone https://github.com/hkevin01/claude-prompts.git
   cd claude-prompts
   npm install
   npm run compile
   # Press F5 to launch extension development host
   ```

### Usage

#### 🎮 Keyboard Shortcuts

- `Ctrl+Shift+P` then `Ctrl+Shift+C` - Show Claude Prompts
- `Ctrl+Shift+F` then `Ctrl+Shift+C` - Search Prompts

#### 🖱️ GUI Access

1. **Activity Bar**: Click the Claude Prompts icon (📖)
2. **Command Palette**: `Ctrl+Shift+P` > "Claude Prompts"
3. **Explorer**: Browse categories and click prompts to insert

#### 📋 Using Prompts

1. Open any file in VS Code
2. Place cursor where you want to insert the prompt
3. Browse or search for a prompt
4. Click the prompt to insert it instantly!

## 🏗️ Extension Architecture

### Core Components

- **Prompt Manager**: Loads and manages prompt collections with YAML frontmatter parsing
- **Tree Data Provider**: Creates hierarchical view of prompts by category
- **Search Provider**: Implements fuzzy search using Fuse.js
- **Command Handlers**: Integrates with VS Code's command palette and editor

### Prompt Format

Each prompt follows this structure:

```yaml
---
title: 'Prompt Name'
description: 'Brief description'
tags: ['tag1', 'tag2']
difficulty: 'beginner|intermediate|advanced'
category: 'coding|creative|business|analysis|educational|personal'
---
Your prompt content here...
```

## 🎨 Example Prompts

### 💻 Coding

- Code review and optimization
- Test-driven development strategies
- System architecture planning
- API design and implementation
- Legacy code modernization

### 🎨 Creative

- Content creation
- Story generation and narrative development
- Creative writing assistance

### 📊 Analysis

- Data analysis and interpretation
- Research methodology guidance
- Task prioritization frameworks

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Adding New Prompts

1. **Fork the repository**
2. **Create a new prompt file** in the appropriate category folder under `src/prompts/`
3. **Follow the YAML frontmatter format** (see template below)
4. **Test your prompt** to ensure it works well with Claude
5. **Submit a pull request** with a clear description

### Prompt Template

```markdown
---
title: 'Your Prompt Title'
description: 'Clear, concise description of what this prompt does'
tags: ['relevant', 'tags', 'here']
difficulty: 'beginner' # or intermediate, advanced
category: 'coding' # or creative, business, analysis, educational, personal
author: 'Your Name' # optional
version: '1.0' # optional
---

# Your Prompt Title

## Context

Provide any necessary context or background information.

## Instructions

Clear, specific instructions for Claude to follow.

## Example Usage

Show how to use this prompt effectively.

## Expected Output

Describe what kind of response to expect.
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/hkevin01/claude-prompts.git
cd claude-prompts

# Install dependencies
npm install

# Build the extension
npm run compile

# Run tests
npm test

# Launch extension development host
code .
# Press F5 to open Extension Development Host
```

## 📋 Validation and Testing

The project includes comprehensive validation:

- **Prompt Validation**: Ensures all prompts have proper YAML frontmatter
- **Link Checking**: Validates all URLs and references
- **Markdown Linting**: Maintains consistent formatting
- **Automated Testing**: Runs validation on all prompts

Run validation locally:

```bash
# Validate all prompts
python scripts/validate_prompts.py

# Check links
python scripts/check_links.py

# Lint markdown
npx markdownlint **/*.md
```

## 🚀 Roadmap

- [ ] **Marketplace Publication**: Submit to VS Code Marketplace
- [ ] **Custom Collections**: Allow users to create private prompt collections
- [ ] **AI Integration**: Direct Claude API integration for testing prompts
- [ ] **Collaborative Features**: Share and rate community prompts
- [ ] **Analytics**: Track prompt usage and effectiveness
- [ ] **Templates**: Advanced prompt template system
- [ ] **Export/Import**: Backup and sync prompt collections

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙋‍♂️ Support

- **Issues**: [GitHub Issues](https://github.com/hkevin01/claude-prompts/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hkevin01/claude-prompts/discussions)
- **Email**: [Support](mailto:support@claude-prompts.dev)

## 🌟 Acknowledgments

- Thanks to all contributors who help improve this collection
- Inspired by the Claude AI community's excellent prompt engineering
- Built with ❤️ for developers who love efficient workflows

---

**Made with ❤️ for the Claude AI community**

## 🏷️ Prompt Organization

Each prompt file follows a standardized format:

- **Filename**: `prompt-name.md`
- **Metadata**: YAML frontmatter with tags, category, difficulty, etc.
- **Content**: Clear prompt description and instructions
- **Examples**: Sample inputs/outputs when applicable
- **Usage Notes**: Tips for effective use

## 📝 Quick Start

1. Browse prompts by category in the `prompts/` directory
2. Copy the prompt content you need
3. Customize variables (marked with `{variable}`) for your use case
4. Use with Claude for best results

## 🔍 Finding Prompts

- **By Category**: Navigate to the appropriate subfolder
- **By Tag**: Check the metadata in prompt files
- **By Search**: Use your editor's search functionality

## 🤝 Contributing

When adding new prompts:

1. Use the template in `templates/prompt-template.md`
2. Include proper metadata and tags
3. Test the prompt before adding
4. Follow the naming convention

## 📋 Categories

### 💻 Coding

- Code review and optimization
- Debugging assistance
- Documentation generation
- Architecture planning

### 🎨 Creative

- Content creation
- Creative writing
- Brainstorming
- Story development

### 📊 Analysis

- Data interpretation
- Research assistance
- Report generation
- Trend analysis

### 💼 Business

- Email drafting
- Meeting summaries
- Strategy planning
- Process optimization

### 🎓 Educational

- Learning assistance
- Concept explanation
- Study guides
- Skill development

### 🔧 Personal

- Task planning
- Decision making
- Goal setting
- Productivity enhancement

---

_Last updated: July 31, 2025_
