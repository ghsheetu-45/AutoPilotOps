import requests
import time
from backend.storage.db import SessionLocal, engine
from backend.storage.models import ApiHealth
from backend.storage.db import Base

Base.metadata.create_all(bind=engine)

def check_api_health(url: str):
    start = time.time()
    db = SessionLocal()

    try:
        r = requests.get(url, timeout=5)
        response_time = (time.time() - start) * 1000

        status = "HEALTHY" if response_time < 2000 else "SLOW"

        db.add(ApiHealth(
            url=url,
            status=status,
            response_time=response_time
        ))
        db.commit()

        return {
            "url": url,
            "status": status,
            "response_time_ms": round(response_time, 2),
            "http_status": r.status_code
        }

    except Exception as e:
        db.add(ApiHealth(
            url=url,
            status="DOWN",
            response_time=0
        ))
        db.commit()

        return {"url": url, "status": "DOWN", "error": str(e)}

    finally:
        db.close()