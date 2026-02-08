from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create FastAPI app with minimal configuration
app = FastAPI(
    title="Todo AI Chatbot API - Debug",
    description="Debug version to isolate middleware issue",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Debug server running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    print("Starting debug Uvicorn server...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False
    )