# Quickstart Guide: AI Chatbot Integration with Cohere

## Overview
This guide explains how to set up and run the AI Chatbot Integration with Cohere feature in the Todo application.

## Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL-compatible database (Neon recommended)
- Cohere API key
- Existing Todo application with Better Auth integration

## Setup Instructions

### 1. Environment Variables
Create a `.env` file in the backend directory with the following variables:
```
COHERE_API_KEY=your_cohere_api_key_here
DATABASE_URL=your_postgresql_database_url
SECRET_AUTH_KEY=your_auth_secret_key
```

### 2. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```bash
   python -m alembic upgrade head
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### 3. Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install JavaScript dependencies:
   ```bash
   npm install
   ```

3. Start the frontend development server:
   ```bash
   npm run dev
   ```

## Usage Instructions

### 1. Chat Interface
- A floating chat icon will appear on all pages of the application
- Click the icon to open the chat interface
- Type natural language commands to manage your tasks

### 2. Supported Commands
- "Add a task to buy groceries" - Creates a new task
- "Show me my tasks" - Lists all your tasks
- "Complete the grocery task" - Marks a task as completed
- "Delete the old task" - Removes a task
- "Update the meeting task to tomorrow" - Updates task details

### 3. Conversation Persistence
- Your conversation history is saved and accessible across sessions
- The chatbot remembers context from previous interactions

## Architecture Components

### Backend Components
- **Models**: SQLModel definitions for Task, Conversation, and Message entities
- **Services**: Business logic for task and conversation management
- **Agents**: AI orchestrator and domain-specific agents
- **Tools**: MCP tools for standardized task operations
- **API**: FastAPI endpoints for chat interactions

### Frontend Components
- **ChatIcon**: Floating icon component accessible on all pages
- **ChatBot**: Main chat interface with message history
- **ApiClient**: Service for communicating with backend chat API

## Troubleshooting

### Common Issues
1. **Cohere API Connection Error**
   - Verify your COHERE_API_KEY is correctly set in the environment
   - Check that the API key has the necessary permissions

2. **Database Connection Error**
   - Ensure your DATABASE_URL is correctly formatted
   - Verify database credentials and permissions

3. **JWT Authentication Error**
   - Confirm that the user is properly authenticated via Better Auth
   - Check that the JWT token is being passed correctly in requests

### Testing the Integration
Run the following command to execute integration tests:
```bash
pytest tests/integration/test_chatbot.py
```