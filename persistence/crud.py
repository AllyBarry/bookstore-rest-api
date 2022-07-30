from sqlalchemy.orm import Session

from persistence import schemas
from persistence.models import Book, User
from core.security import verify_password, get_password_hash

def authenticate_user(db: Session, email: str, password: str):
        user = get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_author(db: Session, author: str):
    return db.query(User).filter(User.author_name == author).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, author_name=user.author_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    obj = db.query(Book).get(book_id)
    db.delete(obj)
    db.commit()
    return obj


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def find_book_by_title(db: Session, title: str):
    return db.query(Book).filter(Book.title == title).all()


def find_book_by_author(db: Session, author: str):
    user = get_user_by_author(db, author)
    if not user:
        return None
    return db.query(Book).filter(Book.author_id == user.id).all()


def create_user_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_book = Book(**book.dict(), author_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
