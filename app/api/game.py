from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base

from models.game import Games
from models.genre import Genres

router = APIRouter()

templates = Jinja2Templates(directory="templates")

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

metadata.create_all(engine)

# Query games
games = session.query(Games, Genres).filter(Genres.id == Games.genre_id).all()

@router.get("/all", response_class=HTMLResponse)
async def all(request: Request):
    return templates.TemplateResponse("list.html", {"request": request, "games": games})