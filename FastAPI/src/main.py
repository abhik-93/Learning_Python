from fastapi import FastAPI, APIRouter

from src import models
from src.database import engine
from src.routers import base_router, user_router, sub_router, bind_router, login_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Subscription")

list_of_routers: list[APIRouter] = [base_router, user_router, sub_router, bind_router, login_router]

for _ in list_of_routers:
    app.include_router(_)
