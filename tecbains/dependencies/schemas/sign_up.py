from typing import Optional
from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str