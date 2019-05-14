#!/usr/bin/env sh
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
echo "BUILDING DOCKER IMAGE"
#docker build -t server-img .
docker-compose up --build
echo "LAUNCHING DOCKER CONTAINER"
sh scripts/run_docker.sh