"""
predict.py

Production prediction module for the Real-Time Financial Fraud Detection Project.

This module is responsible for:
1. Loading the trained XGBoost model.
2. Validating incoming transaction data.
3. Predicting whether a transaction is Fraud or Genuine.
4. Returning fraud probability.

Author: Vipul Soni
"""

import joblib
import numpy as np

from utils.logger import logger

from ml.config import MODELS_DIR
from ml.inference import preprocess_transaction


# ==========================================================
# Load Trained Model
# ==========================================================

MODEL_PATH = MODELS_DIR / "xgboost.pkl"

logger.info("Loading XGBoost Model...")

try:
    model = joblib.load(MODEL_PATH)
    logger.info("XGBoost Model Loaded Successfully")

except Exception as e:
    logger.exception("Failed To Load XGBoost Model")
    raise RuntimeError(f"Failed to load model: {e}")


# ==========================================================
# Model Information
# ==========================================================

EXPECTED_FEATURES = model.n_features_in_


# ==========================================================
# Helper Function
# ==========================================================

def _validate_transaction(transaction):
    """
    Validate transaction input before prediction.

    Parameters
    ----------
    transaction : list or numpy array

    Returns
    -------
    numpy.ndarray
    """

    logger.info("Validating Transaction Input")

    if transaction is None:
        logger.error("Transaction data is None")
        raise ValueError("Transaction data cannot be None.")

    if len(transaction) != EXPECTED_FEATURES:
        logger.error(
            f"Expected {EXPECTED_FEATURES} features but received {len(transaction)}."
        )
        raise ValueError(
            f"Expected {EXPECTED_FEATURES} features but received {len(transaction)}."
        )

    logger.info("Transaction Validation Successful")

    return np.array(transaction).reshape(1, -1)


# ==========================================================
# Prediction Function
# ==========================================================

def predict(transaction):
    """
    Predict whether a transaction is Fraud or Genuine.
    """

    try:

        logger.info("Starting Model Prediction")

        transaction = _validate_transaction(transaction)

        transaction = preprocess_transaction(
            transaction.flatten().tolist()
        )

        transaction = np.array(transaction).reshape(1, -1)

        prediction = model.predict(transaction)

        logger.info(
            f"Prediction Completed Successfully : {prediction[0]}"
        )

        return int(prediction[0])

    except Exception as e:

        logger.exception("Prediction Failed")

        raise RuntimeError(
            f"Prediction failed: {e}"
        )


# ==========================================================
# Fraud Probability Function
# ==========================================================

def predict_probability(transaction):
    """
    Predict fraud probability.
    """

    try:

        logger.info("Calculating Fraud Probability")

        transaction = _validate_transaction(transaction)

        transaction = preprocess_transaction(
            transaction.flatten().tolist()
        )

        transaction = np.array(transaction).reshape(1, -1)

        probability = model.predict_proba(transaction)

        logger.info(
            f"Fraud Probability Calculated : {probability[0][1]}"
        )

        return float(probability[0][1])

    except Exception as e:

        logger.exception("Fraud Probability Calculation Failed")

        raise RuntimeError(
            f"Probability prediction failed: {e}"
        )