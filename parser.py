from pydantic import BaseModel, Field
from typing import List

class ReviewAnalysis(BaseModel):
    sentiment: str = Field(description = "Positive, Negative, Neutral or Mixed")
    sentiment_score: float = Field(description = 'Sentiment score between 0 and 1')
    key_points: List[str] = Field(description = "Important Points from the review")
    summary: str = Field(description= "Concise Summary of the review")