@echo off
:: The destination directory for the .rst files
:: Path is relative to this file
set RST_DEST_DIR=source

:: The source directory of the python code
::  Path is relative to this file
set PYTHON_SRC_DIR=..\l1tf

:: Command to execute
sphinx-apidoc -efPME -o %RST_DEST_DIR% %PYTHON_SRC_DIR%
