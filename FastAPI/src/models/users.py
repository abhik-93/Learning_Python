from sqlalchemy import Column, Integer, String

from src.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
