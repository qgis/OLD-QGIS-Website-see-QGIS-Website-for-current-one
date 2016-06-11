
.. _QGIS-bugreporting:

Bugs, Features and Issues
=========================

QGIS is a largely volunteer driven project, and is the work of a dedicated
team of developers, documenters, translators and supporters.
Despite the efforts of the team to release QGIS without bugs, there may remain
some bugs. If you find a bug or want new features to be added, please report it!

Two different means are offered to report bugs, request enhancements and submit
patches to the project:

* `Redmine trac <http://hub.qgis.org/projects/quantum-gis>`_ for issues
  related to QGIS applications
* and GitHub for `the web site <https://github.com/qgis/QGIS-Website/issues>`_ 
  and `the documentation <https://github.com/qgis/QGIS-Documentation/issues>`_
  matters.

For questions, please contact the :ref:`QGIS-mailinglists`.

Reports on applications
-----------------------

You need an OSGeo account and login in order to submit bug reports on QGIS 
applications (QGIS Desktop, QGIS Browser and QGIS Server). 
To get started, first `Create an OSGeo account
<https://www.osgeo.org/cgi-bin/ldap_create_user.py>`_.

Once you have your account, use `QGIS issue tracking
<http://hub.qgis.org/projects/quantum-gis/issues>`_ to check if the issue
you'd like to report is not already entered.

.. note:: On the `OSGeo userid page <http://www.osgeo.org/osgeo_userid>`_ you can
 find more information about the OSGeo id we use. For example to 
 `change your password <https://www.osgeo.org/cgi-bin/auth/ldap_edit_user.py>`_
 or email address. Lost your password? Then request a password reset
 via info at osgeo.org

Issues
......

Issues are used to report bugs, request enhancements and submit patches. 
Redmine is more than a bug reporting system. Issues can be associated 
with a QGIS Milestone, allowing you to see progress towards completion. 
Completion of a Milestone not only requires closing bugs, but 
completing other tasks related to a release such as documentation, 
web site updates, packaging, and announcements.

Filing an Issue
...............

Before reporting a bug
^^^^^^^^^^^^^^^^^^^^^^

Before filing a bug, review the currently open issues to make sure that 
you aren't creating a duplicate. If you have additional information on an issue, 
you can add it to the existing ticket. Third party plugins might also cause problems. 
If you have installed any, you should also verify that the problem is 
still reproducible without them.
Please don't report multiple unrelated bugs in a single bug report.

Plugin bugs
^^^^^^^^^^^

Plugin bugs must be opened in their respective bug tracking system. 
Check first if the plugin is listed in the 
`plugin overview <http://hub.qgis.org/projects/qgis-user-plugins/>`_.
If so, click on the plugin name then click "New issue". 

Most of the plugins are published in the official `QGIS Plugins repository 
<http://plugins.qgis.org/plugins/>`_. If the plugin is available, you'll find 
in its presentation a link to its bug tracker. Otherwise, consult the plugin 
documentation to find the address of the relevant bug tracking system 
or a developer to contact.

Steps
^^^^^

To report a bug choose New Issue from the menu bar. Note: You can also request 
an enhancement or submit a patch using the Ticket system.

Important information needed when opening a ticket:

* **Tracker** - choose the ticket type from the drop-down list: Bug, Feature 
  (new feature request) or Bounty (ticket for which a bounty has been defined)
* **Subject** - a short description of the issue
* **Description** - Provide a full description of the problem including steps 
  to repeat it; if you think the bug could be related to a certain platform 
  version or dependencies package version (GDAL, OGR, GEOS etc) include that 
  as well. If your QGIS crashes if might be useful to include a backtrace 
  (see below). A very important thing when reporting a bug is to boil down 
  a minimum example that is needed to reproduce the bug. 
  The chances of a bug being addressed in a timely manner is directly related 
  to the speed with which the developer can reproduce the bug. If you make 
  that hard for the developer, chances are the bug will be given up on 
  or ignored for quite a while.
* **Priority** - provide an estimate of the severity of the problem: 
  Low (a problem which doesn't affect QGIS usefulness), 
  Normal (the default value, applicable to most bugs and nearly all feature requests), 
  High (a bug which has a major effect on the usability of a package), 
  or Blocker (a bug that makes QGIS totally unusable, causes serious 
  data loss or a regression from a previous QGIS version)
* **Component** - Choose the aspect of the application that is most closely
  associated with the problem
* **Milestone** - If this issue affects a particular Milestone in the project
  choose it from the drop-down list
* **Version** - Version of QGIS this issue affects
* **Platform** - Choose the platform you are using

Before sending the bug, please check the formatting of your report by clicking 
on "Preview". Please avoid editing existing reports, if not for typos. 
Better add further comments in any other case.

Creating a backtrace
....................

If you have a crash it might be useful to include a backtrace as the bug might
be not reproducible on an other machine.

On Linux QGIS automatically tries to use ``gdb`` to connect to the crashing
process to produce a backtrace. But some distributions disable the possiblity
to connect debuggers to a running processes. In that case ``gdb`` only
produces a rather useless message like::

 QGIS died on signal 11Could not attach to process. 
 If your uid matches the uid of the target process, 
 check the setting of /proc/sys/kernel/yama/ptrace_scope, or try
 again as the root user. 
 For more details, see /etc/sysctl.d/10-ptrace.conf
 ptrace: Operation not permitted.
 No thread selected
 No stack.
 gdb returned 0
 Aborted (core dumped)

In that case you should reenable that option by setting
``kernel.yama.ptrace_scope`` to 0 in ``/etc/sysctl.d/10-ptrace.conf`` (or
``/etc/sysctl.conf`` or some other file in ``/etc/sysctl.d/``) and 
run ``sysctl -p`` as root. When you reproduce the crash after that, 
a backtrace will be printed instead.

If you cannot reproduce the crash, there should still be a core dump in the
current directory, that can be analysed after the process has already
terminated. It's called ``core`` (on some systems a dot and the process id is
append to the filename).

On some distributions the creation of core dumps is also disabled. In the
event that you just get ``Aborted`` instead of ``Aborted (core dumped)`` when the 
crash occurs. Then you need to run ``ulimit -c unlimited`` before starting QGIS. 
You can also include that in your ``.profile``, so that it's always enabled when
you login.

To produce a backtrace from the core file, start ``gdb
/path/to/the/qgis/binary core``. The binary is usually ``/usr/bin/qgis`` or
``/usr/bin/qgis.bin`` on Debian with the GRASS plugin installed. In ``gdb``
you run ``bt`` which will produce the backtrace.

Log output on Windows
.....................

The nightly build in OSGeo4W_ (package qgis-dev) is built with debugging
output, that you can view with DebugView_. If the problem is not easy to
reproduce the output might shed some light about where QGIS crashes.


.. _OSGeo4W: http://trac.osgeo.org/osgeo4w
.. _DebugView: http://technet.microsoft.com/en-us/sysinternals/bb896647.aspx


Website and Documentation's reports
------------------------------------

QGIS project provides an active `web site <http://qgis.org>`_ and a rich 
`documentation <http://qgis.org/en/docs/index.html>`_. Despite our efforts,
if you find an out of date information, a wrong or unclear statement 
or miss a valuable information, please feel free to report it.

The main sources of these documents are hosted and managed in GitHub repositories
so in order to report bugs or submit patches, you need a GitHub account and login.

Reporting an Issue
..................

To get started, first `Create a GitHub account <https://github.com/join>`_.

Then, choose the appropriate repository :

* https://github.com/qgis/QGIS-Documentation/issues for QGIS documentation
* https://github.com/qgis/QGIS-Website/issues for the web site

Check if the issue you'd like to report is not already entered.

Click **New Issue**, type a title and a clear description for your issue.

When you're finished, click **Submit new issue**.

Submitting a Patch
..................

In addition to issue report, you can help to fix them. Fixing issues is done 
in GitHub through pull requests. You need to `fork the repository 
<https://help.github.com/articles/working-with-forks/>`_ you want to 
contribute to and submit pull requests.

You can find a few guidelines that will help you to easily get your patches  
and pull requests into QGIS projects at :ref:`submit_patch`. And more widely, 
You may need to read :ref:`git_access`. 

.. note:: 
  A ``Fix me`` link is provided at the bottom of any page of the web site
  to help you directly improve this page and submit pull request.
  
  This option is also available in the footer of the Testing documentation.
  
