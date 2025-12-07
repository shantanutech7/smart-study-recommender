import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

from src.config import MODELS_DIR
from src.features import FEATURE_COLUMNS, TARGET_COLUMN


def train_and_save_model():
    print("🔹 Loading processed dataset...")
    df = pd.read_csv("data/processed/interactions_processed.csv")

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    print("🔹 Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("🔹 Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("🔹 Training RandomForest model...")
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train_scaled, y_train)

    print("🔹 Evaluating model...")
    y_pred = model.predict(X_test_scaled)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"✅ MAE:  {mae:.4f}")
    print(f"✅ RMSE: {rmse:.4f}")

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    model_path = MODELS_DIR / "model.pkl"
    scaler_path = MODELS_DIR / "scaler.pkl"

    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    print("✅ Model saved at:", model_path)
    print("✅ Scaler saved at:", scaler_path)


if __name__ == "__main__":
    train_and_save_model()
