release: python manage.py migrate
web: gunicorn hackernews.wsgi --log-file -
worker: celery -A hackernews worker -B -l INFO