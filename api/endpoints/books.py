from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from persistence import crud, schemas
from api.utils import get_db

router = APIRouter()

@router.get("/list/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books