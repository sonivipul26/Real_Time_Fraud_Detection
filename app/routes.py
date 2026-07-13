from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from app.schemas import (
    HealthResponse,
    PredictionRequest,
    PredictionResponse,
)

from app.services import predict_transaction

router = APIRouter()


# ==========================================================
# Health Endpoint
# ==========================================================

@router.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return {
        "status": "healthy",
        "model": "XGBoost",
        "version": "1.0.0"
    }


# ==========================================================
# Prediction Endpoint
# ==========================================================

@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_api(
    request: PredictionRequest,
    db: Session = Depends(get_db)
):

    result = predict_transaction(
        request,
        db
    )

    return result