## Install celery first

``` pip install -r requirements.txt ```

## How to start the consumer

 > outside your project directory execute the following command:

   ```celery -A test.app worker --loglevel=info```

## How to execute provider

 > outside your project directory execute the following command:

 ```python -m test_project_celery.run_tasks```