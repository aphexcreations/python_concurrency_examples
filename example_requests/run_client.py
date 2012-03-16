#!/usr/bin/env python


import gevent

## Be sure to import monkey module and run the patcher
from gevent import monkey
monkey.patch_socket()

import sys
import requests

## SSL urls cannot be loaded asyncronously
URL = 'http://resume.aphexcreations.net/'


def _grab(pid):
    """
    Grab url

    Returns: Bool
    """
    requests.get(URL)
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
