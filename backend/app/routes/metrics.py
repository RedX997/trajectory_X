from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.db import get_db
from app.models import BehavioralMetric, DigitalWellbeingDaily
from datetime import date, datetime

router = APIRouter(prefix="/metrics", tags=["metrics"])

class BehavioralMetricSchema(BaseModel):
    study_hours_per_week: float
    project_count: int
    skill_score: float
    class Config: from_attributes = True

class DigitalWellbeingSchema(BaseModel):
    date: date
    total_screen_time: float
    educational_time: float
    productivity_time: float
    focus_score: float
    class Config: from_attributes = True

class SkillAssessmentSchema(BaseModel):
    quiz_score: float
    voice_score: float
    final_score: float
    created_at: datetime
    class Config: from_attributes = True

@router.get("/behavioral/{student_id}", response_model=BehavioralMetricSchema)
def get_behavioral_metrics(student_id: int, db: Session = Depends(get_db)):
    return db.query(BehavioralMetric).filter(BehavioralMetric.student_id == student_id).first()

@router.get("/wellbeing/{student_id}", response_model=List[DigitalWellbeingSchema])
def get_wellbeing_data(student_id: int, db: Session = Depends(get_db)):
    return db.query(DigitalWellbeingDaily).filter(DigitalWellbeingDaily.student_id == student_id).order_by(DigitalWellbeingDaily.date.desc()).all()

@router.post("/wellbeing/sync", response_model=DigitalWellbeingSchema)
def sync_wellbeing(data: DigitalWellbeingSchema, student_id: int, db: Session = Depends(get_db)):
    db_wellbeing = DigitalWellbeingDaily(
        student_id=student_id,
        date=data.date,
        total_screen_time=data.total_screen_time,
        educational_time=data.educational_time,
        productivity_time=data.productivity_time,
        focus_score=data.focus_score
    )
    db.add(db_wellbeing)
    db.commit()
    db.refresh(db_wellbeing)
    return db_wellbeing

@router.get("/skills/{student_id}", response_model=List[SkillAssessmentSchema])
def get_skill_assessments(student_id: int, db: Session = Depends(get_db)):
    from app.models import SkillAssessment
    return db.query(SkillAssessment).filter(SkillAssessment.student_id == student_id).order_by(SkillAssessment.created_at.desc()).all()
