# from fastapi import APIRouter, HTTPException
# from app.service import CSVService
# from app.models import DataModel
# import os

# router = APIRouter()

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# FILE_PATH = os.path.join(BASE_DIR, "data", "students_complete.csv")

# csv_service = CSVService(FILE_PATH)


# @router.get("/data")
# def get_all_data():
#     data = csv_service.load_csv()
#     return data


# @router.get("/data/{record_id}")
# def get_data(record_id: str):

#     record = csv_service.get_data_by_id(record_id)

#     if record is None:
#         raise HTTPException(
#             status_code=404,
#             detail="Record not found"
#         )

#     return record

from fastapi import APIRouter, HTTPException
from app.service import CSVService, insert_into_db
from app.database import SessionLocal
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "students_complete.csv")

csv_service = CSVService(FILE_PATH)


# Get all data
@router.get("/data")
def get_all_data():
    return csv_service.get_all_data()


# Get by ID
@router.get("/data/{record_id}")
def get_data(record_id: str):
    record = csv_service.get_data_by_id(record_id)

    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")

    return record


@router.post("/load-data")
def load_data():
    session = SessionLocal()

    try:
        data = csv_service.get_all_data()
        insert_into_db(data, session)
        return {"message": "Data inserted successfully"}
    finally:
        session.close()