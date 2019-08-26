# -*- coding: UTF-8 -*-
"""
Commandline Initialization
###########################

It creates an object that parses commandline strings into to python objects with necessary and optional arguments
specified by the user. Location of the Data and it's required regularization parameter is necessary arguments while
Logger configuration by default will not be changed, but it can be changed by specifying a proper json file.
This module aids in running quick_use.py file.

"""
import argparse
import json
import logging
import logging.config
import os
import pathlib

import numpy as np
import pandas as pd

import l1tf.help_msg as help_msg

__author__ = "nitesh@gyandata.com"

LOGGER = logging.getLogger(__name__)

_REQ_GROUP_ARG = " Necessary Arguments"
_OPT_ARG = "Optional Argument"


def init_cmd_args(args):
    """
    Initialize the python command line argument parser. Output will have a parser with attributes which can be easily
    readable python objects

    :param args: The list of arguments
    :type args: list

    :return: An initialized argument parser
    :rtype: :class:`argparse.ArgumentParser`
    """

    # argparse initialisation
    parser = argparse.ArgumentParser(description=help_msg.DESCRIPTION)

    # adding necessary arguments in a group #
    req_arguments = parser.add_argument_group(title=_REQ_GROUP_ARG, description='These are necessary arguments')
    req_arguments.add_argument("--data_dir", type=str, required=True, help=help_msg.DATALOC)
    req_arguments.add_argument("--config_dir", type=str, required=True, help=help_msg.DATACONF)

    # optional arguments #
    parser.add_argument("--log_config_file", type=str, required=False, help=_OPT_ARG)

    # Parsing the arguments
    return parser.parse_args(args)


def config_logger(log_file_path):
    """
    configures logging option using the provided .json file

    :param log_file_path: The fully qualified path of the logger's json configuration file.
    :type log_file_path: string

    :raises FileNotFoundError: if the configuration file cannot be found

    :return: Nothing
    :rtype: None
    """

    if not os.path.exists(log_file_path):
        raise FileNotFoundError("Configuration File could not be found at".format(**{"path": log_file_path}))

    with open(log_file_path, 'r') as log_file:
        log_opts_dict = json.load(log_file)
        logging.config.dictConfig(log_opts_dict)
        LOGGER.info("Logging configuration successfully initialized")


def load_data(data_dir_fp, config_dir_fp):
    """
    Loads the data
    :param data_dir_fp: The path to directory containing the input signal
    :type data_dir_fp: :class:`str`

    :param config_dir_fp: The path to directory containing the configuration files.
    :type config_dir_fp: :class:`str`

    :return: A python generator of tuples, where in each tuple

            * first element is the input signal id as a :class:`str`
            * second element is the input signal data as a :class:`pandas.DataFrame`
            * third element is the configuration as a :class:`dict`

    :rtype: :class:`typing.Generator`

    :raises EnvironmentError: If

                                * input signal data directory does not exist in the given path.
                                * configuration directory does not exist at a given path.

    :raises TypeError: if

                        * data_dir_fp is not a string.
                        * config_dir_fp is not a string.



    """

    if not issubclass(type(data_dir_fp), str):
        raise TypeError(" Input signal path must be a string!")

    if not issubclass(type(config_dir_fp), str):
        raise TypeError(" Path to configuration file must be a string!")

    if not os.path.exists(data_dir_fp):
        raise EnvironmentError(" Given path for input signal does not exist in the directory!")

    if not os.path.exists(config_dir_fp):
        raise EnvironmentError(" Given path for configuration does not exist in the directory!")

    # Get list of all configuration. Each configuration corresponding one particular signal in directory
    config_fullpath = [str(os.path.join(config_dir_fp, filename)) for filename in os.listdir(config_dir_fp) if
                       ".json" in str(filename)]

    # iterating over configuration file paths

    for _, config_fp in enumerate(config_fullpath):

        # getting filename from path
        file_name = pathlib.PurePath(config_fp)

        # getting filename without its extension
        file_name_no_ext = str(file_name.stem)

        # appending signal data file extension
        data_file_name = file_name_no_ext + ".csv"

        # constructing the full path
        data_fp = os.path.join(data_dir_fp, data_file_name)

        LOGGER.info("file being read is %s", file_name_no_ext)

        # checking if the path exists or not
        if not os.path.exists(data_fp):
            # If not log the error and continue with operation #
            LOGGER.error(" %s does not exist in the directory", file_name_no_ext)
            continue
        else:
            # reading configuration file #
            with open(config_fp, 'r') as config_file:
                # loading in json
                config = json.load(config_file)

            LOGGER.info(" parameters of l1 trend for %s is being read", file_name_no_ext)

            # loading data files #
            with open(data_fp, 'r') as data_file:

                data_frame = pd.read_csv(data_file, encoding="utf-8", dtype=np.float64)

            yield file_name_no_ext, data_frame, config
