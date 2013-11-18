.. _translate-qgis:

Translate QGIS into your Language
=================================

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

.. _mailinglist-translation:

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

The other available mailingslist can be found at :ref:`QGIS-mailinglists`.

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
If more than one person nominates themselves as coordinator for the same
language, please contact each other and resolve how you will manage your
efforts.

Please :ref:`contact <community-resources>` the Community Assistant or the GUI
translation team leader to see you name entered in the about Box of QGIS.

Helping with an existing translation
....................................

If you like to help translating QGIS into a your language please assign
to the :ref:`translators mailing list <mailinglist-translation>` and ask who
is already working on that language to coordinate and collaborate.

To start QGIS with the appropriate localization, run qgis with the option
--lang=<language code> or change localization in QGIS under
:menuselection:`Settings -> Options -> Locale`.

.. _howto-translate-gui:

HOWTO translate GUI
...................

There are different "levels" for you in the way you'd like to contribute.
Following steps are necessary to help translating QGIS user interface.

Get the translatable file
^^^^^^^^^^^^^^^^^^^^^^^^^

Usually it is enough to download the .ts file from the
`github repository <https://github.com/qgis/Quantum-GIS/tree/master/i18n/>`_
Look for your language code which is added at the end of the files: qgis_*
.ts, where * is your language code.
For example the translation file for german language is called qgis_de.ts.
To further specify the language it is sometimes necessary to have two
language codes defined but we'd like to avoid this as much as we can.

If you click on your language a RAW Button will appear on the top right
corner of that window where you can download your language file.

Work on the translatable file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For now it is recommended to use Qt-Linguist for working on the translatable
file.
You can download and install that program (depending on your operating
system) from:

http://qt-apps.org/content/show.php/Qt+Linguist+Download?content=89360

For the different Linux distributions you should find a package called
"qt4-dev-tools" or similar.

You can create the compiled translation file out of your translation with
Linguist by going to :menuselection:`File -> Release (As)` in the Linguist
menu and save it as a .qm version of the translation.
Afterwards you only have to copy this .qm file to the correct folder within
your QGIS installation to see your translation in action.

Once you finished the translation you can send the .ts file to the
:ref:`current translations team leader <governance>` to have it committed to
the source code repository.
At this place we'd like to encourage you to follow the "release often"
principe of open source.

An advanced level of helping with the translations would be to checkout the
source code and create pull requests for the language file on github.

Working with github and checking out the source code is explained in the
:ref:`Developer Section <reference-missing>'

Documentation
-------------

Description of how you can contribute in the translation of the Documentation
are available in the README.md file which gets displayed on
https://github.com/qgis/QGIS-Documentation


Website
-------

Description of how you can contribute in the translation of the Webpage are
available in the README.md file which gets displayed on
https://github.com/qgis/QGIS-Website
