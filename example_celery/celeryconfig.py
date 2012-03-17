#!/usr/bin/env python

"""
Celery Config
"""

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

CELERYD_CONCURRENCY = 4
CELERY_IMPORTS = ['tasks']

CELERY_TASK_RESULT_EXPIRES = 3600
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0

CELERY_DEFAULT_QUEUE = 'python_examples'
CELERY_QUEUES = {
    'python_examples': {
        'binding_key': 'python_examples'
    }
}
