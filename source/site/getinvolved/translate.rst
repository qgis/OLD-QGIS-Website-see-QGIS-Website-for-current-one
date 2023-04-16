.. _translate-qgis:

Translation
===========

QGIS is natively developed in English, either for the user interface (GUI) or
for its documentation and web site. However, all these components are available
in many other languages since it is designed to be translated into any language
quite easily.
At this moment about forty languages are already available in the Desktop user
interface and about eighty languages are available in transifex ready to be 
translated. Nearly the same apply for the web site and documentation.

The translation process is managed by the :ref:`Translation Team <gui-translation>`
and all the activities are done under the `Transifex <https://www.transifex.com/>`_
platform.


.. _mailinglist-translation:

Translators Mailing list
------------------------

If you plan to contribute to an existing language or you want to translate
QGIS into a not yet existing language, see :ref:`becoming-translator`.
For any other related questions, please contact the
:ref:`Translation Team Leader <gui-translation>` or subscribe to the `QGIS
Translation mailing list <https://lists.osgeo.org/mailman/listinfo/qgis-tr>`_.

After subscribing to the mailing list you are able to send a mail directly to
qgis-tr@lists.osgeo.org asking for help.

We strongly encourage anyone dealing with translations to join this list and
promise that it is usually a very low traffic mailing list.

The other available mailing lists can be found at :ref:`QGIS-mailinglists`.


.. _translate-gui:

GUI Translation
---------------

The QGIS interface is natively programmed in English. However, at this moment
over forty other languages are already available.

To start QGIS with the appropriate localization, run
``qgis --lang <language code>`` in command line or change localization in QGIS under
:menuselection:`Settings --> Options --> General --> Locale` menu.

If you want to find out if your language is already present in QGIS Applications
or who is currently working on your language you have to take a look in the
:menuselection:`Help --> About --> Translators` Box in the QGIS Desktop Application.

You will also find the progress of the translation there (but remember in
every "stable" version it will always stay at the same level).
For finding the current percentage of translation you will either have to
install the nightly build of QGIS or checkout the source code of QGIS.

The entire interface contains over
ten thousand pieces of text and a complete translation will take days if not
weeks to be finished. Besides that, the rapid development of the application
continuously causes new and edited texts to be translated. A huge effort and
your help will be appreciated!

.. _becoming-translator:

Becoming a translator
---------------------

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

Please contact the :ref:`Translation team leader <gui-translation>` or
:ref:`Community Assistant <community-resources>` to see your name entered in
the About Box of QGIS Desktop.

Transifex
.........

The web-based translating platform Transifex is used for all QGIS
translations; the desktop application itself (or GUI), the documentation and
the web site. So the first thing you need is an account to login and get
started.

Join a Project
..............

- Go to https://explore.transifex.com/qgis/
- You can explore available projects we translate, their target languages
  with various statistics:

  * **QGIS Desktop** for all the pieces of text available in QGIS apps
    (QGIS Desktop and QGIS Server),
  * **QGIS Documentation** for the `official documentation <https://docs.qgis.org/latest/>`_,
  * **QGIS Website** to translate the `current website <https://qgis.org>`_.
- Click on the project you would like to help translate
- Click on :guilabel:`JOIN THIS PROJECT` on the right side.
  You will be prompted to sign up.
- Create your account or connect using a third-party platform account.
  Verify your account by the link in the email you will receive.
- Login
- You then get a popup to select which language you want to help translate to.
- If the language of your choice is listed, select it and press :guilabel:`Join Project`.
- If your language is not listed yet, select it and press :guilabel:`Request language`.
  Keep in mind that translating an entire project will take days of work, if not weeks!

  .. note::
    With requesting a new language please bear in mind that we try to make
    it as simple as possible. Just ask for the language you want to translate
    (regardless in which country you reside). Only if there are notable differences
    in the languages (for example portuguese in Portugal vs Brazil) we will create
    its own version.

- Now you will need to wait for the language coordinator or the project maintainers
  to process your request. You will be notified by email when your request has been
  accepted. If your request has no answer for about a week, please consider writing
  to your language coordinator in Transifex or the :ref:`QGIS Translators mailing list
  <mailinglist-translation>`.
- You can also join any of the other QGIS projects and help everywhere too.


Translate
...........

Once your request is accepted, you are able to translate any text in the project(s)
you've chosen. Simply click on your language, select the chapter you want to
translate and click on Translate. Easy, right?

In order to help you make good translation, some instructions are provided in
the `QGIS Translation Guidelines
<https://docs.qgis.org/testing/en/docs/documentation_guidelines/do_translations.html>`_.
We strongly recommend you to read them.

.. tip:: **Quick access to translatable files in Transifex**

  If you find a wrong or missing translation in the current documentation or web site,
  you can use the ``Fix me`` link at the bottom of the page to reach it sources in
  Transifex and perform any update you wish to.

