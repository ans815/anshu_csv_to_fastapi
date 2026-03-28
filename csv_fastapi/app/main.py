from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MySQL Connected Successfully"}

app.include_router(router)