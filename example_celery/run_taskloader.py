#!/usr/bin/env python

"""
Celeryd taskloader
"""

import os
import os.path
import sys

from celery.bin import celeryd

dname = os.path.dirname(__file__)
sys.path.append(os.path.realpath(os.path.join(dname, '../')))
os.chdir(os.path.realpath(dname))


def main():
    """
    Runs Celeryd
    """
    if not os.path.exists(os.path.join(dname, 'celeryconfig.py')):
        print "celeryconfig.py file does not exist!. You must symlink it!"
        return 1
    else:
        sys.argv.append('--loglevel=INFO')
        celeryd.main()
        return 0


if __name__ == '__main__':
    sys.exit(main())
