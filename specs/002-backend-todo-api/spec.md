# Feature Specification: Backend Todo API with JWT Authentication

**Feature Branch**: `002-backend-todo-api`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "Project: Todo Full-Stack Web Application — Backend (Phase II Web + Phase III Ready) Target Outcome: Build a complete, production-ready FastAPI backend for a multi-user Todo web application. The backend must integrate seamlessly with the existing Next.js frontend and support secure authentication, persistent storage, REST APIs, and future AI chatbot expansion. This specification is COMPLETE and must result in a fully working backend. ──────────────────────── Scope ──────────────────────── Build the entire backend system including: - REST API for Todo CRUD - Secure JWT authentication verification - Neon Serverless PostgreSQL integration - SQLModel ORM models - Middleware for auth & user isolation - API behavior aligned with frontend usage - Clean project structure ready for AI chatbot extension Frontend already exists and MUST work without modification. ──────────────────────── Technology Stack (Fixed) ──────────────────────── Backend Framework: FastAPI (Python) ORM: SQLModel Database: Neon Serverless PostgreSQL Authentication: Better Auth (JWT issued by frontend) API Style: REST Deployment Ready: Yes Environment Variables (Required): - BETTER_AUTH_SECRET=AHSUNFBk2aqSfOvYcLGLTSorUo7yZhl7 - BETTER_AUTH_URL=http://localhost:3000 - Neon_db_url='postgresql://neondb_owner:npg_cUoTS5MqsJ2t@ep-round-bonus-ah78iwpd-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require' ──────────────────────── Authentication & Security ──────────────────────── Authentication Model: - Frontend uses Better Auth (Next.js) - Backend receives JWT via Authorization header: Authorization: Bearer <token> Backend Responsibilities: - Verify JWT signature using BETTER_AUTH_SECRET - Decode token to extract: - user_id - email - Reject requests with: - Missing token → 401 - Invalid token → 401 - user_id mismatch → 403 Rules: - Backend is stateless - Backend NEVER stores sessions - Every request must be authenticated - user_id from JWT is the source of truth ──────────────────────── Database Models ──────────────────────── Task: - id (int, PK) - user_id (string, indexed) - title (string, required) - description (string, optional) - completed (boolean, default false) - created_at (datetime) - updated_at (datetime) Constraints: - user_id + id ownership enforced at query level - No cross-user access allowed ──────────────────────── API Endpoints (Required) ──────────────────────── GET /api/{user_id}/tasks - List all tasks for authenticated user POST /api/{user_id}/tasks - Create new task - Body: title, description (optional) GET /api/{user_id}/tasks/{id} - Get single task details PUT /api/{user_id}/tasks/{id} - Update title and/or description DELETE /api/{user_id}/tasks/{id} - Delete task permanently PATCH /api/{user_id}/tasks/{id}/complete - Toggle completion state Rules: - user_id in URL MUST match user_id in JWT - All queries filtered by authenticated user - Proper HTTP status codes required ──────────────────────── Middleware & Architecture ──────────────────────── Implement: - JWT verification middleware - Dependency that injects: - current_user_id - current_user_email - Error-safe decoding and validation Backend must: - Use dependency injection - Avoid global state - Be horizontally scalable ──────────────────────── Frontend Integration Requirements ──────────────────────── Backend must support: - Frontend API client attaching JWT automatically - CORS configured for http://localhost:3000 - JSON responses matching frontend expectations Response behavior: - Clear success responses - Descriptive error messages - Consistent response format ──────────────────────── Non-Goals ──────────────────────── - No frontend UI work - No auth provider implementation - No AI chatbot logic yet (backend must be ready for it) ──────────────────────── Quality Bar ──────────────────────── - Production-ready code - Clean folder structure - No hardcoded secrets - Secure user isolation - Correct SQLModel usage - Clear API contracts ──────────────────────── Acceptance Criteria ──────────────────────── The backend is considered COMPLETE when: - Frontend can: - Sign in user - Fetch tasks - Create, update, delete, complete tasks - JWT auth works reliably - Users can only see their own data - Neon DB persists data correctly - Server restarts do not break functionality - Codebase is ready for Phase III AI chatbot ──────────────────────── Deliverables ──────────────────────── - Fully working FastAPI backend - SQLModel models and migrations - JWT middleware - REST API routes - README with setup instructions - .env usage documented Status: COMPLETE"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Authenticate and Access Tasks (Priority: P1)

As a signed-in user, I want to securely access my tasks through the backend API so that I can manage my to-do items. The system verifies my JWT token and allows me to view only my own tasks.

**Why this priority**: This is the foundational functionality that enables all other task operations. Without secure authentication and proper user isolation, the system cannot function safely.

**Independent Test**: Can be fully tested by authenticating with a valid JWT and successfully retrieving the user's tasks, while ensuring other users' tasks remain inaccessible.

**Acceptance Scenarios**:

1. **Given** user is authenticated with a valid JWT, **When** user requests their tasks via GET /api/{user_id}/tasks, **Then** system returns only tasks belonging to that user
2. **Given** user presents an invalid or expired JWT, **When** user requests their tasks, **Then** system returns 401 Unauthorized error

---

### User Story 2 - Create and Manage Individual Tasks (Priority: P2)

As a user, I want to create, update, delete, and mark tasks as complete through the API so that I can effectively manage my to-do list.

**Why this priority**: This provides the core CRUD functionality that users need to interact with their tasks, building on the authentication foundation.

**Independent Test**: Can be fully tested by creating a task with valid data, updating its properties, toggling its completion status, and deleting it, all while maintaining proper authentication.

**Acceptance Scenarios**:

1. **Given** user is authenticated with valid JWT, **When** user creates a new task via POST /api/{user_id}/tasks, **Then** system creates the task and returns it with a unique ID
2. **Given** user has an existing task, **When** user updates the task via PUT /api/{user_id}/tasks/{id}, **Then** system updates the task details and returns the updated task
3. **Given** user has an existing task, **When** user toggles completion via PATCH /api/{user_id}/tasks/{id}/complete, **Then** system updates the completion status and returns the updated task

---

### User Story 3 - Secure Cross-User Isolation (Priority: P3)

As a security-conscious user, I want to ensure that I can only access my own tasks and never see another user's data, even if I try to access their task IDs directly.

**Why this priority**: This is critical for data privacy and security, ensuring that the system properly isolates user data at the API level.

**Independent Test**: Can be tested by attempting to access another user's tasks using valid authentication but incorrect user/task combinations, ensuring access is denied.

**Acceptance Scenarios**:

1. **Given** user is authenticated with valid JWT for user A, **When** user attempts to access user B's task via GET /api/{user_B_id}/tasks/{task_id}, **Then** system returns 403 Forbidden error
2. **Given** user is authenticated with valid JWT, **When** user attempts to modify another user's task, **Then** system returns 403 Forbidden error

---

### Edge Cases

- What happens when a user's JWT is malformed or tampered with?
- How does the system handle requests with missing authorization headers?
- What occurs when a user attempts to access a non-existent task ID?
- How does the system behave when database connection is temporarily unavailable?
- What happens when a user tries to create a task with an empty title?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST verify JWT tokens using the BETTER_AUTH_SECRET environment variable
- **FR-002**: System MUST extract user_id and email from decoded JWT tokens
- **FR-003**: Users MUST be able to list all their tasks via GET /api/{user_id}/tasks
- **FR-004**: Users MUST be able to create new tasks via POST /api/{user_id}/tasks with title and optional description
- **FR-005**: Users MUST be able to retrieve individual tasks via GET /api/{user_id}/tasks/{id}
- **FR-006**: Users MUST be able to update task details via PUT /api/{user_id}/tasks/{id}
- **FR-007**: Users MUST be able to delete tasks via DELETE /api/{user_id}/tasks/{id}
- **FR-008**: Users MUST be able to toggle task completion via PATCH /api/{user_id}/tasks/{id}/complete
- **FR-009**: System MUST reject requests with missing or invalid JWT tokens with 401 status
- **FR-010**: System MUST reject requests where URL user_id doesn't match JWT user_id with 403 status
- **FR-011**: System MUST store tasks in Neon Serverless PostgreSQL database with SQLModel
- **FR-012**: System MUST enforce user isolation by filtering all queries by authenticated user_id
- **FR-013**: System MUST return appropriate HTTP status codes (200, 201, 401, 403, 404, 500)
- **FR-014**: System MUST configure CORS to allow requests from http://localhost:3000
- **FR-015**: System MUST persist task data with the following attributes: id, user_id, title, description, completed, created_at, updated_at

### Key Entities

- **Task**: Represents a user's to-do item with properties: id (unique identifier), user_id (owner), title (required), description (optional), completed (boolean), timestamps
- **User**: Identified by user_id extracted from JWT, owns zero or more tasks, accesses only their own data

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can authenticate with JWT and successfully perform all CRUD operations on their tasks with 99% success rate
- **SC-002**: System prevents unauthorized access to other users' tasks with 100% accuracy (zero data leakage between users)
- **SC-003**: API responds to requests within 500ms under normal load conditions (95th percentile)
- **SC-004**: System maintains data persistence across server restarts with 100% data integrity
- **SC-005**: Frontend application can seamlessly integrate with the backend API without requiring modifications
- **SC-006**: Backend supports horizontal scaling without session or state dependencies
