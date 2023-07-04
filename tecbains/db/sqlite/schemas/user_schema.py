from pydantic import Field, BaseModel, EmailStr
from typing import List, Optional


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_superuser: bool = False

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "JohnDoe@gmail.com",
                "password": "password",
                "is_superuser": False,
            }
        }


class UserSchemaUpdate(UserSchema):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_superuser: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "JohnDoe@gmail.com",
                "password": "password",
                "is_superuser": False,
            }
        }
