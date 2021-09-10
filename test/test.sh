#!/bin/bash
echo "--- Docker Container ---"
docker ps
echo "--- DB ---"
docker logs video_games_app_1 --tail=10
echo "--- APP ---"
docker logs video_games_db_1 --tail=10