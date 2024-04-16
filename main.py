from fastapi import FastAPI
import requests
from pydantic import BaseModel

class User(BaseModel):
    uuid: int
    username: str
    first_name: str
    last_name: str
    email: str | None = None
    

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
    return {"username":"johndoe","uuid":"69420"}

@app.post('/user/create')
async def create_user(user: User):
    return user