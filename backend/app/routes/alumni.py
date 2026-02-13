from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.db import get_db
from app.models import Alumni

router = APIRouter(prefix="/alumni", tags=["alumni"])

class AlumniResponse(BaseModel):
    id: int
    name: str
    major: str
    company_tier: str
    role_title: str
    salary_range: int
    class Config: from_attributes = True

@router.get("/", response_model=List[AlumniResponse])
def get_alumni(db: Session = Depends(get_db)):
    return db.query(Alumni).all()
