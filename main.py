from fastapi import FastAPI
from apis import minecraft, wabisabi,kuraiorg,al,kuraiapp

from modules import utils
response = utils.get_response_template()

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

import requests


# API Setup ##################################################################################################
app = FastAPI()

app.include_router(minecraft.router,prefix="/minecraft")
app.include_router(wabisabi.router,prefix="/wabisabi")
app.include_router(kuraiorg.router,prefix="/kuraiorg")
app.include_router(al.router,prefix="/al")
app.include_router(kuraiapp.router,prefix="/kuraiapp")

#templates replace <route>
# 
# app.include_router(<route>.router,prefix="/<route>")
# app.include_router(<route>.router,prefix="/<route>")
# app.include_router(<route>.router,prefix="/<route>")
# app.include_router(<route>.router,prefix="/<route>")
import configparser
import os

ini = os.path.join(utils.get_project_root(),"data",".config")
config = configparser.ConfigParser()
config.read(ini)
config_values= {}

for section in config.sections():
  config_values[section]={}
  for option in config.options(section):
    config_values[section][option]= config.get(section,option) 
    


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

# Database setup ##############################################################################################
DATABASE_URL = config_values['database']['database_url']
engine = create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)
database = databases.Database(DATABASE_URL)



@app.get('/')
async def root():
    endpoints=[]
    for route in app.routes:
        endpoint_info = {
            "path": route.path,
            "method": route.methods,
            "name": route.name,
        }
        endpoints.append(endpoint_info)
    return {"message":"Welcome estranged traveler","endpoints":endpoints}

@app.get('/ping')
async def ping():
    response["return"] =  {"message": "pong"}
    return response

# USER Section

@app.get('/users')
async def get_users(limit: int | None=None):
    if limit is not None:
        response["return"] = {"users": users_list[:limit]}
        return response
    else:
        response["return"] = {"users": users_list}
        return response
@app.post('/user/create')
async def create_user(user: User):
    return user

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    response["return"] = {"username":"johndoe","uuid":user_id}
    return response

@app.post('/blogsite/add')
async def create_blogpost(title: str, body: str, ):
    
    response["return"] = {""}
    return response



@app.get('/modules')
async def list_modules():
    modules_list = []
    response["return"] =  {"modules_list": modules_list}
    return response

@app.post('/modules/morse')
async def send_morse_message(message):
    
    response["return"] =  {"message":message}
    return response
