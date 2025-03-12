#!/usr/bin/env python

import pandas as pd

from . import util_funcs, logging_funcs

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

def samplesheet_checks(samplesheet_path, log_file):

    """
    Takes in a filepath for a samplesheet and checks to ensure it is valid:
    1) ensures that expected columns are present
    2) ensures that files in samplesheet exist and are of correct format

    If all checks pass, then return the samplesheet as a Pandas DataFrame object.
    """

    if not samplesheet_path.endswith(".csv"):
        logging_funcs.print_to_log(log_file, "error", f"Samplesheet at {samplesheet_path} does not end with '.csv' file extension.")
        logging_funcs.print_to_log(log_file, "error", f"Ensure your samplesheet is in comma-delimited format, then try again.")
    try:
        sample_df = pd.read_csv(samplesheet_path, sep=",")
    except FileNotFoundError:
        logging_funcs.print_to_log(log_file, "error", f"No samplesheet exists at given location {samplesheet_path}.")

    if not sample_df.columns == ["Sample", "R1_File", "R2_File"]:
        logging_funcs.print_to_log(log_file, "error", f"Samplesheet at {samplesheet_path} does not appear to be formatted correctly.")
        logging_funcs.print_to_log(log_file, "error", 
        f"Ensure that your samplesheet is in comma-delimited format and that it contains the header described in the README, then try again.")
    
    return sample_df
