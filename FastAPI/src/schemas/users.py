from typing import Optional

from pydantic import BaseModel, EmailStr


class Users(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class DisplayUser(BaseModel):
    name: Optional[str]
    email: EmailStr

    class Config:
        orm_mode = True
