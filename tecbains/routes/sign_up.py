from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from tecbains.dependencies.database import get_db 
from tecbains.dependencies import schemas, models

router = APIRouter(
    prefix="/sign-up",
    tags=["Users"],
    responses={404: {"description" : "Not found"}}
)

@router.post("")
def sign_up(
    request: schemas.SignUpSchema,
    db: Session = Depends(get_db)
):
    user = models.User(
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        password=request.password
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return schemas.UserSchema.from_orm(user)