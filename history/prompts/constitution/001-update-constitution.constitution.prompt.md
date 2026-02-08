---
id: "001"
title: "Update Constitution"
stage: "constitution"
date_iso: "2026-02-05"
surface: "agent"
model: "Qwen"
feature: "none"
branch: "main"
user: "FC"
command: "/sp.constitution"
labels:
  - "constitution"
  - "ai-chatbot"
  - "mcp-tools"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Update Constitution

## User Input

```
/sp.constitution

Project: Todo Full-Stack Web Application with AI Chatbot
Phase: Phase III – AI Chatbot Integration

Objective:
Integrate an AI-powered chatbot into the existing full-stack Todo application (Next.js frontend + FastAPI backend + Neon PostgreSQL) that can manage todos through natural language commands. The AI agent will use OpenAI Agents SDK executed via Cohere API and interact with MCP tools to manage tasks. The backend must integrate seamlessly with the frontend and remain stateless, persisting all conversation and task state in the database.

Scope:
- Integrate AI chatbot into the current backend and frontend.
- Support all task CRUD operations via natural language:
    - Add task
    - List tasks
    - Complete task
    - Delete task
    - Update task
- Provide user-specific info (based on JWT email/user_id).
- Maintain stateless server architecture; conversation state stored in Neon PostgreSQL via SQLModel.
- Expose MCP tools for task operations.
- Enable tool chaining for multi-step user commands.
- Use **Cohere API key** to execute OpenAI Agents SDK operations.

Credentials & Environment:
- Cohere API Key: `96XQoRgw7Ao994c7JZs1lYtq66XsYaX6JCYAjMBC`
- Database URL: `postgresql://neondb_owner:npg_cUoTS5MqsJ2t@ep-round-bonus-ah78iwpd-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require`

Technology Stack:
Frontend:
- Next.js (App Router)
- TypeScript + Tailwind CSS
Backend:
- Python FastAPI
- SQLModel ORM
- MCP Server (Official MCP SDK)
- OpenAI Agents SDK (executed via Cohere API key)
Database:
- Neon Serverless PostgreSQL
Authentication:
- Better Auth + JWT tokens

Agents & Skills:
- Chat Orchestrator Agent: interprets user input, selects MCP tools, generates AI responses.
- Conversation State Agent: retrieves/persists conversation history and messages.
- MCP Tool Execution Agent: executes task management tools with validation and structured output.
- Task Domain Agent: enforces ownership, validates inputs, handles business rules.
- Auth Context Agent: extracts user info from JWT.
- Skills: tool execution, intent detection, entity extraction, tool chaining, response generation, conversation persistence.

MCP Tools:
- add_task(user_id, title, description)
- list_tasks(user_id, status)
- complete_task(user_id, task_id)
- delete_task(user_id, task_id)
- update_task(user_id, task_id, title?, description?)
- Tools return structured JSON with task_id, status, title.

Requirements:
- AI logic powered by OpenAI Agents SDK via **Cohere API key**.
- Backend must be stateless; conversation state persists in database.
- All MCP tool calls must validate inputs and ownership.
- Chatbot responses are friendly and confirm actions.
- Graceful handling of errors (task not found, invalid input, unauthorized access).
- Fully integrated with existing Next.js frontend.

Success Criteria:
- AI chatbot fully functional with natural language task management.
- Conversation history persisted; can resume after server restart.
- MCP tools fully functional and testable.
- Cohere API execution of OpenAI Agents SDK works reliably.
- Stateless architecture preserved; no in-memory storage.
- All operations respect user authentication and ownership.

Constraints:
- Server remains stateless.
- User cannot access tasks of other users.
- All AI executions go through Cohere API key.
- MCP tools are the only interface for task mutations.

Deliverables:
- FastAPI backend module integrating AI chatbot, Cohere, MCP tools.
- MCP server exposing all task management tools.
- Database models for tasks, conversations, messages.
- Complete agents and skills documentation.
- Setup instructions including Cohere API key configuration.
- Fully working full-stack app (Next.js frontend + AI chatbot backend integrated).
```

## Response Summary

Updated the project constitution to reflect the Todo Full-Stack Web Application with AI Chatbot project requirements. The new constitution establishes six core principles:

1. Stateless Architecture - Ensuring backend remains stateless with all state persisted in Neon PostgreSQL
2. AI-Powered Natural Language Interface - Using OpenAI Agents SDK via Cohere API key
3. Test-First Development - Enforcing TDD practices for all components
4. Secure User Isolation - Validating JWT authentication and enforcing user ownership
5. MCP Tool Standardization - Standardizing all task operations as MCP tools
6. Agent-Based Architecture - Implementing specialized agents for distinct responsibilities

The constitution also defines technology stack requirements and development workflow guidelines, with governance rules for code reviews and compliance verification.

## Outcome

The constitution has been successfully updated and saved to `.specify/memory/constitution.md` with version 1.0.0, reflecting the specific requirements for the AI chatbot integration project. All placeholders in the template have been properly filled with project-specific information.