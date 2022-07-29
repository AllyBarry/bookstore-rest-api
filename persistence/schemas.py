from typing import List, Union

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: Union[str, None] = None
    price: float
    cover_art: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    author_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: List[Book] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str