from fastapi import FastAPI, HTTPException
from datetime import datetime
import pandas as pd
from pathlib import Path

from src.api.schemas import (
    RecommendationRequest,
    RecommendationResponse,
    RecommendationItem,
    FeedbackRequest
)
from src.recommend import get_top_n_recommendations

app = FastAPI(title="Smart Study Recommendation System API")

FEEDBACK_PATH = Path("data/feedback_log.csv")

# -------------------------
# Health Check
# -------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -------------------------
# Recommendations Endpoint
# -------------------------
@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(request: RecommendationRequest):
    try:
        recommendations = get_top_n_recommendations(
    user_id=request.user_id,
    top_n=request.top_n,
    use_ml=True   # ML enabled by default
)

        return {
            "user_id": request.user_id,
            "recommendations": recommendations
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# -------------------------
# Feedback Endpoint
# -------------------------
@app.post("/feedback")
def submit_feedback(feedback: FeedbackRequest):
    try:
        FEEDBACK_PATH.parent.mkdir(parents=True, exist_ok=True)

        feedback_row = {
            "user_id": feedback.user_id,
            "subject": feedback.subject,
            "topic": feedback.topic,
            "feedback_rating": feedback.feedback_rating,
            "useful": feedback.useful,
            "comments": feedback.comments if feedback.comments else "",
            "timestamp": datetime.utcnow().isoformat()
        }

        df_new = pd.DataFrame([feedback_row])

        # Append to CSV (create if not exists)
        if FEEDBACK_PATH.exists():
            df_existing = pd.read_csv(FEEDBACK_PATH)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new

        df_combined.to_csv(FEEDBACK_PATH, index=False)

        return {"status": "success", "message": "Feedback recorded successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save feedback: {str(e)}")




































