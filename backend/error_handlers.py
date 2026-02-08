from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


def add_error_handlers(app: FastAPI):
    """
    Add error handlers to the FastAPI app for consistent error responses.
    """
    
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """
        Handle HTTP exceptions with consistent error response format.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        Handle request validation errors with consistent error response format.
        """
        return JSONResponse(
            status_code=422,
            content={
                "detail": [
                    {
                        "loc": err["loc"],
                        "msg": err["msg"],
                        "type": err["type"]
                    }
                    for err in exc.errors()
                ]
            }
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """
        Handle general exceptions with consistent error response format.
        """
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"}
        )