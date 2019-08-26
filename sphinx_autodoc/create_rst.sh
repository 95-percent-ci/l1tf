#!/bin/bash

########################################################################################################################
# This is a quick-use script for creating .rst files which are read by Sphinx to create the html documentation.
#
# In order to create the .rst files just execute this shell script and they will automatically be created under the
# source directory within the sphinx_autodoc directory
#
# @author   : Nitesh Kumar Sharma
# @version  : 1.0
#
########################################################################################################################
# The destination directory for the .rst files
# Path is relative to this file
RST_DEST_DIR="source"

# The source directory of the python code
# Path is relative to this file
PYTHON_SRC_DIR="../l1tf"

# Command to execute
sphinx-apidoc -efPME -o $RST_DEST_DIR $PYTHON_SRC_DIR