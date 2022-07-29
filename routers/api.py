from fastapi import APIRouter

from . import books

api_router = APIRouter()

api_router.include_router(books.router, prefix="/users", tags=["books"])