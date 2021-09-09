from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import conn

engine = conn.engine
connection = engine.connect()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = MetaData()

print('---------------------')
print('- - - MySQL Docker Container Python connection ok - - - \n')
print(engine.table_names())

# class Game(Base):
#     __tablename__ = 'game'
#     id = Column(Integer, primary_key=True)
#     game_name = Column(String)
#     genre_id = Column(Integer)

# class Genre(Base):
#     __tablename__ = "genre"
#     id = Column(Integer, primary_key=True)  
#     genre_name = Column(String)


Games = Table('game', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('genre_id', Integer, ForeignKey('genre.id')),
    Column('game_name', String(50)),
)

Genres = Table('genre', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('genre_name', String(50)),
)

Publisher = Table('publisher', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('publisher_name', String(50)),
)

Game_Publisher = Table('game_publisher', metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('game_id', Integer),
    Column('publisher_id', Integer),
)

# Platform = Table('platform', metadata,
#     Column('id', Integer, primary_key=True, nullable=False),
#     Column('platform_name', String(50)),
# )

# Game_Platform = Table('game_platform', metadata,
#     Column('game_publisher_id', Integer),
#     Column('platform_id', Integer),
#     Column('release_year', Integer),
# )

metadata.create_all(engine)

games_names = session.query(Games, Genres).filter(Genres.c.id == Games.c.genre_id).all()
# games_names = games_names.filter(Publisher.c.id == Game_Publisher.c.publisher_id).all()
# games_names = session.query(Game).all()
print(games_names)

# games = session.query(Games, Genres, Publisher, Platform, Game_Platform).join(Genres, Games.c.genre_id == Genres.c.id).join(Game_Publisher, Games.c.id == Game_Publisher.c.game_id).join(Publisher, Publisher.c.id == Game_Publisher.c.publisher_id).join(Game_Platform, Game_Publisher.c.id == Game_Platform.c.game_publisher_id).join(Platform, Platform.c.id == Game_Platform.c.platform_id).all()
# games = session.query(Games, Genres, Publisher, Platform, Game_Platform, Game_Publisher).filter(Games.c.genre_id == Genres.c.id, Games.c.id == Game_Publisher.c.game_id, Publisher.c.id == Game_Publisher.c.publisher_id,Game_Publisher.c.id == Game_Platform.c.game_publisher_id, Platform.c.id == Game_Platform.c.platform_id).all()

# print(games)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/list", response_class=HTMLResponse)
async def list(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "games": games_names})
