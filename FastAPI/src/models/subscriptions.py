from sqlalchemy import Column, Integer, String

from src.database import Base


class Subscriptions(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, index=True, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False, index=True)
    genre = Column(String, nullable=False)
