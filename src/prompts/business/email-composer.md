---
title: "Email Composer"
category: "business"
tags: ["email", "communication", "professional", "business-writing"]
difficulty: "beginner"
author: "Claude Prompts Collection"
date: "2025-07-31"
version: "1.0"
description: "Craft professional emails for various business purposes"
use_cases:
  - "Business correspondence"
  - "Client communications"
  - "Internal team messages"
  - "Networking outreach"
variables:
  - name: "purpose"
    description: "The goal of the email"
    example: "request a meeting to discuss project collaboration"
  - name: "recipient"
    description: "Who you're writing to"
    example: "a potential business partner I met at a conference"
  - name: "tone"
    description: "Desired tone and formality level"
    example: "professional but friendly"
  - name: "key_points"
    description: "Main information to include"
    example: "our company's expertise, mutual benefits, proposed next steps"
---

# Email Composer

## Description
Generate professional, well-structured emails for various business purposes. This prompt ensures your emails are clear, appropriately toned, and achieve their intended goals.

## Prompt

```
Please help me write a professional email with the following details:

**Purpose**: {purpose}
**Recipient**: {recipient}
**Tone**: {tone}
**Key Points to Include**: {key_points}

Email Requirements:
- Appropriate subject line
- Professional greeting
- Clear, concise body with logical flow
- Specific call-to-action or next steps
- Professional closing
- Proper business email etiquette

Structure the email as follows:
1. **Subject Line**: Clear and compelling
2. **Greeting**: Appropriate level of formality
3. **Opening**: Brief context or connection
4. **Body**: Main message with key points
5. **Action Items**: What you want the recipient to do
6. **Closing**: Professional sign-off

Please ensure the email:
- Gets to the point quickly
- Uses clear, jargon-free language
- Maintains the requested tone throughout
- Includes all key information
- Has a clear purpose and desired outcome
- Is an appropriate length for the content

After the email, provide a brief explanation of the tone and structure choices made.
```

## Variables to Customize

- **{purpose}**: Meeting request, project update, introduction, follow-up, complaint, thank you, etc.
- **{recipient}**: Boss, colleague, client, vendor, potential partner, etc.
- **{tone}**: Formal, casual, friendly, urgent, apologetic, enthusiastic, etc.
- **{key_points}**: Specific information, deadlines, requests, offers, updates, etc.

## Usage Examples

### Example 1: Meeting Request
**Input Variables:**
- purpose: "request a meeting to discuss project collaboration"
- recipient: "a potential business partner I met at a conference"
- tone: "professional but friendly"
- key_points: "our company's expertise, mutual benefits, proposed next steps"

**Expected Output:**
A well-structured email with appropriate subject line, warm greeting, clear meeting request, and specific action items.

### Example 2: Project Update
**Input Variables:**
- purpose: "provide weekly project status update"
- recipient: "project stakeholders and team leads"
- tone: "professional and informative"
- key_points: "completed milestones, current challenges, upcoming deadlines"

**Expected Output:**
A structured update email with clear sections, bullet points for easy reading, and highlighted action items.

## Tips for Best Results

- Be specific about the relationship with the recipient
- Include any relevant deadlines or time constraints
- Mention the preferred response method if applicable
- Consider the recipient's perspective and priorities
- Specify if you need a template for similar future emails
- Include any company-specific requirements or constraints

## Related Prompts

- [Meeting Agenda Creator](meeting-agenda-creator.md)
- [Professional Letter Writer](professional-letter-writer.md)
- [Client Communication Template](../personal/client-communication-template.md)

## Changelog

- **v1.0** (2025-07-31): Initial version with comprehensive email structure
