from fastapi import FastAPI
import logging

# Set up logging to see what's happening
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG)

app = FastAPI(title="Debug API", version="1.0.0")

@app.get("/")
def read_root():
    print("Root endpoint called")
    return {"message": "Debug API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8005, log_level="debug", debug=True)