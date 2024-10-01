from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class WordItem(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    en = Column(String)
    part_of_speech = Column(String)
    ch = Column(String)
