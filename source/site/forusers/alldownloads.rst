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

- Download `OSGeo4W Installer <https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe>`_ and start it
- Select *Advanced Install*,
- navigate to the *Desktop* section
- and pick one or more of the following packages:

  +-------------------+------------------------------+------------------------+-------------------------------------------------------+
  | Release           | Version                      | Package                | Description                                           |
  +===================+==============================+========================+=======================================================+
  | Latest Release    | |version|.x |codename|       | qgis                   | Release                                               |
  |                   | |releasenote|                +------------------------+-------------------------------------------------------+
  |                   |                              | qgis-rel-dev [1]_ [4]_ | Nightly build of the upcoming point release           |
  +-------------------+------------------------------+------------------------+-------------------------------------------------------+
  | Long Term Release | |ltrversion|.x |ltrcodename| | qgis-ltr               | Release                                               |
  | Repository        | |ltrnote|                    +------------------------+-------------------------------------------------------+
  |                   |                              | qgis-ltr-dev [2]_ [4]_ | Nightly build of the upcoming point long term release |
  +-------------------+------------------------------+------------------------+-------------------------------------------------------+
  | Development       | |devversion| master          | qgis-dev [3]_ [4]_     | Nightly build of the development version              |
  +-------------------+------------------------------+------------------------+-------------------------------------------------------+

.. [1] Latest release nightlies SHA: :raw-html:`<span id="qgis-rel-dev"> </span>`
.. [2] Latest long-term release nightlies SHA: :raw-html:`<span id="qgis-ltr-dev"> </span>`
.. [3] Master nightlies SHA: :raw-html:`<span id="qgis-dev"> </span>`
.. [4] Nightlies are debug builds (including debugging output)

..
  .. _QGIS-windows-weekly:

  For users that cannot use OSGeo4W for some reason or just prefer it there is
  also a `weekly snapshot <https://qgis.org/downloads/weekly/?C=M;O=D>`_ of
  qgis-dev from OSGeo4W as *standalone installer* (taken on monday).  In the
  feature freeze phase that also acts as **release candidate**.

Before installing any of the nightly builds note the warning_.

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

Quickstart
..........

.. note: In the section following this one, you will find ALL possible options to
   install different versions of QGIS in different versions of Debian/Ubuntu.

Here you will simply install the latest stable QGIS (|version|.x |codename|)
in your Debian or Ubuntu without having to edit config files.

.. note:: Although you see 'Debian' in some places, this also works for
   'Ubuntu', as one is actually a symlink to the other on our server.

First install some tools you will need for this instructions::

 sudo apt install gnupg software-properties-common

Now install the QGIS Signing Key, so QGIS software from 
the QGIS repo will be trusted and installed::

 wget -qO - https://qgis.org/downloads/qgis-2021.gpg.key | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import
 sudo chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg

Add the QGIS repo for the latest stable QGIS (|version|.x |codename|).

Note: "lsb_release -c -s" in those lines will return your distro name::

 sudo add-apt-repository "deb https://qgis.org/ubuntu $(lsb_release -c -s) main"

Update your repository information to reflect also the just added QGIS one::

 sudo apt update

Now, install QGIS::

 sudo apt install qgis qgis-plugin-grass

.. note:: Add 'qgis-server' to this line if you also want to install QGIS Server


Repositories
............

Default Debian and Ubuntu software repositories often hold older versions of
QGIS.

To have newer versions, you have to add alternative software repositories, by
adding one of the deb-lines below to your /etc/apt/sources.list file.

Our main repository contains multiple lines of packages for several versions of
**Debian and Ubuntu** based on the dependencies the individual distributions
provide.

For Ubuntu we also used to have extra packages in a separate repository that
are based on `ubuntugis <https://launchpad.net/~ubuntugis>`_, which held more
uptodate versions of other GIS packages than Ubuntu itself for LTS versions. If
you want those you also need to include ubuntugis-unstable ppa in your
/etc/apt/sources.list file (see `ubuntugis documentation
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
   - build your own set of packages (see build-debian-packages_).

.. _build-debian-packages: https://github.com/qgis/QGIS/blob/master/INSTALL.md#310-building-debian-packages

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
|                       |                                | [5]_                             |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/ubuntugis-nightly-release     |
|                       |                                | upcoming point                   |                                                |
|                       |                                | release with                     |                                                |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
|                       |                                | [5]_                             |                                                |
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
|                       |                                | [5]_                             |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build of                 | https://qgis.org/ubuntugis-nightly-ltr         |
|                       |                                | upcoming point                   |                                                |
|                       |                                | release with                     |                                                |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
|                       |                                | [5]_                             |                                                |
+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+
| Development Version   | |devversion| master            | Nightly build for                | https://qgis.org/debian-nightly                |
|                       |                                | **Debian and Ubuntu**            | https://qgis.org/ubuntu-nightly                |
|                       |                                | [5]_                             |                                                |
|                       |                                +----------------------------------+------------------------------------------------+
|                       |                                | Nightly build with               | https://qgis.org/ubuntugis-nightly             |
|                       |                                | ubuntugis-unstable dependencies  |                                                |
|                       |                                | [5]_                             |                                                |
+-----------------------+--------------------------------+----------------------------------+------------------------------------------------+

.. [5] nightlies are debug builds (including debug output)

| Next point release: |nextpointreleasedate|
| Next release: |nextreleasedate|
| (more dates see Release Schedule on :doc:`../getinvolved/development/roadmap`)


Supported distribution versions:

+---------------+-------------+-------------------+-----------------------+
| Distribution  | Version     | Codename          | Also available based  |
|               |             |                   | on ubuntugis-unstable |
|               |             |                   | dependencies?         |
+===============+=============+===================+=======================+
| Debian        | 11.x        | bullseye          |                       |
|               +-------------+-------------------+-----------------------+
|               | 10.x        | buster [6]_       |                       |
|               +-------------+-------------------+-----------------------+
|               | sid         | unstable          |                       |
+---------------+-------------+-------------------+-----------------------+
| Ubuntu        | 21.10       | impish
|               +-------------+-------------------+-----------------------+
|               | 21.04 (LTS) | hirsute           |                       |
|               +-------------+-------------------+-----------------------+
|               | 20.10       | groovy            |                       |
|               +-------------+-------------------+-----------------------+
|               | 20.04 (LTS) | focal             | yes                   |
|               +-------------+-------------------+-----------------------+
|               | 18.04 (LTS) | bionic [7]_       | yes                   |
+---------------+-------------+-------------------+-----------------------+

.. [6] only up to 3.18 (GDAL too old for 3.20 in buster)
.. [7] only up to 3.18 (python too old for 3.20 in bionic)

Add the lines for one of the repositories to your ``/etc/apt/sources.list``::

 deb     *repository* *codename* main
 deb-src *repository* *codename* main

Example latest release for Debian unstable::

 deb     https://qgis.org/debian unstable main
 deb-src https://qgis.org/debian unstable main

After that type the commands below to install QGIS::

 sudo apt update
 sudo apt install qgis qgis-plugin-grass

In case you would like to install QGIS Server, type::

 sudo apt update
 sudo apt install qgis-server

.. note:: Please remove all the QGIS and GRASS packages you may have
   installed from other repositories before doing the update.

In case of keyserver errors add the qgis.org repository public key to
your apt keyring, type::

 wget -O - https://qgis.org/downloads/qgis-2021.gpg.key | gpg --import
 gpg --fingerprint 46B5721DBBD2996A

Should output::

 pub   rsa4096 2021-08-09 [SCEA] [expires: 2022-08-09]
       2445 D6B2 54DA C452 A498  989E 46B5 721D BBD2 996A
 uid           [ultimate] QGIS Archive Automatic Signing Key (2021) <qgis-developer@lists.osgeo.org>

After you have verified the fingerprint you can add the key to apt with::

 gpg --export --armor 46B5721DBBD2996A | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import
 sudo chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg

Alternatively you can download the key from a keyserver and add the key to apt
in without manual fingerprint verification::
        
 wget -qO - https://qgis.org/downloads/qgis-2021.gpg.key | sudo gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/qgis-archive.gpg --import
 sudo chmod a+r /etc/apt/trusted.gpg.d/qgis-archive.gpg


Fedora
------

Get packages for any Fedora by typing::

 sudo dnf install qgis python3-qgis qgis-grass qgis-server

Default Fedora software repositories often hold older versions of
QGIS.

To have newer versions or the latest LTR, you have to add alternative software repositories
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

+---------------+-------------+--------------+--------------+
| Distribution  | Version     | QGIS         | GRASS GIS    |
|               |             | version      | version      |
|               |             |              |              |
+===============+=============+==============+==============+
| Fedora        | 33          | 3.20         | 7.8          |
|               +-------------+--------------+--------------+
|               | 34          | 3.20         | 7.8          |
+---------------+-------------+--------------+--------------+

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

+---------------+-------------+--------------+--------------+
| Distribution  | Version     | QGIS         | GRASS GIS    |
|               |             | version      | version      |
|               |             |              |              |
+===============+=============+==============+==============+
| Fedora        | 33          | 3.16         | 7.8          |
|               +-------------+--------------+--------------+
|               | 34          | 3.16         | 7.8          |
+---------------+-------------+--------------+--------------+

More information are available at https://copr.fedorainfracloud.org/coprs/dani/qgis-ltr/

RHEL, CentOS, Scientific Linux
------------------------------

QGIS 1.8
........

Try the ELGIS repository: http://elgis.argeo.org/

.. note:: ELGIS requires the EPEL repo enabled, see
   http://wiki.osgeo.org/wiki/Enterprise_Linux_GIS#Note_about_Fedora.2C_ELGIS_and_EPEL

SUSE / openSUSE
---------------

Latest stable and LTR packages called qgis and qgis-ltr are available in the following repositories:

.. list-table::
 :header-rows: 1

 * - Distribution
   - Repository
 * - Tumbleweed
   - https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Tumbleweed/
 * - Leap 15.2
   - https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.2/
 * - Leap 15.1
   - https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.1/
 * - Factory ARM
   - https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_ARM/
 * - Factory PowerPC
   - https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_PowerPC/
 * - SLE 15 SP1 Backports
   - https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports/
 * - SLE 15 SP1 Backports debug
   - https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports_debug/

All packages include GRASS and Python support.

All openSUSE Geo repositories can be found here:
https://download.opensuse.org/repositories/Application:/Geo/

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

Packages on https://slackbuilds.org/result/?search=qgis

Arch Linux
----------

QGIS stable
...........

Arch Linux is available in official repository : https://www.archlinux.org/packages/community/x86_64/qgis/

Install with::

  pacman -S qgis


QGIS LTR
...........

QGIS Long Term Release is available in AUR (Arch User Repository).

Install with yaourt or other package manager which support AUR::

  yaourt -S qgis-ltr

For bugs and other behaviour, read comments here : https://aur.archlinux.org/packages/qgis-ltr/


QGIS testing
............

QGIS testing is available in AUR (Arch User Repository).

Install with yaourt or other package manager which support AUR::

  yaourt -S qgis-git

For bugs and other behaviour, read comments here : https://aur.archlinux.org/packages/qgis-git

Flatpak
-------

There is an QGIS flatpak for QGIS Stable available, maintained by the flathub community.

For general Linux Flatpak install notes, see https://flatpak.org/setup/

QGIS on Flathub: https://flathub.org/apps/details/org.qgis.qgis

To install::

 flatpak install --from  https://flathub.org/repo/appstream/org.qgis.qgis.flatpakref

Then to run::

 flatpak run org.qgis.qgis

To update your flatpak QGIS::

 flatpak update

On certain distributions, you may also need to install xdg-desktop-portal or xdg-desktop-portal-gtk packages in order for file dialogs to appear.

Flathub files: https://github.com/flathub/org.qgis.qgis and report issues here: https://github.com/flathub/org.qgis.qgis/issues

Note: if you need to install additional Python modules, because they are needed by a plugin, you can install the module with (here installing the urllib3 module)::

 flatpak run --command=pip3 org.qgis.qgis install urllib3 --user


Mac OS X / macOS
================

Official All-in-one, signed installers for macOS High Sierra (10.13) and newer can be downloaded from the `QGIS download page <https://qgis.org/en/site/forusers/download.html>`_.

Alternative builds supporting macOS High Sierra (10.13) and newer are available from `kyngchaos.com <https://www.kyngchaos.com/software/qgis/>`_

.. _QGIS-macos-testing:

QGIS nightly release
--------------------
A nightly updated standalone installer from QGIS master can be downloaded from `here <https://qgis.org/downloads/macos/qgis-macos-nightly.dmg>`_.

Old releases
------------
Previous releases of the official installer can be downloaded from https://qgis.org/downloads/macOS/.

Previous releases of the kyngchaos installer can be downloaded from https://www.kyngchaos.com/software/archive/. The oldest installers support macOS 10.4 Tiger.


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


Android
=======

An old and deprecated not touch optimised release of QGIS for Android can be found on the google play store.

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

Refer to INSTALL_ on how to build and install QGIS from source for the different platforms.

.. _INSTALL: https://github.com/qgis/QGIS/blob/master/INSTALL.md
