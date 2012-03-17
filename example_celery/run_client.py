#!/usr/bin/env python

import time
import sys

from celery.execute import send_task


def _build_task_call(pid):
    """
    Grab task result

    Returns: Bool
    """
    return send_task('tasks.example_1', [pid],
                     routing_key='python_examples')


def _join_all(task_calls, timeout=300):
    """
    Blocks and joins on a set of celery task calls
    """
    out = []
    stats = set(xrange(len(task_calls)))
    while True:
        if len(stats) > 0:
            rem = []
            for i in stats:
                t = task_calls[i]
                if t.ready():
                    if t.successful():
                        d = t.get(timeout=timeout)
                        out.append(d)
                    rem.append(i)
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
    print res
    return 0


if __name__ == '__main__':
    sys.exit(main())
