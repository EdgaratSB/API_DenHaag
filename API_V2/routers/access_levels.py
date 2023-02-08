from typing import List
from fastapi import APIRouter, status, Depends

import database.database as database
import schemas.schemas as schemas
from sqlalchemy.orm import Session
import repository.access_levels as access_levels

get_db = database.get_db

router = APIRouter(
    prefix="/access_levels",
    tags=["access_levels"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.access_levels])
def show_all(db : Session = Depends(get_db)):
    return access_levels.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.create_access_levels, db: Session = Depends(get_db)):
    return access_levels.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    return access_levels.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id, request: schemas.create_access_levels, db: Session = Depends(get_db)):
    return access_levels.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.access_levels)
def show(id, db : Session = Depends(get_db)):
    return access_levels.get_one(id, db)