# Data Model: AI Chatbot Integration with Cohere

## Entities

### Task
- **Fields**:
  - id: Integer (Primary Key, Auto-increment)
  - title: String (Required, Max length: 255)
  - description: Text (Optional)
  - status: String (Enum: 'pending', 'completed'; Default: 'pending')
  - user_id: String (Foreign Key to User, Required)
  - created_at: DateTime (Auto-generated)
  - updated_at: DateTime (Auto-generated)

- **Validation Rules**:
  - Title must not be empty
  - Status must be either 'pending' or 'completed'
  - user_id must correspond to an existing user

- **Relationships**:
  - Belongs to one User
  - Owned by one User (via user_id foreign key)

### Conversation
- **Fields**:
  - id: Integer (Primary Key, Auto-increment)
  - user_id: String (Foreign Key to User, Required)
  - created_at: DateTime (Auto-generated)
  - updated_at: DateTime (Auto-generated)

- **Validation Rules**:
  - user_id must correspond to an existing user

- **Relationships**:
  - Belongs to one User
  - Has many Messages

### Message
- **Fields**:
  - id: Integer (Primary Key, Auto-increment)
  - conversation_id: Integer (Foreign Key to Conversation, Required)
  - sender: String (Enum: 'user', 'assistant'; Required)
  - content: Text (Required)
  - timestamp: DateTime (Auto-generated)

- **Validation Rules**:
  - sender must be either 'user' or 'assistant'
  - content must not be empty
  - conversation_id must correspond to an existing conversation

- **Relationships**:
  - Belongs to one Conversation
  - Conversation has many Messages

### User
- **Fields**:
  - id: String (Primary Key, Unique)
  - email: String (Unique, Required)
  - created_at: DateTime (Auto-generated)
  - updated_at: DateTime (Auto-generated)

- **Validation Rules**:
  - Email must be valid email format
  - Email must be unique

- **Relationships**:
  - Has many Tasks
  - Has many Conversations
  - Has many Messages (through Conversations)