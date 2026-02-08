from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import field_validator
from pathlib import Path


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # Database settings
    database_url: str
    db_echo: bool = False  # Set to True to log SQL queries

    # Authentication settings
    better_auth_secret: Optional[str] = None
    better_auth_url: str = "http://localhost:3000"

    # Application settings
    app_name: str = "Todo Backend API"
    debug: bool = False
    allowed_origins: str = "http://localhost:3000"  # Comma-separated list of allowed origins

    @field_validator('database_url')
    @classmethod
    def validate_database_url(cls, v):
        if not v or v == "postgresql://user:password@localhost/dbname":
            raise ValueError('DATABASE_URL must be set in environment variables')
        return v

    @field_validator('better_auth_secret')
    @classmethod
    def validate_auth_secret(cls, v):
        if not v:
            raise ValueError('BETTER_AUTH_SECRET must be set in environment variables')
        return v

    # Allow extra environment variables (e.g., platform-specific vars)
    # Pydantic v2 uses `model_config` for runtime configuration.
    model_config = {
        # Resolve the .env file relative to the backend package directory
        "env_file": str(Path(__file__).resolve().parent.parent / ".env"),
        "extra": "ignore",
    }

# Create a settings instance
settings = Settings()