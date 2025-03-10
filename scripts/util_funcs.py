#!/usr/bin/env python

import os

from . import logging_funcs

def create_dir(filepath):

    """
    Create directory if it does not exist.

    Inputs:
        filepath: String representing location of directory to be creating.
        log_file: Python Logger object.
    """

    if not os.path.exists(filepath):
        try:
            os.makedirs(filepath)
        except:
            print(f"Issue with creating directory at {filepath}, exiting.")