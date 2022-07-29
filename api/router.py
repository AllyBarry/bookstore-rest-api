from fastapi import APIRouter

from api.endpoints import books, users, login

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["login"])