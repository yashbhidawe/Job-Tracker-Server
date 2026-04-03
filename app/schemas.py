from pydantic import BaseModel
from datetime import date
from typing import Optional

class JobCreate(BaseModel):
    company: str
    role: str
    applied_date: date
    notes: Optional[str] = None

class JobResponse(JobCreate):
    id: int
    status: str

    class Config:
        from_attributes = True