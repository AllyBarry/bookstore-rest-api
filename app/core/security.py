import os
import secrets
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# For testing purposes
ALGORITHM = "HS256"
SECRET_KEY = "7987645c6adfb7b658a63eb9270ef86829a88fe51fa2e4b5105bf6791730861f"
# SECRET_KEY = secrets.token_urlsafe(32)

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
