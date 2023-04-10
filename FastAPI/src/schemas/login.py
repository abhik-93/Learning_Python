from pydantic import BaseModel, EmailStr


class TokenData(BaseModel):
    user_email_id: EmailStr
