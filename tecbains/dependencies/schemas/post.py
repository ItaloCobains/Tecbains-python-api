from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    published: bool
    author_id: int
    likes: int
    
    class Config: 
        orm_mode = True