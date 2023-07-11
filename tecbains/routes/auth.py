from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from tecbains.dependencies import models, schemas
from tecbains.dependencies.database import get_db
from tecbains.dependencies.authentication import (
    jwt_methods
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}}
)

@router.post("", status_code=status.HTTP_202_ACCEPTED)
async def authentication(body: schemas.AuthSchema, db:Session = Depends(get_db)):
    email = body.email
    password = body.password
    
    user: models.User = db.query(models.User).filter(models.User.email == email).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    if not user.verify_password(password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    
    jwt_token_payload = jwt_methods.sign_jwt(str(user.id))
    
    return jwt_token_payload