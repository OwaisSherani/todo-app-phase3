import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "")
    
    # Cohere API settings
    cohere_api_key: str = os.getenv("COHERE_API_KEY", "")
    
    # Auth settings
    secret_auth_key: str = os.getenv("SECRET_AUTH_KEY", "")
    
    # Application settings
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    app_name: str = os.getenv("APP_NAME", "Todo AI Chatbot")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignore extra env vars not defined in the model


def get_settings() -> Settings:
    """Get application settings singleton"""
    return Settings()


# Create a global settings instance
settings = get_settings()


def validate_environment() -> bool:
    """Validate that all required environment variables are set"""
    required_vars = [
        "DATABASE_URL",
        "COHERE_API_KEY", 
        "SECRET_AUTH_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    return True