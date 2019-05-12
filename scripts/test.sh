#!/usr/bin/env sh
sh scripts/delete_pycache.sh
sh scripts/flake.sh
sh scripts/pylint.sh
echo "UNIT TESTS"
sudo systemctl start mongodb
python -m pytest --cov=server