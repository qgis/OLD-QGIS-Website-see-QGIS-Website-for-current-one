
.. _QGIS-roadmap:


Road Map
=========

Since QGIS 2.0 further development will occur based on a timebased roadmap.

Odd version numbers (2.1, 2.3 etc) are development versions.

Even version numbers (2.2, 2.4 etc) are release versions.

Release will happen every four month.  In the first three month new development
is taking place.  Then a feature freeze is invoked and the final month is used
for testing, bugfixing, translation and release preparations.  When the release
happens, a branch with a even release number is created and the master branch
advances to the next odd version.  After the release a call for packaging is
issued.

Every third release (starting with 2.8) is a long-term-release (LTR) that is
maintained until the next long-term-release occurs.

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
the upcoming release.  All such issues should be reported 
(see :ref:`Bugs, Features and Issues <QGIS-bugreporting>`). 
Everything that goes unnoticed, will also end up in the next
release.  Only in case of serious problems backports to a latest release will
occur.  Therefore testing of the prereleases and reporting issues is very
important.

In the feature freeze **developers** monitor the hub and start working on
fixing the reported issues.

With the begin of the feature freeze the translation files will be updated so
that **translators** can start their work. Note that this might be an
incremental process as although the features are frozen, bug fixes might still
introduce translation string changes.

.. _QGIS-release-schedule:

Release schedule
----------------

The schedule is aligned to produce roughly the same dates for each year given
our four monthly releases with LTRs in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze
phase is at least 5 weeks.  Remainders are used to extend the freeze phase of
LTR releases.

Point releases will happen every month on the latest release branch and the LTR
branch, if there are backports.

The 2.18 release will replace the 2.14 release as LTR, but not replace 2.14 in
the LTR package repositories before 3.0 is released.


Schedule:

===== ================ ============ ====== =====
Event Version           Date        Week # Weeks
===== ================ ============ ====== =====
PR    2.14.12/2.18.4    24.02.2017   8      4
PR    2.14.13/2.18.5    24.03.2017   12     4
PR    2.14.14/2.18.6    27.04.2017   16     4
LTR   2.14.15/2.18.7    19.05.2017   20     4
PR    2.14.16/2.18.8    23.06.2017   26     4
PR    2.14.17/2.18.9    21.07.2017   29     4
PR    2.14.18/2.18.10   18.08.2017   33     6
FF    (2.99)            18.08.2017   33     6
LR    2.18.11/3.0.0     29.09.2017   39     4
PR    2.18.12/3.0.1     27.10.2017   43     4
PR    2.18.13/3.0.2     24.11.2017   47     3
PR    2.18.14/3.0.3     15.12.2017   50     6
PR    2.18.15/3.0.4     26.01.2018   4      4
PR    2.18.16/3.0.5     23.02.2018   8      4
PR    2.18.17/3.0.6     23.03.2018   12     4
PR    2.18.18/3.0.7     20.04.2018   16     4
PR    2.18.19/3.0.8     18.05.2018   20     6
FF    (3.1)             18.05.2018   20     6
LTR   3.0.9/3.2.0       29.06.2018   26     4
PR    3.0.10/3.2.1      27.07.2018   30     4
PR    3.0.11/3.2.2      24.08.2018   34     4
PR    3.0.12/3.2.3      21.09.2018   38     5
FF    (3.3)             21.09.2018   38     5
LR    3.2.4/3.4.0       26.10.2018   43     4
PR    3.2.5/3.4.1       30.11.2018   48     2
PR    3.2.6/3.4.2       14.12.2018   50     6
PR    3.2.7/3.4.3       25.01.2019   4
===== ================ ============ ====== =====

Event legend:

===== =================================================
Event Description
===== =================================================
LTR   Long term release, begin of new development phase
LR    Regular release, begin of new development phase
FF    Feature freeze, end of development phase
PR    Point release of latest release and LTR branch
===== =================================================


.. _QGIS-prereleases:

Location of prereleases / nightly builds
----------------------------------------

======== =============================================================================
Platform Location
======== =============================================================================
Windows  :ref:`Weekly release candidate <QGIS-windows-weekly>` (standalone installer)
\        :ref:`OSGeo4W <QGIS-windows-testing>`
Linux    :ref:`Debian/Ubuntu <QGIS-debian-testing>`
MacOS    :ref:`Mac OS <QGIS-macos-testing>`
======== =============================================================================

