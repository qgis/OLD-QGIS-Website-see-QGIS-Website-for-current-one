    .. _whoiswho:

Who is who in the project
=========================

QGIS as a Project is currently organised in this way:

Board (Project Steering Committee)
-----------------------------------

The QGIS project is managed by the Board (Project Steering Committee; PSC)
which consists of 7 members (with their individual responsibilities listed in
brackets):

* Tim Sutton (Chair; Testing/QA Manager)
* Paolo Cavallini (Co-Chair; Manager of Plugin Repository) [since January 2008]
* Andreas Neumann (Treasurer; Contact for Sponsorships) [since November 2015]
* Anita Graser (Design Advisor) [since September 2013]
* Richard Duivenvoorde (Infrastructure Manager) [since September 2013]
* Jürgen Fischer (Release Manager) [since September 2013]
* Gary Sherman (Founder and lifetime Honorary Member)

Former members are:

* Marco Hugentobler (until 2016)
* Otto Dassau (Community Advisor) [2007 - 2016]

Read more about the responsibilities of the PSC :ref:`here <psc>`


.. _country-voting-members:

Country Voting Members
----------------------

According to our statutes, for each country user group that is formed, that
group will select a QGIS Country User Group Voting Member to represent
their interests. These voting members are listed :ref:`here<QGIS-usergroups>`.
Please email tim@qgis.org if you have registered a new country user group, or have
changed your user group representative.


.. _community-voting-members:

Community Voting Members
------------------------

According to our statutes, one member from the broader community can be
elected for each country voting member. The following list are the
current community voting members:

* Martin Dobias <wonder.sk[at]gmail.com>
* Nathan Woodrow <madmanwoo[at]gmail.com>
* Matthias Kuhn <matthias[at]opengis.ch>
* Larry Shaffer <larrys[at]dakotacarto.com>
* Nyall Dawson <nyall.dawson[at]gmail.com>
* Giovanni Manghi <giovanni.manghi[at]gmail.com>
* Denis Rouzaud <denis.rouzaud[at]gmail.com>
* Alexander Bruy <alexander.bruy[at]gmail.com>
* Regis Haubourg <regis.haubourg[at]gmail.com>
* Even Rouault <even.rouault[at]spatialys.com>
* Werner Macho <werner.macho[at]gmail.com>
* Vincent Picavet <vincent.ml+qgis[at]oslandia.com>
* Yves Jacolin <yjacolin[at]free.fr>

Added 2017

* Alessandro Pasotti <apasotti[at]gmail.com>
* Victor Olaya <volayaf[at]gmail.com>
* Lene Fischer <lfi[at]ign.ku.dk>
* Paul Blottiere <paul.blottiere[at]oslandia.com>
* Mathieu Pellerin <nirvn.asia[at]gmail.com>
* Luigi Pirelli <luipir[at]gmail.com>
* Alexandre Neto <senhor.neto[at]gmail.com>
* Tom Chadwin <tom.chadwin[at]nnpa.org.uk>
* Marco Hugentobler <marco.hugentobler[at]sourcepole.ch>

.. _release-management:

Release Management
------------------

Current Release Manager:
Jürgen E. Fischer <jef[at]norbit.de>

QGIS Releases are managed by the Release Team (Release Manager and Release
Assistants). Together with numerous contributors, they oversee timely,
regular, stable releases of QGIS on the various supported platforms. The
release team recruits and supports build managers to create packages for
supported platforms and oversee the maintenance of the bug tracking system.

.. _packaging-team:

Packaging Team
..............

QGIS is being packaged for different type of operating systems. The people
responsible for that packages are as following:

* Windows Team: Jürgen E. Fischer <jef[at]norbit.de>, Tim Sutton <tim[at]linfiniti.com>
* OS X Team: William Kyngesburye <kyngchaos[at]kyngchaos.com>,
  Tom Elwertowski <telwertowski[at]comcast.net>
* Linux Team:

  * OpenSuSE RPM Maintainer: Otto Dassau <dassau[at]gbd-consult.de>
  * Fedora RPM Maintainer: Douglas E. Warner <silfreed[at]silfreed.net>
  * Ubuntu Deb Maintainer: Jürgen E. Fischer <jef[at]norbit.de>,
    Jachym Cepicky <jachym.cepicky[at]gmail.com>
  * Debian Deb Maintainer: Jürgen E. Fischer <jef[at]norbit.de>,
    Niccolo Rigacci <qgis[at]rigacci.org> [Lenny]

.. _testing-team:

Testing Team
............

* Ubuntu Linux: Ricardo Soares Garcia <ricardo.garcia.silva[at]gmail.com>, Giovanni
  Manghi <giovanni.manghi[at]faunalia.pt>, Luís de Sousa <luis.a.de.sousa[at]gmail.com>
* Debian Linux: Paolo Cavallini <cavallini[at]cavallini.it>, Pedro Venâncio
  <pedrongvenancio[at]gmail.com>, Ivan Mincik <ivan.mincik[at]gmail.com>
* Windows: Giovanni Manghi <giovanni.manghi[at]faunalia.pt>, Pedro Venâncio
  <pedrongvenancio[at]gmail.com>, Duarte Carreira <dncarreira[at]gmail.com>,
  Andre Mano <andre.s.mano[at]gmail.com>
* OS X: Larry Shaffer <larrys[at]dakotacarto.com>
* Windows 8: Rui Pedro Henriques <henriques.rui[at]gmail.com>

.. _technical-resources:

Technical Resources
-------------------

Current Technical Advisor:
Marco Hugentobler <marco.hugentobler[at]sourcepole.ch>

The Technical Resources are managed by the Technical Manager and Technical
Assistants. They recruit and support code maintainers and provide general
oversight and guidance to the development effort.

.. _code-maintainers:

Code Maintainers
................

Code Maintainers are responsible for discrete areas of the QGIS source code
(core, gui, plugins, providers, tests) and ensure consistency and quality of
code added into the git code repository.

* Core library: Martin Dobias <wonder.sk[at]gmail.com>
* Gui library: Martin Dobias <wonder.sk[at]gmail.com>
* App (dialogs): Tim Sutton <tim[at]linfiniti.com>
* Print composer: Nyall Dawson <nyall.dawson[at]gmail.com>
* PyQGIS: Martin Dobias <wonder.sk[at]gmail.com>
* WMS server: Marco Hugentobler <marco.hugentobler[at]sourcepole.ch>
* WFS/WCS server: René-Luc D'Hont <rldhont[at]gmail.com>
* Python plugins for QGIS Server: Alessandro Pasotti <elpaso[at]itopen.it>
* Access control for QGIS Server: Stephane Brunner <stephane.brunner[at]camptocamp.com>
* Plugin installer: Borys Jurgiel <info[at]borysjurgiel.pl>
* OGR, Postgres-, Oracle- provider: Jürgen E. Fischer <jef[at]norbit.de>
* WMS provider: Jürgen E. Fischer <jef[at]norbit.de>
* WFS provider: Even Rouault <even.rouault[at]spatialys.com>
* QgisWebClient: Andreas Neumann <a.neumann[at]carto.net>
* MSsql provider: Nathan Woodrow <madmanwoo[at]gmail.com>
* Labelling engine: Larry Shaffer <larrys[at]dakotacarto.com>
* Authentication system: Larry Shaffer <larrys[at]dakotacarto.com>
* Diagrams: Matthias Kuhn <matthias.kuhn[at]gmx.ch>
* Attribute table: Matthias Kuhn <matthias.kuhn[at]gmx.ch>
* Processing Toolbox: Victor Olaya <volayaf[at]gmail.com>
* MetaSearch plugin: Tom Kralidis <tomkralidis[at]gmail.com>

.. _community-resources:

Community Resources
-------------------

The QGIS community resources are managed by the Community Team (Community
Manager and Assistants). With numerous contributors they keep contact to the
community, take care of QGIS events, documentation, GUI translations,
and ensure smooth running of the QGIS.org online experience including web
sites, blog, and mailing lists.

Current Community Team Leaders:

* Lene Fischer <lfi[at]ign.ku.dk> (community tasks)
* Yves Jacolin <yjacolin[at]free.fr> (documentation)

Find the list of documentation and website translators at:
https://github.com/qgis/QGIS-Documentation

.. _gui-translation:

Translation
...........

Current Translation Team Lead:
Werner Macho <werner.macho[at]gmail.com>

The QGIS Translation is managed by the Community Assistant (Translation
Team Lead) and supported by additional language specific teams.
Information about the current documentation status and the translation
process are provided at the :ref:`Translators Corner <translate-qgis>`.

Contact : `qgis-community-team <http://lists.osgeo
.org/mailman/listinfo/qgis-community-team>`_ list
or
`QGIS Translation Mailing list
<http://lists.osgeo.org/mailman/listinfo/qgis-tr>`_

.. _press-material:

Press Material + Translation
............................

Current Press Material Team Lead:
Anita Graser <anitagraser[at]gmx.at>

QGIS Press Material and its translations are managed by the Community
Assistant (Press Material Team Lead) and supported by additional language
specific teams. Information about current activities and the translation
process are provided at the Press Centre.

TEAM
----

A successful project requires many people to play many different roles. Some
members write code or documentation, while others are valuable as testers,
submitting patches and suggestions.

The number of Contributors to the project is unbounded. Get involved today.
All contributions (adding code or documentation, fixing typo error, reporting
issues...) to the project are greatly appreciated.

These `individuals <https://github.com/qgis/QGIS/graphs/contributors>`_
are recognised as Contributors to the main code
`github repository <https://github.com/qgis/QGIS>`_.

Follow the lists of maintainers of the `documentation
<https://github.com/qgis/QGIS-Documentation/graphs/contributors>`_ and the
`website <https://github.com/qgis/QGIS-Website/graphs/contributors>`_.
Feel free to join any of those teams.

..
   TODO : add list of translators, bug reporters (is that possible?)

