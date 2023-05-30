from fastapi import FastAPI
from routers import blog,user

import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)