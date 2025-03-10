#!/usr/bin/env python

from . import util_funcs

def setup_outdirectory(outdir):

    """
    This function sets up folders that are required in the outdirectory.

    Inputs:
        outdir: String representing desired location of outdirectory.
        log_file: Python Logger object.
    """
    folders_to_create = ["logs"]
    for folder in folders_to_create:
        util_funcs.create_dir(f"{outdir}/{folder}")
