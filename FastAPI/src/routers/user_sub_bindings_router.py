from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..cruds import user_sub_bindings_crud, users, subscriptions
from ..database import get_db
from ..schemas.user_sub_bindings_schema import UserSubBindings, UserSubBindingsInput

router = APIRouter(tags=["Bindings"], prefix="/bindings")


@router.get("/list", response_model=list[UserSubBindingsInput])
def get_all_bindings(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    bind_objs = user_sub_bindings_crud.get_all_subs(db=db, offset=offset, limit=limit)
    if not bind_objs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No bindings found")
    res = list(map(lambda obj:
                   UserSubBindingsInput(user_email=users.get_user_by_id(db=db, _id=obj.user_binding).email,
                                        subscription_name=subscriptions.get_sub_by_id(db=db, _id=obj.sub_id).name),
                   bind_objs))
    return res


@router.post("/", response_model=UserSubBindings)
def create_user_sub_bindings(bind_obj: UserSubBindingsInput, db: Session = Depends(get_db)):
    _user_obj = users.get_user_by_email(db, bind_obj.user_email)
    if not _user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user found")

    _sub_obj = subscriptions.get_sub_by_name(db, bind_obj.subscription_name)
    if not _sub_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No subscription found")

    bind_obj = UserSubBindings(user_binding=_user_obj.id, sub_id=_sub_obj.id)

    if user_sub_bindings_crud.get_subs_based_on_user_and_sub(db, bind_obj):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Already exists")

    new_bind_objs = user_sub_bindings_crud.create_user_subscriptions(db=db,
                                                                     bind_obj=bind_obj)
    return new_bind_objs
