from sqlalchemy.orm import Session
from .models import User, Post
from .schemas.user_schema import UserSchema
from .schemas.post_schema import PostSchema
import bcrypt


def get_all_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).filter(Post.published == True).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.owner_id == user_id).all()

def create_post(db: Session, post: PostSchema):
    postWithClass = Post(
        title=post.title,
        content=post.content,
        published=post.published,
        owner_id=post.owner_id
    )
    db.add(postWithClass)
    db.commit()
    db.refresh(postWithClass)
    return post

def update_post(db: Session, post_id: int, new_data: PostSchema):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    for field, value in new_data.dict().items():
        if value is not None:
            setattr(db_post, field, value)

    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(db_post)
    db.commit()
    return db_post

def like_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    db_post.likes += 1
    db.commit()
    db.refresh(db_post)
    return db_post

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
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        is_superuser=user.is_superuser
    )
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
