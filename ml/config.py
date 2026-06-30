from pathlib import Path

# ==============================
# Project Root Directory
# ==============================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==============================
# Data Directories
# ==============================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"


# ==============================
# Dataset Path
# ==============================

RAW_DATA_PATH = RAW_DATA_DIR / "creditcard.csv"

# ==============================
# Processed Dataset Paths
# ==============================

PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "creditcard_clean.csv"

X_TRAIN_PATH = PROCESSED_DATA_DIR / "X_train.csv"
X_TEST_PATH = PROCESSED_DATA_DIR / "X_test.csv"

Y_TRAIN_PATH = PROCESSED_DATA_DIR / "y_train.csv"
Y_TEST_PATH = PROCESSED_DATA_DIR / "y_test.csv"


# ==============================
# Model Directories
# ==============================

ML_DIR = PROJECT_ROOT / "ml"

MODELS_DIR = ML_DIR / "models"

ARTIFACTS_DIR = ML_DIR / "artifacts"


# ==============================
# Saved Model Paths
# ==============================

LOGISTIC_MODEL_PATH = MODELS_DIR / "logistic_regression.pkl"

RANDOM_FOREST_MODEL_PATH = MODELS_DIR / "random_forest.pkl"


# ==============================
# Saved Artifacts
# ==============================

SCALER_PATH = ARTIFACTS_DIR / "scaler.pkl"