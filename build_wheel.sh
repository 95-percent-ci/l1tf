#!/bin/bash

########################################################################################################################
#
# This is a quick-use script for building the wheel file from this package
#
# In order to create the wheel file just execute this shell script in the terminal from within the activated
# virtual environment and it will be created in the dist directory
#
# @author   : Nitesh Kumar Sharma
# @version  : 1.0
# @email    : nitesh@gyandata.com
#
########################################################################################################################

echo
echo BUILDING PACKAGE l1tf
echo

# Command to execute
python3 setup.py bdist_wheel