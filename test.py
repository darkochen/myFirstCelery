from __future__ import absolute_import
from celery import Celery
import time

app = Celery('test',
             broker='amqp://guest:guest@10.10.89.51:5672//',
             backend='rpc://')

@app.task(acks_late=True, name='cralwer')
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(3)
    print('long time task finished')
    return x + y


if __name__ == '__main__':
    result = longtime_add.delay({'num': 1, 'test': (1,2,3)}, 111 )
    # at this time, our task is not finished, so it will return False
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print('Task finished? ', result.ready())
    print('Task result: ', result.result)
