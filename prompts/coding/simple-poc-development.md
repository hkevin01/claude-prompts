---
title: "Simple POC Development Guide"
category: "coding"
tags: ["prototyping", "poc", "simple-development", "rapid-iteration"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Guidance for creating simple, direct proof-of-concept code without over-engineering"
use_cases:
  - "Personal projects and prototypes"
  - "Rapid feature validation"
  - "Quick solution development"
  - "Avoiding premature optimization"
variables:
  - name: "project_type"
    description: "Type of project or feature being developed"
    example: "web scraper to collect product data"
  - name: "requirements"
    description: "Basic functional requirements"
    example: "scrape prices from 3 e-commerce sites and save to CSV"
  - name: "constraints"
    description: "Any technical or time constraints"
    example: "needs to run locally, no external databases"
---

# Simple POC Development Guide

## Description
A development approach focused on creating simple, direct solutions for personal projects and proof-of-concepts. Emphasizes shipping working code over perfect architecture.

## Prompt

```
I need help building a simple proof-of-concept for: {project_type}

**Requirements:** {requirements}
**Constraints:** {constraints}

## DEVELOPMENT APPROACH:

### Context Understanding:
- This is a solo developer project, NOT enterprise-level
- I prefer simple, direct solutions over "best practices"
- I'm a vibe coder who values shipping over perfect architecture
- Focus on POC (Proof of Concept) unless explicitly told otherwise

### Default Approach:
1. **Keep It Simple and Direct**
   - Start with the most obvious solution that works
   - Don't overthink the implementation
   - Use single files over multiple files when reasonable
   - Hardcode reasonable defaults instead of building configuration systems

2. **No Frameworks Unless Necessary**
   - Use built-in language features first
   - Avoid adding dependencies for simple tasks
   - Choose the lightest solution that works

3. **Practical Defaults**
   - Hardcode reasonable values instead of complex configuration
   - Use simple data structures (arrays, objects) over complex classes
   - Prefer inline logic over abstracted functions initially

### What NOT to Do:
❌ Don't add abstractions until we actually need them
❌ Don't build for imaginary future requirements  
❌ Don't add complex error handling for unlikely edge cases
❌ Don't suggest design patterns unless the problem requires them
❌ Don't optimize prematurely
❌ Don't add configuration for things that rarely change

### Implementation Strategy:
1. **Start with "The Dumbest Thing That Works"**
   - Single function or script approach
   - Hardcoded values for initial testing
   - Basic error handling only where essential

2. **Quick POC Implementation**
   - Focus on core functionality first
   - Get it working, then improve if needed
   - Use throwaway prototype mentality

3. **If It Needs to Be More Robust:**
   - Add basic error handling (try/catch, input validation)
   - Improve user-facing messages
   - Extract functions only for readability, not "reusability"
   - Keep the same simple approach - just make it more reliable

### Language to Use:
- "Quick POC to test if this works"
- "Throwaway prototype"
- "Just make it work"
- "The dumbest thing that works"
- "Keep it simple and direct"

## OUTPUT FORMAT:
Provide the simplest possible implementation that meets the requirements. Include:
- Single file or minimal files approach
- Hardcoded reasonable defaults
- Basic comments explaining the approach
- Simple test/usage example
- Notes on when/how to make it more robust if needed

Focus on getting it working quickly rather than making it perfect.
```

## Variables to Customize

- **{project_type}**: The type of application or tool you're building
- **{requirements}**: What the code needs to accomplish
- **{constraints}**: Technical limitations or preferences

## Usage Examples

### Example 1: Data Processing Script
**Input Variables:**
- project_type: "CSV data processor for sales reports"
- requirements: "read CSV, calculate totals by region, output summary"
- constraints: "Python script, no external databases"

**Expected Output:**
Simple Python script with hardcoded file paths, basic CSV processing, and direct output to console or file.

### Example 2: Web Scraper
**Input Variables:**
- project_type: "product price monitor"
- requirements: "check prices on 2 websites, compare with target price, send alert"
- constraints: "run locally, no GUI needed"

**Expected Output:**
Straightforward scraping script with hardcoded URLs, simple comparison logic, and basic notification method.

## Tips for Best Results

- Embrace the "good enough" mindset for prototypes
- Resist the urge to over-engineer from the start
- Focus on proving the concept works before optimizing
- Use this approach for personal projects and rapid experimentation
- Gradually improve only when the POC proves valuable
- Remember: shipping beats perfection for learning and validation

## Related Prompts

- [Rapid Prototyping](rapid-prototyping.md)
- [Code Refactoring](../development/refactoring.md)
- [Project Planning](../business/project-planning.md)

## Changelog

- **v1.0** (2025-07-31): Initial version focusing on simple POC development
