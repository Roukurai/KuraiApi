from pydantic import BaseModel,validator
from sqlalchemy import Column,String,Integer
from modules.database import Base
from typing import Optional


class Ticket(BaseModel):
    # id: int
    title: str
    description: str 
    status: str = "open"
    priority: int = 1
    category: str = "General"
    assignee_id: int = 1
    email: str
    
    @validator('title')
    def title_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('Title cannot be empty')
        return value
    
    @validator('description')
    def description_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('Description cannot be empty')
        return value
    
    @validator('email')
    def email_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('Email cannot be empty')
        return value
    
    
    
class TicketDB(Base):
    __tablename__ = "tickets"
    id =Column(Integer, primary_key=True,index= True,autoincrement=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    priority = Column(Integer)
    category = Column(String)
    assignee_id = Column(Integer) 
    email = Column(String) 