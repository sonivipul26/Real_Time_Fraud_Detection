"""
main.py

Entry point of the Real-Time Financial Fraud Detection API.
"""

from fastapi import FastAPI

from app.routes import router
from utils.logger import logger


# ==========================================
# Create FastAPI Application
# ==========================================

app = FastAPI(
    title="Real-Time Financial Fraud Detection API",
    description="Production-level Fraud Detection using XGBoost",
    version="1.0.0"
)


# ==========================================
# Startup Logs
# ==========================================

logger.info("=" * 60)
logger.info("Starting Real-Time Financial Fraud Detection API...")
logger.info("Application Version : 1.0.0")


# ==========================================
# Register Routes
# ==========================================

app.include_router(router)

logger.info("All API Routes Registered Successfully.")


# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():

    logger.info("Home Endpoint Accessed")

    return {
        "message": "Welcome to Real-Time Financial Fraud Detection API",
        "status": "Running"
    }