web: gunicorn config.wsgi:application
worker: celery worker --app=direct_mail.taskapp --loglevel=info
