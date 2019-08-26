# -*- coding: UTF-8 -*-
"""
Module contains the setup script for packaging this library
"""
import os as os

import setuptools as setuptools

__author__ = "nitesh@gyandata.com"

# The package name
package_name = "l1tf"

# The package version
package_version = "1.0.0"

# The package authors
package_authors = "Nitesh kumar sharma"

# The package author emails
package_author_emails = "nitesh@gyandata.com"

# Short description of the package
short_description = "L1 trend filtering"

# Long description of the package
here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md')) as readme:
    long_description = readme.read()

# Classifiers of the package
package_classifiers = [

    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 3 - Alpha",

    # Indicate who your project is intended for
    "Intended Audience :: Developers, Analysts",
    "Topic :: Diagnostics :: Algorithm",

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    "Programming Language :: Python :: 3.6.8",

]

# The minimum required version of python on which the package is expected to work
python_requires = ">=3.5"

# Keywords associated with the project
package_keywords = "l1 trend filtering"

# Packages to exclude
exclude_from_package = ["sphinx_autodoc*", "tests*"]

# The list of files that make up the package itself
package_files = setuptools.find_packages(exclude=exclude_from_package)

# Package license
package_license = "Copyright GyanData Pvt. Ltd. 2018"

# Package dependencies (These will be installed as part of package installation
dependencies = [
    "numpy >=1.15.4",
    "scipy >=1.1.0",
    "pandas >=0.23.4",
    "cvxopt >=1.2.3"

]

# Setup requirements/dependencies
setup_dependencies = ["pytest-runner"]

# Test requirements/dependencies
test_dependencies = ["pytest"]

setuptools.setup(
    name=package_name,
    version=package_version,
    author=package_authors,
    author_email=package_author_emails,
    description=short_description,
    long_description=long_description,
    keywords=package_keywords,
    python_requires=python_requires,
    install_requires=dependencies,
    packages=package_files,
    license=package_license,
    setup_requires=setup_dependencies,
    tests_require=test_dependencies
)
