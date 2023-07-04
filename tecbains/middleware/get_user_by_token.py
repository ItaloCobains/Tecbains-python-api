from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from tecbains.api import (
    security
)
import jwt
import os


async def get_user_by_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token: str = credentials.credentials.replace("Bearer ", "")

    if not token:
        raise HTTPException(status_code=401, detail="Invalid Token")

    try:
        payload = jwt.decode(token, os.getenv("SECRET"), algorithms=["HS256"])

        return payload["userId"]
    except:
        raise HTTPException(status_code=401, detail="Invalid Token")
