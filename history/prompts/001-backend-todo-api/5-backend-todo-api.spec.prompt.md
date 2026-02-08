---
id: 5
title: "backend-todo-api"
stage: spec
date_iso: "2026-01-04"
surface: agent
model: "Qwen Code"
feature: "001-backend-todo-api"
branch: "001-backend-todo-api"
user: "user"
command: "sp.specify"
labels: ["backend", "api", "fastapi", "todo-app", "jwt", "postgresql"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-backend-todo-api/spec.md"
  - "specs/001-backend-todo-api/checklists/requirements.md"
tests_yaml: []
prompt_text: |
  Production-Ready Backend for Todo Full-Stack Web Application Objective: Build a complete, secure, and production-grade backend service for the Todo Web Application using FastAPI. The backend must integrate seamlessly with the existing Next.js frontend, use Neon Serverless PostgreSQL for persistence, and authenticate users via JWT tokens issued by Better Auth. Target Audience: - Hackathon judges - Full-stack developers reviewing architecture and correctness - Spec-driven agents (Claude Code / Qwen CLI) Success Criteria: - All task CRUD operations work end-to-end with the frontend - JWT-based authentication is enforced on every API request - Users can only access and modify their own tasks - Backend connects reliably to Neon PostgreSQL - API responses are consistent, validated, and frontend-ready - Clear error handling (401, 403, 404, 422) - Backend can be started and tested locally without manual fixes Technology Stack: - Backend Framework: FastAPI (Python) - ORM: SQLModel - Database: Neon Serverless PostgreSQL - Authentication: Better Auth (JWT verification only) - API Style: RESTful JSON API Environment Configuration: The backend must rely on the following environment variables: - BETTER_AUTH_SECRET - BETTER_AUTH_URL - DATABASE_URL (Neon PostgreSQL connection string) Example .env: BETTER_AUTH_SECRET=**** BETTER_AUTH_URL=http://localhost:3000 DATABASE_URL=postgresql://<user>:<password>@<host>/<db>?sslmode=require Backend Scope: Included: - FastAPI application setup - Database connection & session management - SQLModel models - JWT verification middleware / dependency - Task CRUD API endpoints - User-level data isolation - Input/output validation - Error handling - CORS configuration for frontend integration Excluded: - Frontend implementation - Auth UI or login logic - Token issuance (handled by Better Auth) - AI/chatbot features (future phase) API Authentication Rules: - Every request must include: Authorization: Bearer <JWT> - Requests without valid token return 401 Unauthorized - JWT signature must be verified using BETTER_AUTH_SECRET - User identity must be extracted from JWT payload - User ID from token must be used for all database queries - URL user_id must match authenticated user (or be removed in favor of token-based identity) Database Models: Task Model: - id: integer (primary key) - user_id: string (indexed) - title: string (1–200 chars, required) - description: text (optional, max 1000 chars) - completed: boolean (default false) - created_at: timestamp - updated_at: timestamp API Endpoints: Base path: /api GET /api/tasks - Returns all tasks for authenticated user - Supports filtering by completion status POST /api/tasks - Creates a new task for authenticated user - Validates input - Returns created task GET /api/tasks/{id} - Returns task details - 404 if not found or not owned by user PUT /api/tasks/{id} - Updates title/description/completed - Enforces ownership PATCH /api/tasks/{id}/complete - Toggles completed status DELETE /api/tasks/{id} - Deletes task - Requires confirmation-safe handling Security Requirements: - User isolation enforced at query level - No task can be accessed across users - JWT expiry must be respected - SQL injection protection via ORM - CORS limited to frontend origin Error Handling: - 401: Missing or invalid token - 403: User mismatch or forbidden access - 404: Task not found - 422: Validation errors - 500: Unexpected server error (no sensitive leaks) Integration Requirements: - API response shape must match frontend expectations - JSON field naming consistency - Proper HTTP status codes - Fast responses suitable for optimistic UI Project Structure Expectations: - main.py (FastAPI app entry) - db.py (database engine & session) - models.py (SQLModel schemas) - auth.py (JWT verification dependency) - routes/tasks.py (task endpoints) Quality Bar: - Clean, readable, modular code - No hardcoded secrets - Production-ready patterns - Easy for judges to reason about correctness - Fully spec-driven (no assumptions) Completion Definition: The backend is considered complete when: - Frontend can authenticate and perform all task operations - Tasks persist across reloads - Unauthorized access is blocked - All endpoints behave as specified
response_text: |
  Created a complete feature specification for a production-ready backend for the Todo Full-Stack Web Application. The specification includes:
  - User scenarios for authentication, task CRUD operations, and error handling
  - Functional requirements covering authentication, task management, data isolation, and error handling
  - Key entities (Task and User)
  - Success criteria with measurable outcomes
  - A quality checklist validating the specification
outcome: |
  Successfully created feature specification in specs/001-backend-todo-api/spec.md with all required sections.
  Created quality checklist in specs/001-backend-todo-api/checklists/requirements.md.
  Ready for the next phase (planning).
evaluation: |
  The specification meets all requirements with clear user scenarios, testable requirements,
  and measurable success criteria. The API design and security requirements are well-defined
  with appropriate attention to data isolation and authentication.
---