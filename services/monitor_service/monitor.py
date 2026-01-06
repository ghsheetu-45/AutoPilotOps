import requests
import time

def check_api_health(url: str):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)
        response_time = (time.time() - start_time) * 1000

        status = "HEALTHY"
        if response_time > 2000:
            status = "SLOW"

        return {
            "url": url,
            "status": status,
            "response_time_ms": round(response_time, 2),
            "http_status": response.status_code
        }

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": "DOWN",
            "error": str(e)
        }