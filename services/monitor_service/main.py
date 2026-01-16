from fastapi import FastAPI, Query
from services.monitor_service.health import check_api_health

app = FastAPI(title="Monitor Service")

@app.get("/health-check")
def health_check(url:str=Query(..., description="API URL to monitor")):
    return check_api_health(url)