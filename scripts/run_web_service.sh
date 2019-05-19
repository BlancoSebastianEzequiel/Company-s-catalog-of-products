#!/usr/bin/env bash
trap 'kill %1; kill %2' SIGINT
sh scripts/wsgi.sh &
sh scripts/run_client.sh