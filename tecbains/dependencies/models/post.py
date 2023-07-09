from sqlalchemy import Boolean, String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from tecbains.dependencies.models.base_model import DeclarativeBase

class Post(DeclarativeBase):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    
    title = Column(String(50), nullable=False, index=True)
    content = Column(String(500), nullable=False, index=True)
    published = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    likes = Column(Integer, default=0)
    
    author = relationship("User", back_populates="posts")