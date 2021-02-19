#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --username "administrator" --email "admin@example.com" --noinput
echo "
from django.contrib.auth.models import User
usr = User.objects.get(username='administrator')
usr.set_password('supersecretkey!#')
usr.save()
" | python manage.py shell

exec "$@"
