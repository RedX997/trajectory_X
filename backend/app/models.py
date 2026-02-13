from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Date, ARRAY, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False) # e.g., 'student', 'admin'
    created_at = Column(DateTime, default=datetime.utcnow)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    major = Column(String, nullable=False)
    semester = Column(Integer)
    gpa = Column(Float)
    attendance = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class StudentSubjectScore(Base):
    __tablename__ = "student_subject_scores"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    semester = Column(Integer, nullable=False)
    subject_name = Column(String, nullable=False)
    marks = Column(Float)

class BehavioralMetric(Base):
    __tablename__ = "behavioral_metrics"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    study_hours_per_week = Column(Float)
    project_count = Column(Integer)
    skill_score = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow)

class DigitalWellbeingDaily(Base):
    __tablename__ = "digital_wellbeing_daily"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date, nullable=False)
    total_screen_time = Column(Float)
    educational_time = Column(Float)
    social_time = Column(Float)
    entertainment_time = Column(Float)
    productivity_time = Column(Float)
    communication_time = Column(Float)
    sleep_hours = Column(Float)
    focus_score = Column(Float)
    synced_at = Column(DateTime, default=datetime.utcnow)

class Badge(Base):
    __tablename__ = "badges"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)

class StudentBadge(Base):
    __tablename__ = "student_badges"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    badge_id = Column(Integer, ForeignKey("badges.id"), primary_key=True)
    earned_at = Column(DateTime, default=datetime.utcnow)

class GapAnalysis(Base):
    __tablename__ = "gap_analysis"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    metric_name = Column(String)
    student_value = Column(Float)
    alumni_average = Column(Float)
    gap_percentage = Column(Float)
    narrative = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class TrajectoryScore(Base):
    __tablename__ = "trajectory_scores"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    score = Column(Float)
    confidence_level = Column(String) # low, medium, high
    calculated_at = Column(DateTime, default=datetime.utcnow)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    content = Column(Text)
    impact_level = Column(String)
    estimated_score_gain = Column(Float)
    generated_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)

class SkillAssessment(Base):
    __tablename__ = "skill_assessments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    quiz_score = Column(Float)
    voice_score = Column(Float)
    final_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Alumni(Base):
    __tablename__ = "alumni"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    major = Column(String)
    gpa = Column(Float)
    attendance = Column(Float)
    study_hours = Column(Float)
    project_count = Column(Integer)
    skill_score = Column(Float)
    company_tier = Column(String) # Tier 1, 2, 3
    role_title = Column(String)
    salary_range = Column(Integer)
    role_major_match = Column(Float)
    graduated_year = Column(Integer)

class LLMLog(Base):
    __tablename__ = "llm_logs"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    job_type = Column(String)
    response_time = Column(Float)
    success = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)
