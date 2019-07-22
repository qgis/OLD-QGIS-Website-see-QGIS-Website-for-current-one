.. _changelog22:


Changelog for QGIS 2.2
======================

Change log for the next release of QGIS 2.2.0. The emphasis on this
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

Application and Project Options
-------------------------------

Feature: Support for measurement in Nautical Miles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For you seafaring folks out there, you can now measure distances using
nautical miles. To enable this, use the
``Settings -> Options -> Map Tools`` option panel.

|image1|

Data Providers
--------------

Feature: One to many relations support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release sports the ability to define 1:n relations. The relations
are defined in the project properties dialog. Once relations exist for a
layer, a new user interface element in the form view (e.g. when
identifying a feature and opening its form) will list the related
entities. This provides a powerful way to express e.g. the inspection
history on a length of pipeline or road segment. You can find out more
about relations support
`here <http://blog.vitu.ch/10112013-1201/qgis-relations>`__.

|image2|

Feature: DXF Export tool
~~~~~~~~~~~~~~~~~~~~~~~~

A new tool for exporting DXF's has been added to the ``Project`` menu

|image3|

Feature: Paste as new vector layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is a common activity in a GIS to create a sub-selection and then to
create a new layer from the selection. In QGIS you can already do
``save selection as`` to save a layer from your selection, and now
offers functionality that allows you to create a new file or memory
layer from whatever is in your clipboard. Simply select some features,
copy them to your clipboard and then do ``Edit -> Paste features as``
and choose either ``New vector layer`` or ``New memory layer`` from the
submenu. The best part of this new feature is that if you have some Well
Known Text (WKT) features in your clipboard from another app, you can
simply paste them into QGIS as a new layer now.

|image4|

Feature: WMS legend graphic in table of contents and composer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to QGIS 2.2 the WMS data provider was not able to display a legend
in the table of contents' layer list. Similarly no legend could be
displayed in the map composer. QGIS 2.2 addresses both of these issues.

Clicking on the layer's legend will open a frame with the legend at full
resolution. The legend will display contextual information based on your
current scale. The WMS legend will be shown only if the WMS server has
GetLegendGraphic capability. Legend resolution can be modified changing
Canvas & Legend options.

|image5|

Digitising
----------

Feature: Fill ring digitizing tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new tool is used to cut holes in polygons and automatically fill
them with new features. If you hold down ``Ctrl`` when finalising the
feature, the attributes will be taken from parent feature.

|image6|

General
-------

Feature: Recent expressions saved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The expression builder will now remember the last 20 used expressions.

|image7|

Feature: Paste WKT from clipboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS can now paste and create a new feature based on WKT that is found
in the clipboard. Simply copy some WKT and paste into a editable layer.
You can also create a new layer by selecting
``Edit -> Paste As -> New Memory Layer``

Map Composer
------------

Feature: Zebra map border improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now set the colours of the ``Zebra`` border on the map element
in the map composer.

|image8|

Feature: Element rotation support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every type of element in the composer can now be rotated, including
scale bars, tables and legends. For example you can rotate a label on
the composition so that it fits into your page layout better (as
illustrated). Resizing of rotated elements has also been improved.

|image9|

Feature: Composer scale added and ruler improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The appearance of rulers has been improved by adjusting the scale logic
and by adding smaller ruler divisions, and by making vertical rulers use
rotated text. There is also a new composer action for hiding/showing
rulers. You can now quickly zoom to 100% page scale using the new
``Zoom to 100%`` tool on the toolbar. The composer window now lets you
quickly switch the page scaling via a new scale combobox in the status
bar. In addition a new indicator has been added to show you the precise
pixel position of your cursor. The ``Close`` and ``Help`` buttons have
been removed from the bottom of the composer window to give you the
maximum amount of screen space for working with your compositions.

|image10|

Feature: World file generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the composer you can now create georefenced maps! Simply ensure that
you choose the correct map element in the ``Composition tab`` and then
export your map as a PNG file. An accompanying world file will be
written, allowing you to load your exported composition in QGIS as a
raster layer.

|image11|

Feature: Working with multiple items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support has been added for moving and resizing multiple items
simultaneously. You can now hold shift while resizing to maintain an
item's ratio while resizing, or hold control to resize from the item's
centre. Shortcut key also apply to moving items, so holding shift while
moving an item constrains the movement to horizontal or vertical
movement, and holding control temporarily disables item snapping. You
can also hold shift while pressing a cursor key to shift all selected
items by a larger amount.

Feature: Atlas enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now preview the individual pages of the map atlas that will be
generated in composer. While in atlas preview mode you can output the
current page without outputting the entire atlas. You can also tweak the
map extent or scale for each feature while previewing the atlas page.
Atlas map settings have been moved from the atlas panel to the map
properties panel, so now more than one map can be controlled by the
atlas generation. There's a new option to automatically centre an
overview map, which comes in handy when creating atlas based maps.
More context information is now available so that you can adjust your
symbology based on whether the feature is the current atlas feature or
not. See `this article for more
info <http://nathanw.net/2013/12/02/waiting-for-qgis-22-highlighting-current-atlas-feature/>`__.

|image12|

Feature: Improved item selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now select more then one item by clicking and dragging a box to
select them, and there's shortcuts for adding to a selection (holding
shift while dragging), subtracting from a selection (hold control while
dragging) and switching to "within" selection mode (hold alt while
dragging). Shift clicking an already selected item will remove it from
the selection. There's also shortcuts and menu items for selecting all
items, clearing a selection, and inverting a selection. It's also
possible now to select items which are hidden below other items by
control-clicking an item, or by using "Select next item above/below" in
the new composer Edit menu.

Feature: Better navigation of compositions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 2.2 includes many improvements to help you navigate your
compositions. You can now zoom in or out from a composition by using the
mouse scroll wheel. A dedicated pan tool has been added which allows you
to drag the composition around, and you can also switch immediately to
pan mode by holding the space bar or the by holding the mouse scroll
wheel. There's also a new zoom tool which allows you to precisely zoom
to a specific area of your composition. You can also switch to zoom mode
at any time by pressing and holding control-space and drawing a zoom
region on the composition.

Feature: Improved styling of pages and shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now control the style of the composition background using the
full range of QGIS' symbology options. It's now possible to export
compositions with a transparent (or semi-transparent) background. Shape
items (rectangles, triangles and ellipses) can also be styled using the
same options as polygon map layers. You can even style the page
background or shapes by using data defined settings based on the current
atlas feature! There's also a new option for rounding the corners of
rectangle shapes.

QGIS Server
-----------

Feature: WCS Support added to QGIS Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS-Server already supports standards : Web Map Service (WMS version
1.3.0 and 1.1.1) and Web Feature Service (WFS version 1.0.0) and Web
Feature Service with Transaction (WFS-T). With this new release of QGIS,
you can now serve raster layers using the Web Coverage Service (WCS
version 1.0.0)) standard.

|image13|

Symbology
---------

Feature: Gradient fill support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new gradient fill feature lets you create even better cartography
than ever before. The feature has numerous options providing for great
flexibility in how you apply gradients to your features. These include:

-  Two colour or ramp based fills
-  Canvas or object based origin for your gradients
-  Gradients originating from the centroid of a feature
-  Conical, linear and radial gradient types
-  Data defined options (to use an expression or a table column) for all
   gradient properties.

Read more about how to use gradient fills
`here <http://nyalldawson.net/2014/01/waiting-for-qgis-2-2-gradient-fills/>`__.

|image14|

Feature: Label support for palleted rasters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rasters that use a fixed colour pallette (typical for e.g. a land cover
map) can now have category labels assigned which will be shown in the
map legend and in the composer legend.

|image15|

Feature: Colour ramps can be inverted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new option has been added to symbology dialogs that deal with colour
ramps to allow you to invert the colour ramp when it is created.

|image16|

Feature: Copy and Paste in Rule based renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the rule based renderer, you can now right click on a rule and then
copy and paste the rule as a new rule.

|image17|

Feature: On the fly feature generalisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 2.2 introduces support for on the fly feature generalisation. This
can improve rendering times when drawing many complex features at small
scales. This feature can be enabled or disabled in the layer settings.
There is also a new global setting that enables generalisation by
default for newly added layers. **Note:** Feature generalisation may
introduce artefacts into your rendered output in some cases. These may
include slivers between polygons and inaccurate rendering when using
offset based symbol layers.

|image18|

Feature: Anchor points can be set for marker layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When defining symbology with marker layers (e.g. a point layer
symbolized with SVG markers) you can now specify what part of the image
should correspond to the 'anchor point'. For example you can indicate
that the bottom-left corner of the image should coincide with the
position of the feature. You can also use the
``data defined properties`` to have this property set at render time
based on an attribute in the data table for that layer (or an arbitrary
expression).

|image19|

Feature: Thematic maps based on expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Categorized and Graduated thematic maps can now be created using the
result of an expression. In the properties dialog for vector layers the
attribute chooser has been augmented with an expression builder. So now
you no longer need to write the classification attribute to a new column
in your attribute table if you want the classification attribute to be a
composite of multiple fields, or a formula of some sort.

|image20|

Feature: Expression support in symbol diagrams for size and attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now use an expression to define the size and attributes when
using the diagramming capabilities of QGIS. For more info see the Pull
Request here `Pull 1039 <https://github.com/qgis/QGIS/pull/1039>`__

|image21|

Feature: Else rule in rule based renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Rule based renderer now supports a ELSE rule that will be run if
none of the other rules on that level match. Else rules can be nested
just like any other rules.

An example might be:

| ``type = 'water' (style grey)``
|  ``ELSE (style red)``

|image22|

Feature: Inner stroke support for polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support has been added for polygon strokes to be limited to the interior
of the polygon (so that it does not overflow into a neighbouring
polygon).

More information on this feature can be found on the `second part of
this
article <http://nyalldawson.net/2014/01/qgis-two-neat-features-in-2-2/>`__.

|image23|

User Interface
--------------

Feature: Improved properties dialogs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All our properties dialogs have had their main property menus updated so
they look slicker with a inverse coloured side bar. This is purely
cosmetic but should make it easier to know what your current context is
in a dialog.

|image24|

Feature: Expression dialog improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have made some tweaks to the expression dialog - power users can now
hide the operator buttons. There are also now splitters between the
function list and function help areas, and between the expression and
function list area. See the `original pull
request <https://github.com/qgis/QGIS/pull/1073>`__ for details.

|image25|

Feature: New keybindings
~~~~~~~~~~~~~~~~~~~~~~~~

We have updated the keyboard shortcuts in QGIS to make it more efficient
to carry out repetitive tasks.

-  ``ctrl-d`` - Remove selected layers in table of contents
-  ``>`` - Select next vertex when using the node tool
-  ``<`` - Select previous vertex when using the node tool
-  ``Delete`` or ``Backspace`` - delete the selected features (you can
   undo these actions), or a node when using the nodetool.
-  ``F5`` updates the canvas (instead of ctrl-r)

See also `Issue 9094 <http://hub.qgis.org/issues/9094>`__ and `Pull
Request 1010 <https://github.com/qgis/QGIS/pull/1010>`__ for more
details.

|image26|

.. |image0| image:: images/projects/qgis-icon_2.png
.. |image1| image:: images/entries/e1115ca7d43ec24fceaee93f976848583148724f.png
.. |image2| image:: images/entries/0e5e0d1b9dfafe9d64dd5b79866877980f03d099.png
.. |image3| image:: images/entries/452e7692b5b8d2704b4d31067265eb71986d969f.png
.. |image4| image:: images/entries/636db14446809f9e284013113a7b881868591ed3.png
.. |image5| image:: images/entries/6e7cd4849824a802558c0e029f605145d5c885aa.png
.. |image6| image:: images/entries/a8c671765578b660cb5d33cca51efa66ecdb17a4.png
.. |image7| image:: images/entries/90a6b4d181fb2dc7699402d17c1f31522c4f3409.png
.. |image8| image:: images/entries/682c36e3ac96b491e2e0a99a7ff9d94b9e0dc4e5.png
.. |image9| image:: images/entries/700e0999552bc2e2bb2cef86ed14240b05f1da4e.png
.. |image10| image:: images/entries/8b148acf4ef24204b42f14ee7cec43d57c87911a.png
.. |image11| image:: images/entries/d5887511afbe8379f9e240c3763f6b68766cac88.png
.. |image12| image:: images/entries/fe668e5f257efec81db855a91fc7d6febc221261.png
.. |image13| image:: images/entries/b93abbe00e7a32ffb06144ac839619ab50521e5c.png
.. |image14| image:: images/entries/7c4cb6c7ce981ca88b27cd2ae55bc4e503a1234f.png
.. |image15| image:: images/entries/232d60f2aa3accb19eb4da3a08b75ad4c15d068a.png
.. |image16| image:: images/entries/3b1e65705f751bb468cc6495267633d613edbe34.png
.. |image17| image:: images/entries/8e69ef57ed6ae838e813d798312d7d1e39913749.png
.. |image18| image:: images/entries/baa801841f58883d93d0ea6ecb5363da963e4ee2.png
.. |image19| image:: images/entries/ecac63dad2e0da0702b2fe5bc361d68f0c0c6a0f.png
.. |image20| image:: images/entries/cc5cad88da77d1868e394a115606f4b1e6ee8c29.png
.. |image21| image:: images/entries/547b5058efeca906c00ee65ee2504f2669ff52f9.png
.. |image22| image:: images/entries/4c38bdd63e64274d22e6a57a6541920ed47bc4be.png
.. |image23| image:: images/entries/81597f0bc2b848fe39e078a2684c57d44fbda79d.png
.. |image24| image:: images/entries/9d817847f89a3ea7836f86ddff3317040543a78f.png
.. |image25| image:: images/entries/150ae30a6d905e008131c28e4befe862f1bf8ed6.png
.. |image26| image:: images/entries/e8766bfccf2da60b09acde28f5d766eb3d76cec9.png
