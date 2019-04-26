#!/usr/bin/env sh

echo "TESTING FLAKE 8"
flake8 server/
echo "TESTING LINTER"
pylint server/