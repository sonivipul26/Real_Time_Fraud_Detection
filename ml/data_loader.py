import pandas as pd

from ml.config import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    X_TRAIN_PATH,
    X_TEST_PATH,
    Y_TRAIN_PATH,
    Y_TEST_PATH
)


def load_raw_data():
    """
    Load the original dataset.
    """

    return pd.read_csv(RAW_DATA_PATH)


def load_processed_data():
    """
    Load cleaned dataset.
    """

    return pd.read_csv(PROCESSED_DATA_PATH)


def load_train_test_data():
    """
    Load train and test datasets.

    Returns:
        X_train, X_test, y_train, y_test
    """

    X_train = pd.read_csv(X_TRAIN_PATH)

    X_test = pd.read_csv(X_TEST_PATH)

    y_train = pd.read_csv(Y_TRAIN_PATH).squeeze()

    y_test = pd.read_csv(Y_TEST_PATH).squeeze()

    return X_train, X_test, y_train, y_test