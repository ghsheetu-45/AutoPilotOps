from fastapi import FastAPI
from monitor import check_api_health

app = FastAPI(title="AutoPilotOps Monitor Service")

@app.get("/")
def root():
    return {"message": "Monitor service is running"}

@app.get("/check")
def check_api(url: str):
    return check_api_health(url)