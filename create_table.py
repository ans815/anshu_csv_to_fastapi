# create_table.py
from app.database import engine
from app.models import Student

Student.metadata.create_all(bind=engine)

print("✅ Table 'Students' created successfully in MySQL")