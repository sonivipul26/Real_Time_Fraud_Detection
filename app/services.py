from ml.predict import predict
from ml.predict import predict_probability

from database.crud import create_transaction

from utils.logger import logger


def predict_transaction(request, db):

    logger.info("Starting Prediction Service")

    # ==========================================
    # Convert Request To Feature List
    # ==========================================

    features = request.to_feature_list()

    logger.info("Feature Vector Created Successfully")

    # ==========================================
    # Prediction
    # ==========================================

    prediction = predict(features)

    logger.info(f"Prediction Generated : {prediction}")

    # ==========================================
    # Fraud Probability
    # ==========================================

    probability = predict_probability(features)

    logger.info(
        f"Fraud Probability : {probability}"
    )

    # ==========================================
    # Save To Database
    # ==========================================

    create_transaction(

        db=db,

        transaction_time=request.Time,

        amount=request.Amount,

        prediction=prediction,

        fraud_probability=probability

    )

    logger.info("Transaction Saved Successfully")

    # ==========================================
    # Return Response
    # ==========================================

    logger.info("Prediction Service Completed")

    return {

        "prediction": prediction,

        "fraud_probability": probability

    }