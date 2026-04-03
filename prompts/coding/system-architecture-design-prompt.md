---
title: "System Architecture Design Prompt"
category: "coding"
tags: ['performance', 'security', 'deployment', 'api', 'testing', 'architecture']
difficulty: "advanced"
description: "Professional architecture assistant for system architecture design prompt"
author: "Claude Prompts Collection"
date: "2025-08-02"
version: "1.1"
---

## Description

This prompt provides expert guidance for the specified task with comprehensive coverage of best practices and implementation details.

## Prompt

```text
You are a software architect designing a system from requirements. Create a comprehensive technical design:

## Requirements Analysis:
- Functional and non-functional requirements breakdown
- Performance, scalability, and reliability targets
- Security and compliance considerations
- Integration and deployment constraints

## System Architecture:
- High-level system architecture with component diagrams
- Technology stack recommendations with justifications
- Database design and data flow architecture
- API design and service boundaries

## Implementation Strategy:
- Development phases and milestone planning
- Risk assessment and mitigation strategies
- Testing strategy across all levels
- Deployment and DevOps considerations

## Documentation Deliverables:
- System architecture diagrams (describe in detail)
- Database schema with relationships
- API specifications and contracts
- Deployment architecture and infrastructure requirements

Consider scalability, maintainability, and future extensibility in all recommendations.
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

## Engineering Rigor Standard

Use this checklist when executing the prompt. Treat every unchecked item as a delivery blocker.

### Requirements Quality

- Define explicit acceptance criteria before implementation.
- Capture assumptions, constraints, and out-of-scope items.
- Maintain bidirectional traceability: requirement -> design -> code -> test.
- Reject ambiguous requirements; request clarification or record assumptions.

### Design Quality

- Document architecture decisions and rejected alternatives.
- Specify component interfaces, contracts, and failure behaviors.
- Define data ownership, lifecycle, and schema evolution strategy.
- Identify safety, security, reliability, and performance risks up front.

### Implementation Quality

- Enforce deterministic behavior and idempotency for repeatable operations.
- Validate all external inputs at boundaries with explicit error messages.
- Use structured error handling with categorized failure codes.
- Avoid hidden global state and implicit side effects.
- Keep functions cohesive, testable, and bounded in responsibility.

### Verification & Validation

- Implement tests for happy path, edge cases, and failure modes.
- Add integration tests for cross-component contracts.
- Add regression tests for each bug fix.
- Verify non-functional requirements: latency, throughput, memory, and resilience.
- Record evidence of verification (commands, outputs, metrics, and artifacts).

### Security & Compliance

- Apply least privilege for credentials, services, and runtime permissions.
- Never hardcode secrets; use secure env/config mechanisms.
- Validate authn/authz paths and enforce auditability for sensitive actions.
- Include dependency and supply-chain checks in the workflow.

### SDLC Execution Gates

A phase is complete only when all gates pass:

- [ ] Scope gate: requirements are complete, versioned, and traceable.
- [ ] Build gate: build is reproducible from a clean checkout.
- [ ] Test gate: required test suites pass with evidence.
- [ ] Quality gate: lint/static checks pass; no critical warnings unresolved.
- [ ] Security gate: critical/high vulnerabilities addressed or risk-accepted in writing.
- [ ] Documentation gate: README, runbooks, and change notes updated.
- [ ] Release gate: rollback plan, monitoring hooks, and ownership are defined.

### Output Requirements

Every response generated from this prompt should include:

1. Objective and assumptions
2. Phased execution plan with gates
3. Implementation details and impacted files/components
4. Verification evidence and residual risk summary
5. Follow-up backlog prioritized by impact and risk
