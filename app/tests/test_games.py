import json
import app

import pytest

def test_all_games(test_app):
    response = test_app.get("/games/all")
    assert response.status_code == 200

def test_game(test_app):
    response = test_app.get(f"/games/1/")
    assert response.status_code == 200

def test_game_incorrect(test_app):
   response = test_app.get("/games/999/")
   assert response.status_code == 404

    