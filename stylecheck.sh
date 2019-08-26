#!/bin/bash

########################################################################################################################
# This is a quick-use script for performing style checks on the package
#
# In order to perform the check just execute this script in a terminal from within the activated virtual environment
# The results of the linting process will be written to file named linter_output.txt
#
# @author   : Ganesh Sankaran
# @version  : 1.0
#
########################################################################################################################

echo
echo RUNNING LINTER ON PACKAGE CODE
echo

# Commands to execute
pylint l1tf --rcfile=pylintrc.ini > linter_output.txt





