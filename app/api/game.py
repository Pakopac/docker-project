from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import *
from sqlalchemy.dialects.mysql import MEDIUMBLOB, MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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

print("---------------------")
print("- - - MySQL Docker Container Python connection ok - - - \n")

metadata.create_all(engine)

# Query games
games = session.query(Games, Genres).filter(Genres.id == Games.genre_id).all()


@router.get("/all", response_class=HTMLResponse)
async def all(request: Request):
    return templates.TemplateResponse(
        "games/list.html", {"request": request, "games": games}
    )


@router.get("/{id}/", response_class=HTMLResponse)
async def one(id: int, request: Request):
    session.rollback()
    game = (
        session.query(Games, Genres)
        .filter(Games.id == id)
        .filter(Genres.id == Games.genre_id)
        .first()
    )
    if game:
        return templates.TemplateResponse(
            "games/game.html", {"request": request, "game": game}
        )
    else:
        raise HTTPException(status_code=404, detail="Item not found")
