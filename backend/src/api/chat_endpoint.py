from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import jwt
from ..config.environment import settings
from ..services.conversation_service import ConversationService
from ..agents.orchestrator_agent import ChatOrchestratorAgent
from sqlmodel import Session
from ..database import engine
from ..db import get_session


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None


class ChatResponse(BaseModel):
    response: str
    conversation_id: int
    actions_performed: List[Dict[str, Any]]
    error: Optional[str] = None


def get_current_user_id(authorization: str = Depends(lambda: None)) -> str:
    """
    Extract user ID from JWT token in Authorization header.
    This is a simplified version - in a real app, you'd use proper auth middleware.
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")
    
    token = authorization[len("Bearer "):]
    
    try:
        # Decode the JWT token to get user info
        payload = jwt.decode(token, settings.secret_auth_key, algorithms=["HS256"])
        user_id = payload.get("user_id")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: no user_id found")
        
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/api/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(
    user_id: str,
    chat_request: ChatRequest,
    current_user_id: str = Depends(get_current_user_id)
):
    """
    Handle chat interactions between user and AI chatbot.
    Accepts user messages and returns AI responses with any side effects (task operations) performed.
    """
    # Verify that the user_id in the path matches the user_id from the token
    if user_id != current_user_id:
        raise HTTPException(status_code=403, detail="User ID in path does not match token")
    
    try:
        # Initialize services and agents
        orchestrator_agent = ChatOrchestratorAgent()
        
        # Get or create conversation
        conversation_id = chat_request.conversation_id
        if not conversation_id:
            # Create a new conversation
            with Session(engine) as session:
                conversation = ConversationService.create_conversation(session, user_id)
                conversation_id = conversation.id
        else:
            # Verify that the conversation belongs to the user
            with Session(engine) as session:
                conversation = ConversationService.get_conversation_by_id(session, conversation_id, user_id)
                if not conversation:
                    raise HTTPException(status_code=404, detail="Conversation not found or does not belong to user")
        
        # Retrieve conversation history for context
        with Session(engine) as session:
            messages = ConversationService.get_messages_for_conversation(session, conversation_id)
            conversation_context = []
            for msg in messages:
                conversation_context.append({
                    "role": msg.sender,
                    "content": msg.content
                })
        
        # Process the user message with the orchestrator agent
        result = orchestrator_agent.process_user_message(chat_request.message, conversation_context)
        
        # Save the user message to the conversation
        with Session(engine) as session:
            ConversationService.add_message_to_conversation(
                session, conversation_id, "user", chat_request.message
            )
            # Save the AI response to the conversation
            ConversationService.add_message_to_conversation(
                session, conversation_id, "assistant", result["response"]
            )
        
        # Return the response with conversation ID and actions performed
        return ChatResponse(
            response=result["response"],
            conversation_id=conversation_id,
            actions_performed=result.get("actions_performed", []),
            error=None
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        # Handle any other errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")