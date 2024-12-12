from sqlalchemy import Column, String, Integer
from .database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
