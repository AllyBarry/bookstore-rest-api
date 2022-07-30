from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from persistence import crud, schemas, models
from api.utils import get_db, get_current_user

router = APIRouter()

@router.get("/list/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all books.
    """
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get("/find_by_title/{title}", response_model=List[schemas.Book])
def read_books(title: str, db: Session = Depends(get_db)):
    """
    Find book by title.
    """
    books = crud.find_book_by_title(db, title)
    return books


@router.get("/find_by_author/{author}", response_model=List[schemas.Book])
def read_books(author: str, db: Session = Depends(get_db)):
    """
    Find book by author.
    """
    books = crud.find_book_by_author(db, author)
    return books


@router.post("/create/", response_model=schemas.Book)
def create_book(book_in: schemas.BookCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """
    Create new book.
    """
    book = crud.create_user_book(db=db, book=book_in, user_id=current_user.id)
    return book


# @router.delete("/{id}", response_model=schemas.Book)
# def delete_book(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     """
#     Delete a book.
#     """
#     book: models.Book = crud.get_book(db=db, book_id=id)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")
#     print(book)
#     # current_user: models.User = await get_current_user(db)
#     print(current_user)
#     if not book.author_id != current_user.id:
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     book = crud.delete_book(db=db, book_id=id)
#     return book
