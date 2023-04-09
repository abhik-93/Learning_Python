from sqlalchemy import Column, Integer, ForeignKey

from src.database import Base


class Bindings(Base):
    __tablename__ = "sub_bindings"
    user_binding = Column(Integer, ForeignKey("users.id"), nullable=False, index=True, primary_key=True)
    sub_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False, index=True, primary_key=True)
