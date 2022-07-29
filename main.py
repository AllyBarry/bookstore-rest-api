from fastapi import FastAPI

from routers.api import api_router

app = FastAPI()

app.include_router(api_router)