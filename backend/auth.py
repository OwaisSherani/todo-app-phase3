import jwt
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import config
from typing import Dict, Optional


security = HTTPBearer()


def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict:
    """
    Verify JWT token and extract user information.
    
    Args:
        credentials: HTTP authorization credentials containing the JWT token
        
    Returns:
        Dictionary containing user information (user_id, email)
        
    Raises:
        HTTPException: If token is invalid, expired, or malformed
    """
    token = credentials.credentials
    
    try:
        # Decode the JWT token using the secret
        payload = jwt.decode(token, config.BETTER_AUTH_SECRET, algorithms=["HS256"])
        
        # Extract user information from the payload
        user_id = payload.get("userId") or payload.get("user_id")
        email = payload.get("email")
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return {"user_id": user_id, "email": email}
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """
    Get the current user's ID from the JWT token.
    
    Args:
        credentials: HTTP authorization credentials containing the JWT token
        
    Returns:
        The user ID extracted from the JWT token
    """
    token_data = verify_jwt_token(credentials)
    return token_data["user_id"]