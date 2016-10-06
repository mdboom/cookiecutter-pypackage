# -*- coding: utf-8 -*-


"""
Miscellaneous utility functions.
"""


import os


WIN = (os.name == 'nt')


def get_default_nthreads():  # pragma: no cover
    """
    Return the default number of threads for a given platform.
    """
    import multiprocessing

    if WIN:
        return 1
    else:
        return multiprocessing.cpu_count()
