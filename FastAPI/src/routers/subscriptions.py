from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..cruds import subscriptions
from ..database import get_db
from ..schemas.subscriptions import Subscriptions

router = APIRouter(tags=["Subscriptions"], prefix="/subscriptions")


@router.get("/list", response_model=list[Subscriptions])
def get_all_subscriptions(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    sub_objs = subscriptions.get_all_subscriptions(db=db, offset=offset, limit=limit)
    if not sub_objs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No subscriptions found")
    return sub_objs


@router.get("/", response_model=list[Subscriptions])
def get_by_genre(genre: str, db: Session = Depends(get_db)):
    sub_obj = subscriptions.get_sub_by_genre(db=db, genre=genre)
    if not sub_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No subscriptions found")
    return sub_obj


@router.post("/", response_model=Subscriptions)
def create_subscriptions(sub: Subscriptions, db: Session = Depends(get_db)):
    return subscriptions.create_subscription(db=db, new_sub=sub)
