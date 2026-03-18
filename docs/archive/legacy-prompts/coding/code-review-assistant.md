---
title: "Code Review Assistant"
category: "coding"
tags: ["code-review", "quality", "feedback", "best-practices"]
difficulty: "intermediate"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Comprehensive code review with constructive feedback and improvement suggestions"
use_cases:
  - "Review pull requests"
  - "Check code quality before deployment"
  - "Learn best practices"
  - "Identify potential bugs and issues"
variables:
  - name: "code"
    description: "The code to be reviewed"
    example: "function calculateTotal(items) { return items.reduce((sum, item) => sum + item.price, 0); }"
  - name: "language"
    description: "Programming language of the code"
    example: "JavaScript"
  - name: "context"
    description: "Additional context about the code's purpose"
    example: "This function calculates the total price of items in a shopping cart"
---

# Code Review Assistant

## Description
This prompt helps you get comprehensive, constructive code reviews that focus on code quality, best practices, potential bugs, and improvement suggestions.

## Prompt

```
Please review the following {language} code and provide detailed feedback:

**Code to Review:**
```{language}
{code}
```

**Context:** {context}

Please analyze the code for:

1. **Code Quality & Style**
   - Readability and maintainability
   - Naming conventions
   - Code organization

2. **Best Practices**
   - Language-specific conventions
   - Design patterns usage
   - Performance considerations

3. **Potential Issues**
   - Bugs or logical errors
   - Edge cases not handled
   - Security vulnerabilities

4. **Improvement Suggestions**
   - Refactoring opportunities
   - Alternative approaches
   - Optimization possibilities

Format your response with:
- ✅ What's working well
- ⚠️ Areas for improvement
- 🐛 Potential bugs/issues
- 💡 Suggestions with code examples
- 📝 Overall assessment and next steps
```

## Variables to Customize

- **{code}**: The actual code you want reviewed
- **{language}**: Programming language (JavaScript, Python, Java, etc.)
- **{context}**: Brief description of what the code is supposed to do

## Usage Examples

### Example 1: JavaScript Function Review
**Input Variables:**
- code: `function calculateTotal(items) { return items.reduce((sum, item) => sum + item.price, 0); }`
- language: "JavaScript"
- context: "Function to calculate total price of shopping cart items"

**Expected Output:**
Detailed review covering code style, potential null checks, edge cases, and suggestions for improvement.

### Example 2: Python Class Review
**Input Variables:**
- code: `class BankAccount: def __init__(self, balance): self.balance = balance`
- language: "Python"
- context: "Basic bank account class for a financial application"

**Expected Output:**
Review focusing on Python conventions, missing methods, error handling, and security considerations.

## Tips for Best Results

- Provide complete code blocks rather than snippets when possible
- Include relevant context about the code's purpose and environment
- Specify the target audience (beginner, experienced developer, etc.)
- Mention any specific concerns you have about the code
- Include error messages if the code isn't working as expected

## Related Prompts

- [Code Optimizer](code-optimizer.md)
- [Bug Finder](bug-finder.md)
- [Documentation Generator](../business/documentation-generator.md)

## Changelog

- **v1.0** (2025-07-31): Initial version with comprehensive review structure
