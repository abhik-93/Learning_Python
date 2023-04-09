from sqlalchemy.orm import Session

from ..models.subscriptions import Subscriptions
from ..schemas.subscriptions import Subscriptions as PySubscriptions


def get_all_subscriptions(db: Session, offset: int, limit: int):
    return db.query(Subscriptions).offset(offset).limit(limit).all()


def get_sub_by_genre(db: Session, genre: str):
    return db.query(Subscriptions).filter(Subscriptions.genre == genre).all()


def get_sub_by_name(db: Session, name: str):
    return db.query(Subscriptions).filter(Subscriptions.name == name).first()


def get_sub_by_id(db: Session, _id: int):
    return db.query(Subscriptions).filter(Subscriptions.id == _id).first()


def create_subscription(db: Session, new_sub: PySubscriptions):
    new_sub_obj = Subscriptions(name=new_sub.name, genre=new_sub.genre)
    db.add(new_sub_obj)
    db.commit()
    db.refresh(new_sub_obj)
    return new_sub_obj
