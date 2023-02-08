from typing import List
from fastapi import APIRouter, status, Depends

import database.database as database
import schemas.schemas as schemas
from sqlalchemy.orm import Session
import repository.roles as roles

get_db = database.get_db

router = APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.roles])
def show_all(db : Session = Depends(get_db)):
    return roles.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.create_roles, db: Session = Depends(get_db)):
    return roles.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    return roles.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id, request: schemas.create_roles, db: Session = Depends(get_db)):
    return roles.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.roles)
def show(id, db : Session = Depends(get_db)):
    return roles.get_one(id, db)