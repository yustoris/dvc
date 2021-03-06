.. image:: https://img.shields.io/travis/iterative/dvc/master.svg?label=Linux%20%26%20Mac%20OS
  :target: https://travis-ci.org/iterative/dvc

.. image:: https://img.shields.io/appveyor/ci/iterative/dvc/master.svg?label=Windows
  :target: https://ci.appveyor.com/project/iterative/dvc/branch/master

.. image:: https://codeclimate.com/github/iterative/dvc/badges/gpa.svg
  :target: https://codeclimate.com/github/iterative/dvc

.. image:: https://codecov.io/gh/iterative/dvc/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/iterative/dvc

Data Version Control or DVC is an open source tool for data science projects. 
It helps data scientists manage their code and data together in a simple form of Git-like commands.

Get started
===========
+-----------------------------------+-------------------------------------------------------------------+
| Step                              | Command                                                           |
+===================================+===================================================================+
| Track code and data together      | | ``$ git add train.py``                                          |
|                                   | | ``$ dvc add images.zip``                                        |
+-----------------------------------+-------------------------------------------------------------------+
| Connect code and data by commands | | ``$ dvc run -d images.zip -o images/ unzip -q images.zip``      |
|                                   | | ``$ dvc run -d images/ -d train.py -o model.p python train.py`` |
+-----------------------------------+-------------------------------------------------------------------+
| Make changes and reproduce        | | ``$ vi train.py``                                               |
|                                   | | ``$ dvc repro model.p.dvc``                                     |
+-----------------------------------+-------------------------------------------------------------------+
| Share code                        | | ``$ git add .``                                                 |
|                                   | | ``$ git commit -m 'The baseline model'``                        |
|                                   | | ``$ git push``                                                  |
+-----------------------------------+-------------------------------------------------------------------+
| Share data and ML models          | | ``$ dvc remote add myremote s3://mybucket/image_cnn``           |
|                                   | | ``$ dvc core.remote myremote``                                  |
|                                   | | ``$ dvc push``                                                  |
+-----------------------------------+-------------------------------------------------------------------+

See more in `tutorial <https://blog.dataversioncontrol.com/data-version-control-tutorial-9146715eda46>`_.

Installation
============

Packages
--------

Operating system dependent packages are the recommended way to install DVC.
The latest version of the packages can be found at GitHub releases page: https://github.com/iterative/dvc/releases

Python Pip
----------

DVC could be installed via the Python Package Index (PyPI).

.. code-block:: bash

   pip install dvc

Homebrew (Mac OS)
-----------------

Formula:
^^^^^^^^

.. code-block:: bash

   brew install iterative/homebrew-dvc/dvc

Cask:
^^^^^

.. code-block:: bash

   brew cask install iterative/homebrew-dvc/dvc

Links
=====

Website: https://dvc.org

Tutorial: https://blog.dataversioncontrol.com/data-version-control-tutorial-9146715eda46

Documentation: http://dvc.org/documentation

Discussion: https://discuss.dvc.org/

Related technologies
====================


#. `Git-annex <https://git-annex.branchable.com/>`_ - DVC uses the idea of storing the content of large files (that you don't want to see in your Git repository) in a local key-value store and uses file hardlinks/symlinks instead of the copying actual files.
#. `Git-LFS <https://git-lfs.github.com/>`_.
#. Makefile (and it's analogues). DVC tracks dependencies (DAG). 
#. `Workflow Management Systems <https://en.wikipedia.org/wiki/Workflow_management_system>`_. DVC is workflow management system designed specificaly to manage machine learning experiments. DVC was built on top of Git.

DVC is compatible with Git for storing code and the dependency graph (DAG), but not data files cache.
Data files caches can be transferred separately - now data cache transfer throught AWS S3 and GCP storge are supported.

How DVC works
=============


.. image:: https://s3-us-west-2.amazonaws.com/dvc-share/images/0.9/how_dvc_works.png
   :target: https://s3-us-west-2.amazonaws.com/dvc-share/images/0.9/how_dvc_works.png
   :alt: how_dvc_works


Copyright
=========

This project is distributed under the Apache license version 2.0 (see the LICENSE file in the project root).

By submitting a pull request for this project, you agree to license your contribution under the Apache license version 2.0 to this project.
