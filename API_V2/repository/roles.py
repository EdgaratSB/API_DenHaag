from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

import models.models as models
import schemas.schemas as schemas

def get_all(db: Session):
    roles = db.query(models.roles).all()
    return roles

def create(request: schemas.create_roles, db: Session):
    new_roles = models.roles(
        roles_name = request.roles_name,
    )
    db.add(new_roles)
    db.commit()
    db.refresh(new_roles)
    return(new_roles)

def delete(id, db: Session):
    roles = db.query(models.roles).filter(models.roles.id == id)
    if not roles.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"roles with id {id} not found.")
    roles.delete(synchronize_session=False)
    db.commit()
    return

def update(id, request: schemas.create_roles, db: Session):
    roles = db.query(models.roles).filter(models.roles.id == id)
    if not roles.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"roles with id {id} not found.")    
    roles.update(request.dict())
    db.commit()
    return

def get_one(id, db: Session):
    roles = db.query(models.roles).filter(models.roles.id == id).first()
    if not roles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"roles id {id} not found.")
    return roles