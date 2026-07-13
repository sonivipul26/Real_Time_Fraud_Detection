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



from ml.config import MODELS_DIR

from ml.inference import preprocess_transaction

# ==========================================================
# Load Trained Model
# ==========================================================

MODEL_PATH = MODELS_DIR / "xgboost.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")



# Number of features expected by the model
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
        Input transaction containing all features.

    Returns
    -------
    numpy.ndarray
        Validated transaction reshaped for prediction.
    """

    if transaction is None:
        raise ValueError("Transaction data cannot be None.")

    if len(transaction) != EXPECTED_FEATURES:
        raise ValueError(
            f"Expected {EXPECTED_FEATURES} features but received {len(transaction)}."
        )

    return np.array(transaction).reshape(1, -1)





# ==========================================================
# Prediction Function
# ==========================================================

def predict(transaction):
    """
    Predict whether a transaction is Fraud or Genuine.

    Parameters
    ----------
    transaction : list

    Returns
    -------
    int

    0 -> Genuine Transaction

    1 -> Fraud Transaction
    """

    try:

        transaction = _validate_transaction(transaction)

        transaction = preprocess_transaction(transaction.flatten().tolist())
        transaction = np.array(transaction).reshape(1, -1)

        prediction = model.predict(transaction)

        return int(prediction[0])

    except Exception as e:
        raise RuntimeError(f"Prediction failed: {e}")


# ==========================================================
# Fraud Probability Function
# ==========================================================

def predict_probability(transaction):
    """
    Predict fraud probability.
    """

    try:

        transaction = _validate_transaction(transaction)

        transaction = preprocess_transaction(
            transaction.flatten().tolist()
        )

        transaction = np.array(transaction).reshape(1, -1)

        probability = model.predict_proba(transaction)

        return float(probability[0][1])

    except Exception as e:

        raise RuntimeError(
            f"Probability prediction failed: {e}"
        )