from sqlalchemy import String, Column, Integer, Boolean
from sqlalchemy.orm import relationship

from tecbains.dependencies.authentication import pwd_context
from tecbains.dependencies.models.base_model import DeclarativeBase

class User(DeclarativeBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password_hash = Column(String(128), nullable=False)
    admin = Column(Boolean, default=False)
    posts = relationship("Post", back_populates="author")
    
    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password_hash)
    
    def get_password_hash(self, password):
        self.password_hash =  pwd_context.hash(password)
    
    def __init__(self, id=None, first_name=None, last_name=None, email=None, password=None, admin=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.admin = admin
    
        if password:
            self.get_password_hash(password)
        