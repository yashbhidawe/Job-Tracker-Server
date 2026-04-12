from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/jobs", tags=["Jobs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.JobResponse)
def create(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db, job)

@router.get("/", response_model=list[schemas.JobResponse])
def get_all(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

@router.get("/{job_id}", response_model=schemas.JobResponse)
def get_by_id(job_id: int, db: Session = Depends(get_db)):
    return crud.get_job_by_id(db, job_id)


@router.delete("/{job_id}", response_model=schemas.JobResponse)
def delete(job_id: int, db: Session = Depends(get_db)):
    return crud.delete_job(db, job_id)
