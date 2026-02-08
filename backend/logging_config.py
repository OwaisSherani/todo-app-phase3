import logging
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def setup_logging(app: FastAPI):
    """
    Set up logging for the application.
    """
    # Create a custom logger
    logger = logging.getLogger("todo_backend")
    logger.setLevel(logging.INFO)
    
    # Create handlers
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatters and add it to handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(console_handler)
    
    # Add middleware to log requests
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = datetime.utcnow()
        response = await call_next(request)
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()
        
        logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration}s")
        
        return response
    
    return logger