from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.cruds import users as crud_users
from ..database import get_db
from ..schemas.users import Users, DisplayUser

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/list", response_model=list[Users])
def get_all_users(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    user_objs = crud_users.get_all_users(db=db, offset=offset, limit=limit)
    if not user_objs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return user_objs


@router.get("/", response_model=Users)
def get_by_email(email: str, db: Session = Depends(get_db)):
    user_obj = crud_users.get_user_by_email(db, email)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return user_obj


@router.post("/", response_model=DisplayUser)
def create_user(_user: Users, db: Session = Depends(get_db)):
    return crud_users.create_user(db=db, new_user=_user)
