#!/usr/bin/env bash
echo "RUNNING SERVER"
gunicorn -w 4 -b 0.0.0.0:4000 server.wsgi:app