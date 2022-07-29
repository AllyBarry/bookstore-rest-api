import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
print(os.getenv('SQLALCHEMY_DATABASE_URL'))

engine = create_engine(    
    os.getenv('SQLALCHEMY_DATABASE_URL')
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()