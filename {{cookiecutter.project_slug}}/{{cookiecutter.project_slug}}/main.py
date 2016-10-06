# -*- coding: utf-8 -*-


"""
Provides a commandline interface for {{ cookiecutter.project_slug }}.
"""

import argparse
import sys


from . import util


parser = argparse.ArgumentParser(description="""
TODO
""")
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--threads', type=int,
                    default=util.get_default_nthreads())


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = parser.parse_args(argv)

    # TODO
