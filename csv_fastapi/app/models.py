from sqlalchemy import Column, String, Integer, Float
from .database import Base

class Student(Base):
    __tablename__ = "Students"

    student_id = Column(String(20), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    major = Column(String(50))
    gpa = Column(Float)
    attendance = Column(Float)
    scholarship = Column(Float)
    city = Column(String(50))
    status = Column(String(20))