from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.db import get_db
from app.models import TrajectoryScore, Recommendation, GapAnalysis
from datetime import datetime

router = APIRouter(prefix="/analytics", tags=["analytics"])

class TrajectoryResponse(BaseModel):
    student_id: int
    score: float
    confidence_level: str
    calculated_at: datetime
    class Config: from_attributes = True

class RecommendationResponse(BaseModel):
    id: int
    student_id: int
    content: str
    impact_level: str
    estimated_score_gain: float
    completed: bool
    class Config: from_attributes = True

class GapAnalysisResponse(BaseModel):
    metric_name: str
    student_value: float
    alumni_average: float
    gap_percentage: float
    narrative: str
    class Config: from_attributes = True

@router.get("/trajectory/{student_id}", response_model=TrajectoryResponse)
def get_trajectory_score(student_id: int, db: Session = Depends(get_db)):
    score = db.query(TrajectoryScore).filter(TrajectoryScore.student_id == student_id).order_by(TrajectoryScore.calculated_at.desc()).first()
    if not score:
        raise HTTPException(status_code=404, detail="No trajectory score found for this student")
    return score

@router.get("/recommendations/{student_id}", response_model=List[RecommendationResponse])
def get_recommendations(student_id: int, db: Session = Depends(get_db)):
    return db.query(Recommendation).filter(Recommendation.student_id == student_id).all()

@router.get("/gap-analysis/{student_id}", response_model=List[GapAnalysisResponse])
def get_gap_analysis(student_id: int, db: Session = Depends(get_db)):
    return db.query(GapAnalysis).filter(GapAnalysis.student_id == student_id).all()
