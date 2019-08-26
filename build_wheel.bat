@ECHO off
REM ####################################################################################################################
REM #
REM #
REM #   Batch file for creating the wheel file from the setup script
REM #   Just execute this batch script through the windows command terminal from the activated virtual environment
REM #   The package will be created in the dist directory
REM #
REM #   @ author  : Nitesh Kumar Sharma
REM #   @ version : 1.0
REM #   @email    : nitesh@gyandata.com
REM #
REM #
REM #
REM ####################################################################################################################
ECHO
ECHO BUILDING PACKAGE FCLOADOPT
ECHO

REM Command to execute
py setup.py bdist_wheel