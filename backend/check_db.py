from app.db import engine
from sqlalchemy import text

with engine.connect() as conn:
    print("Students Columns:")
    res = conn.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name = 'students'"))
    for r in res:
        print(f" - {r[0]}")
    
    print("\nGrades Columns:")
    res = conn.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name = 'grades'"))
    for r in res:
        print(f" - {r[0]}")
