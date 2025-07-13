from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routes import router

# Initialize FastAPI app
app = FastAPI(
    title="KPA Form Data API (MongoDB)",
    description="API for managing bogie checksheets and wheel specifications",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router, prefix="/api")

# Health check endpoint
@app.get("/")
async def root():
    return {
        "message": "KPA Form Data API is running",
        "version": "1.0.0",
        "status": "healthy",
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "bogie_checksheet": "POST /api/forms/bogie-checksheet",
            "wheel_specifications": "GET /api/forms/wheel-specifications"
        }
    }

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "detail": str(exc)
        }
    )
