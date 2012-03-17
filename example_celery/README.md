Celery Concurrency Example
==========================

This demonstrates an example of concurrent blocking celery task calls.

This assumes you hav RabbitMQ and Redis running correcty. You may need
to edit your `celeryconfig.py` file to fit your needs.

First, you will need to run the celery taskloader with
`./run_taskloader.py`. Next, you can run the demonstration with
`./run_client.py`.

