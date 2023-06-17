from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import models
from database.database import engine
from routers import post

app = FastAPI()

app.include_router(post.router)

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    'http://localhost:3000',
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
