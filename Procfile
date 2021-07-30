release: python manage.py migrate
web: gunicorn myproject.wsgi --log-file -
worker: celery -A hackernews worker -B -l INFO