#!/usr/bin/env sh
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
echo "BUILDING DOCKER IMAGE"
docker build -t client-img . -f client/Dockerfile
docker build -t server-img .
echo "LAUNCHING DOCKER CONTAINER"
sh scripts/run_docker.sh