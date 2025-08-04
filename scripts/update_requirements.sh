#!/usr/bin/env bash
set -efux

cd "$(dirname "$0")/.."

if [ ! -f src/requirements-to-freeze.txt ]; then
    echo "No requirements to freeze file found!"
    exit 1
fi

if [ -d "virtualenv" ]; then
    rm -rf virtualenv
fi
echo "Creating VENV..."
python3 -m venv virtualenv

set +e
rm src/requirements.txt
set -e
virtualenv/bin/python -m pip install --upgrade pip
virtualenv/bin/pip install -r src/requirements-to-freeze.txt --upgrade
virtualenv/bin/pip freeze | grep -v "pkg-resources"  > src/requirements.txt
rm -rf virtualenv
