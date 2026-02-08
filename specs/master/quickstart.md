# Quickstart Guide: Todo Backend API

## Prerequisites

- Python 3.11+
- pip package manager
- Access to Neon Serverless PostgreSQL instance
- Better Auth configuration

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Navigate to the backend directory
```bash
cd backend
```

### 3. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up environment variables
Create a `.env` file in the backend directory with the following variables:

```env
BETTER_AUTH_SECRET=your_better_auth_secret_key
BETTER_AUTH_URL=http://localhost:3000
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>?sslmode=require
```

### 6. Run the application
```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`.

## API Usage

### Authentication
All API endpoints require a valid JWT token in the Authorization header:

```
Authorization: Bearer <JWT_TOKEN>
```

The JWT token is issued by Better Auth when a user logs in through the frontend.

### Example Requests

#### Get all tasks for a user
```bash
curl -X GET \
  http://localhost:8000/api/{user_id}/tasks \
  -H 'Authorization: Bearer <JWT_TOKEN>'
```

#### Create a new task
```bash
curl -X POST \
  http://localhost:8000/api/{user_id}/tasks \
  -H 'Authorization: Bearer <JWT_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "New task",
    "description": "Task description",
    "completed": false
  }'
```

## Development

### Running tests
```bash
pytest
```

### Code formatting
```bash
black .
```

### Linting
```bash
flake8 .
```

## Deployment

The backend is designed to run in a containerized environment or directly on a server. Ensure that environment variables are properly set in your deployment environment.

For containerization, a Dockerfile would typically include:
- Python 3.11+ base image
- Dependencies installation
- Environment variable configuration
- Application startup command