---
id: "003"
title: "AI Chatbot Cohere Integration Plan"
stage: "plan"
date_iso: "2026-02-05"
surface: "agent"
model: "Qwen"
feature: "ai-chatbot-cohere-integration"
branch: "001-ai-chatbot-cohere-integration"
user: "FC"
command: "/sp.plan"
labels:
  - "ai-chatbot"
  - "cohere"
  - "mcp-tools"
  - "planning"
links:
  spec: "specs/001-ai-chatbot-cohere-integration/spec.md"
  plan: "specs/001-ai-chatbot-cohere-integration/plan.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-ai-chatbot-cohere-integration/plan.md"
  - "specs/001-ai-chatbot-cohere-integration/research.md"
  - "specs/001-ai-chatbot-cohere-integration/data-model.md"
  - "specs/001-ai-chatbot-cohere-integration/quickstart.md"
  - "specs/001-ai-chatbot-cohere-integration/contracts/chat-api-contract.md"
tests_yaml: []
---

# AI Chatbot Cohere Integration Plan

## User Input

```
/sp.plan

Create:
- Architecture sketch: FastAPI backend + MCP server + Cohere-executed OpenAI Agents SDK + Neon DB + Next.js frontend chat UI.
- Section structure: Agents, Skills, MCP tools, API endpoints, DB models, Frontend chat components.
- Workflow plan: Stepwise instructions for Qwen CLI to implement each backend & frontend integration piece.
- Quality validation: Ensure stateless server, secure Cohere API key usage, JWT-based authentication, proper DB persistence, and friendly chatbot responses.

Decisions Needing Documentation:
1. Agent orchestration approach:
   - Option 1: Single Orchestrator Agent handles all tool calls.
   - Option 2: Specialized agents per task operation (add/list/update/delete/complete).
   - Tradeoff: Modularity vs complexity; Option 2 preferred for maintainability.
2. Conversation state handling:
   - Option 1: In-memory (violates stateless constraint).
   - Option 2: Persist in Neon DB (chosen for stateless design).
3. Frontend integration:
   - Chat icon placement and accessibility across pages.
   - UI behavior for messages, confirmations, and error states.
4. Cohere API usage:
   - Secure storage via .env file.
   - All OpenAI Agents SDK calls routed through Cohere.

Technical Details:
- Use research-concurrent approach: implement agents and MCP tools while coding backend; validate each step.
- Follow existing backend CLAUDE.md patterns for FastAPI + SQLModel.
- Define all function_tools for add_task, list_tasks, complete_task, delete_task, update_task with structured JSON outputs.
- Integrate frontend chat icon and ChatKit UI with backend endpoint `/api/{user_id}/chat`.
- Validate JWT auth in backend; each MCP tool verifies user_id before performing operations.
- Ensure statelessness: all conversation state persisted in Neon PostgreSQL.
- Provide full end-to-end testing: message → agent → MCP tool → DB → frontend response.

Phases:
1. Database & Models
   - Verify task, conversation, message tables.
   - Ensure user_id FK integrity with Better Auth users.
2. MCP Tools Implementation
   - Implement add_task, list_tasks, complete_task, delete_task, update_task as function_tools.
   - Include validation, ownership checks, structured response.
3. Agents & Skills
   - Setup Orchestrator Agent and Task Domain Agent.
   - Skills: intent detection, tool execution, tool chaining, response formatting, error handling.
4. Cohere Integration
   - Replace any Gemini references with Cohere API key.
   - Ensure OpenAI Agents SDK functions execute via Cohere.
5. Backend Chat Endpoint
   - `/api/{user_id}/chat` accepts user message, retrieves conversation history, runs agent, stores responses, returns structured JSON.
6. Frontend Integration
   - Chat icon on UI.
   - Messages displayed in ChatKit.
   - Actions and confirmations shown correctly.
7. Testing & Validation
   - CRUD operations via natural language verified.
   - Conversation persistence across server restarts.
   - Error handling and security checks validated.

Success Criteria:
- AI chatbot fully functional and integrated.
- Cohere-executed OpenAI Agents SDK works reliably.
- MCP tools correctly called and return expected results.
- Stateless backend preserved.
- Frontend chat icon & messages fully functional.
- Friendly confirmations, graceful error handling, conversation persistence validated.

Deliverables:
- Fully implemented backend with MCP + Cohere + Agents SDK.
- Frontend chat UI integrated.
- Agents, Skills, MCP tools documented.
- Setup instructions including .env configuration.
- End-to-end tested full-stack Todo app with AI chatbot.
```

## Response Summary

Completed the implementation planning for the AI Chatbot Integration with Cohere feature. The plan includes:

1. **Technical Context**: Defined the technology stack including Python 3.11, FastAPI, SQLModel, Cohere API, OpenAI Agents SDK, Next.js, and Better Auth.

2. **Constitution Check**: Verified compliance with all core principles including stateless architecture, AI-powered interface, test-first development, secure user isolation, MCP tool standardization, and agent-based architecture.

3. **Project Structure**: Outlined the complete project structure with separate frontend and backend components, including models, services, agents, tools, and API layers.

4. **Research Findings**: Documented key decisions on agent orchestration approach, conversation state handling, Cohere API integration, and frontend chat integration.

5. **Data Models**: Created detailed entity definitions for Task, Conversation, Message, and User with fields, validation rules, and relationships.

6. **API Contracts**: Defined the chat endpoint API contract and MCP tools contracts with request/response structures.

7. **Quickstart Guide**: Provided comprehensive setup and usage instructions for the feature.

8. **Agent Context Update**: Updated the Qwen agent context with the new technologies and frameworks for this feature.

## Outcome

The implementation plan is complete and ready for the task breakdown phase. All necessary design artifacts have been created including research, data models, API contracts, and quickstart documentation. The plan complies with all constitutional principles and is structured for efficient implementation.