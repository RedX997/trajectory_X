from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Date, Time, ARRAY, Text
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
    usn = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    major = Column(String, nullable=False)
    semester = Column(Integer)
    college_name = Column(String)
    is_alumni = Column(Boolean, default=False)
    gpa = Column(Float)
    gpa_trend = Column(String) # Stable, Increasing, Decreasing
    attendance = Column(Float)
    backlogs = Column(Integer, default=0)
    programming_languages = Column(Text)
    strongest_skill = Column(String)
    placement_status = Column(String) # Not Placed, Placed, etc.
    
    # Career & Personal Growth
    biggest_strength = Column(Text)
    biggest_weakness = Column(Text)
    habit_to_improve = Column(Text)
    what_holds_back = Column(Text)
    career_clarity = Column(Float) # 1-5
    chosen_career_path = Column(String)
    daily_placement_prep = Column(Boolean)
    interview_fear = Column(Float) # 1-5
    confidence_level = Column(Float) # 1-5
    
    # Placement Performance
    role_relevance = Column(Float) # 0-100%
    placement_attempts = Column(Integer)
    months_to_get_placed = Column(Integer)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class StudentSubjectScore(Base):
    __tablename__ = "student_subject_scores"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    student_name = Column(String) # For easier identification
    semester = Column(Integer, nullable=False)
    subject_name = Column(String, nullable=False)
    marks = Column(Float)

class BehavioralMetric(Base):
    __tablename__ = "behavioral_metrics"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    study_hours_per_week = Column(Float)
    practice_hours_per_day = Column(Float)
    project_count = Column(Integer)
    project_types = Column(Text)
    deployed_project = Column(Boolean)
    internship_exp = Column(Boolean)
    internship_duration = Column(Integer)
    problem_solving = Column(Float)
    communication = Column(Float)
    teamwork = Column(Float)
    consistency = Column(Float)
    
    # Study Habits
    attend_lab_regularly = Column(Boolean)
    submit_assignments_on_time = Column(Boolean)
    avg_internal_marks = Column(Float)
    follow_study_schedule = Column(Boolean)
    concept_revision_frequency = Column(String)
    online_courses_count = Column(String) # e.g., "2" or "list of courses"
    
    skill_score = Column(Float) # Derived or direct
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
    sleep_schedule = Column(String) # e.g., "Irregular"
    use_phone_while_studying = Column(Boolean)
    distraction_level = Column(Float) # 1-5
    mental_exhaustion = Column(Boolean)
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

class LLMLog(Base):
    __tablename__ = "llm_logs"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    job_type = Column(String)
    response_time = Column(Float)
    success = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)

class CommunityPost(Base):
    __tablename__ = "community_posts"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    media_url = Column(String, nullable=False) # e.g., "/static/uploads/meme_1.jpg"
    media_type = Column(String, nullable=False) # 'meme' or 'reel'
    caption = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    likes_count = Column(Integer, default=0)

class DailyLog(Base):
    __tablename__ = "daily_logs"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    date = Column(Date, nullable=False, default=datetime.utcnow().date)
    activity_description = Column(Text)
    mood_score = Column(Float) # 1-10
    focus_hours = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class StudentActivity(Base):
    """
    Unified table for Schedule, To-Do List, and Day Planner
    
    This single table handles three features:
    1. Schedule: Time-bound events (classes, meetings)
    2. To-Do: Tasks without specific time (assignments, projects)
    3. Planner: Planned time blocks for the day
    
    Why one table? 
    - Simpler queries (get all activities for a day)
    - Flexible (easy to add new activity types)
    - Efficient (single index on student_id + date)
    """
    __tablename__ = "student_activities"
    
    # === PRIMARY IDENTIFICATION ===
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)  # Which day this activity belongs to
    
    # === ACTIVITY DETAILS ===
    title = Column(String, nullable=False)  # "Study DSA", "Submit Assignment", "Morning Jog"
    description = Column(Text)  # Optional: More details about the activity
    
    # Type determines which feature this belongs to
    activity_type = Column(String, nullable=False)  # "schedule" | "todo" | "plan"
    
    # Category helps with filtering and analytics
    category = Column(String)  # "study" | "class" | "personal" | "project" | "exercise"
    
    # === TIMING (Flexible - not all fields required for all types) ===
    # For schedule & planner: both start and end time
    # For todo: only due_date (stored in 'date' field)
    start_time = Column(Time)  # Example: 09:00 AM
    end_time = Column(Time)    # Example: 11:00 AM
    duration_minutes = Column(Integer)  # Calculated or manual: 120 minutes
    
    # === STATUS & PRIORITY ===
    is_completed = Column(Boolean, default=False)  # Has the student finished this?
    priority = Column(Integer, default=2)  # 1=High, 2=Medium, 3=Low
    
    # === METADATA ===
    created_at = Column(DateTime, default=datetime.utcnow)  # When was this created?
    completed_at = Column(DateTime)  # When was it marked complete?
    
    # === OPTIONAL: RECURRING EVENTS ===
    is_recurring = Column(Boolean, default=False)  # Does this repeat?
    recurrence_rule = Column(String)  # "DAILY", "WEEKLY", "MONTHLY"

class VectorProfile(Base):
    __tablename__ = "vector_profiles"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    vector_id = Column(String, unique=True) # ID used in ChromaDB
    last_updated = Column(DateTime, default=datetime.utcnow)
    profile_summary = Column(Text) # Text used to generate the vector
    embedding_vector = Column(ARRAY(Float)) # The actual list of numbers (e.g. [0.1, -0.2...])
