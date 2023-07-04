from sqlalchemy.orm import Session
from .models import User
from .schemas.user_schema import UserSchema
import bcrypt


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserSchema):
    hashed_password = bcrypt.hashpw(
        user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, new_data: UserSchema):
    db_user = db.query(User).filter(User.id == user_id).first()

    for field, value in new_data.dict().items():
        if value is not None:
            if field == 'password':
                hashed_password = bcrypt.hashpw(
                    value.encode('utf-8'), bcrypt.gensalt())
                setattr(db_user, field, hashed_password.decode('utf-8'))
            else:
                setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user



def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user
