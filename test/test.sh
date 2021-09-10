#!/bin/bash
echo "--- Docker Container ---"
docker ps
echo "--- DB ---"
docker logs project-docker_db_1 --tail=10
echo "--- APP ---"
docker logs project-docker_web_1 --tail=10