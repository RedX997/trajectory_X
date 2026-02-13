from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import students, analytics, metrics, gamification, alumni

# Create FastAPI app with enhanced documentation
app = FastAPI(
    title="Trajectory-X API",
    description="Advanced AI-powered University Student Trajectory Planning & Analytics",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(students.router)
app.include_router(analytics.router)
app.include_router(metrics.router)
app.include_router(gamification.router)
app.include_router(alumni.router)

# Optional root route to show backend status
@app.get("/")
def root():
    return {"status": "Trajectory-X backend running"}
