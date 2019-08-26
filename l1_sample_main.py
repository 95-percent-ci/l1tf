# -*- coding: UTF-8 -*-
"""
Main Drive Program
====================
This is sample program to show cases the use of the package.
"""

# importing packages #

import sys as sys
import logging as logging
import numpy as np

import l1tf.helpers as helper
import l1tf.l1 as l1

__author__ = "nitesh@gyandata.com"

LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':

    stored_result = []
    # Getting command line arguments from the user #
    cmd_args = helper.init_cmd_args(sys.argv[1:])

    log_config_file = cmd_args.log_config_file
    data_dir_fp = cmd_args.data_dir
    config_dir_fp = cmd_args.config_dir

    # configure logger if logging information is provided
    if log_config_file:
        helper.config_logger(log_config_file)

    for signal_name, signal_df, run_config in helper.load_data(data_dir_fp, config_dir_fp):
        # converting signal into np.ndarray #
        signal = np.ravel(signal_df.values)
        lamda = run_config["lambda"]
        iter_max = run_config["max_iter"]
        abs_tol = run_config["absolute_tolerance"]
        rel_tol = run_config["relative_tolerance"]
        feas_tol = run_config["feasibility_tolerance"]
        refine = run_config["refine_required"]
        slope_tol = run_config["slope_tolerance"]
        show_progress = run_config["show_progress"]
        LOGGER.info("Initialising l1 trend filter for %s", signal_name)
        trend = l1.l1_trend(signal, lamda, show_progress, iter_max, abs_tol, rel_tol, feas_tol, refine)
        LOGGER.info("Process ended successfully")
