
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
When the release happens, a branch with an even release number is created and
the master branch advances to the next odd version. After the release a call
for packaging is issued.

Every third release (starting with 2.8) is a long-term-release (LTR) that is
maintained until the next long-term-release occurs.

Development phase
-----------------

In the development phase, developers work on adding new features for the next
release. Early adopters can use the nightly builds we have for all major
platforms to see the development progress, do preliminary testing and provide
bug reports and their thoughts to help with development.

Feature freeze
--------------

In the feature freeze phase, new features are not allowed in anymore and the
focus of everyone moves from enhancing QGIS to stabilizing it.  This also turns
the nightly builds effectively into :ref:`prereleases <QGIS-prereleases>`.

**Users** should start extensive testing of these prereleases in their
environment to verify that there are no issues, they wouldn't want to see in
the upcoming release.  All such issues should be reported
(see :ref:`Bugs, Features and Issues <QGIS-bugreporting>`).
Everything that goes unnoticed, will also end up in the next
release.  Only in case of serious problems backports to a latest release will
occur.  Therefore testing of the prereleases and reporting issues is very
important.

In the feature freeze, **developers** monitor the bugtracker and start working on
fixing the reported issues and update the **visual changelog** with the features
they added.

With the start of the feature freeze, the translation files will be updated so
that **translators** can start their work. Note that this might be an
incremental process as although the features are frozen, bug fixes might still
introduce translation string changes.

Two weeks before the release, a hard freeze is initiated after which only fixes
to severe problems and regressions introduced after the feature freeze are
allowed in.

The release manager announces this on feature freeze.

Release
-------

On major and minor release dates, the release branch is created and the release
is tagged and tar balls are prepared.  Point releases are just tagged and tar
balls are created.

The packagers are notified that packaging can begin.

Once some packages are available the release can be announced and the website
is updated accordingly.


.. _QGIS-release-schedule:

Release schedule
----------------

The schedule is aligned to produce roughly the same dates for each year given
our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze
phase is at least 5 weeks.  Remainders are used to extend the freeze phase of
LTR releases.

Point releases will happen every month on the latest release branch branch, if
there are backports.   Beginning with the 3.28 release point releases are only
done with new latest releases.

In the first four months after its release, a new LTR is also the current LR.
In this phase, the new LTR doesn't replace the previous LTR in the LTR
repositories.  This happens as soon as a new LR is released.

This schedule is also available as `"iCalendar" </schedule.ics>`_.

.. include:: schedule.inc

.. csv-table:: Event legend
   :header: "Event", "Description"
   :widths: 1, 9
   :name: eventlegend

   "LTR","Long term release, begin of new development phase"
   "LR","Regular release, begin of new development phase"
   "FF","Feature freeze, end of development phase"
   "PR","Point release of latest release and LTR branch"
   "EPR","Extra Point release"
   ":rm-current:`current`",":rm-current:`currently supported releases:` |ltrrelease| and |release|"
   ":rm-next:`next`",":rm-next:`next releases`"

.. _QGIS-prereleases:

Location of prereleases / nightly builds
----------------------------------------

======== =============================================================================
Platform Location
======== =============================================================================
Windows  :ref:`OSGeo4W <QGIS-windows-testing>`
Linux    :ref:`Debian/Ubuntu <QGIS-debian-testing>`
MacOS    :ref:`Mac OS <QGIS-macos-testing>`
======== =============================================================================

.. Windows  :ref:`Weekly release candidate <QGIS-windows-weekly>` (standalone installer)
