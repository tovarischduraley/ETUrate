import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT.settings')

app = Celery('RT')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_teacher_marks': {
        'task': 'reviews.tasks.update_teachers_marks',
        'schedule': 10.0
    },
    'update_cathedras_marks': {
        'task': 'reviews.tasks.update_cathedras_marks',
        'schedule': 10.0
    },
}
