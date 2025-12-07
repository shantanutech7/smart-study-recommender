from pydantic import BaseModel
from typing import List, Optional


class RecommendationRequest(BaseModel):
    user_id: str
    top_n: int = 5


class RecommendationItem(BaseModel):
    subject: str
    topic: str
    priority_score: float
    reason: str


class RecommendationResponse(BaseModel):
    user_id: str
    recommendations: List[RecommendationItem]


class FeedbackRequest(BaseModel):
    user_id: str
    subject: str
    topic: str
    feedback_rating: int
    useful: bool
    comments: Optional[str] = None
