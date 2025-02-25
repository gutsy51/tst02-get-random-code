#!/usr/bin/env bash

set -o errexit  # Exit on error

pip install -r requirements.txt

echo "Collecting static files..."
python RandomCode/manage.py collectstatic --noinput
ls -l RandomCode/static/

echo "Migrating database..."
python RandomCode/manage.py migrate
