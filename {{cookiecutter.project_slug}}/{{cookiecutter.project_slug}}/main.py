# -*- coding: utf-8 -*-


"""
Provides a commandline interface for {{ cookiecutter.project_slug }}.
"""

import argparse
import os


def main(argv=None):
    parser = argparse.ArgumentParser(description="""
    TODO
    """)
    if argv is None:
        argv = sys.argv[1:]

    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--threads', type=int,
                        default=util.get_default_nthreads())
    args = parser.parse_args(argv)

    # TODO
