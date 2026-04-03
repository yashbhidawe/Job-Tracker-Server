from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(String, default="applied")
    applied_date = Column(Date)
    notes = Column(String, nullable=True)