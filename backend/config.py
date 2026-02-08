import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# JWT Configuration
BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET")
if not BETTER_AUTH_SECRET:
    raise ValueError("BETTER_AUTH_SECRET environment variable is not set")

BETTER_AUTH_URL = os.getenv("BETTER_AUTH_URL", "http://localhost:3000")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # For development, use SQLite; for production, use Neon PostgreSQL
    if os.getenv("ENVIRONMENT") == "production":
        DATABASE_URL = os.getenv("NEON_DB_URL", "postgresql://neondb_owner:npg_cUoTS5MqsJ2t@ep-round-bonus-ah78iwpd-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
    else:
        # Use SQLite for local development
        DATABASE_URL = "sqlite:///./todo_app.db"

# Application Configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"