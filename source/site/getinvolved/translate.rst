.. _translate-qgis:

Translation
===========

.. _translate-gui:

Application (GUI)
-----------------

The translation of the user interface (GUI) is managed by the :ref:`Translation
team lead <gui-translation>`.
Have a look at the :ref:`QGIS Governance <gui-translation>` to find out who is
in charge of guiding you.

If you want to find out if your language is already present in QGIS or who is
currently working on your language you have to take a look in the
:menuselection:`Help -> About -> Translators` Box in the QGIS Desktop
Application.

You will also find the progress of the translation there (but remember in
every "stable" version it will always stay at the same level).
For finding the current percentage of translation you will either have to
install the nightly build of QGIS or checkout the source code of QGIS and
start translating there.

.. _mailinglist-translation-gui:

Translators Mailing list
........................

If you plan to contribute to an existing language or you want to translate
the QGIS GUI into a not yet existing language and for any other related
questions, please contact the Translation Team Leader
(see :ref:`Organigram <gui-translation>`) or subscribe with the
`qgis-gui-translation-team <http://lists.osgeo.org/mailman/listinfo/qgis-tr>`_
mailing list.

After subscribing to the mailing list you are able to send a mail directly to
qgis-tr@lists.osgeo.org asking for help.

We strongly encourage anyone dealing with translations to join this list and
promise that it is usually a very low traffic mailing list.

The other available mailing list can be found at :ref:`QGIS-mailinglists`.

Becoming a translator
.....................

The QGIS project is always looking for people who are willing to invest some
more time translating QGIS into a foreign language - even perhaps to
coordinate the translation effort.

We are trying to improve our project management process and spread the load
more evenly between people who each have a specific area of responsibility,
so any contribution you have to make will be greatly appreciated.

If you would like to nominate yourself as a coordinator for a new language
please go ahead.
If more than one person nominate themselves as coordinator for the same
language, please contact each other and resolve how you will manage your
efforts.

Please :ref:`contact <community-resources>` the Community Assistant or the GUI
translation team leader to see you name entered in the About Box of QGIS.

Helping with an existing translation
....................................

If you like to help translating QGIS into a your language please assign
to the :ref:`translators mailing list <mailinglist-translation-gui>` and ask who
is already working on that language to coordinate and collaborate.

To start QGIS with the appropriate localization, run qgis with the option
--lang=<language code> or change localization in QGIS under
:menuselection:`Settings -> Options -> Locale`.

.. _howto-translate-gui:

HOWTO translate
...............

The QGIS interface is natively programmed in English. However, it is designed
to be translated into any language quite easily. At this moment over fifty
other languages are already available (though not all well maintained).

All available languages are listed in the QGIS About dialog. It also shows
how much of it has been translated yet. The entire interface contains over
ten thousand pieces of text and a complete translation will take days if not
weeks to be finished. Besides that, the rapid development of the application
continuously causes new and edited texts to be translated. A huge effort and
your help will be appreciated!

Transifex
^^^^^^^^^

The web-based translating platform Transifex is used for all QGIS
translations; the desktop application itself (or GUI), the documentation and
the web site. So the first thing you need is an account to login and get
started.

Get an account
^^^^^^^^^^^^^^

- Go to www.transifex.com and create a new account
- Verify your account by the link in the email you will receive
- Login
- Choose your role as “Translator” and answer some other questions about yourself
- At your dashboard page click “Join an existing organisation” and search for “qgis”

Some QGIS organisations are listed now, among them are QGIS Desktop, Website and
Documentation.

- Choose in which part of the project you would like to participate
- You can be part of all projects and help everywhere too
- If the language of your choice is listed, click it and request to join the team.
- If your language is not listed yet, click “Request language” and choose your
  language. Keep in mind that translating the entire Desktop Application will take
  days of work, if not weeks!

Now you will need to wait for the maintainers to process your request. You will be
notified by email when your request has been accepted.

Note on new languages
^^^^^^^^^^^^^^^^^^^^^

With requesting a new language please bear in mind that we try to make it as simple
as possible. Just ask for the language you want to translate (regardless in which
country you reside). Only if there are notable differences in the languages (for
example portuguese in Portugal in Brazil) we will create its own version.

