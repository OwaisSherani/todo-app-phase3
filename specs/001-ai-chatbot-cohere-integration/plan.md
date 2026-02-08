# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement an AI chatbot for the Todo application that allows users to manage tasks via natural language commands. The solution will use OpenAI Agents SDK executed via Cohere API, with MCP tools for standardized task operations. The backend will maintain stateless architecture by persisting all conversation state in Neon PostgreSQL. The frontend will feature a chat icon accessible on all pages with ChatKit UI for message display.

## Technical Context

**Language/Version**: Python 3.11, TypeScript/JavaScript for frontend
**Primary Dependencies**: FastAPI, SQLModel, Cohere API, OpenAI Agents SDK, Next.js, Better Auth
**Storage**: Neon Serverless PostgreSQL via SQLModel ORM
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application (server-side API + client-side UI)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <5s response time for chatbot interactions, 90%+ accuracy in command interpretation
**Constraints**: Must maintain stateless server architecture, secure Cohere API key usage, JWT-based authentication
**Scale/Scope**: Individual user task management with proper data isolation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Verification:
- **Stateless Architecture**: ✓ Plan ensures all conversation state persists in Neon PostgreSQL; no in-memory storage
- **AI-Powered Natural Language Interface**: ✓ Using OpenAI Agents SDK via Cohere API key for natural language processing
- **Test-First Development**: ✓ Tests will be written before implementation for all components
- **Secure User Isolation**: ✓ JWT authentication enforced; MCP tools validate user ownership
- **MCP Tool Standardization**: ✓ Standardized tools for task operations with structured JSON responses
- **Agent-Based Architecture**: ✓ Specialized agents for distinct responsibilities (Chat Orchestrator, Conversation State, etc.)

### Gates:
- All design decisions must comply with stateless architecture principle
- MCP tools must return consistent structured JSON responses
- User authentication and data isolation must be enforced at all levels
- Cohere API key must be securely managed via environment variables

### Post-Design Verification:
- **Data Models**: Task, Conversation, and Message entities properly defined with relationships
- **API Contracts**: Standardized endpoints and MCP tools with consistent response formats
- **Architecture**: Stateless design maintained with all state persisted in database
- **Security**: JWT authentication integrated at all access points

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-chatbot-cohere-integration/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/          # SQLModel database models (Task, Conversation, Message)
│   ├── services/        # Business logic (task operations, conversation management)
│   ├── agents/          # AI agents (orchestrator, task domain, etc.)
│   ├── tools/           # MCP tools (add_task, list_tasks, etc.)
│   └── api/             # FastAPI endpoints (chat endpoint)
├── main.py              # Main application entry point
├── mcp_server.py        # MCP server implementation
└── config.py            # Configuration including Cohere API key handling

frontend/
├── src/
│   ├── components/
│   │   ├── ChatBot/     # Chat interface component
│   │   └── ChatIcon/    # Floating chat icon component
│   ├── pages/
│   ├── services/
│   │   └── apiClient.js # API client for chat endpoint
│   └── utils/
└── tests/

tests/
├── contract/
├── integration/
│   └── test_chatbot.py  # End-to-end chatbot tests
└── unit/
    ├── test_agents/     # Unit tests for agents
    ├── test_tools/      # Unit tests for MCP tools
    └── test_models/     # Unit tests for data models
```

**Structure Decision**: Web application with separate frontend (Next.js) and backend (FastAPI) components. Backend contains models, services, agents, and tools. Frontend contains chat components and API client.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Multiple specialized agents | Need distinct responsibilities for maintainability | Single agent would create monolithic, hard-to-maintain code |
| MCP tool standardization | Required for tool chaining and consistent responses | Direct function calls would lack standardization |
| Separate frontend/backend | Required for proper architecture separation | Monolithic approach would reduce flexibility |
