import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ml.config import SCALER_PATH


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """

    print(f"Before Removing Duplicates : {df.shape}")

    df = df.drop_duplicates()

    print(f"After Removing Duplicates : {df.shape}")

    return df


def split_features_target(df: pd.DataFrame):
    """
    Split dataset into features and target.
    """

    X = df.drop("Class", axis=1)

    y = df["Class"]

    return X, y



def split_train_test(
    X,
    y,
    test_size=0.2,
    random_state=42
):
    """
    Split data into training and testing.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )



def scale_features(
    X_train,
    X_test
):
    """
    Scale Time and Amount columns.
    """

    scaler = StandardScaler()

    columns = ["Time", "Amount"]

    X_train = X_train.copy()
    X_test = X_test.copy()

    X_train[columns] = scaler.fit_transform(
        X_train[columns]
    )

    X_test[columns] = scaler.transform(
        X_test[columns]
    )

    return X_train, X_test, scaler



def save_scaler(scaler):
    """
    Save scaler object.
    """

    joblib.dump(
        scaler,
        SCALER_PATH
    )

    print("Scaler Saved Successfully")


def load_scaler():
    """
    Load the trained scaler.
    """

    return joblib.load(SCALER_PATH)