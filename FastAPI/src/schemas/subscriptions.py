from pydantic import BaseModel


class Subscriptions(BaseModel):
    name: str
    genre: str

    class Config:
        orm_mode = True
