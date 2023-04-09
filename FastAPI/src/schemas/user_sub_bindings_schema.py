from pydantic import BaseModel, EmailStr


class UserSubBindingsInput(BaseModel):
    user_email: EmailStr
    subscription_name: str

    class Config:
        orm_mode = True


class UserSubBindings(BaseModel):
    user_binding: int
    sub_id: int

    class Config:
        orm_mode = True
