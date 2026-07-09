"""
inference.py

Inference preprocessing module.

This module is responsible for:

1. Loading saved scaler.
2. Preprocessing incoming transaction.
3. Returning processed transaction.
"""

import joblib

from ml.config import SCALER_PATH


# ==========================================
# Load Scaler
# ==========================================

try:
    scaler = joblib.load(SCALER_PATH)

except Exception as e:
    raise RuntimeError(f"Failed to load scaler: {e}")


# ==========================================
# Preprocess Transaction
# ==========================================

def preprocess_transaction(features):

    processed = features.copy()

    scaled = scaler.transform(
        [[processed[0], processed[-1]]]
    )

    processed[0] = scaled[0][0]

    processed[-1] = scaled[0][1]

    return processed