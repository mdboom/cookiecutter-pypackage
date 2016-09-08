.. highlight:: shell

============
Installation
============


Stable release
--------------

* TODO when a release has been made

From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from its git repository::

   git clone TODO

The easiest way to install the dependencies is with `Anaconda
<https://www.continuum.io/anaconda-overview>`__ or `Miniconda
<http://conda.pydata.org/miniconda.html>`__.  Once Anaconda or
Miniconda is installed, run the following to create an environment for
running ``{{ cookiecutter.project_slug }}``.

::

   conda env create -n {{ cookiecutter.project_slug }} -f conda-environment.yml

If you wish to develop ``{{ cookiecutter.project_slug }}``, you should instead install all of the
development dependencies as well::

   conda env create -n {{ cookiecutter.project_slug }} -f conda-environment-dev.yml

Then activate the new environment::

   # On Linux and Mac OSX:
   source activate {{ cookiecutter.project_slug }}

   # On Windows
   activate {{ cookiecutter.project_slug }}

Then install this package from source using::

   pip install .

Running tests
-------------

::

   py.test


To generate code coverage reports::

  py.test --cov
  coverage html

and then open ``htmlcov/index.html``.

Building a conda package
------------------------

::

   conda build conda-recipe

The location of the package depends on your operating system and will displayed in the
output.

Creating a standalone Windows EXE
---------------------------------

Prerequisites
`````````````

Install `miniconda <http://conda.pydata.org/miniconda.html>`__.

Open a command prompt.  (Press ``F2``, type ``cmd.exe`` and press OK).

Install git::

  conda install git

Checkout ``{{ cookiecutter.project_slug }}``:

  TODO

Building the EXE
````````````````

From a command prompt, change into the ``{{ cookiecutter.project_slug }}`` source code directory.

Create a new Conda environment just for building the EXE::

  conda env create -n {{ cookiecutter.project_slug }} -f conda-environment-dev.yml

Install the Windows extensions to Python::

  conda install pywin32

Install the development version of `PyInstaller
<https://pythonhosted.org/PyInstaller/>`__ into the environment::

  pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip

Build the EXE::

  pyinstaller {{ cookiecutter.project_slug }}.spec

The resulting EXE file is at ``dist/{{ cookiecutter.project_slug }}-X.Y.Z.exe``, where ``X.Y.Z``
is the current version number.

Clean up the temporary environment::

  deactivate {{ cookiecutter.project_slug }}
  conda env remove -n {{ cookiecutter.project_slug }}
