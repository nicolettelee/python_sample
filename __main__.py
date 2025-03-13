##!/usr/bin/env python

import argparse
import time

from .scripts import logging_funcs, preprocessing_funcs

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
    print(samplesheet_df)
    
    # Finish script
    end_timer = time.perf_counter()
    logging_funcs.print_to_log(log_file, "info", "Ending script.")
    logging_funcs.print_to_log(log_file, "info", f"Time elapsed: {end_timer - start_timer:0.4f} seconds")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--samplesheet", action="store", type=str, required=True,
                        help="Path to samplesheet in string format.")
    parser.add_argument("--outdir", action="store", type=str, required=True,
                        help="Path to outdirectory in string format.")
    
    ######
    # Docker-specific commands
    ######

    parser.add_argument("--platform", action="store", required=False,
                        type=str, default="linux/amd64",
                        help="String describing architecture types. Default: linux/amd64")
    
    options = parser.parse_args()
    main(options)