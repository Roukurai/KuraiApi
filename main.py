from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import requests


class User(BaseModel):
    id: int
    uuid: int
    username: str
    first_name: str
    last_name: str
    email: str | None = None
    
Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, index= True)
    uuid = Column(Integer, unique=True,index=True)
    username = Column(String,unique=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    created_by = Column(String)
    updated_at = Column(DateTime,default=datetime.now())
    updated_by = Column(String)

DATABASE_URL = "postgresql://roukurai:Sama4CA2@192.168.196.13/kuraitachi"
engine = create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)

database = databases.Database(DATABASE_URL)


app = FastAPI()

users_list = [
    {"username": "johndoe", "first_name": "John", "last_name": "Doe", "id": 1},
    {"username": "janedoe", "first_name": "Jane", "last_name": "Doe", "id": 2},
    {"username": "jimdoe", "first_name": "Jim", "last_name": "Doe", "id": 3}
]

@app.get('/')
async def root():
    return {"message":"Welcome estranged traveler"}

@app.get('/ping')
async def ping():
    return {"message": "pong"}

# USER Section

@app.get('/users')
async def get_users(limit: int | None=None):
    if limit is not None:
        return {"users": users_list[:limit]}
    else:
        return {"users": users_list}

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    return {"username":"johndoe","uuid":user_id}

@app.post('/user/create')
async def create_user(user: User):
    return user