from pydantic import BaseModel,validator
from sqlalchemy import Column,String,Integer,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from modules.database import Base
from typing import Optional
from datetime import datetime

Base = declarative_base()

class EventCard(BaseModel):

    title: str
    category: str='General'
    description: str
    user_id: int=0
    # created_at: str
    # updated_at: str
    active: bool=False
    persist: bool=False
    persist_rounds: int =10
    
    @validator('title')
    def title_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('title cannot be empty')
        return value
    
    @validator('category')
    def category_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('category cannot be empty')
        return value
    
    @validator('description')
    def description_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('description cannot be empty')
        return value
    
    @validator('user_id')
    def user_id_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('user_id cannot be empty')
        return value
    
    
class EventCardDB(Base):
    __tablename__ = "event_card"
    id =Column(Integer, primary_key=True,index= True,autoincrement=True)
    title = Column(String)
    category = Column(String)
    description = Column(String)
    user_id = Column(Integer)
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    active = Column(Boolean)
    persist = Column(Boolean) 
    persist_rounds = Column(Integer) 