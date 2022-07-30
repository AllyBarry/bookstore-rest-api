import os

from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from api.router import api_router

app = FastAPI(title=os.getenv('PROJECT_NAME'))

app.include_router(api_router)
