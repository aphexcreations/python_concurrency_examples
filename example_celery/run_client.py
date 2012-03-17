#!/usr/bin/env python

import logging
import time
import sys

from celery.execute import send_task
from celery.exceptions import TimeoutError

logger = logging.getLogger('example_celery')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def _build_task_call(pid):
    """
    Grab task result

    Returns: Bool
    """
    return send_task('tasks.example_1', [pid],
                     routing_key='python_examples')


def _join_all(task_calls, task_timeout=300, join_timeout=600):
    """
    Blocks and joins on a set of celery task calls
    """
    out = []
    stats = set(xrange(len(task_calls)))
    start = time.time()
    while True:
        if len(stats) > 0:
            rem = []
            is_join_timeout = False
            for i in stats:
                diff = time.time() - start
                if diff >= join_timeout:
                    logger.error('Join timed out.')
                    is_join_timeout = True
                    break
                t = task_calls[i]
                if t.ready():
                    if t.successful():
                        try:
                            d = t.get(timeout=task_timeout)
                        except TimeoutError:
                            logger.error('Task wait timed out.')
                        else:
                            out.append(d)
                    rem.append(i)
            if is_join_timeout:
                break
            for r in rem:
                stats.remove(r)
            if len(stats) > 0:
                time.sleep(.01)
        else:
            break
    return out


def main():
    """
    Main

    Returns: Int
    """
    task_calls = [_build_task_call(i) for i in xrange(1, 20)]
    res = _join_all(task_calls)
    logger.info(res)
    return 0


if __name__ == '__main__':
    sys.exit(main())
