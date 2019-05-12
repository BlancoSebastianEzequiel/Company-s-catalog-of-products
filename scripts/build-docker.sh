#!/usr/bin/env sh
echo "BUILDING DOCKER IMAGE"
docker build -t server-img .
echo "LAUNCHING DOCKER CONTAINER"
sh scripts/run.sh