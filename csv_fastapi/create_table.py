from app.database import engine
from app.models import Student

# Create table
Student.metadata.create_all(bind=engine)

print("✅ Table 'Students' created successfully in MySQL")