@echo off
:: Quick use script for building the wheel file from this package
:: Just execute this script from the virtualenv terminal and the wheel file
:: will be created in the dist directory
py setup.py clean --all


rmdir /s /q dist
rmdir /s /q fcloadopt.egg-info