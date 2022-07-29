from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from persistence import crud, schemas
from persistence.database import SessionLocal

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @router.get("/{id}", response_model=schemas.Book)
# def read_book(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get book by ID.
#     """
#     book = crud.book.get(db=db, id=id)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     if not crud.user.is_superuser(current_user) and (book.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return book

