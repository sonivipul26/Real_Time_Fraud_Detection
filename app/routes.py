from fastapi import APIRouter

from app.schemas import (
    HealthResponse,
    PredictionRequest,
    PredictionResponse
)

from app.services import predict_transaction

router = APIRouter()


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


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_api(request: PredictionRequest):

    result = predict_transaction(
    request
)

    return result