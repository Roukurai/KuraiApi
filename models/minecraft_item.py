from pydantic import BaseModel,validator
from sqlalchemy import Column,String,Integer
from modules.database import Base

class Item(BaseModel):
    id: int
    name: str
    quantity: int 
    inventory_id: int
    mod_id: str
    
    
    @validator('quantity')
    def quantity_non_negative(cls,value):
        if value < 0:
            raise ValueError('Quantity must be a non-negative number')
        return value
    
    @validator('name')
    def name_non_empty(cls,value):
        if not value or not value.strip():
            raise ValueError('Name cannot be empty')
        return value
            
    @validator('mod_id')
    def mod_id_must_be_non_empty(cls, value):
        if not value or not value.strip():
            raise ValueError('Mod ID cannot be empty')
        return value


class ItemDB(Base):
    __tablename__ = "minecraft_items"
    id =Column(Integer, primary_key=True,index= True)
    name = Column(String,index=True)
    quantity = Column(Integer)
    inventory_id = Column(Integer)
    mod_id = Column(String)
