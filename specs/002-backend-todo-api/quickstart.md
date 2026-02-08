# Quickstart Guide: Backend Todo API

## Prerequisites

- Python 3.11+
- pip package manager
- Access to Neon Serverless PostgreSQL database
- Better Auth secret key

## Environment Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Create a `.env` file in the backend directory with the following variables:
   ```env
   BETTER_AUTH_SECRET=your_better_auth_secret_here
   BETTER_AUTH_URL=http://localhost:3000
   DATABASE_URL=postgresql://username:password@host:port/database_name
   ```

## Running the Application

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

3. The API will be available at `http://localhost:8000`

## Testing the API

1. To test authentication, include the Authorization header in your requests:
   ```
   Authorization: Bearer <jwt_token>
   ```

2. Example API call to get user's tasks:
   ```bash
   curl -H "Authorization: Bearer <jwt_token>" \
        http://localhost:8000/api/user123/tasks
   ```

## Running Tests

1. From the backend directory, run:
   ```bash
   pytest
   ```

2. To run tests with coverage:
   ```bash
   pytest --cov=.
   ```

## API Endpoints

- `GET /api/{user_id}/tasks` - List all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion status

## Troubleshooting

- If you get a database connection error, verify your Neon database URL is correct
- If authentication fails, ensure your JWT token is valid and properly formatted
- If CORS errors occur, check that your frontend is running on the allowed origin