import time
import requests
from services.analyzer_service.analyzer import analyze


def check_api(url: str):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        response_time_ms = round((time.time() - start_time) * 1000, 2)

        monitor_result = {
            "url": url,
            "http_status": response.status_code,
            "response_time_ms": response_time_ms
        }

        analysis = analyze(monitor_result)

        return {
            **monitor_result,
            "analysis": analysis
        }

    except Exception as e:
        return {
            "url": url,
            "http_status": 0,
            "response_time_ms": None,
            "analysis": {
                "status": "DOWN",
                "severity": "CRITICAL",
                "reason": str(e)
            }
        }