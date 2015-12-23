##############################
Getting started with QtCreator
##############################

This guide will help you to get started with developing for QGIS.

You may also be interested in reading the git guide (To Be Done) and the QGIS coding
standards guide.

QtCreator
=========

QtCreator is an Integrated Development Environment (IDE) for C++ and integrates
especially nice with Qt applications. It consists among other things of a code
editor, a debugging frontend for GDB and a widget/form designer for Qt Widgets.

Installation
============

The installation will not be covered in this guide. If you are about to develop
C++ code you should be able to install an application ;)

Setup the IDE
=============

**Prerequisite**: You should have the QGIS source code cloned on your local
hard drive.

License headers
---------------

Inside the source code, there is a file ``qt_creator_license_template``. Copy
this file to a location outside the source folder and substitute name and mail
address in it. You can now make QtCreator use this file for all the new source
files which you add in the future by selecting it in ``Tools`` -> ``Options``
-> ``C++`` -> ``File Naming``.

Code Format
-----------

QtCreator can also be configured to follow the QGIS coding standard as good as
possible. Go to ``Tools`` -> ``Options`` -> ``Code Style``, click ``Import``
and select the file ``qtcreator_code_style.xml``.

.. note:: You should also configure git to run ``scripts/prepare-commit.sh``
          whenever you do a commit.

Setup the project
=================

**Prerequisite**: You should have the QGIS source code cloned on your local
hard drive.

When opening QtCreator you find a menu entry ``File`` with an item
``Open File or Project``. From there you can locate the ``CMakeFiles.txt``
file in your QGIS source tree.

You will now have to choose a build directory. If you already have one, you may
as well select the existing build directory.
In case you create a new build directory, be sure to pass
``-DCMAKE_BUILD_TYPE=Debug`` to the cmake configuration.
If you have troubles configuring, please see the note below.

Next you will probably want to use the full power of your machine when
compiling. for that switch to the tab "Projects" on the left side of QtCreator.
Locate the section ``Build Steps``, click Details and write ``-j8`` where you
can replace 8 with as many cores as you would like to assign to the build
process.

.. note:: **Dealing with CMake problems**
          Make sure that you have installed all build requirements, there are
          some good hints in the `install file <https://htmlpreview.github.io/?https://github.com/qgis/QGIS/blob/master/doc/INSTALL.html>`_
          . You may also have to enter -DWITH_QWTPOLAR=OFF in the cmake config
          options if you encounter problems with the qwtpolar dependency.

Efficient workflow
==================

The locate bar
--------------

At the bottom right, there's a small text field that let's you search for
almost anything in the source code if used properly. Remember the key
combination ``Ctrl+K``, it will be useful all the time to navigate the source
code.

Build
-----

I prefer to manually trigger builds and not automatically build before every
run. Go to ``Tools`` -> ``Options`` -> ``Build & Run``, deselect ``Always build
project before deploying it``, deselect ``Always deploy project before running
it``. I also like to save files when building (first option).

After that: ``Ctrl+B`` is your friend to trigger a build.

Debug run
---------

``F5``

Quick run (without Debug)
-------------------------

``Ctrl+R``


Set breakpoints
---------------

Just click left of the line number in the editor, a red point will appear and
the debugger will go into step and stop mode.

Please help
===========

Please help to improve this document. It is hosted on github and your help is
very welcome if you have more good hints to increase productivity.
