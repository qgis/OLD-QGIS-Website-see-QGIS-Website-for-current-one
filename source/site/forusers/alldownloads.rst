
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
possible to install both the latest stable version and/or the development
(nightly) version.

The OSGeo4W repository contains a lot of software from OSGeo projects.
QGIS and all dependencies are included, along with Python, GRASS, GDAL, etc.
The installer is able to install from internet or just download all needed
packages beforehand.
The downloaded files are kept in a local directory for future installations.
Steps are:

- Download OSGeo4W Installer and start it

- Select *Advanced Install*,

- navigate to the *Desktop* section and

- pick the *qgis* (release) and/or *qgis-dev* (nightly build) package.

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
Packages like qgis-grass (or qgis-plugin-grass), qgis-mapserver can be
skipped initially, or installed only when you need them.

Below you find instructions to install per distribution.  For most distro's
there are instructions to install QGIS stable and instructions to install a
cutting edge QGIS testing build (note the warning_).


Ubuntu
------

Default Ubuntu software repositories often hold older versions of QGIS. To have the most up-to-date version, add the official QGIS repository to your sources.list file:

For Ubuntu 14.04 (Trusty), type::

 sudo sh -c 'echo "deb http://qgis.org/debian trusty main" >> /etc/apt/sources.list' 

 sudo sh -c 'echo "deb-src http://qgis.org/debian trusty main " >> /etc/apt/sources.list' 

(*For previous versions of Ubuntu, see the list below*)

Then, add the qgis.org repository public key to
your apt keyring (this prevents keyserver errors but might not be necessary) ::

 gpg --keyserver keyserver.ubuntu.com --recv DD45F6C3

 gpg --export --armor DD45F6C3 | sudo apt-key add -

Now install QGIS::

 sudo apt-get update 

 sudo apt-get install qgis python-qgis 

If you want the GRASS plugin make sure to install the optional package::

 sudo apt-get install qgis-plugin-grass

QGIS stable
...........

.. note:: The following packages are only produced once shortly after a new
   version has been released.  As not yet released ubuntu versions can have
   library changes the packages might sooner or later be broken, when the
   development in ubuntu moves on.  If that's the case you can either move to a
   stable ubuntu version and use the released packages for it, rebuild the
   packages for the current state of debian (see INSTALL_ or switch to the
   testing packages which are rebuild on regular basis.

.. _INSTALL: http://htmlpreview.github.io/?https://github.com/qgis/QGIS/blob/master/doc/INSTALL.html

Repositories for plain Ubuntu:
^^^^^^^^^^^^^^^^

Trusty Tar (14.04 LTS)::

 deb     http://qgis.org/debian trusty main
 deb-src http://qgis.org/debian trusty main

Utopic Unicorn (14.10)::

 deb     http://qgis.org/debian utopic main
 deb-src http://qgis.org/debian utopic main

Vivid Vervet (15.04)::

 deb     http://qgis.org/debian vivid main
 deb-src http://qgis.org/debian vivid main

Precise Pangolin (12.04 LTS)::

 deb     http://qgis.org/debian precise main
 deb-src http://qgis.org/debian precise main

 VIA ubuntugis:

The ubuntugis_ project provides newer versions of various FOSSGIS packages,
QGIS being one of them.

If you want to use those packages, remove the http://qgis.org/debian lines
from your sources.list and upgrade updated dependencies by typing::

 sudo apt-get install python-software-properties
 sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
 sudo apt-get update
 sudo apt-get install qgis python-qgis qgis-plugin-grass

.. _ubuntugis: https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable

.. _QGIS-ubuntu-testing:

QGIS testing
............

Note the warning_.

On plain Ubuntu:
^^^^^^^^^^^^^^^^

Nightly builds of QGIS testing are available from following repository (i386
and amd64):

Trusty Tar (14.04 LTS)::

 deb     http://qgis.org/debian-nightly trusty main
 deb-src http://qgis.org/debian-nightly trusty main

Saucy Salamander (13.10)::

 deb     http://qgis.org/debian-nightly saucy main
 deb-src http://qgis.org/debian-nightly saucy main

Utopic Unicorn (14.10)::

 deb     http://qgis.org/debian-nightly utopic main
 deb-src http://qgis.org/debian-nightly utopic main

Vivid Vervet (15.04)::

 deb     http://qgis.org/debian-nightly vivid main
 deb-src http://qgis.org/debian-nightly vivid main

Precise Pangolin (12.04 LTS)::

 deb     http://qgis.org/debian-nightly precise main
 deb-src http://qgis.org/debian-nightly precise main

Based on dependencies from ubuntugis:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are also nightly builds that depend on updated dependencies found in
ubuntugis.
Be sure to remove the http://qgis.org/debian ones first, otherwise you'll end
up with a mix of dependencies.

Trusty Tar (14.04 LTS)::

 deb     http://qgis.org/ubuntugis-nightly trusty main
 deb-src http://qgis.org/ubuntugis-nightly trusty main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu trusty main

Precise Pangolin (12.04 LTS)::

 deb     http://qgis.org/ubuntugis-nightly precise main
 deb-src http://qgis.org/ubuntugis-nightly precise main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu precise main

Debian
------

To add the public key for any of the http://qgis.org debian repositories below, type::

 gpg --recv-key DD45F6C3
 gpg --export --armor DD45F6C3 | sudo apt-key add -


QGIS stable
...........

.. note:: The packages are only produced once shortly after a new version has
   been released.  As unstable and not yet released debian versions can have
   library changes the packages might sooner or later be broken, when the
   development in debian moves on.  If that's the case you can either move to a
   stable debian version and use the released packages for it, rebuild the
   packages for the current state of debian (see INSTALL_) or switch to the
   testing packages which are rebuild on regular basis.

Packages for Debian *Wheezy, Jessie and Unstable* for i386 and amd64 are
available at:

Wheezy (7.x)::

 deb     http://qgis.org/debian wheezy main
 deb-src http://qgis.org/debian wheezy main

Jessie (8.x; testing, not yet released)::

 deb     http://qgis.org/debian jessie main
 deb-src http://qgis.org/debian jessie main

Unstable::

 deb     http://qgis.org/debian sid main
 deb-src http://qgis.org/debian sid main


Add the lines for one of the repositories to your
``/etc/apt/sources.list`` file (see below to choose the appropriate one) and
type::

 sudo apt-get update
 sudo apt-get install qgis python-qgis qgis-plugin-grass

.. note:: Please remove all the QGIS and GRASS packages you may have
   installed from other repositories before doing the update.


.. _QGIS-debian-testing:

QGIS testing
............

Note the warning_.

Nightly builds of QGIS testing are available from following repository (i386
and amd64):

Wheezy (7.x)::

 deb     http://qgis.org/debian-nightly wheezy main
 deb-src http://qgis.org/debian-nightly wheezy main

Jessie (8.x)::

 deb     http://qgis.org/debian-nightly jessie main
 deb-src http://qgis.org/debian-nightly jessie main

Sid (Unstable)::

 deb     http://qgis.org/debian-nightly sid main
 deb-src http://qgis.org/debian-nightly sid main

Although the nightly builds can be used to test newer versions,
they are mainly meant to test, if the newer qgis versions still build fine on
the various distributions using the various (older) versions of libraries
found there.
Therefore it is not intended to build versions that depend on more current
libraries.
That means if you need current qgis version with more up to date libraries
you will have to build them yourself.


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

Latest openSUSE package called qgis2 is available for 13.1, 13.2, Factory_PowerPC 
and Tumbleweed (32 and 64bit).
Add the following repository to your installation manager together with the
openSUSE VERSION you work with (e.g. openSUSE_13.2).
::

 http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS testing
............

A regularly updated development package from qgis master called qgis-master
is available for 13.1, 13.2, Factory_PowerPC and Tumbleweed (32 and 64bit).
Add the following repository to your installation manager together with the
openSUSE VERSION you work with (e.g. openSUSE_13.1).
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

Alpha and nightly builds as well as further documentation can be obtained at
http://hub.qgis.org/android-qgis/Download/

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

