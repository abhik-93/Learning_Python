from sqlalchemy.orm import Session

from ..models.users import Users
from ..schemas.users import Users as PyUsers


def get_all_users(db: Session, offset: int, limit: int):
    return db.query(Users).offset(offset).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()


def get_user_by_id(db: Session, _id: int):
    return db.query(Users).filter(Users.id == _id).first()


def create_user(db: Session, new_user: PyUsers):
    new_user_obj = Users(name=new_user.name, email=new_user.email, password=new_user.password)
    db.add(new_user_obj)
    db.commit()
    db.refresh(new_user_obj)
    return new_user_obj
