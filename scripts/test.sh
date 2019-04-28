#!/usr/bin/env sh
echo "DELETING ALL __PYCACHE__ DIRECTORIES"
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
sudo rm -r .pytest_cache
echo "TESTING FLAKE 8"
flake8 server/
echo "TESTING LINTER"
pylint server/
echo "UNIT TESTS"
sudo systemctl start mongodb
python -m pytest --cov=server
echo "DELETING ALL __PYCACHE__ DIRECTORIES"
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
sudo rm -r .pytest_cache