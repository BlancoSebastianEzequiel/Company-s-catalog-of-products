#!/usr/bin/env bash
echo "RUNNING SERVER"
gunicorn -w 4 -b ${HOST}:${PORT} server.wsgi:app