from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.db import get_db
from app.models import Badge, StudentBadge
from datetime import datetime

router = APIRouter(prefix="/gamification", tags=["gamification"])

class BadgeResponse(BaseModel):
    id: int
    name: str
    description: str
    class Config: from_attributes = True

class StudentBadgeResponse(BaseModel):
    badge_id: int
    earned_at: datetime
    class Config: from_attributes = True

@router.get("/badges", response_model=List[BadgeResponse])
def get_all_badges(db: Session = Depends(get_db)):
    return db.query(Badge).all()

@router.get("/student-badges/{student_id}", response_model=List[StudentBadgeResponse])
def get_student_badges(student_id: int, db: Session = Depends(get_db)):
    return db.query(StudentBadge).filter(StudentBadge.student_id == student_id).all()
