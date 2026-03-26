from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

CSV_FILE = "students_complete.csv"
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE, encoding="utf-8")
    if df.empty:
        df_loaded = False
    else:
        df = df.fillna("").astype(str)
        df_loaded = True
else:
    df = pd.DataFrame()
    df_loaded = False

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return {"message": "Here you will get the data from the CSV file"}

@app.get("/view")
def view():
    if not df_loaded:
        return {"error": "CSV file not found or empty"}
    return JSONResponse(content=df.to_dict(orient="records"))