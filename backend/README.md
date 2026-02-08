# Todo API Backend

This is a FastAPI-based backend for a multi-user Todo web application with secure JWT authentication verification, Neon Serverless PostgreSQL integration, and SQLModel ORM.

## Features

- Secure JWT authentication using Better Auth
- REST API for Todo CRUD operations
- User isolation - users can only access their own tasks
- Neon Serverless PostgreSQL integration
- SQLModel ORM for database operations
- Ready for AI chatbot integration

## Prerequisites

- Python 3.11+
- pip package manager
- Access to Neon Serverless PostgreSQL database
- Better Auth secret key

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Navigate to the backend directory:
   ```bash
   cd backend
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the backend directory with the following variables:
   ```env
   BETTER_AUTH_SECRET=your_better_auth_secret_here
   BETTER_AUTH_URL=http://localhost:3000
   DATABASE_URL=postgresql://username:password@host:port/database_name
   ```

## Running the Application

1. From the backend directory, run:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion status

## Testing

1. From the backend directory, run:
   ```bash
   pytest
   ```

2. To run tests with coverage:
   ```bash
   pytest --cov=.
   ```

## Environment Variables

- `BETTER_AUTH_SECRET`: Secret key for JWT verification (required)
- `BETTER_AUTH_URL`: URL of the Better Auth service (default: http://localhost:3000)
- `DATABASE_URL`: Connection string for the PostgreSQL database (required)
- `DEBUG`: Enable debug mode (default: False)

## Security

- All API endpoints require JWT authentication
- Users can only access their own tasks
- User ID in JWT token is validated against user ID in URL
- Input validation is performed on all requests