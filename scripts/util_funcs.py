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

def run_docker(image_tag, platform, vols_dict, args_dict, log_file, **kwargs):

    """
    Executes system command for running a Docker image.
    Includes parameter for specifying architecture:
        - use linux/amd64 if running locally from Mac
        - use linux/arm64 if running on Linux-based distro
    """

    cmd = f"docker run --platform {platform}"

    # mount volumes
    for local_path, mount_path in vols_dict.items():
        cmd += f" -v {local_path}:{mount_path}"
    
    # add tag
    cmd += f" -t {image_tag}"

    # if included, add command for invocation
    if "invoke_cmd" in kwargs:
        cmd += f" {kwargs['invoke_cmd']}"
    
    # add parameters

    for param, arg_val in args_dict:
        cmd += f" {param} {arg_val}"
    
    logging_funcs.print_to_log(log_file, "info", f"Running Docker for image {image_tag}:")
    logging_funcs.print_to_log(log_file, "info", cmd)