On Ubuntu
#################
The following instructions are for Ubuntu 16.04 LTS. For your Ubuntu installation the versions might vary.

Setting up Python
************************************
Ensure that you have python 3.5 or above installed on your machine. In case you do not have it installed
execute the following command in a terminal to install it

.. code-block:: bash

    $ sudo apt-get install python3.5

You can verify your python installation by typing the following command in the terminal

.. code-block:: bash

    $ python3.5 --version

and it should print out the python version as shown below

.. code-block:: bash

    Python 3.5.2

Setting up Pip
************************************
Once it has been installed you should install python's dependency manager pip by executing the following command in a
terminal

.. code-block:: bash

    $ sudo apt-get install python3-pip

As with python you can verify your pip installation by typing

.. code-block:: bash

    $ pip3 --version

and it should print the version of pip that has been installed. Note the python version it points to, it should be
python 3.5 or greater

.. code-block:: bash

    pip 9.0.1 from /usr/local/lib/python3.5/dist-packages (python 3.5)

In some scenarios one might want to upgrade pip itself, in which case execute the following command

.. code-block:: bash

    $ sudo pip3 install --upgrade pip

which will download and upgrade your pip to the latest version

Setting up Virtual-Environment
************************************
Since we want the build to not affect our primary python installation on the machine, a virtual environment needs to be
created. Starting from python 3.5 python on Ubuntu ships with the virtual environment tool which makes our lives easy.

First create a directory which is where we will be performing the build.

.. code-block:: bash

    $ mkdir L1_Trend_Filtering_build

Now move into it

.. code-block:: bash

    $ cd L1_Trend_Filtering_build

Here create a virtual environment called **L1_Trend_Filtering_venv** by executing the following command

.. code-block:: bash

    $ python3.5 -m venv L1_Trend_Filtering_venv

This will create an environment called L1_Trend_Filtering_venv  containing the necessary packages for the virtual environment to
function

We now activate the virtual environment by executing the activate script

.. code-block:: bash

    $ . ./L1_Trend_Filtering_venv/bin/activate

You will now notice that your bash shell displays the name of the virtual environment.
The following steps will be performed from within the virtual environment

Cloning your repository
************************************
In order to clone the repository you need to have git installed on your system. This can be done by executing the
following command

.. code-block:: bash

    $ sudo apt-get install git

We can check if the installation succeeded by executing

.. code-block:: bash

    $ git --version

which will print out your git version

.. code-block:: bash

    git version 2.7.4

Now clone your repository with the following command

.. code-block:: bash

    $ git clone <https-link-to-repository>

where you need to replace <https-link-to-repository> with the link of this repository. This will clone the project and
create a directory containing the project source. At this juncture if you had followed all the steps you should have the
following directories in your L1_Trend_Filtering_build directory

.. code-block:: bash

    L1_Trend_Filtering  L1_Trend_Filtering_venv

Installing dependencies required for building
***********************************************

Navigate into the L1_Trend_Filtering directory. Here you will find a requirements.txt file which contains all the dependencies
required for building the project into a wheel (.whl) file. You have to install these dependencies into the
virtual-environment by executing

.. code-block:: bash

    $ pip3 install -r requirements.txt

This will download the required dependencies from pypi index. Also ensure you have the latest version of setuptools
installed within this virtual-environment by upgrading it

.. code-block:: bash

    $ pip3 install setuptools --upgrade


Building the project
*********************

In the same L1_Trend_Filtering directory, you will also find a build_wheel.sh shell script. Just execute this shell script and
the wheel file will be built for you

.. code-block:: bash

    $ ./build_wheel.sh

This causes a directory called **dist** to be created which contains the final wheel(.whl) file which can then be used to
install this package in other projects

Running tests on the package
*****************************
If you wish to run the test suite on the built package you can use tox which has been integrated into the project.
Just execute the following command

.. code-block:: bash

    $ tox

and it will create the package in an isolated virtual-environment and run the entire test suite. The test report will be
dumped as a html file in the directory **test_report** under the **tests** directory. The coverage data and report will
be dumped as several html files into the directory **coverage_report** under **tests** directory.

Building the documentation
****************************
Navigate into the sphinx_autodoc directory

.. code-block:: bash

    $ cd sphinx_autodoc

Here execute the shell script **create_rst.sh** to create .rst files from the code docstrings. These will be placed
within the source folder.

Once the .rst files have been created execute the following command to create html help files

.. code-block:: bash

    $ make html

The created html files are present in a directory named **html** under a directory called **docs** within the
**sphinx_autodoc** directory

Using the built wheel file in another project
***********************************************
In order to use the wheel file in another project as a dependency, in the project virtual-environment execute the
following command

.. code-block:: bash

    $ pip3 install <path-to-wheel-file>

where you have to replace the <path-to-wheel-file> with the fully qualified path to where you have stored your wheel
file

