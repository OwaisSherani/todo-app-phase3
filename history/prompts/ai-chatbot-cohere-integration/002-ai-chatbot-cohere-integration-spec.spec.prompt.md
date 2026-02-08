---
id: "002"
title: "AI Chatbot Cohere Integration Spec"
stage: "spec"
date_iso: "2026-02-05"
surface: "agent"
model: "Qwen"
feature: "ai-chatbot-cohere-integration"
branch: "001-ai-chatbot-cohere-integration"
user: "FC"
command: "/sp.specify"
labels:
  - "ai-chatbot"
  - "cohere"
  - "mcp-tools"
  - "natural-language-processing"
links:
  spec: "specs/001-ai-chatbot-cohere-integration/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-ai-chatbot-cohere-integration/spec.md"
  - "specs/001-ai-chatbot-cohere-integration/checklists/requirements.md"
tests_yaml: []
---

# AI Chatbot Cohere Integration Spec

## User Input

```
Feature: Todo AI Chatbot Integration with Cohere Objective: Implement a fully functional AI chatbot within the existing Todo full-stack application. The chatbot should use OpenAI Agents SDK executed via Cohere API and be fully integrated with frontend UI (Next.js) and backend (FastAPI + MCP tools). Users should be able to manage todos via natural language commands. Scope: - Integrate OpenAI Agents SDK with Cohere API key. - Replace all Gemini references in code with Cohere API integration. - Backend (FastAPI) should host the MCP server exposing tools for: - add_task - list_tasks - complete_task - delete_task - update_task - Chatbot receives user messages via POST /api/{user_id}/chat endpoint. - Chatbot can perform actions and respond with friendly confirmations. - Persist conversation state in Neon PostgreSQL using SQLModel. - Ensure stateless server: no in-memory conversation state. - Frontend integration: - Chatbot icon in UI accessible on all pages. - Messages flow from frontend ChatKit → backend Agents SDK → MCP tools → response. - Display AI responses, tool confirmations, and error messages. Cohere Integration Details: - Use environment variable `COHERE_API_KEY`. - Replace AsyncOpenAI provider with Cohere-compatible API client. - Ensure OpenAI Agents SDK uses Cohere as the execution backend. - Implement function_tools for task operations (add, update, complete, delete, list). - Ensure proper structured JSON responses from all function tools. Conversation Flow: 1. User types message in frontend chat. 2. Message sent to FastAPI `/api/{user_id}/chat`. 3. Backend: - Retrieves conversation history from DB. - Builds message array for Agent. - Agent calls appropriate MCP tool(s) via function_tools. - Persists user message and assistant response to DB. 4. Response returned to frontend for display in ChatKit UI. Success Criteria: - Cohere API executes OpenAI Agents SDK correctly. - All MCP tools callable via chatbot and return expected results. - Chatbot integrated into frontend UI with accessible chat icon. - Stateless backend architecture preserved; conversation resumes after server restart. - User authentication enforced via JWT; user can only access own tasks. - Full CRUD operations via chatbot commands. - Friendly confirmations and graceful error handling. Constraints: - Server must remain stateless; all conversation state in DB. - No direct frontend manipulation of task state; all via MCP tools. - Cohere API key must be securely loaded via environment variables. - Responses must be structured and easily parsed by frontend. Deliverables: - Backend FastAPI module integrating Agents SDK + Cohere + MCP tools. - Function_tools implementations for all task operations. - Frontend chat UI integrated with chat icon and message display. - Fully working end-to-end AI chatbot within full-stack Todo app. - Documentation of all Agents, function_tools, and API integration. - Setup instructions including environment variables for Cohere API key.
```

## Response Summary

Created a comprehensive feature specification for the AI Chatbot Integration with Cohere. The specification includes:

1. Three prioritized user stories:
   - Natural Language Task Management (P1)
   - Persistent Conversation Experience (P2)
   - Secure Task Access Control (P3)

2. Thirteen functional requirements covering:
   - AI chatbot interface accessibility
   - Natural language task operations (create, view, update, complete, delete)
   - Conversation state persistence
   - Stateless architecture maintenance
   - User authentication and access control
   - Error handling

3. Four key entities defined:
   - Task, Conversation, Message, and User

4. Eight measurable success criteria including:
   - 90% accuracy for natural language commands
   - 5-second response time for chatbot
   - 95% success rate for task operations
   - Data isolation enforcement

The specification removes implementation-specific details to focus on user value and business needs, making it technology-agnostic while maintaining clear requirements for development teams.

## Outcome

The feature specification is complete and ready for the planning phase. The branch `001-ai-chatbot-cohere-integration` has been created with the spec file at `specs/001-ai-chatbot-cohere-integration/spec.md` and a quality checklist at `specs/001-ai-chatbot-cohere-integration/checklists/requirements.md`.