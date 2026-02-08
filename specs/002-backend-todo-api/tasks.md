# Development Tasks: Backend Todo API with JWT Authentication

**Feature**: Backend Todo API with JWT Authentication  
**Branch**: 002-backend-todo-api  
**Generated**: 2026-02-06  
**Input**: spec.md, plan.md, data-model.md, contracts/todo-api-openapi.yaml

## Implementation Strategy

Build the backend in priority order of user stories, starting with authentication and task access (US1), then CRUD operations (US2), and finally security isolation (US3). Each user story should be independently testable and form a complete, functional increment.

**MVP Scope**: US1 (authentication and task access) with basic models and database layer.

## Phase 1: Project Setup

Initialize the project structure, dependencies, and configuration.

- [X] T001 Create backend directory structure with all required subdirectories
- [X] T002 Create requirements.txt with FastAPI, SQLModel, PyJWT, Neon driver, pytest
- [X] T003 Create main.py with basic FastAPI app initialization
- [X] T004 Create config.py to manage environment variables (BETTER_AUTH_SECRET, DATABASE_URL)
- [X] T005 Set up .env file with required environment variables
- [X] T006 Configure CORS middleware to allow http://localhost:3000

## Phase 2: Foundational Components

Build the foundational components that all user stories depend on.

- [X] T007 Create database.py with Neon PostgreSQL connection and session management
- [X] T008 Create models.py with Task SQLModel definition (id, user_id, title, description, completed, timestamps)
- [X] T009 Create schemas.py with Pydantic models for requests/responses (TaskRead, TaskCreate, TaskUpdate)
- [X] T010 Create auth.py with JWT verification utilities and middleware
- [X] T011 Create dependencies.py with FastAPI dependency for current user extraction
- [X] T012 Create tests/conftest.py with test configuration and fixtures
- [X] T013 Create basic tests for database connection and model validation

## Phase 3: User Story 1 - Authenticate and Access Tasks (Priority: P1)

As a signed-in user, I want to securely access my tasks through the backend API so that I can manage my to-do items. The system verifies my JWT token and allows me to view only my own tasks.

**Why this priority**: This is the foundational functionality that enables all other task operations. Without secure authentication and proper user isolation, the system cannot function safely.

**Independent Test**: Can be fully tested by authenticating with a valid JWT and successfully retrieving the user's tasks, while ensuring other users' tasks remain inaccessible.

- [X] T014 [P] [US1] Create GET /api/{user_id}/tasks endpoint to list user's tasks
- [X] T015 [P] [US1] Implement JWT token verification in auth.py
- [X] T016 [US1] Add authentication check to GET /api/{user_id}/tasks endpoint
- [X] T017 [US1] Implement user_id validation (JWT vs URL)
- [X] T018 [US1] Add user isolation filter to GET /api/{user_id}/tasks (filter by user_id)
- [X] T019 [US1] Create test for successful task retrieval with valid JWT
- [X] T020 [US1] Create test for 401 error with invalid/expired JWT
- [X] T021 [US1] Create test for 403 error when JWT user_id doesn't match URL user_id

## Phase 4: User Story 2 - Create and Manage Individual Tasks (Priority: P2)

As a user, I want to create, update, delete, and mark tasks as complete through the API so that I can effectively manage my to-do list.

**Why this priority**: This provides the core CRUD functionality that users need to interact with their tasks, building on the authentication foundation.

**Independent Test**: Can be fully tested by creating a task with valid data, updating its properties, toggling its completion status, and deleting it, all while maintaining proper authentication.

- [X] T022 [P] [US2] Create POST /api/{user_id}/tasks endpoint to create new tasks
- [X] T023 [P] [US2] Create PUT /api/{user_id}/tasks/{id} endpoint to update tasks
- [X] T024 [P] [US2] Create DELETE /api/{user_id}/tasks/{id} endpoint to delete tasks
- [X] T025 [P] [US2] Create PATCH /api/{user_id}/tasks/{id}/complete endpoint to toggle completion
- [X] T026 [US2] Add authentication and user_id validation to all new endpoints
- [X] T027 [US2] Implement user isolation checks for all task operations
- [X] T028 [US2] Add validation for required fields (title) in task creation
- [X] T029 [US2] Create tests for successful task creation
- [X] T030 [US2] Create tests for successful task updates
- [X] T031 [US2] Create tests for successful task deletion
- [X] T032 [US2] Create tests for successful completion toggling
- [X] T033 [US2] Create tests for 403 error when accessing another user's task

## Phase 5: User Story 3 - Secure Cross-User Isolation (Priority: P3)

As a security-conscious user, I want to ensure that I can only access my own tasks and never see another user's data, even if I try to access their task IDs directly.

**Why this priority**: This is critical for data privacy and security, ensuring that the system properly isolates user data at the API level.

**Independent Test**: Can be tested by attempting to access another user's tasks using valid authentication but incorrect user/task combinations, ensuring access is denied.

- [X] T034 [P] [US3] Enhance all endpoints with robust user ownership validation
- [X] T035 [US3] Create comprehensive tests for cross-user access prevention
- [X] T036 [US3] Implement additional security checks for edge cases
- [X] T037 [US3] Add logging for unauthorized access attempts
- [X] T038 [US3] Create tests for malformed JWT handling
- [X] T039 [US3] Create tests for missing authorization header handling
- [X] T040 [US3] Create tests for non-existent task ID handling

## Phase 6: Polish & Cross-Cutting Concerns

Final touches, documentation, and integration validation.

- [X] T041 Add comprehensive error handling with appropriate HTTP status codes
- [X] T042 Create README.md with setup and usage instructions
- [X] T043 Add input validation and sanitization
- [X] T044 Implement proper timestamp handling for created_at and updated_at
- [X] T045 Add database transaction management where needed
- [X] T046 Perform end-to-end integration tests
- [X] T047 Validate API responses match frontend expectations
- [X] T048 Run all tests to ensure no regressions
- [X] T049 Document API endpoints with examples
- [X] T050 Prepare for integration with existing frontend

## Dependencies

- **US2 depends on**: US1 (requires authentication foundation)
- **US3 depends on**: US1 and US2 (requires both authentication and CRUD operations to test isolation)

## Parallel Execution Opportunities

- **Within US1**: JWT verification (T015) and endpoint creation (T014) can be done in parallel
- **Within US2**: All four CRUD endpoints (T022-T025) can be developed in parallel
- **Across stories**: Database and model setup (Phase 2) can happen before user stories are implemented