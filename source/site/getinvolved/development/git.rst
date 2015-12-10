########################
Getting started with git
########################

This guide will help you to get started with using git to develop for QGIS.

Git is a concurrent versioning system. This allows working on different
features at the same time each in its own sandbox, so each feature can be
brought to production quality before being included into the master version.

There is also the `github user documentation
<https://help.github.com/categories/bootcamp/>`_ which offers good information
about working with github and git. It also contains a very useful `glossary
<https://help.github.com/articles/github-glossary/>`_.

Build from git
==============

If you only want to build QGIS and do not want to submit your own improvements
to QGIS it is sufficient to `clone the repository
<https://help.github.com/articles/cloning-a-repository/>`_. Cloning is a
one-time operation to initialize your local copy.

.. code::

  git clone https://github.com/qgis/QGIS.git

In the future, if you want to keep up to date with the latest changes you will
have to `pull <https://help.github.com/articles/fetching-a-remote/#pull>`_.

.. code::

  git pull


Developing with git
===================

First steps
-----------

Please shortly read through this steps. We deliberately tried to keep them
short.

Fork
....

Before starting to write code you will need to `fork the repo
<https://help.github.com/articles/fork-a-repo/>`_. Once you
have done that, you have your own copy of the QGIS source code which you may
freely modify and from where you can propose changes back to the project
(often referred to as "upstream").

Setup pre-commit hook
.....................

There is a nice script that comes with the QGIS source code and does not only
check but also fix various formatting problems with your changes. You should
run this script automatically to make your life easier.

.. code::

  ln -s scripts/prepare-commit.sh .git/hooks/pre-commit
  
The script needs a customized version of `artistic style <http://astyle.sourceforge.net/>`_. You should enable the option `WITH_ASTYLE` in cmake.

Setup remote repositories
.........................

A *remote* is a link from your source folder to a repository. You will normally
work with two remotes:

* Your own fork to develop features
* The upstream QGIS source code to which constantly new changes by others get
  added

To check which remotes are currently setup, you may use the following command:

.. code::

  git remote -v

Normally the first remote which gets added gets the name ``origin``. I renamed
it here (in the file ``.git/config``) to avoid confusion and give explicit names.

.. code::

  qgis  git@github.com:qgis/QGIS.git (fetch)
  qgis  git@github.com:qgis/QGIS.git (push)
  gh-mku  git@github.com:m-kuhn/QGIS.git (fetch)
  gh-mku  git@github.com:m-kuhn/QGIS.git (push)

I have the upstream repository configured with the name ``qgis`` (this is where
I get the latest and greatest from) and my own with the name ``gh-mku`` (this
is where I upload the awesome results of my development).

Example workflow
----------------

First of all, let's make sure we are up to date with our master branch, since
that's where we start off and we don't want to be starting with an old version.

.. code::

  git checkout master
  git pull

We do not want to work on the master branch. This one is reserved for being in
sync with the status quo of the source code. Therefore we create a new branch,
starting from the current state of master.

.. code::

  git checkout -b myfeature

You can verify that you are now on this new branch with

.. code::

  git status

So let's go and change some files. After you have done some changes, you want
to commit them. This is a local operation, we will bring this to github later.

.. code::

  git add .
  git commit -m 'A descriptive message here'

Please note, that you should always give descriptive commit messages. Avoid
messages like "fixed a bug". It's better to use a message like this:

.. code::

  Do not crash when opening shp files on windows

  Although QGIS is free and open source software it should respect that there
  are non-free operating systems and formats on the market and this is no
  reason to crash.
  Fix #3211

This has two advantages:

* When somebody reviews your changes before merging them back to master, it
  will be much easier for him to follow your thoughts.
* When somebody in the future wants to know why a particular line of code was
  changed he can look, when this was changed and if there's a verbose message
  he will be able to stay in line with your plans from now.

You can now change more and add more commits. Once you are happy with the
changes, you can propse to integrate them back into the master branch. First
you will need to push your changes to github.

.. code::

  # Replace `gh-mku` with your remote name and `myfeature` with your branch name
  git push -u gh-mku myfeature

Now the code will be uploaded to github and you can use your favorite web
browser to make a pull request.

Pull Requests
-------------

Pull requests are the way to propose your changes on the QGIS source code to be
merged into the master development branch which will eventually become the next
stable QGIS release.

Pull requests need to be reviewed before they are merged. Reviewing is a pure
volunteer process. Therefore please be patient. The following tips normally
help to get merged quickly.

* Be explicit in the pull reuqest title. It should be clear what it's about.
* Keep pull requests bite-sized. A pull request should be one complete task
  but not a mix of different matters.
* Write some prose in the description that explains what you have done.
  Normally it's good to add some reasoning, an example and - if applicable -
  please add some screenshots.
* Add a unit test that checks what you have implemented and at the same time
  can be used by the reviewer as explication for the API.
* Be responsive when questions are risen. If somebody asks a question he has
  put his head around your problem, try to respond while his head is still
  close to the topic.
* If your pull request gets forgotten you can kindly ask the responsible
  developer about the status sometimes.

Rebase, merge and cherry-pick
=============================

Is the way to go when the delta between your branch and master is too big.
Please refer to other pages or help us to fill something useful in here.

Resolving merge conflicts
-------------------------

Sometimes you will get merge conflicts. Good luck!

Please help
===========

Please help to improve this document. It is hosted on github and your help is
very welcome if you have more good hints to increase productivity.
