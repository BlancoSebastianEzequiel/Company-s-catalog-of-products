#!/usr/bin/env sh
echo "RUN LINTER NODE ON CLIENT"
cd client
npm test
cd ..
sh scripts/delete_pycache.sh
sh scripts/flake.sh
sh scripts/pylint.sh
echo "UNIT TESTS"
sudo systemctl start mongodb
python -m pytest --cov=server server/tests/