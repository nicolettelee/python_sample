##!/usr/bin/env python

import argparse
import time

from .scripts import logging_funcs, preprocessing_funcs, util_funcs

def main(options):

    # Start timer, set up directories, and create log
    start_timer = time.perf_counter()
    time_str = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    
    preprocessing_funcs.setup_outdirectory(options.outdir)
    log_file = f"{options.outdir}/logs/{time_str}.log"
    logging_funcs.create_log(log_file)

    # Begin script
    logging_funcs.print_to_log(log_file, "info", "Beginning script.")

    # samplesheet checks
    samplesheet_df = preprocessing_funcs.samplesheet_checks(options.samplesheet, log_file)
    samples = list(samplesheet_df["Sample"])

    logging_funcs.print_to_log(log_file, "info", f"Samples to be processed:")
    logging_funcs.print_to_log(log_file, "info", samples)

    ####################
    # Step 1. FastQC on raw reads
    ####################

    logging_funcs.print_to_log(log_file, "info", f"Starting Step 1: FastQC on raw reads.")

    # not parallelized for now
    # construct commands
    for sample in samples:
        sample_row = samplesheet_df.loc[samplesheet_df["Sample"] == sample]
        R1_read = sample_row["R1_File"][0]
        R2_read = sample_row["R2_File"][0]
    
        fastqc_image_tag = options.fastqc_img
        platform = options.platform

        # construct dictionary for inputs & outputs
        vols_dict = {}

        # construct dictionary for general arguments
        args_dict = {}

        util_funcs.run_docker(fastqc_image_tag, platform, vols_dict, args_dict, log_file, invoke_cmd="fastqc")

    ####################
    # Step 2. Trim - implement later
    ####################

    ####################
    # Step 3. FastQC on trimmed reads - implement later
    ####################

    ####################
    # Step 4. Align
    ####################
    
    # Finish script
    end_timer = time.perf_counter()
    logging_funcs.print_to_log(log_file, "info", "Ending script.")
    logging_funcs.print_to_log(log_file, "info", f"Time elapsed: {end_timer - start_timer:0.4f} seconds")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    ####################
    # General parameters
    ####################

    parser.add_argument("--samplesheet", action="store", type=str, required=True,
                        help="Path to samplesheet in string format.")
    parser.add_argument("--outdir", action="store", type=str, required=True,
                        help="Path to outdirectory in string format.")
    
    ####################
    # Docker-specific parameters
    ####################

    parser.add_argument("--platform", action="store", required=False,
                        type=str, default="linux/amd64",
                        help="String describing architecture type. Default: linux/amd64")

    ####################
    # Step 1-specific parameters
    ####################

    parser.add_argument("--fastqc_img", action="store", required=False,
                        type=str, default="biocontainers/fastqc:v0.11.9_cv8",
                        help="String in the format of [repository]:[tag] describing image to use for FastQC.s")
    
    options = parser.parse_args()
    main(options)