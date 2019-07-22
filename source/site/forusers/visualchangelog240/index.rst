.. _changelog24:

Changelog for QGIS 2.4
======================

Change log for the next release of QGIS 2.4.0. The emphasis on this
release has been very much on polish and performance - we have added
many new features, tweaks and enhancements to make the user interface
more consistent and professional looking (and hopefully easier to use).
The composer (used for creating print ready maps) has had a lot of work
done to it to make it a more viable platform for creating great
cartographic outputs.

Whenever new features are added to software they introduce the
possibility of new bugs - if you encounter any problems with this
release, please file a ticket `on the QGIS Bug
Tracker <http://hub.qgis.org>`__.

We would like to thank the developers, documenters, testers and all the
many folks out there who volunteer their time and effort (or fund people
to do so).

From the QGIS community we hope you enjoy this release! If you wish to
donate time, money or otherwise get involved in making QGIS more
awesome, please wander along to `qgis.org <https://qgis.org>`__ and lend
a hand!

Finally we would like to thank our official sponsors for the invaluable
financial support they provide to this project:

-  GOLD Sponsor: `Asia Air Survey,
   Japan <http://www.asiaairsurvey.com/>`__
-  SILVER Sponsor: `G.A.I.A. mbH, Germany <http://www.gaia-mbh.de/>`__
-  SILVER Sponsor: `State of Vorarlberg,
   Austria <http://www.vorarlberg.at/>`__
-  BRONZE Sponsor: `www.molitec.it, Italy <http://www.molitec.it/>`__
-  BRONZE Sponsor: `www.argusoft.de, Germany <http://www.argusoft.de>`__
-  BRONZE Sponsor: `www.openrunner.com,
   France <http://www.openrunner.com>`__
-  BRONZE Sponsor: `www.eschenlaub.de,
   Germany <http://www.eschenlaub.de>`__

A current list of donors who have made financial contributions large and
small to the project can be seen on our `donors
list <https://qgis.org/en/site/about/sponsorship.html#list-of-donors>`__.

If you would like to make a donation or sponsor our project, please
visit `our sponsorship
page <https://qgis.org/en/site/about/sponsorship.html#sponsorship>`__ for
details. QGIS is
Free software and you are under no obligation to do so. Sponsoring
QGIS helps us to fund our six monthly developer meetings, maintain
project infrastructure
and fund bug fixing efforts.

.. contents::
   :local:


General
-------

Feature: Generate band name with NetCDF EXTRA\_DIM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NetCDF provided extra dimensional information. This information
provides metadata on each band. These metadata can be used to explain
the name of each band. For example, the bands of a NetCDF file
represents the temperature at a given depth. For the user, it is easier
to select a band with depth information, rather than only the band
number.

|image1|

Feature: Applying scale and offset to raster data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some raster datasources, data are stored as interger with a scale and
an offset in the metadata. The scale and offset can be used to get the
right data. QGIS applies its to raster data to provider to users right
information for legend, histogram and identify.

|image2|

Feature: Quick field field calc bar in attribute table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a great new feature for those working with calculated fields in
vector attribute tables. The new quick calculation bar lets you update
the values in a column in the attribute table quickly and easily.

|image3|

Feature: Colour preview modes in composer and map canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A really innovative feature that has been added to 2.4 is support for
grayscale and colour blindness previews. This allows you to visualise
how people with colour blindness will perceive your cartography and map
layout, or how your map will look if it's printed in grayscale. You can
read more about this new feature
`here <http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/>`__.

|image4|

Feature: QLR QGIS Layer files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added support for QGIS Layer Definition files or simply QLR (see
http://nathanw.net/2014/03/12/qgis-qlr/). QLR file is a file that points
to the data, contains all the styling, and other information. You can
then just add this file and it will do all the other magic for you. QLR
makes it easy to add same layer to multiple map documents, inheriting
all of the properties which have been set and works with any layer
supported in QGIS, expect special plugin layers.

Feature: New expression functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have some new functions available in the expression builder.

-  bounding box (bounds)
-  bounding box width & height (bounds\_width/bounds\_height)
-  min/max x/y coordinates (xmin/xmax/ymin/ymax)
-  new wordwrap function that returns a string wrapped to a
   maximum/minimum number of characters

|image5|

Feature: Copy, paste and drag and drop colours
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now copy, paste, drag and drop colours between any colour input
widget in QGIS. See this
`article <http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/>`__
for more information on how this new feature works. Hex color codes and
rgb strings can also be pasted on to colour buttons to allow importing
colours from outside of QGIS.

|image6|

Feature: Multi-threaded rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is one feature we simply cannot do justice to with a screenshot -
QGIS now supports multi-threaded rendering! What this means is that when
drawing the map, QGIS will split the drawing work between all of the
cores in your CPU, making the process more efficient and responsive. By
**responsive** we mean that you no longer need to wait for the map view
to update before you can pan or zoom again. Also the map display updates
incrementally allowing you to see if the map is positioned correctly
early on in the drawing process. Take a look at `this
article <http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering>`__
for a more detailed overview of the multi-threaded rendering system. You
will find some options in the QGIS settings dialog that allow you to
manage the behaviour of multi-threaded rendering.

|image7|

Labelling
---------

Feature: Label features multiple times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Long lines (such as contour lines or roads) can now be repeatedly
labeled at regular intervals. One can choose between mm and map units
for specifying the repetition interval. At the time of the release there
is still an issue with "merge connected lines to avoid duplicate"
setting.

|image8|

Map Composer
------------

Feature: Improvements to composer picture items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The image item in composer is now 'atlas friendly' - you can use an
**expression to define which image** should be shown for each atlas
page. You can also now set the **resize mode** (zoom, clip, stretch
etc.) for the image in relation to its frame size and dimensions. You
can also specify the placement of the image relative to its frame using
the new **placement** item property.

|image9|

Feature: Predefined scales mode for atlas maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When working with atlas map items, you can now specify a predefined
scale mode for the map. It will use the best fitting option from the
list of predefined scales in you your project properties settings (see
Project -> Project Properties -> General -> Project Scales to configure
these predefined scales).

|image10|

Feature: Improved attribute tables in composer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have made a number of improvements to the ability to display tables
in your composer layouts:

-  Support has been added for reordering columns within a table
-  Added support for expression based columns
-  You can now set the alignment of individual table columns, and also
   specify the alignment for the table's header cells
-  Table contents can be filtered by an expression

|image11|

Feature: General composer improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of additions to the map composer to make life easier
while working in map composition mode:

-  Added button to view current map item extent in main map canvas
-  Ability to export SVG images from composer with layers
-  Set line join and cap style for scalebars
-  Support for setting the line join style for item frames

|image12|

Feature: Improvements to HTML frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTML Frames in the composer have been improved. There is a new **add
frame** button which can be used to manually create multiple linked
frames. We have also improved our page break logic making it less likely
that you will get page breaks that cut through the middle of lines of
text when paginating HTML frames.

|image13|

Plugins
-------

Feature: MetaSearch Catalogue Client Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MetaSearch is a QGIS plugin to interact with metadata catalogue
services, supporting the OGC Catalogue Service for the Web (CSW)
standard. This plugin provides an easy and intuitive approach and
user-friendly interface to searching metadata catalogues within QGIS and
now ships by default with the QGIS core product.

|image14|

Symbology
---------

Feature: Shapeburst fill style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a great new render in QGIS 2.4. The shapeburst renderer will
allow you to fill polygons with a gradient extending from the line edge
towards the polygon interior. You can read more about **shapeburst**
`here <http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4>`__.

|image15|

Feature: Option to shift marker line placement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using a marker line along a line or polygon edge, you can now
specify an **offset** so that the marker line starts a set distance from
the beginning of the line. If a marker line is set to "first vertex" or
"last vertex" mode, than this offset will control how far along the line
from the vertex the marker is placed.

|image16|

Feature: New Inverted Polygon renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new renderer has been added for polygon features, allowing you to
style everything **outside** your polygons. This can be useful for
highlighting areas, or for creating cartographic masks. When used with
new shapeburst style, you can now produce output as shown in the image
for this entry.

**Note:** The new version of plugin mask helps to easily create mask
layers from the current selection, label features only in those areas,
and generate an automatic mask in Atlas map generation.

|image17|

Feature: Saving and recovering styles with Spatialite layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous version was possible to save style with postgres
layers, now will be possible for Spatialite layers too.
This functions allow to embed different styles inside a spatialite
container simplifying sharing data and their presentation.
A video tutorial of this funcionality can be found here
http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/

|image18|

.. |image0| image:: images/projects/qgis-icon_2.png
.. |image1| image:: images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.png
.. |image2| image:: images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.png
.. |image3| image:: images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.png
.. |image4| image:: images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.png
.. |image5| image:: images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.png
.. |image6| image:: images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.png
.. |image7| image:: images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.png
.. |image8| image:: images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.png
.. |image9| image:: images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.png
.. |image10| image:: images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.png
.. |image11| image:: images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.png
.. |image12| image:: images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.png
.. |image13| image:: images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.png
.. |image14| image:: images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.png
.. |image15| image:: images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.png
.. |image16| image:: images/entries/884f1735cee30abc7024f6fc21756b8609770173.png
.. |image17| image:: images/entries/b58dd06d363524d112de7a40748f599730c4276e.png
.. |image18| image:: images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.png
