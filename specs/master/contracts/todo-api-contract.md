# API Contract: Todo Backend API

## Base Path
`/api/{user_id}`

## Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <JWT_TOKEN>
```

## Common Error Responses
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: User mismatch (attempting to access another user's data)
- `404 Not Found`: Resource not found
- `422 Unprocessable Entity`: Validation error in request body
- `500 Internal Server Error`: Unexpected server error

## Endpoints

### GET /api/{user_id}/tasks
**Description**: Retrieve all tasks for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user whose tasks to retrieve

**Query Parameters**:
- `completed` (boolean, optional): Filter tasks by completion status

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Success Response**:
- `200 OK`
```json
{
  "tasks": [
    {
      "id": 1,
      "user_id": "user123",
      "title": "Sample task",
      "description": "Sample description",
      "completed": false,
      "created_at": "2023-01-01T10:00:00Z",
      "updated_at": "2023-01-01T10:00:00Z"
    }
  ]
}
```

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id

---

### POST /api/{user_id}/tasks
**Description**: Create a new task for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user creating the task

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Request Body**:
```json
{
  "title": "New task title",
  "description": "Optional task description",
  "completed": false
}
```

**Validation**:
- `title` is required and must be 1-200 characters
- `description` is optional and must be max 1000 characters
- `completed` is optional and defaults to false

**Success Response**:
- `201 Created`
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "New task title",
  "description": "Optional task description",
  "completed": false,
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-01T10:00:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id
- `422 Unprocessable Entity`: Validation error in request body

---

### GET /api/{user_id}/tasks/{id}
**Description**: Retrieve a specific task for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user whose task to retrieve
- `id` (integer): The ID of the task to retrieve

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Success Response**:
- `200 OK`
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Sample task",
  "description": "Sample description",
  "completed": false,
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-01T10:00:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id or task doesn't belong to user
- `404 Not Found`: Task with given ID doesn't exist

---

### PUT /api/{user_id}/tasks/{id}
**Description**: Update a specific task for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user whose task to update
- `id` (integer): The ID of the task to update

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated task description",
  "completed": true
}
```

**Validation**:
- `title` is required and must be 1-200 characters
- `description` is optional and must be max 1000 characters
- `completed` is optional

**Success Response**:
- `200 OK`
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Updated task title",
  "description": "Updated task description",
  "completed": true,
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-02T15:30:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id or task doesn't belong to user
- `404 Not Found`: Task with given ID doesn't exist
- `422 Unprocessable Entity`: Validation error in request body

---

### PATCH /api/{user_id}/tasks/{id}/complete
**Description**: Toggle the completion status of a specific task for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user whose task to update
- `id` (integer): The ID of the task to update

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Request Body**:
```json
{
  "completed": true
}
```

**Success Response**:
- `200 OK`
```json
{
  "id": 1,
  "user_id": "user123",
  "title": "Sample task",
  "description": "Sample description",
  "completed": true,
  "created_at": "2023-01-01T10:00:00Z",
  "updated_at": "2023-01-02T15:30:00Z"
}
```

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id or task doesn't belong to user
- `404 Not Found`: Task with given ID doesn't exist

---

### DELETE /api/{user_id}/tasks/{id}
**Description**: Delete a specific task for the authenticated user

**Path Parameters**:
- `user_id` (string): The ID of the user whose task to delete
- `id` (integer): The ID of the task to delete

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Success Response**:
- `204 No Content`

**Error Responses**:
- `401 Unauthorized`: Missing or invalid token
- `403 Forbidden`: user_id in URL doesn't match JWT user_id or task doesn't belong to user
- `404 Not Found`: Task with given ID doesn't exist