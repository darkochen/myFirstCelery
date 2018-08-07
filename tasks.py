from __future__ import absolute_import
from test_project_celery.celery_worker import app
import time


@app.task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(3)
    print('long time task finished')
    return x + y
