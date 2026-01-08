from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .db import Base

class ApiHealth(Base):
    _tablename_ = "api_health"

    id = Column(Integer, primary_key=True)
    url = Column(String, index=True)
    status = Column(String)
    response_time = Column(Float)
    checked_at = Column(DateTime, default=datetime.utcnow)