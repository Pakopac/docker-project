from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
import conn

import conn

engine = conn.engine
connection = engine.connect()

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = MetaData()

print('- - - MySQL Docker Container Python connection ok - - - \n')

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
