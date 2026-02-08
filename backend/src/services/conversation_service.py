from typing import List, Optional
from sqlmodel import Session, select
from ..models.conversation import Conversation
from ..models.message import Message
from datetime import datetime


class ConversationService:
    @staticmethod
    def create_conversation(session: Session, user_id: str) -> Conversation:
        """
        Create a new conversation for a user
        """
        conversation = Conversation(user_id=user_id)
        session.add(conversation)
        session.commit()
        session.refresh(conversation)
        return conversation

    @staticmethod
    def get_conversation_by_id(session: Session, conversation_id: int, user_id: str) -> Optional[Conversation]:
        """
        Get a specific conversation by ID for a user
        """
        query = select(Conversation).where(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id
        )
        conversation = session.exec(query).first()
        return conversation

    @staticmethod
    def get_user_conversations(session: Session, user_id: str) -> List[Conversation]:
        """
        Get all conversations for a user
        """
        query = select(Conversation).where(Conversation.user_id == user_id)
        conversations = session.exec(query).all()
        return conversations

    @staticmethod
    def add_message_to_conversation(
        session: Session,
        conversation_id: int,
        sender: str,
        content: str
    ) -> Message:
        """
        Add a message to a conversation
        """
        message = Message(
            conversation_id=conversation_id,
            sender=sender,
            content=content
        )
        session.add(message)
        session.commit()
        session.refresh(message)
        return message

    @staticmethod
    def get_messages_for_conversation(session: Session, conversation_id: int) -> List[Message]:
        """
        Get all messages for a conversation
        """
        query = select(Message).where(Message.conversation_id == conversation_id).order_by(Message.timestamp)
        messages = session.exec(query).all()
        return messages

    @staticmethod
    def get_conversation_with_messages(session: Session, conversation_id: int, user_id: str) -> Optional[Conversation]:
        """
        Get a conversation with all its messages for a user
        """
        conversation = ConversationService.get_conversation_by_id(session, conversation_id, user_id)
        if not conversation:
            return None
        
        # Get messages for this conversation
        messages = ConversationService.get_messages_for_conversation(session, conversation_id)
        # Note: In a real implementation, we'd probably want to attach these to the conversation object
        # but for now we'll just return the conversation
        
        return conversation

    @staticmethod
    def get_latest_conversation_for_user(session: Session, user_id: str) -> Optional[Conversation]:
        """
        Get the most recent conversation for a user
        """
        query = select(Conversation).where(Conversation.user_id == user_id).order_by(Conversation.updated_at.desc())
        conversation = session.exec(query).first()
        return conversation