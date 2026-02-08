from fastapi import Depends, HTTPException, status
from typing import Dict
import auth
import database
from sqlmodel import Session


def get_current_user_with_validation(credentials: Dict = Depends(auth.verify_jwt_token)):
    """
    Get the current user from the JWT token and validate their information.
    
    Args:
        credentials: Dictionary containing user information from JWT token
        
    Returns:
        Dictionary containing validated user information
    """
    user_id = credentials.get("user_id")
    email = credentials.get("email")
    
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID not found in token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {
        "user_id": user_id,
        "email": email
    }


def get_db_session():
    """
    Get a database session.
    
    Yields:
        Database session for use in API endpoints
    """
    with database.get_session() as session:
        yield session