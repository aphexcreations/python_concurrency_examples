#!/usr/bin/env python

"""
Example Celery Tasks
"""

from celery.task import task


@task(ignore_result=False)
def example_1(pid):
    """
    Example 1
    """
    r = ':'.join(['OK', str(pid)])
    print ('TASK', r)
    return r
