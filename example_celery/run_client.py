#!/usr/bin/env python

import gevent

## Be sure to import monkey module and run the patcher
from gevent import monkey
monkey.patch_socket()

import sys

from celery.execute import send_task


def _grab(pid):
    """
    Grab task reult

    Returns: Bool
    """
    r = send_task('tasks.example_1',
                  [pid],
                  routing_key='gevent_examples.examples')
    r.get()
    ## If you see the pids printed in random order,
    ## this is indicative of asyncronous loading
    print 'Done:', pid
    return True


def main():
    """
    Main

    Returns: Int
    """
    threads = [gevent.spawn(_grab, i) for i in xrange(1, 20)]
    gevent.joinall(threads)
    return 0


if __name__ == '__main__':
    sys.exit(main())
