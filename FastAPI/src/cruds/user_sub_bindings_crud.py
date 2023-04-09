from sqlalchemy.orm import Session

from ..models.user_sub_bindings import Bindings
from ..schemas.user_sub_bindings_schema import UserSubBindings


def get_all_subs(db: Session, offset: int, limit: int):
    return db.query(Bindings).offset(offset).limit(limit).all()


def get_subs_based_on_user_and_sub(db: Session, bind_obj: UserSubBindings):
    return db.query(Bindings).filter(Bindings.user_binding == bind_obj.user_binding and
                                     Bindings.sub_id == bind_obj.sub_id).first()


def create_user_subscriptions(db: Session, bind_obj: UserSubBindings):
    new_obj = Bindings(user_binding=bind_obj.user_binding,
                       sub_id=bind_obj.sub_id)
    db.add(new_obj)
    db.commit()
    db.refresh(new_obj)
    return new_obj
