import secrets
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

from src.schemas.token_data import TokenData

SECRET_KEY: str = secrets.token_hex(64)  # Might want to store this in AWS Secrets Manager
ALGORITHM: str = "HS256"
EXPIRE_TIME_IN_MINUTES: int = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_TIME_IN_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, algorithm=ALGORITHM, key=SECRET_KEY)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="Invalid Auth Credentials",
                                         headers={"WWW-Authenticate": "Bearer"}, )
    try:
        decoded_jwt: dict = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = decoded_jwt.get('sub')
        if user_email is None:
            raise credential_exception
        TokenData(user_email_id=user_email)
    except JWTError:
        raise credential_exception
