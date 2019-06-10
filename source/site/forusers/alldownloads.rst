.. role:: raw-html(raw)
   :format: html

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

For more advanced QGIS users you can use OSGeo4W packages, which make it
possible to install several versions in parallel.

The OSGeo4W repository contains a lot of software from OSGeo projects.
QGIS and all dependencies are included, along with Python, GRASS, GDAL, etc.
The installer is able to install from internet or just download all needed
packages beforehand.
The downloaded files are kept in a local directory for future installations.
Steps are:

- Download OSGeo4W Installer (`32 bit <http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86.exe>`_ or
  `64 bit <http://download.osgeo.org/osgeo4w/osgeo4w-setup-x86_64.exe>`_) and start it
- Select *Advanced Install*,
- navigate to the *Desktop* section
- and pick one or more of the following packages:

  +-------------------+------------------------------+-------------------+-------------------------------------------------------+
  | Release           | Version                      | Package           | Description                                           |
  +===================+==============================+===================+=======================================================+
  | Latest Release    | |version|.x |codename|       | qgis              | Release                                               |
  |                   | |releasenote|                +-------------------+-------------------------------------------------------+
  |                   |                              | qgis-rel-dev [1]_ | Nightly build of the upcoming point release           |
  +-------------------+------------------------------+-------------------+-------------------------------------------------------+
  | Long Term Release | |ltrversion|.x |ltrcodename| | qgis-ltr          | Release                                               |
  | Repository        | |ltrnote|                    +-------------------+-------------------------------------------------------+
  |                   |                              | qgis-ltr-dev [2]_ | Nightly build of the upcoming point long term release |
  +-------------------+------------------------------+-------------------+-------------------------------------------------------+
  | Development       | |devversion| master          | qgis-dev [3]_     | Nightly build of the development version              |
  +-------------------+------------------------------+-------------------+-------------------------------------------------------+

.. [1] Latest release nightlies SHA: 32 bit :raw-html:`<span id="qgis-rel-dev-x86"> </span>`, 64 bit :raw-html:`<span id="qgis-rel-dev-x86_64"> </span>`
.. [2] Latest long-term release nightlies SHA: 32 bit :raw-html:`<span id="qgis-ltr-dev-x86"> </span>`, 64 bit :raw-html:`<span id="qgis-ltr-dev-x86_64"> </span>`
.. [3] Master nightlies SHA: 32 bit :raw-html:`<span id="qgis-dev-x86"> </span>`, 64 bit :raw-html:`<span id="qgis-dev-x86_64"> </span>`

.. _QGIS-windows-weekly:

For users that cannot use OSGeo4W for some reason or just prefer it there is
also a `weekly snapshot <https://qgis.org/downloads/weekly/?C=M;O=D>`_ of
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

Our main repository contains multiple lines of packages for several versions of
**Debian and Ubuntu** based on the dependencies the individual distributions
provide.

For Ubuntu we also have extra packages in a separate repository that are based
on `ubuntugis <https://launchpad.net/~ubuntugis>`_, which holds more uptodate
versions of other GIS packages than Ubuntu itself. If you want those you also
need to include ubuntugis-unstable ppa in your /etc/apt/sources.list file (see
`ubuntugis documentation
<https://trac.osgeo.org/ubuntugis/wiki/UbuntuGISRepository>`_).


.. note:: The release packages are only produced once shortly after a new
   version has been released.  As unstable, not yet released debian versions
   (testing) and ubuntugis-unstable can have library changes the packages might sooner
   or later be broken for these targets, when the development in debian, ubuntu
   or ubuntugis-unstable moves on and their packages used as dependencies in qgis
   change.  In that event you can either

   - move to a stable debian version and use the released packages for it,
   - wait for the next point release (due |nextpointreleasedate|), which
     happens every month and will include the updated dependencies,
   - switch to a nightly repository (available for the **two** release
     branches and master) whose packages are rebuild on regular basis and will also
     pickup the updated dependencies automatically or
   - build your own set of packages (see INSTALL_).

.. _INSTALL: https://htmlpreview.github.io/?https://github.com/qgis/QGIS/blob/master/doc/INSTALL.html#toc11

.. _QGIS-debian-testing:

Lines of packages:

+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+
| Release               | Version                        | Description                      | Repository                                     |
+=======================+================================+==================================+================================================+
| Latest Release        | |version|.x |codename|         | Release for                      | https://qgis.org/debian                        |
|                       | |releasenote|                  | **Debian and Ubuntu**            | https://qgis.org/ubuntu                        |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Release with                     | https://qgis.org/ubuntugis                     |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/debian-nightly-release        |
|                       |                                | upcoming point release           | https://qgis.org/ubuntu-nightly-release        |
|                       |                                | for Debian and Ubuntu            |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/ubuntugis-nightly-release     |
|                       |                                | upcoming point                   |                                                |
|                       |                                | release with                     |                                                |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+
| Long Term Release     | |ltrversion|.x |ltrcodename|   | Release for                      | https://qgis.org/debian-ltr                    |
| Repository            | |ltrnote|                      | **Debian and Ubuntu**            | https://qgis.org/ubuntu-ltr                    |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Release with                     | https://qgis.org/ubuntugis-ltr                 |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/debian-nightly-ltr            |
|                       |                                | upcoming point release           | https://qgis.org/ubuntu-nightly-ltr            |
|                       |                                | for Debian and Ubuntu            |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/ubuntugis-nightly-ltr         |
|                       |                                | upcoming point                   |                                                |
|                       |                                | release with                     |                                                |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+
| Development Version   | |devversion| master            | Nightly build for                | https://qgis.org/debian-nightly                |
|                       |                                | **Debian and Ubuntu**            | https://qgis.org/ubuntu-nightly                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build with               | https://qgis.org/ubuntugis-nightly             |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+

| Next point release: |nextpointreleasedate|
| Next release: |nextreleasedate|
| (more dates see Release Schedule on :doc:`../getinvolved/development/roadmap`)


Supported distribution versions:

+---------------+-------------+-------------------+-----------------------+-------+
| Distribution  | Version     | Codename          | Also available based  | with  |
|               |             |                   | on ubuntugis-unstable | 3D    |
|               |             |                   | dependencies?         | [6]_  |
+===============+=============+===================+=======================+=======+
| Debian        | 9.x         | stretch [4]_      |                       |       |
|               +-------------+-------------------+-----------------------+-------+
|               | 10.x        | buster            |                       | yes   |
|               +-------------+-------------------+-----------------------+-------+
|               | sid         | unstable          |                       | yes   |
+---------------+-------------+-------------------+-----------------------+-------+
| Ubuntu        | 19.04       | disco             |                       | yes   |
|               +-------------+-------------------+-----------------------+-------+
|               | 18.10       | cosmic            |                       | yes   |
|               +-------------+-------------------+-----------------------+-------+
|               | 18.04 (LTS) | bionic            | yes                   | yes   |
|               +-------------+-------------------+-----------------------+-------+
|               | 16.04 (LTS) | xenial [4]_ [5]_  | yes                   |       |
+---------------+-------------+-------------------+-----------------------+-------+

.. [4] only up to 3.4 (3.6 requires Qt 5.9 and above)
.. [5] only with ubuntugis-unstable (3.4 requires GDAL2)
.. [6] 3D requires Qt 5.9 and above

Add the lines for one of the repositories to your ``/etc/apt/sources.list``::

 deb     *repository* *codename* main
 deb-src *repository* *codename* main

Example latest release for Debian unstable::

 deb     https://qgis.org/debian unstable main
 deb-src https://qgis.org/debian unstable main

After that type the commands below to install QGIS::

 sudo apt-get update
 sudo apt-get install qgis python3-qgis qgis-plugin-grass

In case you would like to install QGIS Server (note that it's not a common practice
to install both client and server applications on the same machine), type::

 sudo apt-get update
 sudo apt-get install qgis-server python3-qgis

.. note:: Please remove all the QGIS and GRASS packages you may have
   installed from other repositories before doing the update.

In case of keyserver errors add the qgis.org repository public key to
your apt keyring, type::

 wget -O - https://qgis.org/downloads/qgis-2017.gpg.key | gpg --import
 gpg --fingerprint CAEB3DC3BDF7FB45

Should output::

 pub   2048R/BDF7FB45 2017-08-16 [expires: 2019-08-16]
       Key fingerprint = 61E0 A086 749E 463E DE50  2255 CAEB 3DC3 BDF7 FB45
 uid                  QGIS Archive Automatic Signing Key (2017) <qgis-developer@lists.osgeo.org>
 sub   2048R/E959BBCF 2017-08-16 [expires: 2019-08-16]

After you have verified the fingerprint you can add the key to apt with::

 gpg --export --armor CAEB3DC3BDF7FB45 | sudo apt-key add -

Alternatively you can download the key from a keyserver and add the key to apt
in one go (without manual fingerprint verification)::
        
 sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45


Fedora
------

Get packages for any Fedora by typing::

 sudo dnf install qgis qgis-python qgis-grass qgis-server

Default Fedora software repositories often hold older versions of
QGIS.

To have newer versions, you have to add alternative software repositories
based on the version you want to install (stable, LTR or testing).

QGIS stable
...........

Enable the repository::

 sudo dnf copr enable dani/qgis

After that type the commands below to install QGIS::

 sudo dnf install qgis python3-qgis qgis-grass

In case you would like to install QGIS Server (note that it's not a common practice
to install both client and server applications on the same machine), type::

 sudo dnf install qgis-server python3-qgis

This repository also provides a copy of SAGA 2.3.1 compatible with Processing.
It can be installed with the following commands::

 sudo dnf install saga

+---------------+-------------+--------------+--------------+-------+
| Distribution  | Version     | QGIS         | GRASS GIS    | with  |
|               |             | version      | version      | 3D    |
|               |             |              |              |       |
+===============+=============+==============+==============+=======+
| Fedora        | 28          | 3.6          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 29          | 3.6          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 30          | 3.6          | 7.6          | yes   |
+---------------+-------------+--------------+--------------+-------+

More information are available at https://copr.fedorainfracloud.org/coprs/dani/qgis/

QGIS LTR (Long Term Release)
............................

Enable the repository::

 sudo dnf copr enable dani/qgis-ltr

After that type the commands below to install QGIS::

 sudo dnf install qgis python3-qgis qgis-grass

In case you would like to install QGIS Server (note that it's not a common practice
to install both client and server applications on the same machine), type::

 sudo dnf install qgis-server python3-qgis

This repository also provides a copy of SAGA 2.3.1 compatible with Processing.
It can be installed with the following commands::

 sudo dnf install saga

+---------------+-------------+--------------+--------------+-------+
| Distribution  | Version     | QGIS         | GRASS GIS    | with  |
|               |             | version      | version      | 3D    |
|               |             |              |              |       |
+===============+=============+==============+==============+=======+
| Fedora        | 28          | 3.4          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 29          | 3.4          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 30          | 3.4          | 7.6          | yes   |
+---------------+-------------+--------------+--------------+-------+

More information are available at https://copr.fedorainfracloud.org/coprs/dani/qgis-ltr/

QGIS testing
............

Enable the repository::

 sudo dnf copr enable dani/qgis-testing

After that type the commands below to install QGIS::

 sudo dnf install qgis python3-qgis qgis-grass

In case you would like to install QGIS Server (note that it's not a common practice
to install both client and server applications on the same machine), type::

 sudo dnf install qgis-server python3-qgis

+---------------+-------------+--------------+--------------+-------+
| Distribution  | Version     | QGIS         | GRASS GIS    | with  |
|               |             | version      | version      | 3D    |
|               |             |              |              |       |
+===============+=============+==============+==============+=======+
| Fedora        | 28          | 3.7          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 29          | 3.7          | 7.4          | yes   |
|               +-------------+--------------+--------------+-------+
|               | 30          | 3.7          | 7.6          | yes   |
|               +-------------+--------------+--------------+-------+
|               | rawhide     | 3.7          | 7.6          | yes   |
+---------------+-------------+--------------+--------------+-------+

Testing builds are updated on a weekly basis.
More information are available at https://copr.fedorainfracloud.org/coprs/dani/qgis-testing/

RHEL, CentOS, Scientific Linux
------------------------------

QGIS 1.8
........

Try the ELGIS repository: http://elgis.argeo.org/

.. note:: ELGIS requires the EPEL repo enabled, see
   http://wiki.osgeo.org/wiki/Enterprise_Linux_GIS#Note_about_Fedora.2C_ELGIS_and_EPEL

openSUSE
--------

QGIS stable
...........

Latest stable openSUSE package called qgis is available for 13.1, 13.2, 
Leap_42.1, Leap_42.2 and Tumbleweed (32 and 64bit).  Add the following 
repository to your installation manager, where <VERSION> is for example 'openSUSE_Tumbleweed'.
::

 https://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS LTR (Long Term Release)
............................

Long Term Release package for openSUSE called qgis-ltr is available for 13.1, 
13.2, Leap_42.1, Leap_42.2 and Tumbleweed (32 and 64bit). Add the following 
repository to your installation manager, where <VERSION> is for example 'openSUSE_Tumbleweed'.
::

 https://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

All packages include GRASS and Python support.

QGIS testing
............

A regularly updated development package from qgis master called qgis-master
is available for 13.1, 13.2, Leap_42.1, Leap_42.2 and Tumbleweed (32 and 64bit). 
Add the following repository to your installation manager, 
where <VERSION> is for example 'openSUSE_Tumbleweed'.
::

  https://download.opensuse.org/repositories/Application:/Geo/<VERSION>/

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

QGIS stable
...........

Archlinux is available in official repository : https://www.archlinux.org/packages/community/x86_64/qgis/

Install with :

pacman -S qgis


QGIS LTR
...........

Qgis Long Term Release is available in AUR (Arch User Repository).

Install with yaourt or other package manager which support AUR :

yaourt -S qgis-ltr

For bugs and other behaviour, read comments here : https://aur.archlinux.org/packages/qgis-ltr/


QGIS testing
............

Qgis testing is available in AUR (Arch User Repository).

Install with yaourt or other package manager which support AUR :

yaourt -S qgis-git

For bugs and other behaviour, read comments here : https://aur.archlinux.org/packages/qgis-git


Mac OS X / macOS
================

Installation instructions are in the ReadMe on the disk image. Downloads are on the QGIS download page.

QGIS current
------------

The current QGIS package uses the `python.org Python 3.6 <http://www.python.org/>`_, at least version 3.6.5, the "macosx10.9" build - other distributions are not supported. Install packages in the numbered order.  Especially note that Python must be installed before the GDAL Complete package and QGIS, else the GDAL and other needed Python modules will not be installed.

QGIS stable
-----------

The stable package uses the system Python 2.7 - other distributions are not supported. It also requires the NumPy and Matplotlib packages on the disk image. Install packages in the numbered order. If an older major version is being upgraded (2.16 or older), delete QGIS.app from your Applications folder before installing this version.

Other Python modules for plugins to use are available from `kyngchaos.com <http://www.kyngchaos.com/software/python>`_.

Standalone Installer
--------------------

A standalone installer is available at `<https://lutraconsulting.github.io/qgis-mac-packager/>`_.

.. _QGIS-macos-testing:

FreeBSD
=======

QGIS stable
-----------

To install QGIS from binary packages type
::

 pkg install qgis

Or to customize compilation options, you can build it from FreeBSD ports
::

 cd /usr/ports/graphics/qgis
 make install clean



QGIS LTR
-----------

To install QGIS from binary packages type
::

 pkg install qgis-ltr

Or to customize compilation options, you can build it from FreeBSD ports
::

 cd /usr/ports/graphics/qgis-ltr
 make install clean



Flatpak
=======

There is an *experimental* QGIS flatpak for QGIS Stable available.

For general Linux Flatpak install notes, see https://flatpak.org/setup/

QGIS on Flathub: https://flathub.org/apps/details/org.qgis.qgis

To install::

 flatpak install --from  https://flathub.org/repo/appstream/org.qgis.qgis.flatpakref

Then to run::

 flatpak run org.qgis.qgis

To update your flatpak QGIS::

 flatpak update

Flathub files: https://github.com/flathub/org.qgis.qgis


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

Installing from Source
======================

Refer to the `INSTALL guide <http://htmlpreview.github.io/?https://raw.github.com/qgis/QGIS/master/doc/INSTALL.html>`_ on how to build and install QGIS from source for the different platforms.
