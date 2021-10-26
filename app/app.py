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

# Connect to db and make session for query
engine = conn.engine
connection = engine.connect()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = MetaData()

print('---------------------')
print('- - - MySQL Docker Container Python connection ok - - - \n')
print(engine.table_names())

# Create sqlAlchemy tables
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

# Query games
games = session.query(Games, Genres).filter(Genres.c.id == Games.c.genre_id).all()

# Start app
app = FastAPI()

# Link static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Link templates files
templates = Jinja2Templates(directory="templates")

# Route '/' Home
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route '/list' List Games
@app.get("/list", response_class=HTMLResponse)
async def list(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "games": games})
