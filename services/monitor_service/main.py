from fastapi import FastAPI
from services.monitor_service.monitor import check_api

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Monitor service running"}

@app.get("/check")
def check(url: str):
    return check_api(url)