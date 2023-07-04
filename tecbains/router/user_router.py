from fastapi import APIRouter, Depends
from ..use_cases.user_use_case import UserUseCase
from ..get_db import get_db
from ..db.sqlite.schemas.user_schema import UserSchema, UserSchemaUpdate
from sqlalchemy.orm import Session

userRouter = APIRouter()

@userRouter.post("/create", tags=["user"], summary="Create User")
def create(user: UserSchema, db: Session = Depends(get_db)):
        
        userCase = UserUseCase(db)
        
        user = userCase.create(user)
        
        if not user:
            return None
        
        return user

@userRouter.post("/signup", tags=["user"], summary="Sign Up")
def signup(email: str, password: str, username: str, db: Session = Depends(get_db)):
    
    userCase = UserUseCase(db)
    
    user = userCase.signUp(email, password, username)
    
    if not user:
        return None
    
    return user

@userRouter.post("/login", tags=["user"], summary="Login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    
    loginCase = UserUseCase(db)
    
    token = loginCase.login(email, password)
    
    if not token:
        return None

    return {"token": token, "token_type": "bearer"}

@userRouter.get("/listAll", tags=["user"], summary="List All Users")
def getAllUsers(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    
    userCase = UserUseCase(db)
    
    users = userCase.getAllUsers(skip=skip, limit=limit)
    
    
    return users

@userRouter.get("/list/{id}", tags=["user"], summary="List User By Id")
def getOneUser(db: Session = Depends(get_db), id: int = 0):
    
    userCase = UserUseCase(db)
    
    user = userCase.getOneUser(id)
    
    if not user:
        return None
    
    return user

@userRouter.put("/update/{id}", tags=["user"], summary="Update User")
def update(id: int, user: UserSchemaUpdate, db: Session = Depends(get_db)):
    
    userCase = UserUseCase(db)
    
    user = userCase.update(id, user)
    
    if not user:
        return None
    
    return user

@userRouter.delete("/delete/{id}", tags=["user"], summary="Delete user")
def delete(id: int, db: Session = Depends(get_db)):
    
    userCase = UserUseCase(db)
    
    user = userCase.delete(id)
    
    if not user:
        return None
    
    return user