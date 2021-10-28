from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Genres(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, nullable=False)
    genre_name = Column(String(50))
