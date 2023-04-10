from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..cruds.users import get_user_by_name
from ..utils.hashed_pwd import verify_hash_pwd
from ..utils.jwt_token import generate_token

router = APIRouter()


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    fetched_user_details = get_user_by_name(db=db, name=request.username)
    if not fetched_user_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found")
    if not verify_hash_pwd(req_pwd=request.password, db_pwd=fetched_user_details.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Entered password is wrong")
    access_token = generate_token(data={"sub": fetched_user_details.email})
    return {"access_token": access_token, "token_type": "bearer"}
