******************************************
 Building QGIS from source - step by step
******************************************

Last Updated: *Friday April 15, 2016*

Last Change : *Friday April 15, 2016*


Introduction
===============

This document is the original installation guide of the described software 
QGIS. The software and hardware descriptions named in this 
document are in most cases registered trademarks and are therefore subject 
to the legal requirements. QGIS is subject to the GNU General Public 
License. Find more information on the QGIS Homepage:
http://qgis.org

The details, that are given in this document have been written and verified 
to the best of knowledge and responsibility of the editors. Nevertheless, 
mistakes concerning the content are possible. Therefore, all data are not 
liable to any duties or guarantees. The editors and publishers do not take 
any responsibility or liability for failures and their consequences. You are 
always welcome for indicating possible mistakes.

You can download this document as part of the QGIS 'User and 
Installation Guide' in HTML and PDF format via http://qgis.org. A current 
version is also available at:
http://htmlpreview.github.io/?https://raw.github.com/qgis/QGIS/master/doc/INSTALL.html

Translations of this document can also be downloaded at the documentation area 
of the QGIS project at http://qgis.org. More information is available via
http://qgis.org/en/site/getinvolved/governance/organisation/governance.html#community-resources. 

Please visit http://qgis.org for information on joining our mailing lists 
and getting involved in the project further.

.. note:: **To document writers**
  
   Please use this document as the central
   place for describing build procedures. Please do not remove this notice. 

   This document is generated from 
   doc/INSTALL.t2t - if you need to edit this document, be sure to edit that 
   file rather than the generated INSTALL document found in the root of the 
   source directory.


Overview
=========

QGIS, like a number of major projects (eg. KDE 4.0), uses CMake
(http://www.cmake.org) for building from source.

Following a summary of the required dependencies for building:

Required build tools:

- CMake >= 2.8.6
- Flex >= 2.5.6
- Bison >= 2.4

Required build dependencies:

- Qt >= 4.8.0
- Proj >= 4.4.x
- GEOS >= 3.4
- Sqlite3 >= 3.0.0
- GDAL/OGR >= 1.4.x
- Qwt >= 5.0 & (< 6.1 with internal QwtPolar)
- expat >= 1.95
- QScintilla2

Optional dependencies:

- for GRASS providers and plugin - GRASS >= 6.0.0. QGIS may be compiled with GRASS 6 or GRASS 7.
  It can also be compiled with both GRASS versions in a single build but only if QGIS
  is not installed with rpath. The desired GRASS version is chosen on runtime by setting
  LD_LIBRARY_PATH or PATH.
- for georeferencer - GSL >= 1.8
- for postgis support and SPIT plugin - PostgreSQL >= 8.0.x
- for gps plugin - gpsbabel
- for mapserver export and PyQGIS - Python >= 2.3 (2.5+ preferred)
- for python support - SIP >= 4.12, PyQt >= 4.8.3 must match Qt version, Qscintilla2
- for qgis mapserver - FastCGI
- for oracle provider - Oracle OCI library

Indirect dependencies:

Some proprietary formats (eg. ECW and MrSid) supported by GDAL require
proprietary third party libraries.  QGIS doesn't need any of those itself to
build, but will only support those formats if GDAL is built accordingly.  Refer
to http://gdal.org/formats_list.html ff. for instructions how to include
those formats in GDAL.


Building on GNU/Linux
========================


Building QGIS with Qt 4.x
---------------------------

**Requires**: Ubuntu / Debian derived distro

.. note:: Refer to the section Building Debian packages for building
   debian packages.  Unless you plan to develop on QGIS, that is probably the
   easiest option to compile and install QGIS.

These notes are for Ubuntu - other versions and Debian derived distros may
require slight variations in package names.

These notes are for if you want to build QGIS from source. One of the major
aims here is to show how this can be done using binary packages for **all**
dependencies - building only the core QGIS stuff from source. I prefer this
approach because it means we can leave the business of managing system packages
to apt and only concern ourselves with coding QGIS!

This document assumes you have made a fresh install and have a 'clean' system.
These instructions should work fine if this is a system that has already been
in use for a while, you may need to just skip those steps which are irrelevant
to you.


Prepare apt
...........

The packages QGIS depends on to build are available in the "universe" component
of Ubuntu. This is not activated by default, so you need to activate it:

1. Edit your /etc/apt/sources.list file.
2. Uncomment all the lines starting with "deb"

Also you will need to be running Ubuntu 'precise' or higher in order for
all dependencies to be met.

Now update your local sources database::

  sudo apt-get update


Install build dependencies
..........................

============= ======================================================
Distribution  install command for packages
============= ======================================================
wheezy        ``apt-get install bison cmake doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal1-dev libgeos-dev libgsl0-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools python python-dev python-gdal python-mock python-nose2 python-psycopg2 python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
jessie        ``apt-get install bison cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl0-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools pyqt4.qsci-dev python-all python-all-dev python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
stretch       ``apt-get install bison cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools pyqt4.qsci-dev python-all python-all-dev python-future python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
precise       ``apt-get install bison cmake doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl0-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt5-qt4-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools python python-gdal python-mock python-psycopg2 python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
trusty        ``apt-get install bison cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl0-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt5-qt4-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools python-all python-all-dev python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
wily          ``apt-get install bison cmake cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl0-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt5-qt4-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools pyqt4.qsci-dev python-all python-all-dev python-future python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
xenial        ``apt-get install bison cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt5-qt4-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools pyqt4.qsci-dev python-all python-all-dev python-future python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
sid           ``apt-get install bison cmake dh-python doxygen flex gdal-bin git graphviz grass-dev libexpat1-dev libfcgi-dev libgdal-dev libgeos-dev libgsl-dev libopenscenegraph-dev libosgearth-dev libpq-dev libproj-dev libqca2-dev libqca2-plugin-ossl libqscintilla2-dev libqt4-dev libqt4-opengl-dev libqt4-sql-sqlite libqtwebkit-dev libqwt5-qt4-dev libspatialindex-dev libspatialite-dev libsqlite3-dev lighttpd locales pkg-config poppler-utils pyqt4-dev-tools pyqt4.qsci-dev python-all python-all-dev python-future python-gdal python-mock python-nose2 python-psycopg2 python-pyspatialite python-qscintilla2 python-qt4 python-qt4-dev python-qt4-sql python-sip python-sip-dev python-yaml qt4-doc-html spawn-fcgi txt2tags xauth xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable xvfb cmake-curses-gui``
============= ======================================================

(extracted from the control.in file in :file:`debian/`)


Setup ccache (Optional)
........................

You should also setup ccache to speed up compile times::

  cd /usr/local/bin
  sudo ln -s /usr/bin/ccache gcc
  sudo ln -s /usr/bin/ccache g++


Prepare your development environment
....................................

As a convention I do all my development work in :file:`$HOME/dev/<language>`, so in
this case we will create a work environment for C++ development work like
this::

  mkdir -p ${HOME}/dev/cpp
  cd ${HOME}/dev/cpp

This directory path will be assumed for all instructions that follow.


Check out the QGIS Source Code
...............................

There are two ways the source can be checked out. Use the anonymous method
if you do not have edit privileges for the QGIS source repository, or use
the developer checkout if you have permissions to commit source code
changes.

#. Anonymous Checkout

::

  cd ${HOME}/dev/cpp
  git clone git://github.com/qgis/QGIS.git

#. Developer Checkout

::

  cd ${HOME}/dev/cpp
  git clone git@github.com:qgis/QGIS.git


Starting the compile
..........................

I compile my development version of QGIS into my :file:`~/apps` directory to avoid
conflicts with Ubuntu packages that may be under :file:`/usr`. This way for example
you can use the binary packages of QGIS on your system along side with your
development version. I suggest you do something similar:

::

  mkdir -p ${HOME}/apps

Now we create a build directory and run ccmake:

::

  cd QGIS
  mkdir build-master
  cd build-master
  ccmake ..

When you run ccmake (note the .. is required!), a menu will appear where
you can configure various aspects of the build. If you want QGIS to have
debugging capabilities then set ``CMAKE_BUILD_TYPE`` to Debug. If you do not have
root access or do not want to overwrite existing QGIS installs (by your
package manager for example), set the ``CMAKE_INSTALL_PREFIX`` to somewhere you
have write access to (I usually use :file:`${HOME}/apps`). Now press
'c' to configure, 'e' to dismiss any error messages that may appear.
and 'g' to generate the make files. Note that sometimes 'c' needs to
be pressed several times before the 'g' option becomes available.
After the 'g' generation is complete, press 'q' to exit the ccmake
interactive dialog.

Now on with the build:

::

  make
  make install

It may take a little while to build depending on your platform.

After that you can try to run QGIS:

::

  $HOME/apps/bin/qgis

If all has worked properly the QGIS application should start up and appear
on your screen. If you get the error message "error while loading shared libraries",
execute this command in your shell.

::

  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${HOME}/apps/lib/


Building Debian packages
..........................

Instead of creating a personal installation as in the previous step you can
also create debian package.  This is done from the QGIS root directory, where
you'll find a debian directory.

First you need to install the debian packaging tools once:

::

  apt-get install build-essential

First you need to create an changelog entry for your distribution. For example
for Ubuntu Precise:

::

  dch -l ~precise --force-distribution --distribution precise "precise build"

The QGIS packages will be created with:

::

  dpkg-buildpackage -us -uc -b

.. note:: Install ``devscripts`` to get ``dch``.

.. note:: If ``dpkg-buildpackage`` complains about unmet build dependencies
   you can install them using apt-get and re-run the command.

.. note:: If you have ``libqgis1-dev`` installed, you need to remove it first
   using ``dpkg -r libqgis1-dev``. Otherwise dpkg-buildpackage will complain
   about a build conflict.

.. note:: By default tests are run in the process of building and their
   results are uploaded to http://dash.orfeo-toolbox.org/index.php?project=QGIS.
   You can turn the tests off using ``DEB_BUILD_OPTIONS=nocheck`` in front of the
   build command. The upload of results can be avoided with ``DEB_TEST_TARGET=test``.

The packages are created in the parent directory (ie. one level up).
Install them using dpkg.  E.g.:

::

  sudo debi


Building QGIS with Qt 5.x
..........................

.. warning:: Qt 5 is not officially supported. Building against Qt 5
   libraries seems to work quiet well alrady but be prepared that you are one
   of very few with this setup. We strongly recommend using QGIS with Qt 4.

Python bindings in particular are not expected to be compatible. When Qt 5
is enabled, the build system automatically activates Python 3 and PyQt5 as well.
There are no plugins and not even the python code shipped along the QGIS source
code is compatible with PyQt5.

You have been warned.


On Fedora Linux
...............

We assume that you have the source code of QGIS ready and created a
new subdirectory called ``build`` or ``build-qt5`` in it.


Install build dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  dnf install qt5-qtwebkit-devel qt5-qtlocation-devel qt5-qttools-static
  qt5-qtscript-devel qca-qt5-devel python3-qt5-devel python3-qscintilla-qt5-devel 
  qscintilla-qt5-devel python3-qscintilla-devel python3-qscintilla-qt5
  clang flex bison geos-devel gdal-devel sqlite-devel libspatialite-devel
  qt5-qtsvg-devel qt5-qtxmlpatterns-devel spatialindex-devel expat-devel proj-devel
  qwt-devel gsl-devel postgresql-devel

Make sure that your build directory is completely empty when you enter the
following command. Do never try to "re-use" an existing Qt4 build directory.
If you want to use ``ccmake`` or other interactive tools, run the following
command in the empty build directory once before starting to use the interactive
tools.

::

  cmake -DENABLE_QT5=ON -DWITH_QWTPOLAR=OFF ..

If everything went ok you can finally start to compile. (As usual append a -jX
where X is the number of available cores option to make to speed up your build
process)

::

  make

Run from the build directory

::

  ./output/bin/qgis

Or install to your system

::

  make install


Building on Windows
===================


Building with Microsoft Visual Studio
-------------------------------------

This section describes how to build QGIS using Visual Studio on Windows. This
is currently also how the binary QGIS packages are made (earlier versions used
MinGW).

This section describes the setup required to allow Visual Studio to be used to
build QGIS. 


Visual C++ Express Edition
..........................

The free (as in free beer) Express Edition installer is available under:
http://download.microsoft.com/download/c/d/7/cd7d4dfb-5290-4cc7-9f85-ab9e3c9af796/vc_web.exe

You also need the Windows SDK for Windows 7 and .NET Framework 4:
http://download.microsoft.com/download/A/6/A/A6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D/winsdk_web.exe


Other tools and dependencies
............................

Download and install following packages:

============================ ==========
Tool                         Website  
============================ ==========
CMake                        http://www.cmake.org/files/v3.0/cmake-3.0.2-win32-x86.exe
GNU flex, GNU bison and GIT  http://cygwin.com/setup-x86.exe (32bit) or http://cygwin.com/setup-x86_64.exe (64bit)
OSGeo4W                      http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86.exe (32bit) or http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86_64.exe (64bit)
============================ ==========

OSGeo4W does not only provide ready packages for the current QGIS release and
nightly builds of master, but also offers most of the dependencies needs to
build it.

For the QGIS build you need to install following packages from cygwin:

- bison
- flex
- git

and from OSGeo4W (select Advanced Installation):

- expat
- fcgi
- gdal
- grass
- gsl-devel
- iconv
- pyqt4
- qt4-devel
- qwt5-devel-qt4
- sip
- spatialite
- libspatialindex-devel
- python-qscintilla

This will also select packages the above packages depend on.

If you install other packages, this might cause issues. Particularly, make sure
**not** to install the ``msinttypes`` package. It installs a ``stdint.h`` file in
:file:`OSGeo4W[64]\\include`, that conflicts with Visual Studio own ``stdint.h``,
which for example breaks the build of the virtual layer provider.

Earlier versions of this document also covered how to build all above
dependencies. If you're interested in that, check the history of this page in the Wiki
or the SVN repository.


Setting up the Visual Studio project with CMake
...............................................

.. warning:: **Consider this section as example**. It tends to outdate, when OSGeo4W and
   SDKs move on. :file:`ms-windows/osgeo4w/package-nightly.cmd` is used for the
   nightly builds and constantly updated and hence might contain necessary
   updates that are not yet reflected here.

To start a command prompt with an environment that both has the VC++ and the OSGeo4W
variables create the following batch file (assuming the above packages were
installed in the default locations):

::

  @echo off
  set VS90COMNTOOLS=%PROGRAMFILES%\Microsoft Visual Studio 9.0\Common7\Tools\
  call "%PROGRAMFILES%\Microsoft Visual Studio 9.0\VC\vcvarsall.bat" x86
  
  set INCLUDE=%INCLUDE%;%PROGRAMFILES%\Microsoft SDKs\Windows\v7.1\include
  set LIB=%LIB%;%PROGRAMFILES%\Microsoft SDKs\Windows\v7.1\lib
  
  set OSGEO4W_ROOT=C:\OSGeo4W
  call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
  path %PATH%;%PROGRAMFILES%\CMake\bin;C:\cygwin\bin
  
  @set GRASS_PREFIX=C:/OSGeo4W/apps/grass/grass-6.4.4
  @set INCLUDE=%INCLUDE%;%OSGEO4W_ROOT%\include
  @set LIB=%LIB%;%OSGEO4W_ROOT%\lib;%OSGEO4W_ROOT%\lib
  
  @cmd

Start the batch file and on the command prompt checkout the QGIS source from
git to the source directory QGIS:

::

  git clone git://github.com/qgis/QGIS.git

Create a ``build`` directory somewhere. This will be where all the build output
will be generated.

Now run ``cmake-gui`` (still from cmd) and in the :guilabel:`Where is the source code:`
box, browse to the top level QGIS directory.

In the :guilabel:`Where to build the binaries:` box, browse to the 'build' directory you
created.

If the path to bison and flex contains blanks, you need to use the short name
for the directory (i.e. file:`C:\\Program Files` should be rewritten to
:file:`C:\\Progra~n`, where ``n`` is the number as shown in ``dir /x C:\\``).

Verify that the :guilabel:`BINDINGS_GLOBAL_INSTALL` option is not checked, so that python
bindings are placed into the output directory when you run the INSTALL target.

Hit :guilabel:`Configure` to start the configuration and select ``Visual Studio 9 2008``
and keep ``native compilers`` and click :guilabel:`Finish`.

The configuration should complete without any further questions and allow you to
click :guilabel:`Generate`.

Now close ``cmake-gui`` and continue on the command prompt by starting
``vcexpress``. Use :menuselection:`File --> Open --> Project/Solutions` and open the
``qgis-x.y.z.sln`` File in your project directory.

Change :guilabel:`Solution Configuration` from ``Debug`` to ``RelWithDebInfo`` (Release
with Debug Info) or ``Release`` before you build QGIS using the ALL_BUILD
target (otherwise you need debug libraries that are not included).

After the build completed you should install QGIS using the INSTALL target.

Install QGIS by building the INSTALL project. By default this will install to
:file:`C:\\Program Files\\qgis<version>` (this can be changed by changing the
``CMAKE_INSTALL_PREFIX`` variable in ``cmake-gui``). 

You will also either need to add all the dependency DLLs to the QGIS install
directory or add their respective directories to your PATH.


Packaging
.........

To create a standalone installer there is a perl script named ``creatensis.pl``
in file:`qgis/ms-windows/osgeo4w`. It downloads all required packages from OSGeo4W
and repackages them into an installer using NSIS.

The script can be run on both Windows and Linux.

On Debian/Ubuntu you can just install the 'nsis' package.

NSIS for Windows can be downloaded at:
http://nsis.sourceforge.net

And Perl for Windows (including other requirements like *wget*, *unzip*, *tar*
and *bzip2*) is available at:
http://cygwin.com


Packaging your own build of QGIS
................................

Assuming you have completed the above packaging step, if you want to include
your own hand built QGIS executables, you need to copy them in from your
windows installation into the ms-windows file tree created by the creatensis
script.

::

  cd ms-windows/
  rm -rf osgeo4w/unpacked/apps/qgis/*
  cp -r /tmp/qgis1.7.0/* osgeo4w/unpacked/apps/qgis/

Now create a package.

::

  ./quickpackage.sh

After this you should now have a nsis installer containing your own build 
of QGIS and all dependencies needed to run it on a windows machine.


Osgeo4w packaging
.................

The actual packaging process is currently not documented, for now please take a
look at :file:`ms-windows/osgeo4w/package.cmd`


Building using MinGW
--------------------

.. note:: This section might be outdated as nowadays Visual C++ is use to build
   the "official" packages.

   For a detailed account of building all the dependencies yourself you
   can visit Marco Pasetti's website here
   http://www.webalice.it/marco.pasetti/qgis+grass/BuildFromSource.html

Read on to use the simplified approach with pre-built libraries...


MSYS
....

MSYS provides a unix style build environment under windows. We have created a
zip archive that contains just about all dependencies.

Get this: http://download.osgeo.org/qgis/win32/msys.zip
and unpack to :file:`C:\\msys`

If you wish to prepare your msys environment yourself rather than using 
our pre-made one, detailed instructions are provided elsewhere in this
document.


Qt
...

Download Qt opensource precompiled edition exe and install (including the
download and install of mingw) from here:
http://qt.nokia.com/downloads/

When the installer will ask for MinGW, you don't need to download and install
it, just point the installer to :file:`C:\\msys\\mingw`

When Qt installation is complete:
Edit :file:`C:\\Qt\\4.8.0\\bin\\qtvars.bat` and add the following lines:

::

  set PATH=%PATH%;C:\msys\local\bin;C:\msys\local\lib 
  set PATH=%PATH%;"C:\Program Files\Subversion\bin" 

I suggest you also add :file:`C:\\Qt\\4.8.0\\bin` to your Environment Variables
Path in the Windows system preferences.

If you plan to do some debugging, you'll need to compile debug version of Qt::

  C:\Qt\4.8.0\bin\qtvars.bat compile_debug

.. note:: There is a problem when compiling debug version of Qt 4.7, the script ends with
   this message  ``mingw32-make: *** No rule to make target `debug`. Stop.``. To 
   compile the debug version you have to go out of :file:`src` directory and execute the
   following command:

   ::

     C:\Qt\4.8.0 make 


Flex and Bison
..............

Get Flex at 
http://sourceforge.net/project/showfiles.php?group_id=23617&package_id=16424
(the zip bin) and extract it into :file:`C:\\msys\\mingw\\bin`


Python stuff (optional)
.......................

Follow this section in case you would like to use Python bindings for QGIS. To
be able to compile bindings, you need to compile SIP and PyQt4 from sources as
their installer doesn't include some development files which are necessary.


Download and install Python - use Windows installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(It doesn't matter to what folder you'll install it)

http://python.org/download/


Download SIP and PyQt4 sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

http://www.riverbankcomputing.com/software/sip/download
http://www.riverbankcomputing.com/software/pyqt/download

Extract each of the above zip files in a temporary directory. Make sure
to get versions that match your current Qt installed version.


Compile SIP
^^^^^^^^^^^

::

  C:\Qt\4.8.0\bin\qtvars.bat 
  python configure.py -p win32-g++ 
  make 
  make install 


Compile PyQt
^^^^^^^^^^^^

::

  C:\Qt\4.8.0\bin\qtvars.bat 
  python configure.py 
  make 
  make install 


Final python notes
^^^^^^^^^^^^^^^^^^

You can delete the directories with unpacked SIP and PyQt4 sources after a
successfull install, they're not needed anymore.


git
....

In order to check out QGIS sources from the repository, you need a git client.
This installer should work fine:
http://msysgit.googlecode.com/files/Git-1.7.4-preview20110204.exe


CMake
......

CMake is build system used by QGIS. Download it from here:
http://www.cmake.org/files/v2.8/cmake-2.8.2-win32-x86.exe


QGIS
.....

Start a cmd.exe window ( Start -> Run -> cmd.exe ). Create development 
directory and move into it

::

  md C:\dev\cpp 
  cd C:\dev\cpp 

Check out sources from GIT:

::

  git clone git://github.com/qgis/QGIS.git


Compiling
..........

As a background read the generic building with CMake notes at the end of 
this document.

Start a cmd.exe window ( Start -> Run -> cmd.exe ) if you don't have one
already.  Add paths to compiler and our MSYS environment:

::

  C:\Qt\4.8.0\bin\qtvars.bat 

For ease of use add :file:`C:\\Qt\\4.8.0\\bin` to your system path in system
properties so you can just type ``qtvars.bat`` when you open the cmd console.
Create ``build`` directory and set it as current directory:

::

  cd C:\dev\cpp\qgis 
  md build 
  cd build 


Configuration
..............

::

  cmakesetup ..  

.. note:: You must include the '..' above.

Click :guilabel:`Configure` button. When asked, you should choose ``MinGW Makefiles`` as
generator.

There's a problem with MinGW Makefiles on Win2K. If you're compiling on this
platform, use ``MSYS Makefiles`` generator instead.

All dependencies should be picked up automatically, if you have set up the
Paths correctly. The only thing you need to change is the installation
destination (``CMAKE_INSTALL_PREFIX``) and/or set 'Debug'.

For compatibility with NSIS packaging scripts I recommend to leave the install
prefix to its default :file:`C:\\program files`

When configuration is done, click **OK** to exit the setup utility.


Compilation and installation
.............................

::

   make make install 


Run qgis.exe from the directory where it's installed (CMAKE_INSTALL_PREFIX)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure to copy all .dll:s needed to the same directory as the qgis.exe
binary is installed to, if not already done so, otherwise QGIS will complain
about missing libraries when started.

A possibility is to run qgis.exe when your path contains :file:`C:\\msys\\local\\bin`
and :file:`C:\\msys\\local\\lib` directories, so the DLLs will be used from that place.


Create the installation package: (optional)
............................................

Download and install NSIS from (http://nsis.sourceforge.net/Main_Page)

Now using windows explorer, enter the ``win_build`` directory in your QGIS source
tree. Read the README file there and follow the instructions. Next right click
on ``qgis.nsi`` and choose the option **Compile NSIS Script**. 


Creation of MSYS environment for compilation of QGIS
----------------------------------------------------


Initial setup
..............


MSYS
^^^^^

This is the environment that supplies many utilities from UNIX world in Windows and is needed
by many dependencies to be able to compile.

Download from here:
http://puzzle.dl.sourceforge.net/sourceforge/mingw/MSYS-1.0.11-2004.04.30-1.exe

Install to :file:`C:\\msys`

All stuff we're going to compile is going to get to this directory (resp. its subdirs).


MinGW
^^^^^

Download from here:
http://puzzle.dl.sourceforge.net/sourceforge/mingw/MinGW-5.1.3.exe

Install to :file:`C:\\msys\\mingw`

It suffices to download and install only ``g++`` and ``mingw-make`` components.


Flex and Bison
^^^^^^^^^^^^^^^

Flex and Bison are tools for generation of parsers, they're needed for GRASS and also QGIS compilation.

Download the following packages:

* http://gnuwin32.sourceforge.net/downlinks/flex-bin-zip.php
* http://gnuwin32.sourceforge.net/downlinks/bison-bin-zip.php
* http://gnuwin32.sourceforge.net/downlinks/bison-dep-zip.php

Unpack them all to :file:`C:\\msys\\local`


Installing dependencies
........................


Getting ready
^^^^^^^^^^^^^^

Paul Kelly did a great job and prepared a package of precompiled libraries for GRASS.
The package currently includes:

- zlib-1.2.3
- libpng-1.2.16-noconfig
- xdr-4.0-mingw2
- freetype-2.3.4
- fftw-2.1.5
- PDCurses-3.1
- proj-4.5.0
- gdal-1.4.1

It's available for download here:
http://www.stjohnspoint.co.uk/grass/wingrass-extralibs.tar.gz

Moreover he also left the notes how to compile it (for those interested):
http://www.stjohnspoint.co.uk/grass/README.extralibs

Unpack the whole package to :file:`C:\\msys\\local`


GRASS
^^^^^

Grab sources from CVS or use a weekly snapshot, see:
http://grass.itc.it/devel/cvs.php

In MSYS console go to the directory where you've unpacked or checked out sources
(e.g. :file:`C:\\msys\\local\\src\\grass-6.3.cvs`)

Run these commands:

::

  export PATH="/usr/local/bin:/usr/local/lib:$PATH"
  ./configure --prefix=/usr/local --bindir=/usr/local --with-includes=/usr/local/include --with-libs=/usr/local/lib --with-cxx --without-jpeg \
  --without-tiff --with-postgres=yes --with-postgres-includes=/local/pgsql/include --with-pgsql-libs=/local/pgsql/lib --with-opengl=windows --with-fftw \
  --with-freetype --with-freetype-includes=/mingw/include/freetype2 --without-x --without-tcltk --enable-x11=no --enable-shared=yes \
  --with-proj-share=/usr/local/share/proj
  make
  make install

It should get installed to :file:`C:\\msys\\local\\grass-6.3.cvs`

By the way, these pages might be useful:

- http://grass.gdf-hannover.de/wiki/WinGRASS_Current_Status
- http://geni.ath.cx/grass.html


GEOS
^^^^^

Download the sources:
http://geos.refractions.net/geos-2.2.3.tar.bz2

Unpack to e.g. :file:`C:\\msys\\local\\src`

To compile, I had to patch the sources: in file :file:`source/headers/timeval.h` line 13.
Change it from:

::

  #ifdef _WIN32

to:

::

  #if defined(_WIN32) && defined(_MSC_VER)

Now, in MSYS console, go to the source directory and run:

::

  ./configure --prefix=/usr/local
  make
  make install


SQLITE
^^^^^^^

You can use precompiled DLL, no need to compile from source:

Download this archive:
http://www.sqlite.org/sqlitedll-3_3_17.zip

And copy :file:`sqlite3.dll` from it to :file:`C:\\msys\\local\\lib`

Then download this archive:
http://www.sqlite.org/sqlite-source-3_3_17.zip

And copy :file:`sqlite3.h` to :file:`C:\\msys\\local\\include`


GSL
^^^

Download sources:
ftp://ftp.gnu.org/gnu/gsl/gsl-1.9.tar.gz

Unpack to :file:`C:\\msys\\local\\src`

Run from MSYS console in the source directory:

::

  ./configure
  make
  make install


EXPAT
^^^^^^

Download sources:
http://dfn.dl.sourceforge.net/sourceforge/expat/expat-2.0.0.tar.gz

Unpack to :file:`C:\\msys\\local\\src`

Run from MSYS console in the source directory:

::

  ./configure
  make
  make install


POSTGRES
^^^^^^^^^

We're going to use precompiled binaries. Use the link below for download:
http://wwwmaster.postgresql.org/download/mirrors-ftp?file=%2Fbinary%2Fv8.2.4%2Fwin32%2Fpostgresql-8.2.4-1-binaries-no-installer.zip

copy contents of :file:`pgsql` directory from the archive to :file:`C:\\msys\\local`


Cleanup
........

We're done with preparation of MSYS environment. Now you can delete all stuff in
:file:`C:\\msys\\local\\src` - it takes quite a lot
of space and it's not necessary at all.


Building on MacOS X
====================

In this approach I will try to avoid as much as possible building dependencies
from source and rather use frameworks wherever possible.

"Universal", SDK and non-default arch builds require more complex options and
some fiddling with the system. It is best to stick with a single, default,
architecture build and follow these instructions for an initial build.
Included are notes for building on Mac OS X 10.5 (Leopard), 10.6
(Snow Leopard), 10.7 (Lion), 10.8 (Mt. Lion) and 10.9 (Mavericks)
(These names will be used throughout the instructions.)
Make sure to read each section completely before typing the first command you see.

General note on Terminal usage:  When I say "cd" to a folder in a Terminal,
it means type "cd " (without the quotes, make sure to type a space after) and
then type the path to said folder, then <return>. A simple way to do this
without having to know and type the full path is, after type the "cd " part,
drag the folder (use the icon in its window title bar, or drag a folder from
within a window) from the Desktop to the Terminal, then tap <return>.

**Parallel Compilation**: On multiprocessor/multicore Macs, it's possible to
speed up compilation, but it's not automatic. Whenever you type "make" (but
NOT "make install"), instead type:

::

  make -j [#cpus]

Replace ``[#cpus]`` with the number of cores and/or processors your Mac has. On recent
models with hyperthreading processors this can be double the physical count of
processors and cores.

ie: Mac Pro "8 Core" model (2 quad core processors) = 8

ie: Macbook Pro i5 (hyperthreading) = 2 cores X 2 = 4

To find out how many CPUs you have available, run the following in Terminal:

::

  /usr/sbin/sysctl -n hw.ncpu

which can be used in build shell scripts like:

::

  make -j $(/usr/sbin/sysctl -n hw.ncpu)

.. note:: If you get an error in parallel compilation, try removing the -j # flag,
   so it's just 'make', or using a smaller number.  Sometimes make can hiccup on too
   many threads.


Install Developer Tools
------------------------

Developer tools are not a part of a standard OS X installation. Up through
Snow Leopard, the Developer Tools, later called Xcode, were included with the
system install disks, though it's best to download the latest version compatible
with your system to get important updates fixing various issues.
Starting with Lion, Xcode is available as a download and from the App Store.

Downloading Xcode/Developer Tools for up through Snow Leopard requires a free
developer account at
developer.apple.com. Up through Snow Leopard, get the latest Xcode that is
supported for your system. For Lion and above, you can get Xcode from either a
free developer account or for a minimal fee from the app store.
When installing Xcode up through Snow Leopard, make sure to
do a custom install and install the Unix Development or Command Line Tools option.

On Lion, if you have installed Xcode 4.0 - 4.2 and are upgrading to 4.3, it's
a good idea to uninstall the old version first with:

::

  sudo /Developer/Library/uninstall-devtools

On Lion and Mt. Lion, using Xcode 4.4+, the developer command line tools can be
installed via the Xcode preferences.

Xcode 4.3+ also introduces the clang frontend to the LLVM compiler as default.

.. note:: In XCODE 4.5 installed from the app store, you need to install the
   command line tools from :menuselection:`XCode -> Preferences -> Downloads`
   and choose command line tools.

http://clang.llvm.org/

The supplied clang version 4 can compile QGIS, but presents many warnings
compared to just using LLVM. You can specifically use LLVM by exporting paths to
the compilers in Terminal, or shell scripts, prior to building QGIS:

::

  export CC=/usr/bin/llvm-gcc
  export CXX=/usr/bin/llvm-g++

If you have trouble building some of the dependencies listed below with clang
(e.g. OSG & osgEarth), try using only the LLVM compilers.


Install Qt4 from disk image
---------------------------

You need a minimum of Qt-4.4.0. I suggest getting the latest (Qt 4, not 5). There is no need
for the full Qt SDK, so save yourself some download time and get the frameworks
only. This is available in the Libraries section of the Qt download page.

.. note::
   **Snow Leopard**

   If you are building on Snow Leopard+, you will need to
   decide between 32-bit support in the older Qt Carbon branch, or 64-bit
   support in the Qt Cocoa branch. Appropriate installers are available for both
   as of Qt-4.5.2, though they stopped making Carbon packages at Qt 4.7.4.
   Qt 4.6+ is recommended for Cocoa.
   Starting with Lion, Carbon may not work properly, if at all.
   Starting with Qt 4.8, only 64bit Cocoa installers are available.

.. note:: Support for new system versions in any given Qt version may
   not be present and may cause a 'This version of Mac OS X
   is unsupported' error when building QGIS. Try the next Qt version.

.. note:: **For PPC:**
   
   The readymade Qt Cocoa installers don't include PPC support, you'd
   have to compile Qt yourself. But, there appear to be issues with Qt Cocoa on
   PPC Macs anyways. Qt Carbon is recommended on PPC Macs.

http://qt-project.org/downloads

If you want debug frameworks, Qt also provides a separate download with these.
These are in addition to the non-debug frameworks.

Earlier OS X systems may need an old Qt version - check the requirements of the
current Qt version. To get old Qt downloads, there is an FTP link at the bottom
of the download page. Files are in the qt/source (yes, even the binary packages).

Once downloaded open the disk image and run the installer. Note you need admin
privileges to install.

.. note:: **For Leopard+**
   
   Qt includes a couple non-framework libraries in :file:`/usr/lib`.
   When using a system SDK these libraries will not be found. To fix this problem,
   add symlinks to :file:`/usr/local`:

   ::

     sudo ln -s /usr/lib/libQtUiTools.a /usr/local/lib/
     sudo ln -s /usr/lib/libQtCLucene.dylib /usr/local/lib/

These should then be found automatically. Earlier systems
may need some help by adding '-L/usr/local/lib' to ``CMAKE_SHARED_LINKER_FLAGS``,
``CMAKE_MODULE_LINKER_FLAGS`` and ``CMAKE_EXE_LINKER_FLAGS`` in the cmake build.


Install CMake for OSX
----------------------

Get the latest source release from here:
http://www.cmake.org/cmake/resources/software.html

Binary installers are available for OS X, but they are not recommended
(2.4 versions install in :file:`/usr` instead of :file:`/usr/local`, and 2.6+
versions are a strange application). Instead, download the source.

.. note:: 2.8.5 is broken for detecting part of Qt. Fixed in 2.8.6.
   Double-click the source tarball to unpack it, then cd to the source folder and:

   ::

     ./bootstrap --docdir=/share/doc/CMake --mandir=/share/man
     make -j [#cpus]
     sudo make install


Optional setup: ccache
.......................

.. note:: **Xcode 4.4+**

   You will probably not need to install ccache if you are using
   the clang frontend to LLVM compiler, a setup that already provides fairly quick
   compile times.

Setup ccache to significantly speed up compile times after initial build.
(Switching git branches will again cause longer initial build times unless
separate build directories are used for each branch.)

Get the latest source release from here:
http://ccache.samba.org/

Double-click the source tarball to unpack, then, in Terminal.app, cd to the
source folder and:

::

  ./configure
  make
  sudo make install

After install, symbolically link compilers to :file:`/usr/local/bin/ccache`.
(Note: this differs from instructions at http://ccache.samba.org/manual.html
Changing the  :file:`/usr/bin:/usr/local/bin` order in PATH is not recommended on OS X).

::

  sudo mkdir /usr/local/bin/compilers && cd /usr/local/bin/compilers
  sudo ln -s ../ccache gcc
  sudo ln -s ../ccache g++
  sudo ln -s ../ccache cc
  sudo ln -s ../ccache c++

Add the following to the end of your :file:`~/.bash_profile` (and optionally :file:`~/.bashrc`)
to allow your login shell to discover the symbolically linked compilers before
/usr/bin compilers and to easily toggle using ccache off, by commenting out the
line and starting a new login session in Terminal.

::

  export PATH=/usr/local/bin/compilers:$PATH

If you have trouble building some of the dependencies listed below (e.g. OSG &
osgEarth), try bypassing ccache.


Install development frameworks for QGIS dependencies
-----------------------------------------------------

Download William Kyngesburye's excellent GDAL Complete package that includes
PROJ, GEOS, GDAL, SQLite3, Spatialite, and image libraries, as frameworks.
There are also GSL and FreeType frameworks.
http://www.kyngchaos.com/software/frameworks

Once downloaded, open and install the frameworks.

William provides an additional installer package for Postgresql (for PostGIS
support). QGIS just needs the libpq client library, so unless you want to
setup the full Postgres + PostGIS server, all you need is the client-only
package. It's available here:
http://www.kyngchaos.com/software/postgres

Also available is a GRASS application:
http://www.kyngchaos.com/software/grass

Old versions of these packages for older systems are available in the
software archive section.


Additional dependencies: General compatibility note
....................................................

There are some additional dependencies that, at the time of writing, are not
provided as frameworks or installers so we will need to build these from source.
If you are wanting to build QGIS as a 64-bit application, you will need to
provide the appropriate build commands to produce 64-bit support in dependencies.
Likewise, for 32-bit support on Snow Leopard, you will need to override the
default system architecture, which is 64-bit, according to instructions for
individual dependency packages.

Stable release versions are preferred. Beta and other development versions may
have problems and you are on your own with those.


Additional dependencies: Expat
...............................

.. note:: **Snow Leopard**

   Snow Leopard includes a usable expat, so this step is
   not necessary on Snow Leopard or above.

Get the expat sources:
http://sourceforge.net/project/showfiles.php?group_id=10127

Double-click the source tarball to unpack, then, in Terminal.app, cd to the
source folder and:

::

  ./configure
  make
  sudo make install


Additional dependencies: Spatialindex
......................................

Get the libspatialindex sources:
http://download.osgeo.org/libspatialindex/

Double-click the source tarball to unpack, then, in Terminal.app, cd to the
source folder and:

::

  ./configure --disable-dependency-tracking CFLAGS=-Os
  make
  sudo make install


Additional dependencies: Python
................................

.. note:: **Leopard +**

   Starting with Leopard a usable Python is included in the system.
   This is Python 2.5, 2.6 and 2.7, respectively for Leo, Snow and Lion+.
   So there is no need to install Python on Leopard and newer.
   You can still install Python from python.org if preferred.

If installing from python.org, make sure you install the latest Python
2.x from

http://www.python.org/download/

Python 3 is a major change, and may have compatibility issues, so try it at
your own risk.


Additional dependencies: SIP
.............................

.. note:: **Mt Lion** SIP 4.15.7 appears to not work on Mt Lion. Install either
   a prior version to 4.14.6 or a later version 4.16.3+

Retrieve the python bindings toolkit SIP from

http://www.riverbankcomputing.com/software/sip/download

Double-click the source tarball to unpack it, then, in Terminal.app,
cd to the source folder. Then for your chosen Python:

python.org Python

::

  python configure.py
  make
  sudo make install

Leopard system Python
^^^^^^^^^^^^^^^^^^^^^^

SIP wants to install in the system path -- this is not a good idea.
More configuration is needed to install outside the system path:

::

  python configure.py -n -d /Library/Python/2.5/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip -s MacOSX10.5.sdk

Snow Leopard system Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to Leopard, you should install outside the system Python path.
Also, you need to specify the architecture you want and make sure to run the
versioned python binary (this one responds to the 'arch' command, 'python' does
not). Substitute '2.7' for python version and 10.7 for SDK version below for
Lion.

If you are using 32-bit Qt (Qt Carbon)::

  python2.6 configure.py -n -d /Library/Python/2.6/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip --arch=i386 -s MacOSX10.6.sdk

For 64-bit Qt (Qt Cocoa), use this configure line::

  python2.6 configure.py -n -d /Library/Python/2.6/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip --arch=x86_64 -s MacOSX10.6.sdk

Lion+ system Python
^^^^^^^^^^^^^^^^^^^^

Similar to Snow Leopard, you should install outside the system Python path.
The SDK option should match the system you are compiling on:

for Lion::

  python2.7 configure.py -d /Library/Python/2.7/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip --arch=x86_64 -s MacOSX10.7.sdk

for Mt. Lion::

  python2.7 configure.py -d /Library/Python/2.7/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip --arch=x86_64 -s MacOSX10.8.sdk

for Mavericks::

  python2.7 configure.py -d /Library/Python/2.7/site-packages -b /usr/local/bin \
  -e /usr/local/include -v /usr/local/share/sip --arch=x86_64 -s MacOSX10.9.sdk

continue...

Then continue with compilation and installation::

  make
  sudo make install


Additional dependencies: QScintilla2
.....................................

Retrieve the Qt version of the Scintilla-based text editor widget from
http://www.riverbankcomputing.co.uk/software/qscintilla/download

Double-click the tarball to unpack it. Then, cd to the QScintilla2.x.x source
folder in a Terminal.

QScintilla2 wants to install in the system path -- with libraries going into
:file:`/Library/Frameworks` and headers into :file:`/usr/include/Qsci` -- this is not a good
idea, and it also basically breaks the QtDesigner plugin. More configuration
is needed to install outside the system path, in :file:`/usr/local/`::

  cd Qt4Qt5

Edit :file:`QScintilla-gpl-2.x.x/Qt4Qt5/qscintilla.pro` in the following manner::

  current line --> new line
  
  target.path = $$[QT_INSTALL_LIBS]  -->  target.path = /usr/local/lib
  header.path = $$[QT_INSTALL_HEADERS]  -->  header.path = /usr/local/include

Save the qscintilla.pro file and build the QScintilla2 C++ library::

  qmake -spec macx-g++ qscintilla.pro
  make -j [#cpus]
  sudo make install

adjust the install_name_tool command for the version installed of QScintilla installed::

  sudo install_name_tool -id /usr/local/lib/libqscintilla2.11.dylib \
    /usr/local/lib/libqscintilla2.11.dylib

This installs QScintilla2's dylib in :file:`/usr/local/lib/` and the header files in
:file:`/usr/local/include/Qsci/`, both of which should be automatically found when
building QGIS.


Optional setup: QScintilla2 QtDesigner plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The plugin allows QScintilla2 widgets to be used within QtDesigner.

::

  cd <QScintilla2 source directory>
  cd designer-Qt4Qt5
  qmake -spec macx-g++ designer.pro
  make
  sudo make install

Installs in :file:`/Developer/Applications/Qt/plugins/designer/`


Additional dependencies: PyQt
..............................

Retrieve the python bindings toolkit for Qt from
http://www.riverbankcomputing.com/software/pyqt/download

Double-click the source tarball to unpack it, then, in Terminal.app,
cd to the source folder. Then for your chosen Python:

python.org Python

::

  python configure.py -n /usr/local/Qt4.8/qsci
  yes

Leopard system Python
^^^^^^^^^^^^^^^^^^^^^^

PyQt wants to install in the system path -- this is not a good idea.
More configuration is needed to install outside the system path::

  python configure.py -d /Library/Python/2.5/site-packages -b /usr/local/bin -n /usr/local/Qt4.8/qsci -v /usr/local/share/sip/PyQt4

Snow Leopard system Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to Leopard, you should install outside the system Python path.
Also, you need to specify the architecture you want (requires at least PyQt 4.6),
and make sure to run the versioned python binary (this one responds to the
'arch' command, which is important for pyuic4, 'python' does not).
Substitute '2.7' for python version and 10.7 for SDK version below for Lion.

If you are using 32-bit Qt (Qt Carbon)::

  python2.6 configure.py -d /Library/Python/2.6/site-packages -b /usr/local/bin \
  -n /usr/local/Qt4.8/qsci -v /usr/local/share/sip/PyQt4 --use-arch i386

For 64-bit Qt (Qt Cocoa), use this configure line::

  python2.6 configure.py -d /Library/Python/2.6/site-packages -b /usr/local/bin \
  -n /usr/local/Qt4.8/qsci -v /usr/local/share/sip/PyQt4 --use-arch x86_64

Lion, Mt. Lion, and Mavericks system Python

Similar to Snow Leopard, you should install outside the system Python path.
But you don't need the use-arch option::

  python2.7 configure.py -d /Library/Python/2.7/site-packages -b /usr/local/bin -n /usr/local/Qt4.8/qsci -v /usr/local/share/sip/PyQt4

continue...

::

  make -j [#cpus]
  sudo make install

If there is a problem with undefined symbols in QtOpenGL on Leopard, edit
QtOpenGL/makefile and add -undefined dynamic_lookup to LFLAGS.
Then make again.


Additional dependencies: QScintilla2 Python Module
..................................................

This will create the Qsci.so module in :file:`/Library/Python/2.x/site-packages/PyQt4`.
Like PyQt, it needs help to not install in system locations.

Snow Leopard: substitute '2.6' for Python version

::

  cd <QScintilla2 source dir>
  cd Python
  python2.7 configure.py -o /usr/local/lib -n /usr/local/include \
  -d /Library/Python/2.7/site-packages/PyQt4 -v /usr/local/share/sip/PyQt4 \
  --sip-incdir=/usr/local/include --pyqt-sipdir=/usr/local/share/sip/PyQt4
  cat >>Qsci.pro <<EOF
  QMAKE_LFLAGS_PLUGIN -= -dynamiclib
  QMAKE_LFLAGS_PLUGIN += -bundle
  EOF
  qmake -spec macx-g++ Qsci.pro
  make -j [#cpus]
  sudo make install

The -o and -n options should match the QScintilla2 C++ dylib install options.


Additional dependencies: Qwt
.............................

The GPS tracking feature uses Qwt.

.. note:: PyQwt is not compatible with PyQt 4.9, so we will skip that.

Download the latest Qwt 6.0 source (6.1 does not work with the QwtPolar in QGIS) from:
http://sourceforge.net/projects/qwt

Double-click the tarball to unpack it. Now, cd to the qwt source folder in a
Terminal.

Type these commands to build and install 6.0.x (assumes v6.0.2, adjust commands
for other version as needed):

::

  cat >> qwtconfig.pri <<EOF
  QWT_CONFIG -= QwtFramework
  EOF
  qmake -spec macx-g++
  make -j [#cpus]
  sudo make install
  
  sudo install_name_tool -id /usr/local/qwt-6.0.2/lib/libqwt.6.dylib \
    /usr/local/qwt-6.0.2/lib/libqwt.6.dylib

The Qwt shared library is now installed in /usr/local/qwt-6.0.x (x is
the point version). Remember this for QGIS configuration.


Additional dependencies: Bison
..............................

The version of bison available by default on Mac OS X is too old so you
need to get a more recent one on your system. Download at least version 2.4 from:
ftp.gnu.org/gnu/bison/

Now build and install it to a prefix of /usr/local. Double-click the source
tarball to unpack it, then cd to the source folder and:

::

  ./configure --disable-dependency-tracking CFLAGS=-Os
  make
  sudo make install


Additional dependencies: gpsbabel
.................................

For integrated GPS Tools functions, a gpsbabel executable is required. You can
find this at:
http://www.gpsbabel.org/

Download the GPSBabel OS X package, and copy GPSBabelFE.app from the disk image to
/Applications.


Optional dependencies: libfcgi
...............................

If you want to use the QGIS Mapserver, you need libfcgi. This is included on
systems up through Snow Leopard, but was dropped at Lion. So, on Lion you need
to get the source from:
http://www.fastcgi.com/dist/

Grab the latest fcgi SNAP package there. Double-click the source
tarball to unpack it, then cd to the source folder and:

::

  ./configure --disable-dependency-tracking CFLAGS=-Os
  make
  sudo make install


Optional dependencies: OSG & osgEarth
.....................................

If you want the Globe plugin in QGIS (default OFF), OSG and osgEarth are needed.

First, OpenSceneGraph.  The main site is very out of date, just go to
github:
http://github.com/openscenegraph/osg/tags

Download the latest 3.1 version (you can select a tarball when you hover over
the entry). Double-click the source tarball to unpack it.
(There is a version numbering oddity in the source, but since we'll be
bundling OSG as it's meant to be, it really doesn't matter).

Installation is a bit out of touch with OS X standards, so we'll stage it to a
temporary location first. You could stage it to the folder that the OSG source
folder is in, or a common staging area like /Users/Shared/unix/osg. Pick a
folder not hidden and that doesn't need admin permissions to write to for simplicity.

If you are building on Leopard, its configure forces a old ppc/i386 32bit build.
If you want 64bit you need to fix CMakeLists.txt - in a text editor, find the
if-block that starts with::

  ELSEIF(${OSG_OSX_SDK_NAME} STREQUAL "macosx10.6" OR ${OSG_OSX_SDK_NAME} STREQUAL "macosx10.5")

In that section before the next ELSEIF, change::

  ppc;i386

to::

  i386;x86_64

and change::

  mmacosx-version-min=10.5

to::

  mmacosx-version-min=10.6

In a new Terminal cd to the source folder and:

::

  mkdir build
  cd build
  cmake -D CMAKE_INSTALL_PREFIX=/path/to/some/staging/folder \
  -D OSG_COMPILE_FRAMEWORKS=ON \
  -D OSG_PLUGIN_SEARCH_INSTALL_DIR_FOR_PLUGINS=OFF \
  -D JASPER_LIBRARY=/Library/Frameworks/UnixImageIO.framework \
  -D JASPER_INCLUDE_DIR=/Library/Frameworks/UnixImageIO.framework/Headers \
  -D TIFF_LIBRARY=/Library/Frameworks/UnixImageIO.framework \
  -D TIFF_INCLUDE_DIR=/Library/Frameworks/UnixImageIO.framework/Headers \
  ..
  make
  make install
  sudo mkdir -p "/Library/Application Support/OpenSceneGraph/PlugIns"

Open the staging folder you chose for the CMAKE_INSTALL_PREFIX option above.

Now move all ``.frameworks`` from the :file:`lib/` folder in the staging area to
:file:`/Library/Frameworks`. Move the files in the :file:`lib/osgPlugins` folder
to :file:`/Library/Application Support/OpenSceneGraph/PlugIns`.  The :file:`bin/`
executables can be left where they are.

Next up is libzip.  Get the latest tarball at:
http://nih.at/libzip/

Double-click the source tarball to unpack it.
In a new Terminal cd to the source folder and:

::

  ./configure --disable-dependency-tracking --disable-shared CFLAGS=-Os
  make
  sudo make install

Then it's time for osgEarth. Downloads are also on github:
http://github.com/gwaldron/osgearth/tags

Download a tarball for the latest stable release (sorting can be confusing here).
Double-click the source tarball to unpack it.

.. note:: for now stick with version 2.3. There are compile errors in 2.4
   that need attention.

This one also needs an intermediate staging area. Choose a folder similar to OSG.

In a new Terminal cd to the source folder and:

::

  mkdir build
  cd build
  export PATH="/path/to/osg/staging/folder/bin:$PATH"
  cmake -D CMAKE_INSTALL_PREFIX=/path/to/some/staging/folder \
  -D CMAKE_BUILD_TYPE=MinSizeRel \
  -D OSGEARTH_BUILD_FRAMEWORKS=true \
  ..
  make
  make install
  sudo mkdir -p "/Library/Application Support/OpenSceneGraph/Headers"

Open the staging folder you chose for the ``CMAKE_INSTALL_PREFIX`` option above.
Also open the OSG staging path :file:`/bin` folder from the OSG build.

Move all the ``.frameworks`` from the :file:`lib/` folder to :file:`/Library/Frameworks`.
Move the files in the osgPlugins folder in the :file:`lib/` folder to
:file:`/Library/Application Support/OpenSceneGraph/PlugIns`. Move the 
:file:`include/osgEarthDrivers` folder to :file:`/Library/Application Support/OpenSceneGraph/Headers`.
(you may need to create this folder)
And as for OSG, you can leave the :file:`bin/` executables where they are.


API documentation
------------------

If you want to build a local copy of the API docs (like those at
http://doc.qgis.org/api) you will need Graphviz and Doxygen installed:

http://www.graphviz.org/Download_macos.php

http://www.stack.nl/~dimitri/doxygen/download.html

Graphviz is simply installed via a regular Mac package installer. Install it
first. It will place some of its binaries in :file:`/usr/local/bin/`.

For Doxygen, compiling the source is recommended over installing the app.
Double-click the source tarball to unpack it, then cd to the source folder and:

::

  ./configure
  make -j [#cpus]
  sudo make install

The documentation will be output to the build directory, and if using more complete
QGIS.app bundling on install, inside the app in:
:file:`QGIS.app/Contents/Resources/doc`


QGIS source
-----------

Unzip the QGIS source tarball to a working folder of your choice
(/usr/somewhere is not a good choice as it's hidden and requires root
privileges).  If you are reading this from the source, you've already done
this.

If you want to experiment with the latest development sources, go to the github
QGIS project page:
http://github.com/qgis/QGIS

It should default to the master branch. Click the Downloads button and
select Download .tar.gz. Double-click the tarball to unzip it.

Alternatively, install git from http://git-scm.com and do the following.

Make a specific repository directory somewhere, e.g. :file:`~/QGIS/QGIS`, and cd
into it. The following will read-only clone the master branch to the directory:

::

  git init
  git remote add -f -t master -m master qgisupstream git://github.com/qgis/QGIS.git
  git merge qgisupstream
  


Configure the build
-------------------

CMake supports out of source build so we will create a 'build' dir for the
build process. OS X uses ${HOME}/Applications as a standard user app folder (it
gives it the system app folder icon). If you have the correct permissions you
may want to build straight into your :file:`/Applications` folder. The instructions
below assume you are building into a :file:`${HOME}/Applications` directory.

You have two interactive options for configuring the build: ccmake or run
Terminal commands. ccmake is a curses interface inside Terminal for CMake and
allows a tabular layout for viewing and editing ALL available QGIS source CMake
options. To get started initially run the Terminal method.

In a Terminal cd to the qgis source folder previously downloaded, then:

::

  mkdir build
  cd build
  cmake -D CMAKE_INSTALL_PREFIX=~/Applications \
  -D CMAKE_BUILD_TYPE=MINSIZEREL -D ENABLE_TESTS=FALSE \
  -D WITH_PYSPATIALITE=FALSE \
  -D SPATIALINDEX_LIBRARY=/usr/local/lib/libspatialindex.dylib \
  -D SPATIALINDEX_INCLUDE_DIR=/usr/local/include/spatialindex \
  -D QWT_LIBRARY=/usr/local/qwt-6.0.2/lib/libqwt.dylib \
  -D QWT_INCLUDE_DIR=/usr/local/qwt-6.0.2/include \
  -D BISON_EXECUTABLE=/usr/local/bin/bison \
  ..

.. note:: Don't forget the .. on the last line, which tells CMake to look for
   the source files in one directory up.

After the initial Terminal configure, you can use ccmake to make further changes:

::

  cd build
  ccmake ..

This will automatically find and use the previously installed frameworks, and
the GRASS application if installed.  Remember to change the Qwt version if a
different version was installed, and possibly paths, e.g. for Qwt 6.0.2 installed
as a framework use:

::

  -D QWT_LIBRARY=/usr/local/qwt-6.0.2/lib/qwt.framework/qwt \
  -D QWT_INCLUDE_DIR=/usr/local/qwt-6.0.2/lib/qwt.framework/Headers \

If you want to use a newer PostgreSQL client than the default Mac OS X version,
e.g. install from kyngchaos.com, set the following option to pg_config's path::

  -D POSTGRES_CONFIG=/usr/local/pgsql/bin/pg_config \

To build a local copy of the API docs (see API documentation section above)::

  -D WITH_APIDOC=TRUE \

.. note:: **Snow Leopard**

   To handle 32-bit Qt (Carbon), create a 32bit python wrapper
   script and add arch flags to the configuration:

   ::
   
      sudo cat >/usr/local/bin/python32 <<EOF
      #!/bin/sh
      exec arch -i386 /usr/bin/python2.6 \${1+"\$@"}
      EOF
  
      sudo chmod +x /usr/local/bin/python32
  
      cmake -D CMAKE_INSTALL_PREFIX=~/Applications \
      -D CMAKE_BUILD_TYPE=MINSIZEREL -D ENABLE_TESTS=FALSE \
      -D WITH_INTERNAL_SPATIALITE=FALSE -D WITH_PYSPATIALITE=FALSE \
      -D SPATIALINDEX_LIBRARY=/usr/local/lib/libspatialindex.dylib \
      -D SPATIALINDEX_INCLUDE_DIR=/usr/local/include/spatialindex \
      -D QWT_LIBRARY=/usr/local/qwt-5.2.2/lib/libqwt.dylib \
      -D QWT_INCLUDE_DIR=/usr/local/qwt-5.2.2/include \
      -D BISON_EXECUTABLE=/usr/local/bin/bison \
      -D CMAKE_OSX_ARCHITECTURES=i386 -D PYTHON_EXECUTABLE=/usr/local/bin/python32 \
      ..

.. note:: **Mapserver** 
   
   The QGIS Mapserver feature requires fastcgi support. This is included in

   Leopard and Snow Leopard, but was dropped at Lion. To build the Mapserver
   component on Leopard and Snow, add the following line before the last line in
   the above configuration::

     -D WITH_SERVER=TRUE \

On Lion you are on your own to figure out how to install libfcgi and add fcgi
support to the system Apache. Not recommended for the average user.

.. note:: **Globe Plugin** 

   If you want the Globe plugin (and you compiled and installed OSG/osgEarth),
   add the following lines before the last line in the above configuration:

   ::

     -D WITH_GLOBE=true \
     -D OSGEARTH_INCLUDE_DIR="/Library/Application Support/OpenSceneGraph/Headers" \
     -D OSG_PLUGINS_PATH="/Library/Application Support/OpenSceneGraph/PlugIns" \

.. note:: **Bundling** 
   
   Older Qt versions may have problems with some Qt plugins and
   QGIS. The way to handle this is to bundle Qt inside the QGIS application. The
   default is to bundle Qt (and osg/osgEarth, if configured).

Even better for distribution purposes, to also bundle any extra non-framework,
non-standard, libs (ie postgres' libpq) set the bundle value to 2::

  -D QGIS_MACAPP_BUNDLE=2 \


Building
---------

Now we can start the build process (remember the parallel compilation note at
the beginning, this is a good place to use it, if you can)::

  make -j [#cpus]

If all built without errors you can then install it::

  make install

or, for an /Applications build::

  sudo make install


Post-Install
-------------

A couple things to take care of.

**gpsbabel**

For QGIS to easily find gpsbabel, you need to copy the gpsbabel executable
to the QGIS application. Assuming you installed QGIS in your home folder::

  cp -fp /Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel ~/QGIS.app/Contents/MacOS/bin/

If you installed in :file:`/Applications`, adjust the path accordingly and prefix the
whole command with 'sudo '.

**QGIS Mapserver**

See the QGIS Mapserver wiki page at:
http://hub.qgis.org/projects/quantum-gis/wiki/QGIS_Server_Tutorial

for instructions on setting up Apache fastcgi and testing Mapserver, including
installing the mod-fastcgi that is missing on Lion.


Setting up the WCS test server on GNU/Linux
============================================

**Requires**: Ubuntu / Debian derived distro

These notes are for Ubuntu - other versions and Debian derived distros may
require slight variations in package names.


Preparation
------------

Note the git repo below will change to the default QGIS repo once this work
is integrated into master.

::

  git remote add blazek git://github.com/blazek/Quantum-GIS.git
  git fetch blazek
  git branch --track wcs2 blazek/wcs2
  git checkout wcs2
  cd /var/www/
  sudo mkdir wcs
  sudo chown timlinux wcs
  cd wcs/
  mkdir cgi-bin
  cd cgi-bin/


Setup mapserver
----------------

::

  sudo apt-get install cgi-mapserver

Set the contents of :file:`cgi-bin/wcstest-1.9.0` to:

::

   #! /bin/sh
   MS_MAPFILE=/var/www/wcs/testdata/qgis-1.9.0/raster/wcs.map
   export MS_MAPFILE
   /usr/lib/cgi-bin/mapserv

Then do:

::

   chmod +x cgi-bin/wcstest-1.9.0
   mkdir -p /var/www/wcs/testdata/qgis-1.9.0/raster/
   cd /var/www/wcs/testdata/qgis-1.9.0/raster/
   cp -r /home/timlinux/QGIS/tests/testdata/raster/* .

Edit wcs.map and set the shapepath to this::

  SHAPEPATH "/var/www/wcs/testdata/qgis-1.9.0/raster"

Then create :file:`/var/www/wcs/7-wcs.qgis.org.conf` setting the contents to this:

::

  <VirtualHost *:80>
  ServerName wcs.qgis.org
  ServerAdmin tim@linfiniti.com
  
  LogLevel warn
  LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" \"%{forensic-id}n\"" combined
  CustomLog /var/log/apache2/wcs_qgis.org/access.log combined
  ErrorLog /var/log/apache2/wcs_qgis.org/error.log
  
  DocumentRoot /var/www/wcs/html
  
  ScriptAlias /cgi-bin/ /var/www/wcs/cgi-bin/
  <Directory "/var/www/wcs/cgi-bin">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
        Order allow,deny
        Allow from all
  </Directory>
  
  RewriteEngine on
  RewriteRule /1.9.0/wcs /cgi-bin/wcstest-1.9.0 [PT]
  
  </VirtualHost>


Create a home page
------------------

::

  mkdir html
  vim html/index.html

Set the contents to:

::

  This is the test platform for QGIS' wcs client. You can use these services
  from QGIS directly (to try out WCS for example) by pointing your QGIS to:
  http://wcs.qgis.org/1.9.0/wcs


Now deploy it
-------------

::

  sudo mkdir /var/log/apache2/wcs_qgis.org
  sudo chown www-data /var/log/apache2/wcs_qgis.org
  cd /etc/apache2/sites-available/
  sudo ln -s /var/www/wcs/7-wcs.qgis.org.conf .
  cd /var/www/wcs/
  sudo a2ensite 7-wcs.qgis.org.conf
  sudo /etc/init.d/apache2 reload


Debugging
----------

::

  sudo tail -f /var/log/apache2/wcs_qgis.org/error.log


Setting up a Jenkins Build Server
====================================

**Assumption**: You know how to make a working build environment and want to
deploy it under Jenkins for continuous integration testing now.

These notes are terse, I will expand on them later as the need arises. The 
procedure is:

- Install Jenkins and get it configured according to your own preferences
- Make sure you have the git, github, junit etc plugins installed. A complete
  list of the plugins I have installed follows (note that you almost certainly
  don't need evey plugin listed here):
  
  - External Monitor Job Type Plugin
  - LDAP Plugin
  - pam-auth
  - javadoc
  - ant
  - Jenkins Subversion Plug-in
  - Git Plugin
  - Maven 2 Project Plugin
  - Jenkins SLOCCount Plug-in
  - Jenkins Sounds plugin
  - Jenkins Translation Assistance plugin
  - ruby-runtime
  - Jenkins CVS Plug-in
  - Coverage/Complexity Scatter Plot PlugIn
  - Status Monitor Plugin
  - Git Parameter Plug-In
  - github-api
  - GitHub plugin
  - Jenkins Violations plugin
  - git-notes Plugin
  - Twitter plugin
  - Jenkins Cobertura Plugin
  - Jenkins Gravatar plugin
  - Jenkins SSH Slaves plugin
  
- Create a Job called 'QGIS'
- Use the following options for your job:

  - Job Name: QGIS
  - Job Type: Build a free-style software project
  - Tick enable project based security (you need to elsewhere configure your
    Jenkins security to per project settings)
  - Allow Anonymous user Read and Discover access
  - Set the github project to https://github.com/qgis/QGIS/
  - Set source code management to Git
  - Set repository url to git://github.com/qgis/QGIS.git
  - In advanced repository url settings set refspec to : 

  ::

    +refs/heads/master:refs/remotes/origin/master


  - Set branch to build to master
  - Repository Browser: Auto
  - Build triggers: set to Poll SCM and set schedule to * * * * * (polls every minute)
  - Build - Execute shell and set shell script to:

  ::

    cd build
    cmake ..
    xvfb-run --auto-servernum --server-num=1 \
             --server-args="-screen 0 1024x768x24" \
             make Experimental || true
    if [ -f Testing/TAG ] ; then
       xsltproc ../tests/ctest2junix.xsl \
         Testing/`head -n 1 < Testing/TAG`/Test.xml > \
         CTestResults.xml
    fi


  - Add Junit post build action and set 'Publish Junit test result report' to:
    `build/CTestResults.xml`
  - Email notification: Send separate e-mails to individuals who broke the build
  - Jenkins sounds - set up sounds for Failure, Success and Unstable.
  - Save

Now open the Job dash board and push something to QGIS and wait a minute to
validate automated builds work.

.. note:: You will need to log in to the Jenkins user account and go to
   :file:`/var/lib/jenkins/jobs/QGIS/workspace`, then make a build directory and run
   the initial cmake setup and then do test build. This process is the same as
   described elsewhere in this doc.

I based some of the set up from this nice blog article here:
http://alexott.blogspot.com/2012/03/jenkins-cmakectest.html


Debug output and running tests
=================================

If you are interested in seeing embedded debug output, change the following
CMake option:

::

  -D CMAKE_BUILD_TYPE=DEBUG (or RELWITHDEBINFO)

This will flood your terminal or system log with lots of useful output from
QgsDebugMsg() calls in source code.

If you would like to run the test suite, you will need to do so from the build
directory, as it will not work with the installed/bundled app. First set the
CMake option to enable tests:

::

  -D ENABLE_TESTS=TRUE

Then run all tests from build directory:

::
 
  cd build
  make test

To run all tests and report to http://dash.orfeo-toolbox.org/index.php?project=QGIS

::

  cd build
  make Experimental

You can define the host name reported via 'make Experimental' by setting a CMake
option:

::

  -D SITE="my.domain.org"

To run specific test(s) (see 'man ctest'):

::

  cd build
  # show listing of tests, without running them
  ctest --show-only
  
  # run specific C++ or Python test(s) matching a regular expression
  ctest --verbose --tests-regex SomeTestName


Authors and Acknowledgments
==============================

The following people have contributed to this document:

**Windows MINGW Section**

- Tim Sutton, Godofredo Contreras 2006
- CMake additions Magnus Homann 2007
- Python additions Martin Dobias 2007
- With thanks to Tisham Dhar for preparing the initial msys environment

**Windows MSVC Section (Detailed install)**

- David Willis 2007
- MSVC install additions Tim Sutton 2007
- PostgreSQL, Qt compile, SIP, Python, AutoExp additions Juergen Fischer 2007

**Windows MSVC Section (Simplified install)**

- Tim Sutton 2007
- Juergen Fischer 2007
- Florian Hillen 2010

**OSX Section**

- Tim Sutton 2007
- With special thanks to Tom Elwertowski and William Kyngesburye
- Larry Shaffer 2012

**GNU/Linux Section**

- Tim Sutton 2006
- Debian package section: Juergen Fischer 2008

**WCS Test Server Section**

- Tim Sutton
- Radim Blazek 2012

**Jenkins CI Configuration**: Tim Sutton 2012

**Latex Generator**: Tim Sutton 2011

**Debug Output/Tests Section**: Larry Shaffer 2012, by way of 'Test Friday' Tim Sutton

