
.. _QGIS-roadmap:


Road Map
=========

Releases and development of QGIS follow a timebased schedule.

- Even version numbers (2.18, 3.2 etc) are release versions.

- Odd version numbers (2.99, 3.1 etc) are development versions.

A new release will happen every four months. In the first three months, new 
development is taking place. In the last month before a release, a feature
freeze is invoked and the final month is used for testing, bugfixing, 
translation and release preparations.
When the release happens, a branch with a even release number is created and
the master branch advances to the next odd version. After the release a call
for packaging is issued.

Every third release (starting with 2.8) is a long-term-release (LTR) that is
maintained until the next long-term-release occurs.

.. note::
  During the development of QGIS 3.0 and 3.2, an exception to this schedule
  has been put into place. See the roadmap below for adjusted information.

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

In the first four month after it's release a new LTR is also the current LR.
In this phase the new LTR doesn't replace the previous LTR in the LTR
repositories.  This happens as soon as a new LR is released.

The 2.18 release will replace the 2.14 release as LTR, but not replace 2.14 in
the LTR package repositories before 3.0 is released.


Schedule:

===== ======= ========= ========== ==== =====
Event Latest  Long-Term Date       Week Weeks
              (repos)              #
===== ======= ========= ========== ==== =====
PR    2.18.4  2.14.12   24.02.2017 8    4
PR    2.18.5  2.14.13   24.03.2017 12   2
EPR   2.18.6            07.04.2017 14   2
PR    2.18.7  2.14.14   21.04.2017 16   4
LTR   2.18.8  2.14.15   19.05.2017 20   4
EPR   2.18.9            26.05.2017 21   3
PR    2.18.10 2.14.16   23.06.2017 26   4
PR    2.18.11 2.14.17   21.07.2017 29   4
PR    2.18.12 2.14.18   18.08.2017 33   6
FF    (2.99)            18.08.2017 33   6
LR    3.0.0   2.18.12   29.09.2017 39   4
PR    3.0.1   2.18.13   27.10.2017 43   4
PR    3.0.2   2.18.14   24.11.2017 47   3
PR    3.0.3   2.18.15   15.12.2017 50   6
FF    (3.1)             15.12.2018 50   6
PR    3.2.0   2.18.16   26.01.2018 4    4
PR    3.2.1   2.18.17   23.02.2018 8    4
PR    3.2.2   2.18.18   23.03.2018 12   4
PR    3.2.3   2.18.19   20.04.2018 16   4
FF    (3.3)             20.04.2018 16   5
LTR   3.4.0   3.2.4     18.05.2018 20   6
PR    3.4.1   3.2.5     29.06.2018 26   4
PR    3.4.2   3.2.6     27.07.2018 30   4
PR    3.4.3   3.2.7     24.08.2018 34   4
FF    (3.5)             24.08.2018 34   5
PR    3.6.0   3.2.8     21.09.2018 38   5
LR    3.6.1   3.2.9     26.10.2018 43   4
PR    3.6.2   3.2.10    30.11.2018 48   2
PR    3.6.3   3.2.11    14.12.2018 50   6
===== ======= ========= ========== ==== =====

Event legend:

===== =================================================
Event Description
===== =================================================
LTR   Long term release, begin of new development phase
LR    Regular release, begin of new development phase
FF    Feature freeze, end of development phase
PR    Point release of latest release and LTR branch
EPR   Extra Point release
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

