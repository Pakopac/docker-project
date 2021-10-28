from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import ping, home, game

# Start app
# app = FastAPI()

# Link templates files
templates = Jinja2Templates(directory="templates")

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(home.router)
    application.include_router(
        game.router, prefix="/games", tags=["games"]
    )
    return application


app = create_application()

# Link static files
app.mount("/static", StaticFiles(directory="static"), name="static")
