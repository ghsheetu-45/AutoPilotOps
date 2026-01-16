import time
import requests

def check_api_health(url: str):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=5)
        response_time = round((time.time() - start_time) * 1000, 2)

        return {
            "url": url,
            "status": "UP",
            "http_status": response.status_code,
            "response_time_ms": response_time
        }

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "status": "DOWN",
            "error": str(e)
        }