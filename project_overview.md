# Trajectory-X Project Overview

## 🚀 Project Description
**Trajectory-X** is an AI-powered educational platform designed to analyze, predict, and improve university student performance. It moves beyond simple grade tracking to offer a holistic view of a student's journey, incorporating academic results, behavioral metrics, digital wellbeing, and career aspirations.

The core value proposition is **"Trajectory Planning"**—using data to guide students from their current state to their desired career outcome.

---

## 🏗️ Architecture & Tech Stack

### **Backend**
*   **Framework:** FastAPI (Python) - chosen for speed and automatic OpenAPI documentation.
*   **Database:** PostgreSQL (Relation Data) & ChromaDB (Vector Data).
*   **ORM:** SQLAlchemy - for interacting with the SQL database.
*   **AI/ML:** 
    *   `sentence-transformers` (all-MiniLM-L6-v2) for generating semantic embeddings of student profiles.
    *   Vector search for finding similar students (Alumni analysis).

### **Data Flow**
1.  **Ingestion:** Data is imported from CSVs into normalized PostgreSQL tables.
2.  **Vectorization:** Detailed text summaries of students (including grades, habits, and wellbeing) are converted into vector embeddings.
3.  **API Layer:** RESTful endpoints expose this data to the frontend or other services.

---

## 🗄️ Database Schema (Key Models)

The database is designed to capture a 360-degree view of the student.

1.  **`Student`**: Core profile (Demographics, GPA, Career Desires, Placement Stats).
2.  **`StudentSubjectScore`**: Academic performance (Subject-wise marks).
3.  **`BehavioralMetric`**: Study habits, project work, consistency, assignment submission.
4.  **`DigitalWellbeingDaily`**: Daily logs of screen time, focus, sleep, and app usage.
5.  **`StudentActivity`**: A unified table for:
    *   **Schedule**: Time-bound classes/meetings.
    *   **To-Do**: Task lists.
    *   **Planner**: Daily structured time blocks.
6.  **`VectorProfile`**: Stores the generated text summary and high-dimensional vector for AI analysis.
7.  **`CommunityPost`**: Social engagement (Memes/Reels uploads).

---

## 🔌 API Modules (Endpoints)

The backend is modularized into `app/routes/`:

### **1. Students (`/students`)**
*   Create and list student profiles.
*   Manage subject scores.
*   **Key Feature:** Validation of GPA (0-10) and Attendance (0-100).

### **2. Analytics (`/analytics`)**
*   **Trajectory Score:** AI-calculated score predicting future success.
*   **Gap Analysis:** Compares a student against successful alumni.
*   **Vector Generation:** Triggers the embedding engine to update student vectors.

### **3. Metrics (`/metrics`)**
*   **Behavioral:** Fetches study hours, project counts, and soft skills.
*   **Wellbeing:** Log and fetch daily screen time, sleep, and focus scores.
*   **Logs:** Daily journal entries for mood and focus.

### **4. Activities (`/activities`)**
*   **One-Stop-Shop:** Manage Schedule, Todos, and Plans in one place.
*   **Filtering:** Fetch by date, type (schedule/todo), or status (pending/completed).
*   **Efficiency:** Uses `POST` for fetching to allow complex filtering.

### **5. Community (`/community`)**
*   Upload and view memes/reels.
*   Simple social features like "Likes".

---

## 🧠 AI & Vector Engine (`vector_gen_service.py`)

This is the "Brain" of the project.
*   **Mechanism:** It concatenates all user data (Academics + Behavior + Wellbeing + Planning) into a single natural language "Profile Summary".
*   **Vectorization:** This summary is encoded into a list of numbers (vector).
*   **Usage:** These vectors allow the system to ask questions like *"Who is similar to this student?"* or *"What did successful students like this one do differently?"*

---

## 🛠️ Key Files & structure

*   `backend/app/main.py`: Entry point, configures CORS and includes routers.
*   `backend/app/models.py`: SQLAlchemy database definitions.
*   `backend/import_csv_data.py`: sophisticated script to wipe DB, sync schema, and import diverse datasets from a master CSV, including auto-generating vectors.
*   `backend/app/services/`: Business logic layer (separating logic from routes).

---

## 📝 Recent Achievements
*   **Switched to POST:** All fetch endpoints were migrated to `POST` requests for better security and flexibility.
*   **Unified Activities:** Created a robust `StudentActivity` model to handle three different features (Schedule/Todo/Plan) efficiently.
*   **Detailed Wellbeing:** Expanded digital wellbeing tracking to include granular details like social media usage vs. educational time.
