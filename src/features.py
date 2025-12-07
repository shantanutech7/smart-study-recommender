import pandas as pd


FEATURE_COLUMNS = [
    "normalized_score",
    "recency",
    "difficulty_rating",
    "attempts",
    "time_spent_minutes"
]

TARGET_COLUMN = "label_or_priority"


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features required for rule-based and ML models.
    """
    df = df.copy()

    # Normalize score
    df["normalized_score"] = df["last_score"] / 100.0

    # Recency feature
    df["recency"] = df["last_studied_days_ago"]

    return df


def compute_urgency_score(
    df: pd.DataFrame,
    w1: float = 0.5,
    w2: float = 0.3,
    w3: float = 0.2
) -> pd.DataFrame:
    """
    Compute rule-based urgency score.
    """
    df = df.copy()

    df["urgency_score"] = (
        w1 * (1 - df["normalized_score"]) +
        w2 * (df["recency"] / 60) +
        w3 * (df["difficulty_rating"] / 5)
    )

    return df


def get_model_features(df: pd.DataFrame):
    """
    Return X, y for ML training.
    """
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return X, y
