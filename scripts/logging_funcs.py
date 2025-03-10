#!/usr/bin/env python

import logging

def create_log(filepath):

    """
    This function instantiates a Python Logger object at the specified location.
    
    Input:
        filepath: String representing desired location of log file
    """
    logging.basicConfig(filename=filepath, format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)

def print_to_log(filepath, log_type, output, **kwargs):
    
    """
    This function logs messages to a Python log file.
    """

    log_obj = logging.getLogger(filepath)

    if log_type == "info":
        print(output)
        log_obj.info(output)
    elif log_type == "warning":
        print(output)
        log_obj.warning(output)
    elif log_type == "error":
        log_obj.error(output)
        if "error_type" in kwargs:
            if kwargs["error_type"] == "name":
                raise NameError(output)
            if kwargs["error_type"] == "value":
                raise ValueError(output)
        else:
            raise Exception(output)
    elif log_type == "exception":
        print(output)