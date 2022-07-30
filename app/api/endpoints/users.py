from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from persistence import crud, schemas
from api.utils import get_db

router = APIRouter()

@router.get("/list/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users