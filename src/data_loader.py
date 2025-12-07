import pandas as pd
from src.config import RAW_DATA_PATH, PROCESSED_DATA_DIR


def load_raw_data() -> pd.DataFrame:
    """
    Load raw interactions data from CSV.
    """
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw data file not found at {RAW_DATA_PATH}")

    df = pd.read_csv(RAW_DATA_PATH)
    return df


def load_processed_data() -> pd.DataFrame:
    """
    Load processed interactions dataset.
    """
    processed_path = PROCESSED_DATA_DIR / "interactions_processed.csv"

    if not processed_path.exists():
        raise FileNotFoundError(
            f"Processed data file not found at {processed_path}. "
            "Run feature engineering first."
        )

    df = pd.read_csv(processed_path)
    return df


def save_processed_data(df: pd.DataFrame) -> None:
    """
    Save processed dataset to disk.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    processed_path = PROCESSED_DATA_DIR / "interactions_processed.csv"
    df.to_csv(processed_path, index=False)


def load_user_data(user_id: str, use_processed: bool = True) -> pd.DataFrame:
    """
    Load data for a specific user.
    """
    if use_processed:
        df = load_processed_data()
    else:
        df = load_raw_data()

    user_df = df[df["user_id"] == user_id]

    if user_df.empty:
        raise ValueError(f"No data found for user_id: {user_id}")

    return user_df
