# import csv


# class CSVService:

#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.data = self.load_csv()


#     def load_csv(self):

#         data = []

#         with open(self.file_path, mode="r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)

#             for row in reader:

#                 row["age"] = int(row["age"])
#                 row["attendance"] = float(row["attendance"])
#                 row["scholarship"] = int(row["scholarship"])

#                 try:
#                     row["gpa"] = float(row["gpa"])
#                 except:
#                     pass

#                 data.append(row)

#         return data


#     def get_all_data(self):
#         return self.data


#     def get_data_by_id(self, record_id: str):

#         for record in self.data:

#             if record["student_id"] == record_id:
#                 return record

#         return None

import csv
from app.models import Student

class CSVService:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_csv()

    def load_csv(self):
        data = []

        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["age"] = int(row["age"])
                row["attendance"] = float(row["attendance"])
                row["scholarship"] = int(row["scholarship"])

                try:
                    row["gpa"] = float(row["gpa"])
                except:
                    row["gpa"] = 0.0

                data.append(row)

        return data

    def get_all_data(self):
        return self.data

    def get_data_by_id(self, record_id: str):
        for record in self.data:
            if record["student_id"] == record_id:
                return record
        return None


def insert_into_db(data, session):
    from app.models import Student 

    for row in data:
        existing = session.query(Student).filter_by(student_id=row["student_id"]).first()

        if not existing:
            student = Student(**row)
            session.add(student)

    session.commit()
