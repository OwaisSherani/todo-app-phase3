# API Contract: Chatbot Endpoint

## Endpoint: POST /api/{user_id}/chat

### Description
Handles chat interactions between user and AI chatbot. Accepts user messages and returns AI responses with any side effects (task operations) performed.

### Parameters
- **Path Parameter**:
  - `user_id` (string, required): Unique identifier of the user initiating the chat

### Request Body
```json
{
  "message": "string (required): The user's message to the chatbot",
  "conversation_id": "integer (optional): ID of existing conversation to continue, or null for new conversation"
}
```

### Response
```json
{
  "response": "string (required): The AI chatbot's response to the user",
  "conversation_id": "integer (required): ID of the conversation",
  "actions_performed": [
    {
      "action": "string (required): Type of action performed (e.g., 'task_created', 'task_updated', 'task_completed')",
      "task_id": "integer (optional): ID of affected task if applicable",
      "details": "object (optional): Additional details about the action"
    }
  ],
  "error": "string (optional): Error message if any occurred"
}
```

### Authentication
- JWT token required in Authorization header
- Token must correspond to the user_id in the path

### Error Responses
- **401 Unauthorized**: Invalid or missing JWT token
- **403 Forbidden**: JWT token doesn't match user_id in path
- **422 Unprocessable Entity**: Invalid request body
- **500 Internal Server Error**: Unexpected server error during processing

### Example Request
```json
{
  "message": "Add a task to buy groceries",
  "conversation_id": null
}
```

### Example Response
```json
{
  "response": "I've created a task for you: 'buy groceries'",
  "conversation_id": 123,
  "actions_performed": [
    {
      "action": "task_created",
      "task_id": 456,
      "details": {
        "title": "buy groceries",
        "status": "pending"
      }
    }
  ]
}
```

## MCP Tools Contracts

### Tool: add_task
- **Input**: `{user_id: string, title: string, description?: string}`
- **Output**: `{success: boolean, task_id: integer, message: string}`

### Tool: list_tasks
- **Input**: `{user_id: string, status?: "pending"|"completed"|null}`
- **Output**: `{success: boolean, tasks: Array<{id: integer, title: string, description: string, status: string}>}`

### Tool: complete_task
- **Input**: `{user_id: string, task_id: integer}`
- **Output**: `{success: boolean, message: string}`

### Tool: delete_task
- **Input**: `{user_id: string, task_id: integer}`
- **Output**: `{success: boolean, message: string}`

### Tool: update_task
- **Input**: `{user_id: string, task_id: integer, title?: string, description?: string, status?: "pending"|"completed"}`
- **Output**: `{success: boolean, message: string}`