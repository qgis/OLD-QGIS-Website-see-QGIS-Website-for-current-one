
.. _QGIS-download:

QGIS Installers
===============

How to obtain QGIS?

QGIS is freely available on Windows, Linux, MacOS X, BSD, and Android.

We recommend installing the packages of the released software.

To evaluate the upcoming release and to allow non-developers to support
development we also provide testing packages (note the
warning_).

In the feature frozen phase preceding a release (see
:ref:`QGIS-release-schedule`) these packages are effectively **pre-releases,
which we strongly urge users to test**.

.. _QGIS-windows-testing:

Windows
=======

For Windows installers please go to
`The main installers page <./download.html>`_.

For new users we recommend the standalone installers.

For more advanced QGIS users you can use the OSGeo4W package, which makes it
possible to install several versions in parallel.

The OSGeo4W repository contains a lot of software from OSGeo projects.
QGIS and all dependencies are included, along with Python, GRASS, GDAL, etc.
The installer is able to install from internet or just download all needed
packages beforehand.
The downloaded files are kept in a local directory for future installations.
Steps are:

- Download OSGeo4W Installer and start it

- Select *Advanced Install*,

- navigate to the *Desktop* section and

- and pick one or more of the following packages:

  +-------------------+------------------------------+--------------+-------------------------------------------------------+
  | Release           | Version                      | Package      | Description                                           |
  +===================+==============================+==============+=======================================================+
  | Latest Release    | |version|.x |codename|       | qgis         | Release                                               |
  |                   |                              +--------------+-------------------------------------------------------+
  |                   |                              | qgis-rel-dev | Nightly build of the upcoming point release           |
  +-------------------+------------------------------+--------------+-------------------------------------------------------+
  | Long Term Release | |ltrversion|.x |ltrcodename| | qgis-ltr     | Release                                               |
  |                   |                              +--------------+-------------------------------------------------------+
  |                   |                              | qgis-ltr-dev | Nightly build of the upcoming point long term release |
  +-------------------+------------------------------+--------------+-------------------------------------------------------+
  | Development       | |devversion| Master          | qgis-dev     | Nightly build of the development version              |
  +-------------------+------------------------------+--------------+-------------------------------------------------------+

.. _QGIS-windows-weekly:

For users that cannot use OSGeo4W for some reason or just prefer it there is
also a `weekly snapshot <http://qgis.org/downloads/weekly/?C=M;O=D>`_ of
qgis-dev from OSGeo4W as *standalone installer* (taken on monday).  In the
feature freeze phase that also acts as **release candidate**.

Note the warning_.

.. note:: Don't blindly do a full install of OSGeo4W. Only install QGIS and
   maybe other components you like.  Dependencies will be included
   automatically.  A full install pulls in components that require third party
   additions, which need to be installed manually.  These components render the
   installation unusable without those additions.

Linux
=====

Most linux distributions split QGIS into several packages; you'll probably
need qgis and qgis-python (to run plugins).
Packages like qgis-grass (or qgis-plugin-grass), qgis-server can be
skipped initially, or installed only when you need them.

Below you find instructions to install per distribution.  For most distro's
there are instructions to install QGIS stable and instructions to install a
cutting edge QGIS testing build (note the warning_).


Debian/Ubuntu
-------------

Default Debian and Ubuntu software repositories often hold older versions of
QGIS.

To have newer versions, you have to add alternative software repositories, by
adding one of the deb-lines below to your /etc/apt/sources.list file.

We provide multiple lines of packages for several version of Debian and Ubuntu.

For Ubuntu we also provide packages that are based on ubuntugis, which holds
more uptodate versions of other GIS packages than Ubuntu itself. If you want
those you also need to include ubuntugis ppa in your /etc/apt/sources.list
file.


.. _QGIS-debian-testing:

Lines of packages:

+-----------------------+--------------------------------+------------------------+-------------------------------------------+
| Release               | Version                        | Description            | Repository                                |
+=======================+================================+========================+===========================================+
| Latest Release        | |version|.x |codename|         | Release                | http://qgis.org/debian                    |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Release with           | http://qgis.org/ubuntugis                 |
|                       |                                | ubuntugis dependencies |                                           |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Nightly build of       | http://qgis.org/debian-nightly-release    |
|                       |                                | upcoming point release |                                           |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Nightly build of       | http://qgis.org/ubuntugis-nightly-release |
|                       |                                | upcoming point         |                                           |
|                       |                                | release with           |                                           |
|                       |                                | ubuntugis dependencies |                                           |
+-----------------------+--------------------------------+------------------------+-------------------------------------------+
| Long Term Release     | |ltrversion|.x |ltrcodename|   | Release                | http://qgis.org/debian-ltr                |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Release with           | http://qgis.org/ubuntugis-ltr             |
|                       |                                | ubuntugis dependencies |                                           |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Nightly build of       | http://qgis.org/debian-nightly-ltr        |
|                       |                                | upcoming point release |                                           |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Nightly build of       | http://qgis.org/ubuntugis-nightly-ltr     |
|                       |                                | upcoming point         |                                           |
|                       |                                | release with           |                                           |
|                       |                                | ubuntugis dependencies |                                           |
+-----------------------+--------------------------------+------------------------+-------------------------------------------+
| Development Version   | |devversion|.x Master          | Nightly build          | http://qgis.org/debian-nightly            |
|                       |                                +------------------------+-------------------------------------------+
|                       |                                | Nightly build with     | http://qgis.org/ubuntugis-nightly         |
|                       |                                | ubuntugis dependencies |                                           |
+-----------------------+--------------------------------+------------------------+-------------------------------------------+

Supported distribution versions:

+---------------+-------------+----------+-----------------------+
| Distribution  | Version     | Codename | Also available based  |
|               |             |          | on ubuntugis          |
|               |             |          | dependencies?         |
+===============+=============+==========+=======================+
| Debian        | 7.x         | wheezy   |                       |
|               +-------------+----------+                       |
|               | 8.x         | jessie   |                       |
|               +-------------+----------+                       |
|               | unstable    | sid      |                       |
+---------------+-------------+----------+-----------------------+
| Ubuntu        | 14.04 (LTS) | trusty   | yes                   |
|               +-------------+----------+-----------------------+
|               | 15.10       | wily     |                       |
|               +-------------+----------+                       |
|               | 15.04       | vivid    |                       |
|               +-------------+----------+-----------------------+
|               | 12.04 (LTS) | precise  | yes                   |
+---------------+-------------+----------+-----------------------+

Add the lines for one of the repositories to your ``/etc/apt/sources.list``::

 deb     *repository* *codename* main
 deb-src *repository* *codename* main

Example latest release for Debian jessie::

 deb     http://qgis.org/debian jessie main
 deb-src http://qgis.org/debian jessie main

If you use one of our ubuntugis based repositories you also need to add
following line::

 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu *codename* main

After that type::

 sudo apt-get update
 sudo apt-get install qgis python-qgis qgis-plugin-grass

.. note:: Please remove all the QGIS and GRASS packages you may have
   installed from other repositories before doing the update.

In case of keyserver errors add the qgis.org repository public key to
your apt keyring, type::

 wget -O - http://qgis.org/downloads/qgis-2015.gpg.key | gpg --import
 gpg --fingerprint 3FF5FFCAD71472C4

Should output::

 pub   2048R/D71472C4 2015-08-19 [expires: 2016-08-18]
      Key fingerprint = D004 063C BF60 B252 6363  19AA 3FF5 FFCA D714 72C4
 uid                  QGIS Archive Automatic Signing Key (2015) <qgis-developer@lists.osgeo.org>
 sub   2048R/3B45F5E8 2015-08-19 [expires: 2016-08-18]

After you have verified the fingerprint you can add the key to apt with::

 gpg --export --armor 3FF5FFCAD71472C4 | sudo apt-key add -

Alternatively you can download the key from a keyserver and add the key to apt
in one go (without manual fingerprint verification)::

 sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 3FF5FFCAD71472C4


Fedora
------

QGIS stable
...........

Get packages for any Fedora by typing::

 sudo yum update
 sudo yum install qgis qgis-python qgis-grass qgis-mapserver

Currently Fedora 20 ships QGIS 2.0 and Fedora 21 ships QGIS 2.6.

There is an alternative repository for QGIS 2.8.1 on Fedora 20 and Fedora 21
::

 sudo wget fedora.vitu.ch/QGIS/qgis.repo -P /etc/yum.repos.d/
 sudo rpm --import http://fedora.vitu.ch/Fedora/RPM-GPG-Key-vitu
 sudo yum update
 sudo yum install qgis qgis-python qgis-grass
 # For mapserver on Fedora 20
 sudo yum install qgis-mapserver
 # For mapserver on Fedora 21
 sudo yum install qgis-server

QGIS testing
............

Note the warning_.

A newer version might be available in the testing repository -- usually around
one week::

 yum install --enablerepo=updates-testing qgis qgis-python qgis-grass qgis-mapserver

RHEL, CentOS, Scientific Linux
------------------------------

QGIS 1.8
........

Try the ELGIS repository: http://elgis.argeo.org/

.. note:: ELGIS requires the EPEL repo enabled, see
   http://wiki.osgeo.org/wiki/Enterprise_Linux_GIS#Note_about_Fedora.2C_ELGIS_and_EPEL

QGIS stable
...........

QGIS stable can be installed from an alternative repository.
Python support is strongly limited due to old dependencies.
Note: It requires, that ELGIS and EPEL are also installed.
::

 sudo wget fedora.vitu.ch/EL/qgis.repo -P /etc/yum.repos.d/
 sudo rpm --import http://fedora.vitu.ch/Fedora/RPM-GPG-Key-vitu
 sudo yum update
 sudo yum install qgis qgis-python qgis-grass qgis-mapserver

openSUSE
--------

QGIS stable
...........

Latest stable openSUSE package called qgis is available for 13.1 and 13.2 
(32 and 64bit). Add the following repository to your installation manager 
together with the openSUSE VERSION you work with (e.g. openSUSE_13.2).
::

 http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS LTR (Long Term Release)
............................

Long Term Release package for openSUSE called qgis-ltr is available for 13.1 
and 13.2 (32 and 64bit). Add the following repository to your installation 
manager together with the openSUSE VERSION you work with (e.g. openSUSE_13.2).
::

 http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS testing
............

A regularly updated development package from qgis master called qgis-master
is available for 13.1 and 13.2 (32 and 64bit). Add the following repository 
to your installation manager together with the openSUSE VERSION you work with
(e.g. openSUSE_13.2).
::

  http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

Mandriva
--------

QGIS stable
...........

Current::

 urpmi qgis-python qgis-grass

Slackware
---------

QGIS stable
...........

Packages on http://qgis.gotslack.org

ArchLinux
---------

Archlinux users are encouraged to use the Arch User Repository (AUR).

Information about available versions, bugs and archlinux specific
instructions can be found at: https://aur.archlinux.org/packages/?O=0&K=qgis


MacOS X
=======

A single installer package is available for both OS X Lion (10.7) and Snow
Leopard (10.6).

QGIS stable
-----------

Installing QGIS stable in OS X requires separate installation of several
`dependency frameworks <http://www.kyngchaos.com/software/frameworks>`_
(GDAL Complete and GSL).
GRASS http://www.kyngchaos.com/software/grass is supported with this version.
Some common Python modules http://www.kyngchaos.com/software/python are also
available for common QGIS plugin requirements.

QGIS download page on KyngChaos http://www.kyngchaos.com/software/qgis
(framework requirements listed there) has more information.

.. _QGIS-macos-testing:

QGIS testing
------------

QGIS testing builds (Nightly build) at http://qgis.dakotacarto.com are
provided by Dakota Cartography.

Note the warning_.

FreeBSD
=======

QGIS stable
-----------

To compile QGIS from binary packages type
::

 pkg install qgis

QGIS testing
------------

To compile QGIS from sources in FreeBSD you need to type
::

 cd /usr/ports/graphics/qgis
 make install clean

Note the warning_.

Android
=======

There is an experimental version available on google play store.

https://play.google.com/store/apps/details?id=org.qgis.qgis

.. warning::
   There is currently no support for Android 5. Best support is given for
   Android 4.3 and 4.4.x.
   This is a direct port of the QGIS desktop application. It is only slightly
   optimized for touch devices and therefore needs to be carefully evaluated
   for its suitability in day-to-day use. There are other apps available which
   are designed and optimized specifically for touch devices.

QGIS Testing warning
====================

.. _warning:

.. warning::
   QGIS testing packages are provided for some platforms in
   addition to the QGIS stable version.
   QGIS testing contains unreleased software that is currently being worked
   on.
   They are only provided for testing purposes to early adopters
   to check if bugs have been resolved and that no new bugs have been
   introduced.  Although we carefully try to avoid breakages, it may at any
   given time not work, or may do bad things to your data.
   Take care. You have been warned!

