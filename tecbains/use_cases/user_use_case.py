from ..utils.util import verify_password
import jwt
import os
from ..db.sqlite.schemas.user_schema import UserSchema
from ..db.sqlite.crud import (
    get_user_by_email, 
    create_user, get_users, 
    get_user_by_id, 
    update_user, 
    delete_user
)
from sqlalchemy.orm import Session


class UserUseCase:
    def __init__(self, dbSession):
        self.db: Session = dbSession

    def login(self, email: str, password: str):
        user = get_user_by_email(self.db, email)
        if not user:
            return None
        if not verify_password(password.encode("utf-8"), user.hashed_password):
            return None

        token = jwt.encode({"userId": user.id}, os.getenv(
            "SECRET"), algorithm="HS256")

        return token

    def signUp(self, email: str, password: str, username: str):
        user = get_user_by_email(self.db, email)
        if user:
            return None

        userSchema = UserSchema(email=email, password=password, name=username)

        user = create_user(self.db, userSchema)
        return user

    def create(self, user: UserSchema):
        user = create_user(self.db, user)
        return user

    def getAllUsers(self, skip: int = 0, limit: int = 100):
        users = get_users(self.db, skip, limit)
        return users

    def getOneUser(self, id: int = 0):
        user = get_user_by_id(self.db, id)
        return user

    def update(self, id: int, user: UserSchema):
        user = update_user(self.db, id, user)
        return user

    def delete(self, id: int):
        user = delete_user(self.db, id)
        return user
