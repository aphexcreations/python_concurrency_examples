#!/usr/bin/env python

"""
Celery Config
"""

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

CELERYD_CONCURRENCY = 1
CELERY_IMPORTS = ['tasks']

# 10 seconds
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0

CELERY_QUEUES = {
    'gevent_examples.examples': {
        'binding_key': 'gevent_examples.examples'
    }
}
