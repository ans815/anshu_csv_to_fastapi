# import csv
# from app.database import engine, SessionLocal
# from app.models import Student
# from sqlalchemy.exc import SQLAlchemyError

# # Ensure tables exist
# from app.database import Base
# Base.metadata.create_all(bind=engine)

# session = SessionLocal()

# csv_file_path = "data/students_complete.csv"  # aapke structure ke hisaab se

# try:
#     with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         inserted_count = 0

#         for row in reader:
#             # Check if student_id already exists in DB
#             exists = session.query(Student).filter_by(student_id=row["student_id"]).first()
#             if exists:
#                 print(f"Skipping duplicate student_id: {row['student_id']}")
#                 continue

#             student = Student(
#                 student_id=row["student_id"],
#                 first_name=row["first_name"],
#                 last_name=row["last_name"],
#                 age=int(row["age"]) if row["age"] else None,
#                 major=row["major"],
#                 gpa=float(row["gpa"]) if row["gpa"] else None,
#                 attendance=float(row["attendance"]) if row["attendance"] else None,
#                 scholarship=float(row["scholarship"]) if row["scholarship"] else None,
#                 city=row["city"],
#                 status=row["status"]
#             )
#             session.add(student)
#             inserted_count += 1

#         session.commit()
#         print(f"CSV data inserted successfully into MySQL ✅ Total inserted: {inserted_count}")

# except FileNotFoundError:
#     print(f"File not found: {csv_file_path}")

# except SQLAlchemyError as e:
#     session.rollback()
#     print("Database error:", e)

# finally:
#     session.close()

import csv
from app.database import engine, SessionLocal
from app.models import Student
from sqlalchemy.exc import SQLAlchemyError

from app.database import Base
Base.metadata.create_all(bind=engine)

session = SessionLocal()
csv_file_path = "data/students_complete.csv"

try:
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        total_inserted = 0
        for row in reader:
            # Check if student_id already exists
            exists = session.query(Student).filter_by(student_id=row["student_id"]).first()
            if exists:
                print(f"Skipping duplicate student_id: {row['student_id']}")
                continue
            
            student = Student(
                student_id=row["student_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                age=int(row["age"]) if row["age"] else None,
                major=row["major"],
                gpa=float(row["gpa"]) if row["gpa"] else None,
                attendance=float(row["attendance"]) if row["attendance"] else None,
                scholarship=float(row["scholarship"]) if row["scholarship"] else None,
                city=row["city"],
                status=row["status"]
            )
            session.add(student)
            total_inserted += 1

        session.commit()
        print(f"CSV data inserted successfully into MySQL ✅ Total inserted: {total_inserted}")

except FileNotFoundError:
    print(f"File not found: {csv_file_path}")

except SQLAlchemyError as e:
    session.rollback()
    print("Database error:", e)

finally:
    session.close()