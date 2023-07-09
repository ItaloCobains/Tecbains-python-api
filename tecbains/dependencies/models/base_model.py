from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

class BaseModel(object):
    last_modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
DeclarativeBase = declarative_base(cls=BaseModel)