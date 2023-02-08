from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

import models.models as models
import schemas.schemas as schemas

def get_all(db: Session):
    access_levels = db.query(models.access_levels).all()
    return access_levels

def create(request: schemas.create_access_levels, db: Session):
    new_access_levels = models.access_levels(
        access_levels_name = request.access_levels_name,
        cases_id = request.cases_id
    )
    db.add(new_access_levels)
    db.commit()
    db.refresh(new_access_levels)
    return(new_access_levels)

def delete(id, db: Session):
    access_levels = db.query(models.access_levels).filter(models.access_levels.id == id)
    if not access_levels.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"access_levels with id {id} not found.")
    access_levels.delete(synchronize_session=False)
    db.commit()
    return

def update(id, request: schemas.create_access_levels, db: Session):
    access_levels = db.query(models.access_levels).filter(models.access_levels.id == id)
    if not access_levels.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"access_levels with id {id} not found.")    
    access_levels.update(request.dict())
    db.commit()
    return

def get_one(id, db: Session):
    access_levels = db.query(models.access_levels).filter(models.access_levels.id == id).first()
    if not access_levels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"access_levels id {id} not found.")
    return access_levels