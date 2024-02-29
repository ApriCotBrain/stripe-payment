#!/bin/sh

while ! nc -z db 5432;
    do sleep .5;
    echo "wait database";
done;
    echo "connected to the database";

python manage.py migrate --no-input;
python manage.py collectstatic --no-input;
python manage.py loaddata /app/data/data_dump.json;
gunicorn stripe_payment.wsgi:application --bind 0:8000;
