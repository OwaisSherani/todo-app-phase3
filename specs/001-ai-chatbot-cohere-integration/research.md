# Research: AI Chatbot Integration with Cohere

## Decision: Agent Orchestration Approach
**Rationale**: After evaluating options, we chose Option 2 (Specialized agents per task operation) for better modularity and maintainability, despite increased complexity.
**Alternatives considered**: 
- Option 1: Single Orchestrator Agent (simpler but less maintainable)
- Option 2: Specialized agents per task operation (chosen for maintainability)

## Decision: Conversation State Handling
**Rationale**: Selected Option 2 (Persist in Neon DB) to comply with stateless architecture requirement.
**Alternatives considered**:
- Option 1: In-memory (violates stateless constraint)
- Option 2: Persist in Neon DB (chosen for stateless design)

## Decision: Cohere API Integration
**Rationale**: All OpenAI Agents SDK calls will be routed through Cohere API to leverage their execution capabilities.
**Alternatives considered**:
- Direct OpenAI API calls
- Cohere API for execution (selected for project requirements)

## Decision: Frontend Chat Integration
**Rationale**: Chat icon will be placed as a floating element accessible on all pages, with ChatKit UI for message display.
**Alternatives considered**:
- Dedicated chat page
- Floating chat icon with overlay (selected for accessibility)

## Technical Unknowns Resolved

### 1. Cohere API Implementation Details
- **Question**: How to properly configure OpenAI Agents SDK to execute via Cohere API
- **Answer**: Use Cohere's compatibility layer that allows OpenAI SDK calls to be processed by Cohere's backend

### 2. MCP Tools Implementation
- **Question**: How to implement standardized MCP tools for task operations
- **Answer**: Use the official MCP SDK to create tools that map to our task operations (add, list, complete, delete, update)

### 3. Conversation Persistence Strategy
- **Question**: How to store and retrieve conversation history efficiently
- **Answer**: Store conversations and messages in Neon PostgreSQL using SQLModel, with indexed foreign keys for performance

### 4. JWT Authentication Integration
- **Question**: How to extract and validate user identity from JWT tokens in chat endpoints
- **Answer**: Use existing Better Auth middleware to validate tokens and extract user_id for all chat operations

### 5. Frontend-Backend Communication
- **Question**: How to structure the API for chat interactions
- **Answer**: Create a POST endpoint `/api/{user_id}/chat` that accepts user messages and returns structured responses