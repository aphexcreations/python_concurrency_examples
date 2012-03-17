#!/usr/bin/env python

"""
Example Celery Tasks
"""


import random
import time

from celery.task import task


@task(ignore_result=False)
def example_1(pid):
    """
    Example 1
    """
    time.sleep(random.randint(1, 3))
    r = ':'.join(['OK', str(pid)])
    print ('TASK', r)
    return r
