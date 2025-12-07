from typing import List, Dict
import pandas as pd
import joblib
from pathlib import Path

from src.data_loader import load_user_data
from src.features import (
    add_engineered_features,
    compute_urgency_score,
    FEATURE_COLUMNS
)
from src.config import MODEL_PATH, SCALER_PATH


# -----------------------------
# Load ML Model (if available)
# -----------------------------
_model = None
_scaler = None

if MODEL_PATH.exists() and SCALER_PATH.exists():
    _model = joblib.load(MODEL_PATH)
    _scaler = joblib.load(SCALER_PATH)


# -----------------------------
# Reason Generator
# -----------------------------
def generate_reason(row: pd.Series) -> str:
    reasons = []

    if row["last_score"] < 60:
        reasons.append("low recent score")

    if row["difficulty_rating"] >= 4:
        reasons.append("high difficulty")

    if row["last_studied_days_ago"] >= 15:
        reasons.append("not studied for many days")

    if not reasons:
        reasons.append("moderate performance but needs periodic revision")

    return ", ".join(reasons)


# -----------------------------
# ML Prediction Engine
# -----------------------------
def ml_predict_priority(df: pd.DataFrame) -> pd.Series:
    """
    Predict priority using trained ML model.
    """
    if _model is None or _scaler is None:
        raise RuntimeError("ML model or scaler not loaded.")

    X = df[FEATURE_COLUMNS]
    X_scaled = _scaler.transform(X)
    predictions = _model.predict(X_scaled)
    return pd.Series(predictions, index=df.index)


# -----------------------------
# Main Recommendation Function
# -----------------------------
def get_top_n_recommendations(
    user_id: str,
    top_n: int = 5,
    use_ml: bool = True,
    w1: float = 0.5,
    w2: float = 0.3,
    w3: float = 0.2
) -> List[Dict]:
    """
    Generate top-N recommendations for a given user.
    Uses ML model if available, otherwise falls back to rule-based.
    """

    # 1. Load user data
    df_user = load_user_data(user_id, use_processed=True)

    # 2. Add engineered features
    df_user = add_engineered_features(df_user)

    # 3. Choose scoring method
    if use_ml and _model is not None:
        df_user["priority_score"] = ml_predict_priority(df_user)
        scoring_method = "ml"
    else:
        df_user = compute_urgency_score(df_user, w1=w1, w2=w2, w3=w3)
        df_user["priority_score"] = df_user["urgency_score"]
        scoring_method = "rule"

    # 4. Sort by priority
    df_user = df_user.sort_values(by="priority_score", ascending=False)

    # 5. Select Top-N
    df_top = df_user.head(top_n)

    # 6. Format output
    recommendations = []

    for _, row in df_top.iterrows():
        recommendations.append({
            "subject": row["subject"],
            "topic": row["topic"],
            "priority_score": round(float(row["priority_score"]), 3),
            "reason": generate_reason(row),
            "model_used": scoring_method
        })

    return recommendations




















































































