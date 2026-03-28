from sqlalchemy import Column, Integer, String, Float
from database import Base 

class Student(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True)   
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    major = Column(String(100))
    gpa = Column(Float)
    attendance = Column(Float)
    scholarship = Column(Float)   
    city = Column(String(100))
    status = Column(String(50))

# student = Student(
#     student_id=row.get("student_id", "").strip(),
#     first_name=row.get("first_name", "").strip(),
#     last_name=row.get("last_name", "").strip(),
#     age=int(row["age"]) if row.get("age") and row["age"].isdigit() else 0,
#     major=row.get("major", "").strip(),
#     gpa=float(row["gpa"]) if row.get("gpa") else 0.0,
#     attendance=float(row["attendance"]) if row.get("attendance") else 0.0,
#     scholarship=float(row["scholarship"]) if row.get("scholarship") else 0.0,
#     city=row.get("city", "").strip(),
#     status=row.get("status", "").strip()
# )