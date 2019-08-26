#!/bin/bash

########################################################################################################################
# This is a quick-use script for cleaning the build and dist and .egg-info directories after a failed build
#
# In order to perform the clean just execute this script in a terminal from within the activated virtual environment
#
# @author   : Nitesh Kumar Sharma
# @version  : 1.0
# @email    : nitesh@gyandata.com
#
########################################################################################################################

echo
echo CLEANING BUILD DIRECTORIES
echo

# Command to execute
python3 setup.py clean --all

# Manually remove the dist .egg-info and .eggs directories
rm -rf dist
ls -a1 | grep .egg | xargs rm -rf
ls -a1 | grep .tox | xargs rm -rf

