
QGIS Development
================

Welcome to the QGIS Development pages


.. _QGIS-bugreporting:

Bugs, Features and Issues
=========================

If you find a bug, please report it!

You need an OSGeo account and login in order to submit bug reports. To get
started, first create `Create an OSGeo4 account
<https://www.osgeo.org/cgi-bin/ldap_create_user.py>`_.

Once you have your account, use `QGIS issue tracking
<http://hub.qgis.org/projects/quantum-gis/issues>`_ to search if the issue
you'd like to report is probably already entered.

Issues
------

Issues are used to report bugs, request enhancements and submit patches. Redmine is more than a bug reporting system. Issues can be associated with a QGIS Milestone, allowing you to see progress towards completion. Completion of a Milestone not only requires closing bugs, but completing other tasks related to a release such as documentation, web site updates, packaging, and announcements.

Filing an Issue
---------------

Before reporting a bug
......................

Before filing a bug, review the currently open issues to make sure that you aren't creating a duplicate. If you have additional information on an issue, you can add it to the existing ticket. Third party plugins might also cause problems. If you have installed any, you should also verify that the problem is still reproducible without them.
Please don't report multiple unrelated bugs in a single bug report.

Plugin bugs
...........

Plugin bugs must be opened in their respective bug tracking system. Check first if the plugin is listed in the `plugin overview <http://hub.qgis.org/projects/qgis-user-plugins/>`_.
If so, click on the plugin name then click "New issue". Otherwise, consult the plugin documentation to find the address of the relevant bug tracking system or a developer to contact.

Steps
.....

To report a bug choose New Issue from the menu bar. Note: You can also request an enhancement or submit a patch using the Ticket system.

Important information needed when opening a ticket:

* Tracker - choose the ticket type from the drop-down list: Bug, Feature (new feature request) or Bounty (ticket for which a bounty has been defined)
* Subject - a short description of the issue
* Description - Provide a full description of the problem including steps to repeat it; if you think the bug could be related to a certain platform version or dependencies package version (GDAL, OGR, GEOS etc) include that as well. If your QGIS crashes if might be useful to include a backtrace (see below).  A very important thing when reporting a bug is to boil down a minimum example that is needed to reproduce the bug. The chances of a bug being addressed in a timely manner is directly related to the speed with which the developer can reproduce the bug. If you make that hard for the developer, chances are the bug will be given up on or ignored for quite a while.
* Priority - provide an estimate of the severity of the problem: Low (a problem which doesn't affect QGIS usefulness), Normal (the default value, applicable to most bugs and nearly all feature requests), High (a bug which has a major effect on the usability of a package), or Blocker (a bug that makes QGIS totally unusable, causes serious data loss or a regression from a previous QGIS version)
* Component - Choose the aspect of the application that is most closely associated with the problem
* Milestone - If this issue affects a particular Milestone in the project choose it from the drop-down list
* Version - Version of QGIS this issue affects
* Platform - Choose the platform you are using 

Before sending the bug, please check the formatting of your report by clicking on "Preview". Please avoid editing existing reports, if not for typos. Better add further comments in any other case.

Creating a backtrace
--------------------

If you have a crash it might be useful to include a backtrace as the bug might be not reproducible on an other machine. On Unix you can create a backtrace using a core dump and gdb. A core dump is a memory dump of the state of the process when the crash happened.
Depending on you distribution the automatic creation of core dumps might be disabled. In that case you only see for instance Segmentation fault and not ``Segmentation fault (core dumped)`` in the shell you started QGIS from and you need to run ``ulimit -c unlimited`` before starting QGIS. You could also include that in your ``.profile``.
Start qgis from the shell and repeat the steps to reproduce the crash. After the crash the core file will be located in the current directory.
To produce a backtrace from it you start ``gdb /path/to/the/qgis/binary core``. The binary is usually ``/usr/bin/qgis`` or ``/usr/bin/qgis.bin`` on Debian with the GRASS plugin installed.
In ``gdb`` you run ``bt`` which will produce the backtrace.

Log output on Windows
---------------------

The nightly build in OSGeo4W_ (package qgis-dev) is built with debugging
output, that you can view with DebugView_.  If the problem is not easy to
reproduce the output might shed some light about where QGIS crashes.

.. _OSGeo4W: http://trac.osgeo.org/osgeo4w
.. _DebugView: http://technet.microsoft.com/en-us/sysinternals/bb896647.aspx

Creating a patch
----------------

To be done

.. _QGIS-roadmap:

Road Map
========

Since QGIS 2.0 further development will occur based on a timebased roadmap.

Odd version numbers (2.1, 2.3 etc) are development versions.

Even version numbers (2.2, 2.4 etc) are release versions.

Release will happen every four month.  In the first three month new development
is taking place.  Then a feature freeze is invoked and the final month is used
for testing, bugfixing, translation and release preparations.  When the release
happens, a branch with a even release number is created and the master branch
advances to the next odd version.  After the release a call for packaging is
issued.

Development phase
-----------------

In the development phase developers work on adding new features for the next
release. Early adopters can use the nightly builds we have for all major
platforms to see the development progress, do preliminary testing and provide
bug reports and their thoughts to help with development.

Feature freeze
--------------

In the feature freeze phase new features are not allowed in anymore and the
focus of everyone moves from enhancing QGIS to stablizing it.  This also turns
the nightly builds effectively into :ref:`prereleases <QGIS-prereleases>`.

**Users** should start extensive testing of these prereleases in their
environment to verify that there are no issues, they wouldn't want to see in
the upcoming release.  All such issues should be reported (see `Bugs, Features
and Issues`_).  Everything that goes unnoticed, will also end up in the next
release.  Only in case of serious problems a point release (eg 2.4.1) will
occur.  Therefore testing of the prereleases and reporting issues is very
important.

In the feature freeze **Developers** monitor the hub and start working on
fixing the reported issues.

With the begin of the feature freeze the translation files will be updated so
that **translators** can start their work. Note that this might be an
incremental process as although the features are frozen, bug fixes might still
introduce translation string changes.

.. _QGIS-release-schedule:

Release schedule
----------------

Following is the schedule for 2014

==== ====== =================
Week Date   Event
==== ====== =================
4    24.01  2.1 freeze begins
8    21.02  2.2 is released
21   23.05  2.3 freeze begins
26   27.06  2.4 is released
39   26.09  2.5 freeze begins
43   24.10  2.6 is released
==== ====== =================

.. _QGIS-prereleases:

Location of prereleases / nightly builds
----------------------------------------

======== =============================================================================
Platform Location
======== =============================================================================
Windows  :ref:`Weekly release candidate <QGIS-windows-weekly>` (standalone installer)
\ 	 :ref:`OSGeo4W <QGIS-windows-testing>`
Linux    :ref:`Debian <QGIS-debian-testing>`
\        :ref:`Ubuntu <QGIS-ubuntu-testing>`
MacOS    :ref:`Mac OS <QGIS-macos-testing>`
======== =============================================================================


Development
===========

See INSTALL_


API Documentation
-----------------

There is `API documentation <http://qgis.org/api/>`_ for C++.


Plugin Development
==================

QGIS has a plugin infrastructure. You can add a lot of new functionality by
writing your own plugins.

These plugins can either be written in C++ or in Python

C++ plugin development
----------------------

To learn how to write your first C++ plugin, please go here: :ref:`QGIS-cpp-plugin-development`

Via a script you will generate a plugin stub which can be used further.



Python plugin development
-------------------------

QGIS has a lot to offer for python developers too.

QGIS has python bindings so you can automate tasks in QGIS via python.

Interested in python plugin development, go to :ref:`QGIS-python-plugin-development`
or have a look into the :ref:`PyQGIS-Developer-Cookbook`.

Looking for examples of python plugins, see http://plugins.qgis.org

You can find the QGIS-iface which you can use via python here:

http://qgis.org/api/classQgisInterface.html (for QGIS testing)

http://qgis.org/api/2.0/classQgisInterface.html (for QGIS 2.0)

http://qgis.org/api/1.8/classQgisInterface.html (for QGIS 1.8)

.. _INSTALL: http://htmlpreview.github.io/?https://github.com/qgis/QGIS/blob/master/doc/INSTALL.html

Adding GRASS tools
------------------

:ref:`adding-grass-tools`
