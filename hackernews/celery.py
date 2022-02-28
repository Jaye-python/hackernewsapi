import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackernews.settings')

app = Celery('hackernews')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    
    'sync-db-five-minutes': {
        
        'task': 'sync_db_task',

        # Schedule      
        'schedule': 300.0,

        # arguments (we have none for syncing) 
        # 'args': ("Hello",) 
    },}