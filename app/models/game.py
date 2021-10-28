from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Games(Base):
    __tablename__ = 'game'
    
    id = Column(Integer, primary_key=True, nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    game_name = Column(String(50))