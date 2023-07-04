from pydantic import Field, BaseModel, EmailStr
from typing import Optional


class PostSchema(BaseModel):
    title: str
    content: str
    published: bool
    owner_id: int
    likes: int

    class Config:
        schema_extra = {
            "example": {
                "title": "Post Title",
                "content": "Post Content",
                "published": False,
                "owner_id": 1,
                "likes": 0
            }
        }


class PostSchemaUpdate(PostSchema):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    owner_id: Optional[int] = None
    likes: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "Post Title",
                "content": "Post Content",
                "published": False,
                "owner_id": 1,
                "likes": 0
            }
        }
