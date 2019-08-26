Usage
======

Quick use scripts
********************

Usage of this package is relatively simple using the quick use initialization scripts which are provided as part of the
package.

A sample python script has been provided in the repository titled **l1_sample_main.py** along with sample data in
directory **sample_data**.

We shall delve into this file in detail in this section to understand how to use the package through this code snippet.

.. code-block:: python

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
            LOGGER.info("Initialising l1 trend filter for %s", signal_name)
            trend = l1.l1_trend(signal, lamda, iter_max, abs_tol, rel_tol, feas_tol, refine)
            LOGGER.info("Process ended successfully")



Initialization of helper functions
*****************************************
We first start off by initializing the command line arguments using one of the quick-use initialization function present
in the :py:mod:`helpers` module. This allows is to do two things,

* Make the Python script display a help menu, which will immensely helpful while deploying the package in system only
  have command line interface.
* Allow command line arguments to be passed to this script

For example if one were to request for a help message like so

.. code-block:: bash

   $python3 l1_sample_main.py --help

the following help message will be displayed

.. code-block:: bash

    usage: l1_sample_main.py [-h] --data_dir DATA_DIR --config_dir CONFIG_DIR
                         [--log_config_file LOG_CONFIG_FILE]

    Demonstrates quick use of the package

    optional arguments:
      -h, --help            show this help message and exit
      --log_config_file LOG_CONFIG_FILE
                            Optional Argument

     Necessary Arguments:
      These are necessary arguments

      --data_dir DATA_DIR   Specify path to directory where input signal is
                            located
      --config_dir CONFIG_DIR
                            Specify path to directory where lambda
                            (Regularization) and solver settings are stored


It provides crucial information about arguments to be passed. For the program to run successfully it needs 2
necessary arguments: 1) path to directory where signal is stored in a .csv file and 2) path to directory where
regularization parameter :math:`\lambda` and solver options are stored in .json file.

An example of call code would look like this

.. code-block:: bash

    $ python3 l1_sample_main.py --data_dir="/home/gdpl_012/PycharmProjects/L1_Trend_Filtering/sample_data" --config_dir="/home/gdpl_012/PycharmProjects/L1_Trend_Filtering/sample_config"


Logger configuration .json
*****************************************
If users wish to have fine-grained control over their logging they can also pass the optional **log_config_file** argument
as a path to a logging configuration json file. For example in the json file provided below

.. code-block:: json

    {
      "version"                 : 1,
      "disable_existing_loggers": false,
      "formatters"              : {
        "package_formatter": {
          "format": "[%(levelname)s] - [%(name)s] : %(message)s"
        }
      },
      "handlers"                : {
        "console": {
          "class"    : "logging.StreamHandler",
          "level"    : "DEBUG",
          "formatter": "package_formatter"
        }
      },
      "loggers"                 : {
        "l1tf.helpers": {
          "level"   : "DEBUG",
          "propagate": false,
          "handlers": [
            "console"
          ]
        }
      },
      "root"                    : {
        "level"   : "INFO",
        "handlers": [
          "console"
        ]
      }
    }

sets level for the logger present in the :py:mod:`l1tf.helpers` module has been set to level DEBUG.
For a complete guide on python logging framework refer to the official documentation at
`link <https://docs.python.org/3/library/logging.html>`_.


Results
*********
The sample script provided scans automatically for the input signals files and required configuration in the specified
directory. Algorithm is executed for each input signal and it status is displayed simultaneously.

Python :py:mod:`dict` is returned for each signal. The dictionary has the following keys

* segment_result : Segment wise result after :math:`l1` trend filtering are stored in a list. It contains segment wise
  extracted results corresponding to a linear segment.
* overall_mse : Mean square error between the signal and the :math:`l1` trend fit.


