from pydantic import BaseModel
from datetime import datetime

class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    created_at: str
    updated_by: str
    updated_at: str
    
