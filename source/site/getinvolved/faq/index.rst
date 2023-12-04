
====
FAQ
====

Here we collect answers to question which come up very often.

We will start of with this one page, maybe restructure it into sections, or
even more pages if needed


User
====

Downloading issues
------------------

If you are trying to download QGIS and nothing seems to happen, please check your browser's download manager.
It can be usually found as an icon (arrow, stop-watch or pie-chart) at the top-right corner of your browser window.
Click on the icon to see the download progress or cancel the download. The normal procedure with downloads in the
browser is, that it first asks you where to save the file (with a file browser dialogue) and then you have to wait
until the download is finished. Because QGIS install packages, depending on the operating system, can be rather large
you have to be patient. The download size can be anywhere between several hundred megabytes to sometimes more than
one gigabyte (in case of MS Windows MSI packages).

I have to donate in order to download QGIS
------------------------------------------

This is a misconception that we hear from time to time, but it is simply not true. Donating to QGIS is optional.
After downloading QGIS, there is a message appearing, reminding that you can donate to QGIS. However, you can press
"Close this message" and continue downloading without any problem. We want QGIS to be accessible to anyone, no matter
how your financial situation might be. If you are a first-time QGIS user, we recommend that you download, install and test
QGIS first and find out if the software is useful for the tasks you want to solve. Only if you like QGIS and it
substantially helps with your business, tasks or processes, you should think about donating towards QGIS or
supporting it as a sustaining member.

.. _how-to-ask-a-QGIS-question:

How to ask a QGIS question?
---------------------------

If you are going to ask QGIS related question via the :ref:`mailing lists <QGIS-mailinglists>`,
please provide enough information to help others easily understand what your problem is.
Without a clear and precise question, it is very hard to answer for anybody or
takes just too much time because the answer will be a question to you etc etc.
You may provide information such as:

* preferably a descriptive title for your email
* which QGIS version you used at that moment (exact)
* what are you expecting to get
* if applicable, what have you tried and the result you got
* if your question is about something broken, you may also provide:

  * what exactly is the error (if possible: screendump, stacktrace, copy of error text)
  * which Operating System and version
  * how you installed it (osgeo4w? standalone-installer? own build?)
  * at what time did it break (reinstall, new install, system update, project changes)

Keep in mind that the more precise is your question, the quicker and more
accurate can be the answer.

.. note::
   In case of a broken function, you may give a look at `QGIS issue tracker
   <https://github.com/qgis/QGIS/issues>`_ before
   mailing to the list. More information at :ref:`QGIS-bugreporting`.


How are QGIS release names selected?
------------------------------------

After a successful developer meeting in Zurich (Switzerland), we decided that
the next release should be related to it. Since then, all releases have been named
after locations of our developer meetings. 

How to cite QGIS?
-----------------

To cite QGIS in your piece of work, or for an assignment, please use citation type that can be more helpful:


**Cite the QGIS project in general**


QGIS.org, |yeartag|. QGIS Geographic Information System. QGIS Association. http://www.qgis.org


**Cite the QGIS Developers Manual**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System Developers Manual. QGIS Association. 
Electronic document: |devcite|


**Cite the QGIS Installation Guide**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System Installation Guide. QGIS Association. 
Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md


**Cite the QGIS User Guide**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System User Guide. QGIS Association. 
Electronic document: |userguidecite|

**Cite the QGIS Server Documentation**

QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System API Documentation. QGIS Association. 
Electronic document: |servercite|


**Cite the QGIS API Documentation**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System API Documentation. QGIS Association. 
Electronic document: |apicite|





**Preferred format:** `BibTeX <https://en.wikipedia.org/wiki/BibTeX>`_


Example BibTeX entry:

.. parsed-literal::

  <pre>
      @Manual{QGIS_software,
        title = {QGIS Geographic Information System},
        author = {{QGIS Development Team}},
        organization = {QGIS Association},
        year = {|yeartag|},
        url = {https://www.qgis.org},
      }
  </pre>

I created a map with QGIS, do I have to mention QGIS?
-----------------------------------------------------

There is no requirement to mention QGIS for maps produced with it.
It is of course really welcome if would like to add a note saying that the map was produced with QGIS.
"Made with QGIS" or "Map created using the Free and Open Source QGIS" are good examples of such a note.

.. note::
    Do not say ©QGIS as QGIS does not hold copyrights on your work.

Can I open ECW files with QGIS?
-------------------------------

Yes you can... BUT depending on your Operating System, it is more or less difficult.

If you are under Windows and are using the OSGeo4w installer, it is included.

If you are using macOS, you can find the ECW plugin and install instructions at
https://www.kyngchaos.com/software/frameworks

For other instructions, eg look here: https://www.faunalia.eu/en/blog/2019-05-21_ecw_support

Development
===========

Can I compile QGIS myself?
--------------------------

Yes, compiling QGIS from source is possible whatever OS you use (Windows, OS X,
Linux). Please read `Building QGIS from source
<https://github.com/qgis/QGIS/blob/master/INSTALL.md>`_


