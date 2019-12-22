#!/bin/sh

echo "waiting for mongo..."

while ! nc -z db 27017; do
  sleep 0.1
done

echo "mongo started"

python manage.py runserver
