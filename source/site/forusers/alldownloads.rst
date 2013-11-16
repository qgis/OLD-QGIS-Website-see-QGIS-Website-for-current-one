
.. _QGIS-download:

QGIS Installers
===============

How to obtain QGIS?

QGIS is freely available on Windows, Linux, MacOS X, BSD, and Android.

.. warning:: QGIS testing versions are provided for some platforms in addition to the QGIS stable version. QGIS testing contains unreleased software that is currently being worked on. As such they are unsupported and only provided for testing purposes to early adopters to check if bugs have been resolved and that no new bugs have been introduced. At any given time it may not work, or may do bad things to your data. Use at your own risk. You have been warned!

Windows
=======

For Windows installers please go to `The main installers page <./download.html>`_.

For new users we recommend the standalone installers.

For more advanced QGIS users you can use the OSGeo4W package, which makes it 
possible to install both the latest stable version and/or the development (nightly) version (but not the warning above!).

The OSGeo4W repository contains a lot of software from
OSGeo projects. QGIS and all dependencies are included, along with Python, GRASS,
GDAL, etc. The installer is able to install from internet or just download all
needed packages beforehand. The downloaded files are kept in a local directory
for future installations. Steps are::

 Download OSGEO4W Installer
 Start it
 Select **Advanced Install** and then the *qgis* or *qgis-dev* package from the Desktop
  section. Also other libraries can be selected.



Linux
=====

Most linux distributions split QGIS into several packages; you'll probably need 
qgis and qgis-python (to run plugins). Packages like qgis-grass (or qgis-plugin-grass), qgis-mapserver 
can be skipped initially, or installed only when you need them.

Below you find instructions to install per distro. For most distro's there are
instructions to install QGIS stable and instructions to
install a cutting edge QGIS testing build (but mind the warning above!).

Ubuntu
------

Default Ubuntu software repositories often hold older versions of QGIS.

To have newer versions, you have to add alternative software repositories, by
adding one of the deb-lines below to your /etc/apt/sources.list file.
Or add these repositories via your favourite Ubuntu software installation GUI.

Then type::

 sudo apt-get update
 sudo apt-get install qgis python-qgis

If you want the GRASS plugin make sure to install the optional package::

 sudo apt-get install qgis-plugin-grass


In case of keyserver errors. To add the the qgis.org repository public key to your apt keyring, type::

 gpg --keyserver keyserver.ubuntu.com --recv 47765B75
 gpg --export --armor 47765B75 | sudo apt-key add -


QGIS stable
...........

On plain Ubuntu:
^^^^^^^^^^^^^^^^

Saucy::

 deb     http://qgis.org/debian saucy main
 deb-src http://qgis.org/debian saucy main

Raring::

 deb     http://qgis.org/debian raring main
 deb-src http://qgis.org/debian raring main

Quantal::

 deb     http://qgis.org/debian quantal main
 deb-src http://qgis.org/debian quantal main

Precise::

 deb     http://qgis.org/debian precise main
 deb-src http://qgis.org/debian precise main

Lucid::

 deb     http://qgis.org/debian lucid main
 deb-src http://qgis.org/debian lucid main


Via ubuntugis:
^^^^^^^^^^^^^^

The ubuntugis project provides newer versions of various FOSSGIS packages, QGIS being one of them.

Current packages available for lucid, maverick, natty, oneiric, precise and raring.

If you want to use those packages, remove the http://qgis.org/debian lines from your sources.list and
upgrade updated dependencies by typing::

 sudo apt-get install python-software-properties
 sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
 sudo apt-get update
 sudo apt-get install qgis python-qgis qgis-plugin-grass


QGIS testing
............

On plain Ubuntu:
^^^^^^^^^^^^^^^^

Nightly builds of QGIS testing are available from following repository (i386 and amd64):

Quantal::

 deb     http://qgis.org/debian-nightly quantal main
 deb-src http://qgis.org/debian-nightly quantal main

Precise::

 deb     http://qgis.org/debian-nightly precise main
 deb-src http://qgis.org/debian-nightly precise main


Via ubuntugis:
^^^^^^^^^^^^^^

There are also nightly builds that depend on updated dependencies found in ubuntugis.
Be sure to remove the http://qgis.org/debian ones first, otherwise you'll endup with a mix of dependencies.

Raring::

 deb     http://qgis.org/ubuntugis-nightly raring main
 deb-src http://qgis.org/ubuntugis-nightly raring main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu raring main

Quantal::

 deb     http://qgis.org/ubuntugis-nightly quantal main
 deb-src http://qgis.org/ubuntugis-nightly quantal main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu quantal main

Precise::

 deb     http://qgis.org/ubuntugis-nightly precise main
 deb-src http://qgis.org/ubuntugis-nightly precise main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu precise main

Lucid::

 deb     http://qgis.org/ubuntugis-nightly lucid main
 deb-src http://qgis.org/ubuntugis-nightly lucid main
 deb     http://ppa.launchpad.net/ubuntugis/ubuntugis-unstable/ubuntu lucid main


Debian
------

QGIS stable
...........

Packages for Debian *Wheezy, Jessie and Unstable* for i386 and amd64 are
available at:

Wheezy (7.x)::

 deb     http://qgis.org/debian wheezy main
 deb-src http://qgis.org/debian wheezy main

Jessie (8.x) and Sid (Unstable)::

 Jessie and Sid have library changes all the time.
 The QGIS stable package will break at a certain time.
 Nightly/untested builds for QGIS stable would not be 'stable'.

 As an alternative, please run QGIS testing on Jessie and Sid.
 OR 
 compile QGIS stable yourself on Jessie/Sid (see INSTALL)

.. deb     http://qgis.org/debian jessie main
.. deb-src http://qgis.org/debian jessie main


.. deb     http://qgis.org/debian sid main
..  deb-src http://qgis.org/debian sid main

To add the the http://qgis.org repository public key to your apt keyring, type::

 gpg --recv-key 47765B75
 gpg --export --armor 47765B75 | sudo apt-key add -

Then add the lines for one of the repositories to your ``/etc/apt/sources.list``
file (see below to choose the appropriate one) and type::

 sudo apt-get update
 sudo apt-get install qgis python-qgis qgis-plugin-grass

.. note:: Please remove all the QGIS and GRASS packages you may have installed from other repositories before doing the update.


QGIS testing
............

Nightly builds of QGIS testing are available from following repository (i386 and amd64):

Wheezy (7.x)::

 deb     http://qgis.org/debian-nightly wheezy main
 deb-src http://qgis.org/debian-nightly wheezy main

Jessie (8.x)::

 deb     http://qgis.org/debian-nightly jessie main
 deb-src http://qgis.org/debian-nightly jessie main

Sid (Unstable)::

 deb     http://qgis.org/debian-nightly sid main
 deb-src http://qgis.org/debian-nightly sid main

Although the nightly builds can be used to test newer versions, they are mainly
meant to test, if the newer qgis versions still build fine on the various
distributions using the various (older) versions of libraries found there.
Therefore it is not intended to build versions that depend on more current
libraries. That means if you need current qgis version with more uptodate
libraries you will have to build them yourself.



Fedora
------

QGIS stable
...........

Get packages for any Fedora by typing::

 sudo yum update
 sudo yum install qgis qgis-python qgis-grass qgis-mapserver

Currently Fedora 18 and 19 have QGIS 1.8 while Fedora 20 is expected to have QGIS 2.0.

There is an alternative repository for QGIS 2.0 on Fedora 19 ::

 sudo wget fedora.vitu.ch/QGIS/qgis.repo -P /etc/yum.repos.d/
 sudo rpm --import http://fedora.vitu.ch/Fedora/RPM-GPG-Key-vitu
 sudo yum update
 sudo yum install qgis qgis-python qgis-grass qgis-mapserver


QGIS testing
............

A newer version might be available in the testing repository -- usually around
one week::

 yum install --enablerepo=updates-testing qgis qgis-python qgis-grass qgis-mapserver



RHEL, CentOS, Scientific Linux
------------------------------

QGIS 1.8
........

Try the ELGIS repository: http://elgis.argeo.org/

.. note:: ELGIS requires the EPEL repo enabled, see http://wiki.osgeo.org/wiki/Enterprise_Linux_GIS#Note_about_Fedora.2C_ELGIS_and_EPEL

QGIS stable
...........

QGIS stable can be installed from an alternative repository. Note: It requires, that ELGIS
and EPEL are also installed. ::

 sudo wget fedora.vitu.ch/EL/qgis.repo -P /etc/yum.repos.d/
 sudo rpm --import http://fedora.vitu.ch/Fedora/RPM-GPG-Key-vitu
 sudo yum update
 sudo yum install qgis qgis-python qgis-grass qgis-mapserver



openSUSE
--------

QGIS stable
...........

Latest openSUSE package called qgis2 is available for 12.1, 12.2, 12.3, Factory and 
Tumbleweed (32 and 64bit). Add the following repository to your installation manager 
together with the openSUSE VERSION you work with (e.g. openSUSE_12.3). 

::

  http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS testing
............

A regularly updated development package from qgis master called qgis-master is available 
for 12.1, 12.2, 12.3, Factory and Tumbleweed (32 and 64bit). Add the following repository 
to your installation manager together with the openSUSE VERSION you work with (e.g. openSUSE_12.3). 

::

  http://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS 1.8
........

OpenSUSE package for QGIS 1.8 is called qgis. It is available for 12.1,
12.2, 12.3, Factory and Tumbleweed (32 and 64bit). Add the following
repository to your installation manager together with the openSUSE VERSION 
you work with (e.g. openSUSE_12.3).

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

Information about available versions, bugs and archlinux specific instructions can be found at: https://aur.archlinux.org/packages/?O=0&K=qgis



MacOS X
=======

A single installer package is available for both OS X Lion (10.7) and Snow Leopard (10.6).

QGIS stable
^^^^^^^^^^^

Installing QGIS stable in OS X requires separate installation of several
`dependency frameworks <http://www.kyngchaos.com/software/frameworks>`_
(GDAL Complete and GSL). GRASS http://www.kyngchaos.com/software/grass is supported
with this version. Some common Python modules http://www.kyngchaos.com/software/python
are also available for common QGIS plugin requirements.


QGIS download page on KyngChaos http://www.kyngchaos.com/software/qgis (framework
requirements listed there) has more information.


QGIS testing
^^^^^^^^^^^^

QGIS testing builds (Nightly build) at http://qgis.dakotacarto.com are provided by Dakota Cartography.


FreeBSD
=======


QGIS stable
^^^^^^^^^^^

To compile QGIS from binary packages type::

 pkg_add -r qgis


QGIS testing
^^^^^^^^^^^^

To compile QGIS from sources in FreeBSD you need to type::

 cd /usr/ports/graphics/qgis
 make install clean


Android
=======

Alpha and nightly builds as well as further documentation can be obtained at
http://android.qgis.org


