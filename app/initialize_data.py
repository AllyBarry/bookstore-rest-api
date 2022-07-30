import csv
import os
import logging

from faker import Faker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

fake = Faker()

from persistence.database import SessionLocal, engine
from persistence import schemas, crud, models

script_dir = os.path.dirname(os.path.realpath(__file__))
sample_users = os.path.join(script_dir, "sample-data", "users.csv")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_sample_data(db: SessionLocal):
    # Loads test data into the database
    with open(sample_users, "r") as f:
        csv_reader = csv.DictReader(f, delimiter=';')

        for row in csv_reader:
            print(row)
            user = crud.get_user_by_email(db, email=row["email"])
            if not user:
                    user_in = schemas.UserCreate(
                        email=row["email"],
                        password=row["password"],
                        author_name=row["author_name"],
                        is_superuser=False,
                    )
                    user = crud.create_user(db, user_in)

            for _ in range(3):
                new_book = schemas.BookCreate(
                    title=fake.sentence(4),
                    description= fake.sentence(10),
                    price=100.50,
                    cover_art=fake.image_url()
                )
                crud.create_user_book(db, new_book, user.id)

def init_db(db: SessionLocal):
    print(os.getenv('SQLALCHEMY_DATABASE_URL'))
    # Should apply migrations rather
    models.Base.metadata.create_all(bind=engine)

    load_sample_data(db)


def init():
    db = SessionLocal()
    init_db(db)


def main():
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
