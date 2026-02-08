from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.tasks
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Todo API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routers.tasks.router, prefix="/api/{user_id}", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Todo API is running"}

# Global exception handler for debugging
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return {"detail": "Internal server error"}