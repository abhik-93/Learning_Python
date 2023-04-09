from fastapi import FastAPI

from src import models
from src.database import engine
from src.routers import base_router, user_router, sub_router, bind_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="News Subscription")

app.include_router(router=base_router)
app.include_router(router=user_router)
app.include_router(router=sub_router)
app.include_router(router=bind_router)
