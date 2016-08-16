
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

Point releases will happen every months on the latest release branch and the
LTR branch, if there are backports.

After the release of 2.16 the work on the new major release 3.0 will begin.
This will involve a switch from our fixed release schedule to an open release.

3.0 will involve many wide-ranging changes, so it not clear in advance how much
time it will take.  We think it should take between 8-12 month to get to
3.0.  After that we'll return to the old method.


Schedule:

===== ============= ========== =========== =====
Event Version       Date       Week number Weeks
===== ============= ========== =========== =====
PR    2.8.4/2.12.1  27.11.2015 47
PR    2.8.5/2.12.2  18.12.2015 50
PR    2.8.6/2.12.3  15.01.2016 2
LTR   2.14          26.02.2016 8           14
PR    2.8.7         26.02.2016 8
PR    2.8.8/2.14.1  25.03.2016 12
PR    2.8.9/2.14.2  29.04.2016 17
PR    2.14.3        20.05.2016 20
FF    (2.15)        03.06.2016 22          5
LR    2.16          08.07.2016 27          10
PR    2.14.4        08.07.2016 27
PR    2.14.5/2.16.1 29.07.2016 30
PR    2.14.x/2.16.x 26.08.2016 34
PR    2.14.x/2.16.x 16.09.2016 37
PR    2.14.x/?      21.10.2016 42
PR    2.14.x/?      25.11.2016 47
PR    2.14.x/?      16.12.2016 50
PR    2.14.x/?      13.01.2017 2
PR    2.14.x/?      24.02.2017 8
===== ============= ========== =========== =====

.. FF   (2.17)         16.09.2016 37          5
.. LR    2.18.x        21.10.2016 42
.. (3.5)  DEV   19.05.2017 20          5
.. 3.6    LR    23.06.2017 25          12
.. (3.7)  DEV   15.09.2017 37          5
.. 3.9    LR    20.10.2017 42          12
.. (3.10) DEV   12.01.2018 2           6
.. 3.12   LTR   23.02.2018 8           12
.. (3.13) DEV   18.05.2018 20          5
.. 3.14   LR    22.06.2018 25

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

