from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

import models.models as models
import schemas.schemas as schemas

def get_all(db: Session):
    cases = db.query(models.cases).all()
    return cases

def create(request: schemas.create_cases, db: Session):
    new_cases = models.cases(
        cases_name = request.cases_name,
        roles_id = request.roles_id,
        cases_identifier = request.cases_identifier
    )
    db.add(new_cases)
    db.commit()
    db.refresh(new_cases)
    return(new_cases)

def delete(id, db: Session):
    cases = db.query(models.cases).filter(models.cases.id == id)
    if not cases.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cases with id {id} not found.")
    cases.delete(synchronize_session=False)
    db.commit()
    return

def update(id, request: schemas.cases, db: Session):
    cases = db.query(models.create_cases).filter(models.cases.id == id)
    if not cases.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"cases with id {id} not found.")    
    cases.update(request.dict())
    db.commit()
    return

def get_one(id, db: Session):
    cases = db.query(models.cases).filter(models.cases.id == id).first()
    if not cases:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"cases id {id} not found.")
    return cases