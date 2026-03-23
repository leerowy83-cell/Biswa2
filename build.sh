#!/usr/bin/env bash
# build.sh — runs on Render/Railway during deploy
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_superuser_if_not_exists
