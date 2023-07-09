from typing import List
from pydantic import BaseModel

from tecbains.dependencies.schemas.post import PostSchema


class UserSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    admin: bool
    posts: List[PostSchema] = []
    
    
    
    class Config:
        orm_mode = True