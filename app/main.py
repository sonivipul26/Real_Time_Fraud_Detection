from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Real-Time Financial Fraud Detection API",
    description="Production-level Fraud Detection using XGBoost",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Real-Time Financial Fraud Detection API",
        "status": "Running"
    }