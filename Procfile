web: gunicorn analytics_api.wsgi --log-file -
# web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput