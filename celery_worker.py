from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://guest:guest@10.10.89.51:5672//',
             backend='rpc://',
             include=['test_project_celery.tasks'])
