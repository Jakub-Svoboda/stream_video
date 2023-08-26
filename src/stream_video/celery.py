import os

from datetime import timedelta

from celery import Celery


METADATA_PULL_PERIOD = 60


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream_video.settings')

app = Celery('stream_video')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'periodic_task': {
        'task': 'video_manager.tasks.metadata_pull',  
        'schedule': timedelta(seconds=METADATA_PULL_PERIOD),        
    },
}
