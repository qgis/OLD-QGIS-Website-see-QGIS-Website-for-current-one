.. _changelog310:


Changelog for QGIS 3.10
=======================

|image1|

Release date: 2019-11-02

QGIS 3.10 brings an extensive list of new changes and a lot of polishing of existing features - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through donations or contributions to the code documentation, web site and so on.

**Thanks**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to qgis.org and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our :ref:`donors list <list_of_donors>`. If you would like to become an official sustaining member, please visit :ref:`our sustaining members page <QGIS_sustaining_memberships>` for details. Supporting QGIS helps us to fund our bi-annual developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

:raw-html:`<div id="qgissustainingmembersatom"> <!-- to be filled via javascript loading of atom feed --> </div>`

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity.


.. contents::
   :local:

Map Tools
---------

Feature: 3D line lengths shown in identify tool results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Identify Features tool on a 3D linestring now includes the 3d Cartesian length of the line in the results (alongside the existing 2D Cartesian and 2D ellipsoidal lengths).

|image2|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Symbology
---------

Feature: Default resampling setting for newly-added raster layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.10 we've added a new setting for the default resampling mode to use when for newly-added raster datasets. (This setting can be found in the rendering panel of the options dialog).

|image3|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Improved copy/paste of symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We're passionate about making QGIS a user-friendly cartographic tool which is a joy to work with, so we've added a bunch of new shortcuts throughout the interface which allow you to copy and paste symbols from one part of QGIS to another. E.g, you can copy a symbol from a category and paste it directly onto another category, or a layout shape item, or inside the style manager dialog!

|image4|

This feature was funded by `SMEC/SJ <https://www.smec.com/en_au>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: "Center of segment" placement mode for marker and hash line symbol layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added a brand new "Center of segment" mode for placement of marker line or hashed lines symbols. This allows you to place markers or hash lines over the center point of individual line segments, exposing cartographic effects which were not possible before (and improving the quality of layers converted from ArcMap using the `SLYR <https://north-road.com/slyr/>`__ tool).

|image5|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: More flexible data defined offset expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In previous QGIS releases, only string values of the format 'x,y' would be permitted for data-defined symbol and label offsets. We've listened to user feedback that this was confusing, and in QGIS 3.10 we now allow arrays of numbers as a valid expression result for offsets. E.g. "array(3,5)".

|image6|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Labelling
---------

Feature: Create and manage text formats and label settings in QGIS styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.10 we've finally implemented a long-awaited feature, allowing users to manage their own libraries of custom text formats and label settings alongside their existing symbol libraries!

Now, the Style Manager dialog can be used to manage text formats (which store the font, color, buffers, shadows, and backgrounds of text formats) and layer-wide label settings. (A "text format" includes just font settings and other appearance related settings, while a "labe setting" also includes layer-type specific settings such as label placement, priority, and rendering settings).

Text Formats and Label Settings offer all the same functionality as you're used to for managing symbols and color ramps within styles, including import and export to XML files, tagging, smart groups, favoriting etc...

|image7|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `North Road <http://north-road.com>`__

Feature: Marker symbols as label backgrounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alongside all the other exciting labeling improvements which we've landed in 3.10, we now allow use of marker symbols as a background for labels. This allows you to use all the rich functionality available for marker symbols as a background to labels, and complements the existing shapes and SVG background choices!

|image8|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `North Road <http://north-road.com>`__

Feature: Label callouts!
~~~~~~~~~~~~~~~~~~~~~~~~

A common practice when placing labels on a crowded map is to use 'callouts' - labels which are placed outside (or displaced from) their associated feature, with a line connecting the label and the feature. In QGIS 3.10, we've added native support for quickly and easily creating beautiful label callouts (no more expression mangling or drawing by hand!).

We've added many settings for controlling exactly how these label callouts are drawn, and naturally, you can take full advantage of the richness of QGIS line symbol support within your callouts! This includes all the existing line symbol styles, layer effects, and even support for data-defined settings!

In 3.10, we expose options for either a "simple" (direct line) or "Manhattan" (straight lines) callout styles. If you're interested in sponsoring additional callout styles in a future release, get in contact with the QGIS team to find out how you can make this happen!

|image9|

This feature was funded by `SMEC/SJ <https://www.smec.com/en_au>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Change multi-line label alignment for individual labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added an additional option to allow you to control multi-line alignment on a label-by-label basis. Just active the Label Properties tool and click on your map labels, and a new setting for the text alignment is now available.

|image10|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Show unplaced labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you've ever been concerned about automatic label placement hiding away important labels on your map -- this feature is for you! In QGIS 3.10 we've added an option to show "Unplaced labels" on your map, so you can see immediately exactly what's been hidden from view (AKA "see what others can't")!

This new setting (which is accessed through the Labeling toolbar) will render these Unplaced Labels in a red color (but the color can be changed from the project Label Settings dialog). After identifying any missing labels in your map, we suggest you use the existing Labeling tools such as the "move label" or "show/hide label" tool to rearrange your map and make these labels visible again.

|image11|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Overrun distance for line labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We understand that making a cartographic masterpiece is a demanding task, so in QGIS 3.10 we've extended the capabilities of curved labels by adding a new "overrun distance" setting. This setting allows you to control exactly how far a curved label is allowed to extend past to ends of a line feature. Bumping up the distance will result in giving the labeling engine more flexibility in placing your labels, resulting in more labels being placed in better locations on your map! Win! The setting works for both curved and parallel label modes, and supports distances in mm/map units/pixels/etc, and data-defined distances.

|image12|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Data defined control for "label every part of multipart features" setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "label every part" option was one of the very few settings which couldn't be previously data-definable for labels. We've remedied this omission in QGIS 3.10, and you can now control whether you want all parts labelled on a feature-by-feature basis!

|image13|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Control "label all parts" via the label properties tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We aren't lying when we say that QGIS 3.10 is a love-letter to map labelling! Another new option we've added in this version is interactive control over whether all parts of a feature should be labeled via the Label Properties tool.

|image14|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Vertical text orientation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of 3.10, QGIS is now fully equipped to render vertically oriented labels. To our Chinese, Japanese, and Korean users: spread the word! :)

You can choose between two vertical orientation mode: one that always renders labels vertically, or an alternative mode that dynamically picks the orientation based on the label rotation.

|image15|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Control over font kerning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another option we've added for improving the conversion of ArcMap symbology to QGIS (via `SLYR <https://north-road.com/slyr/>`__) is a new setting for controlling whether label fonts are kerned (or not).

|image16|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Rendering
---------

Feature: Rendering raster layers outside the reported extent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on the server technology used, sometimes the map extent reported by raster layers may be smaller than the actual area which can be rendered (especially notably for WMS servers with symbology which takes more space than the data extent). Previous version of QGIS would crop raster layers to the reported extents, resulting in truncated symbols on the borders of these layers. Now, there's a new option to allow you to override this behaviour and ignore the reported extent for affected servers.

This feature was developed by Matthias Kuhn (Opengis.ch)

Feature: Georeference PDFs and TIFs when saving the map canvas as image/PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.10 we've implemented support for embedded georeferencing within PDFs and TIFs when using the save [map canvas] as image or PDF.

|image17|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: New map canvas image decoration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added a brand new decoration for the QGIS main canvas, allowing you to add a bitmap and SVG image overlay (logo, legend, etc.) to your map window.

As with other parts of QGIS, the image decoration supports customizable fill and outline color for parameter-enabled SVGs.

|image18|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Logarithmic scale classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now use a logarithmic based classification technique when creating ranges for the graduated renderer.

|image19|

This feature was developed by `OPENGIS.ch <https://www.opengis.ch>`__

3D Features
-----------

Feature: Measurement tool in 3D map view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can measure distances in 3D map views! This new tool is available in the 3D map view toolbar, and has the same workflow as the 2D measurement tool (with the same configuration settings of rubber band color, units, decimal place, etc). It also has the same behavior (left-click to add a new point, middle-click to delete the last point, and right-click to restart the measurement). This allows you to measure distances in 3d, e.g. the distance between two building’s roofs or the length of a river running down a mountain. See the 3D measurement tool in action:

.. raw:: html

   <div class="col-lg-8 col-md-offset-1">

.. raw:: html

   </div>

This feature was funded by `Google Summer of Code Program <https://summerofcode.withgoogle.com/projects/#5265985207009280>`__

This feature was developed by `Ismail Sunni <http://ismailsunni.id>`__

Feature: Billboard Rendering for Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added a new kind of rendering style for point layers. It allows you to show the point with a QGIS symbol (e.g. marker, SVG, etc) that always faces the user and always has the same size. You can see sample usage in the video.

.. raw:: html

   <div class="col-lg-8 col-md-offset-1">

.. raw:: html

   </div>

This feature was funded by `Google Summer of Code Program <https://summerofcode.withgoogle.com/projects/#5265985207009280>`__

This feature was developed by `Ismail Sunni <http://ismailsunni.id>`__

Feature: 3D On-Screen Navigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In earlier QGIS versions, you could already navigate the 3D world by using a mouse and keyboard. Unfortunately, for a new user, it is not easy to start using them! 3D On-Screen Navigation will help to navigate the 3D world. There are buttons to zoom in/out, tilt up/down, pan up/down/left/right, and rotate the 3D map view. This feature can be activated from the 3D map view toolbar. See how to use it in this video:

|image20|

.. raw:: html

   <div class="col-lg-8 col-md-offset-1">

.. raw:: html

   </div>

This feature was funded by `Google Summer of Code Program <https://summerofcode.withgoogle.com/projects/#5265985207009280>`__

This feature was developed by `Ismail Sunni <http://ismailsunni.id>`__

Print Layouts
-------------

Feature: Right-to-left arrangement for legends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thanks to funding from our right-to-left locale users, we've added a new choice for arrangement of legend elements. These include symbols to the left OR symbols to the right of the legend text, and alignment options for groups, subgroups and item text.

This feature allows creation of right-to-left locale friendly legends. To make things user-friendly, we even default to this right-to-left style alignment when creating new legends under a RTL based locale.

|image21|

This feature was funded by `Kaplan Open Source <https://kaplanopensource.co.il/>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Control margin under legend group and subgroup headings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're after pixel-perfect control over your legend appearance -- this one's for you! QGIS 3.10 now allows you to tweak the spacing applied under group or subgroup headings.

|image22|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Data defined settings in text formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since so much of QGIS' cartographic power comes from the flexibility of data-defined symbol settings, we've now allowed them to be used for text formats too! This means you can now use data defined properties wherever text formats are used, e.g. within layout scalebar text.

|image23|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: @scale\_value variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To complement the new support for data-defined settings within text formats, we added a new @scale\_value expression variable. This can be used when evaluating data defined text format properties while rendering scale bar text, and ultimately allows you to have per-label customisation of the text format inside scale bars (e.g. showing certain distance labels in bold).

|image24|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Scalebar label placement options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've extended layout scale bars with additional styling options, adding a pair of settings to refine the placement of scalebar labels. Now you can define whether labels are shown above or below the scalebar itself, as well as setting whether labels are centered in the middle of a segment or placed at its end.

|image25|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Simplify PDF or SVG exports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous QGIS versions would often generate HUGE PDF (or SVG) outputs, as these outputs included many redundant vertices which were not discernably different at the export DPI. Now, by default, we apply a simplification while writing out PDF or SVG files, causing geometries to be simplified and automatically removing any redundant vertices which are (e.g. if export DPI is 300 dpi, vertices less then 1/600 inch different from each other will be removed).

This new setting, "Simplify geometries to reduce output file size", is exposed in the SVG or PDF export settings dialogs shown when exporting a layout/atlas/report to PDF or SVG.

No more ridiculously complex and large export file size for your QGIS print layouts! Aside from the file size issues, these also cause problems when trying to load into other applications, e.g. Inkscape, which chokes on the huge number of vertices and grinds to a crawl.... ouch!

|image26|

This feature was funded by GeoPDF export group: Land Vorarlberg; Cantons of Zug, Thurgovia and Neuchâtel; Cities of Vienna and Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Improved SVG layered exports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User feedback told us that the way we created layered SVG files in past releases was frustrating to work with. So, in QGIS 3.10, we've revamped this feature and now SVG layer names will match the layer names from QGIS, making it much easier for designers to understand the contents of the document! Read more about this are related features `here <https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/>`__.

|image27|

This feature was funded by GeoPDF export group

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Layout map redraw indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In earlier QGIS releases, there was no way to tell whether a map refresh had finished inside a QGIS print layout designer window. So, we've added a new indicator in the status bar which shows whenever there's a redraw is humming away in the background. No more user confusion!

|image28|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: GeoPDF Export
~~~~~~~~~~~~~~~~~~~~~~

If you export PDF's from QGIS now, there is an option to export it as GeoPDF. If you open this PDF with a compatible PDF viewer, you will then be able to toggle layers on and off, pan and zoom around the PDF and interactively interrogate features! Futhermore, you can re-import these GeoPDF documents back into QGIS as vector layers, and see all the features in their original locations and with their original attribute values.

GeoPDF export is available for either print layouts or map canvas exports. We've added lots of flexibility to this new option, e.g. with options for controlling which layers will be exported as interactive layers. You can even choose to export multiple map themes into a single GeoPDF document, so that your readers can interactive switch between these themes! (Wow!)

Note that GeoPDF export requires a QGIS build based on GDAL 3.0 or later.

Read more at `QGIS 3.10 Loves GeoPdf <https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/>`__

|image29|

This feature was funded by GeoPDF export group: Land Vorarlberg; Cantons of Zug, Thurgovia and Neuchâtel; Cities of Vienna and Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Data defined control grid properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added data defined control over layout map grids, to give you extra flexibility in the appearance and behaviour of these grids, and to allow you to create layout templates and atlases with grids which dynamically respond to map scale changes.

Now, you're able to set data-defined control for:

-  grid enabled state
-  grid x/y intervals
-  grid x/y offsets
-  grid frame size and margin
-  annotation distances from the grid frame
-  grid cross size
-  grid frame line thickness

|image30|

This feature was funded by Andreas Neumann

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Dynamic grid segment sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like the existing scalebar setting of the same name, this new setting allows you to set a page-size-based range for map grid intervals. The grid interval will be dynamically calculated based on the map extent and scale to pick the largest possible "pretty" interval which results in grid sizes inside the desired range.

This change makes it possible for you to create layouts and layout templates with grids which respond elegantly to a wide range of map scales!

|image31|

This feature was funded by Andreas Neumann

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Spatial bookmarks for layout maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another long-requested feature we've implemented for QGIS 3.10 is a new button in the layout map item properties toolbar, which allows you to directly set a map item to the extent of a spatial bookmark!

|image32|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Expressions
-----------

Feature: New expression functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **attributes()**: returns a map containing all attributes from a feature, with field names as map keys. We've got flexible, robust support for working with map values in expressions now, so this allows rapid conversion of all feature attributes to a map to use with these handy functions!
-  New optional "format" parameters were added to the **to\_date**, **to\_datetime**, and **to\_time** functions
-  | **collect\_geometries**: this new function collects a set of geometries into a multi-part geometry object. Geometry parts can either be specified as separate arguments to the function or (more flexibly), as an array of geometry parts. This function allows geometries to be generated using iterator based approaches, such as transforming an array generated using generate\_series, e.g:
   | ``collect_geometries(     array_foreach(       generate_series( 0, 330, 30),       project($geometry, .2, radians(@element))     )   )``
   | Gives a nice radial effect of points surrounding the central feature point when used as a MultiPoint geometry generator

-  A new **make\_line** expression function variant which accepts an array of points. This allows creation of lines from variable numbers of points, and from sequences from aggregates/dynamically generated sequences.

Digitising
----------

Feature: GPS timestamp support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've overhauled the existing GPS based functionality in QGIS 3.10, adding new options for automatically retrieving and storing GPS timestamps alongside GPS based features.

This feature was funded by `NIWA <https://niwa.co.nz/>`__

This feature was developed by `Alessandro Pasotti (North Road) <http://north-road.com>`__

Feature: Allowed gap exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.4 we introduced the ability to configure QGIS layers to run topological checks on every save operation. For 3.10, we have now added a new option to the check for "gaps" which allows you to actively mark some gaps as allowed. These exceptions will be saved on a separate, configurable layer. Whenever a gap is detected, you either have the possibility to fix it or to add it to the allowed exceptions with the press of a button.

|image33|

This feature was funded by `Kanton Solothurn <https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/>`__

This feature was developed by `Matthias Kuhn (OPENGIS.ch) <https://www.opengis.ch>`__

Data Management
---------------

Feature: Composite Foreign Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.10, we added the possibility to create layer relationships which utilise composite foreign keys. QGIS now fully supports editing parent and child features which are linked with more than one attribute. This functionality is accessed in the Project Properties -> Relations tab.

|image34|

This feature was funded by `California Geological Survey <https://www.conservation.ca.gov/cgs>`__

This feature was developed by `OPENGIS.ch <https://www.opengis.ch>`__

Feature: Add circular data dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ever had issues with snapping when editing a feature that is modified by someone else (or a nasty database trigger)? Data dependencies allow refreshing the content of the dependent layers when the data is changed. We improved the dependencies support in QGIS by allowing refreshing the modified layer itself, which is kind of a circular dependency (a point layer and a line layer depending on each other for instance). No more snapping on ghost features!

More info in the `pull request <https://github.com/qgis/QGIS/pull/30947>`__

|image35|

This feature was funded by `QGIS.org <https://qgis.org>`__

This feature was developed by `Julien Cabieces (Oslandia) <https://oslandia.com/en/>`__

Forms and Widgets
-----------------

Feature: Update depending widgets real-time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates widget values on real time while editing the referenced fields. When widget A contains a default value depending on widget B, it updates as soon as widget B is edited.

|image36|

This feature was funded by `Kanton Schaffhausen <https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html>`__

This feature was developed by `David Signer (OPENGIS.ch) <http://www.opengis.ch>`__

Analysis Tools
--------------

Feature: Stored filter expressions for attribute tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While previous versions of QGIS allowed you to filter attribute tables using a custom expression, these expressions were lost whenever the attribute table was closed. Now, we've added the ability to store and manage your custom expression filters to the attribute table dialog. You can now build up your own personal collection of useful filters, which will always be available for re-use with a few simple mouse clicks!

|image37|

This feature was funded by `Kanton Schaffhausen <https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html>`__

This feature was developed by `David Signer (OPENGIS.ch) <https://www.opengis.ch>`__

Feature: New operators for Raster Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You ask, we listen: ``abs`` , ``min`` and ``max`` are now available in the Raster Calculator user interface!

|image38|

This feature was developed by `Alessandro Pasotti <https://www.qcooperative.net>`__

Processing
----------

Feature: New algorithm "Point to layer"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm creates a new vector layer which contains a single feature with geometry matching a point parameter. It can be used in models to convert a point input into a layer, which can then be used for other algorithms which require a layer based input.

|image39|

This feature was developed by Olivier Dalang

Feature: Advanced model parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When creating inputs for a Processing model, you can now mark these input parameters as "Advanced" options. (Advanced parameters are hidden by default when users run your model through the Processing toolbox)

|image40|

This feature was developed by Alex Bruy

Feature: All GDAL based algorithms now support free-form "additional parameters"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added an optional "Additional command-line parameters" parameter to all GDAL algorithms , useful for cases when you need to pass a specific command-line argument(s) which is not exposed in the algorithm UI.

|image41|

This feature was developed by Alex Bruy

Feature: Metatile size for XYZ tiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now specify a custom metatile size when generating XYZ tiles. Larger values may speed up the rendering of tiles and provide better labelling (fewer gaps without labels) at the expense of using more memory.

|image42|

This feature was developed by Martin Dobias

Feature: New parameter type for colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 3.10 brings a new parameter type for use in Processing models and scripts, which allows for users to pick a color value. Useful for any models and algorithms which require a color value as an input!

|image43|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: New algorithm "Create style database from project"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm extracts all style objects (symbols, color ramps, text formats and label settings) from a QGIS project and stores them in a new style XML database, which can then be managed and imported via the Style Manager dialog.

|image44|

This feature was funded by `SMEC/SJ <https://www.smec.com/en_au>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: File filter and default values for file and folder inputs in models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For file or folder inputs in Processing models we've added a new file filter setting (with some standard file formats available as an optional preset), and now allow you to set a default value for these inputs.

|image45|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: New algorithm "Combine style databases"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The new "Combine style databases" algorithm combines multiple QGIS style databases into a single output style database. If any symbols exist with duplicate names between the different source databases these will be renamed to have unique names in the output combined database. It's designed to give users an easy way to condense multiple separate style databases into a single unified database.

It works brilliantly with results generated by running the "Create style database from project" in a batch mode!

|image46|

This feature was funded by `SMEC/SJ <https://www.smec.com/en_au>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Generate XYZ tiles using multiple threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The existing Generate XYZ tiles algorithm has been optimised and can now generate tiles using multiple processing threads.

|image47|

This feature was developed by Isghj5

Feature: New algorithms for exporting and importing bookmarks to/from map layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To complement the spatial bookmark overhaul in QGIS 3.10, we've added new Processing algorithms which allow you to create a bunch of new bookmarks corresponding to the features from a layer, or to export existing spatial bookmark extents to a new polygon layer.

|image48|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: New algorithm "Split features by character"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This brand new algorithm splits features into multiple output features, by splitting a field value with a specified character.

For instance, if a layer contains features with multiple comma separated values contained in a single field, this algorithm can be used to split these values up across multiple output features. Geometries and other attributes remain unchanged in the output.

Optionally, the separator string can be a regular expression for added flexibility.

This algorithm was designed for use in models which need to process input files with multiple concatenated values in a single attribute, e.g. geocoding a table with "address1,address2,address3" format strings.

|image49|

This feature was funded by `SMEC/SJ <https://www.smec.com/en_au>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: New algorithm Climb Along Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously available as a plugin, the "Climb Along Line" algorithm has been added to the out-of-the-box QGIS toolset. This algorithm calculates the accumulated height differences for lines in an input line layer, calculated using the Z values of the line vertices. A copy of the input line layer is returned with additional attributes for accumulated climb and descent, as well as the minimum and maximum Z values for each line.

|image50|

This feature was developed by `Håvard Tveite (NMBU) and Matteo Ghetta (Faunalia) <https://www.faunalia.eu>`__

Feature: Port Create Grid algorithm to C++
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We ported the Create Grid algorithm from Python to C++ in order to speed up the algorithm. The algorithm now performs much faster for you and is also capable of creating point\|line\|rectangle\|diamond\|hexagon regular vector grids in high resolution in huge extents (eg. whole nations) in a reasonable amount of time.

|image51|

This feature was funded by `Clemens Raffler <https://twitter.com/root676>`__

This feature was developed by `Clemens Raffler <https://github.com/root676>`__

Browser
-------

Feature: Extract symbols from QGIS projects within the browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS' Browser panel just keeps getting more and more powerful! In 3.10, we've added a new option when right-clicking a QGIS project within the browser: "Extract Symbols". Selecting this option opens a style manager dialog showing all symbols, color ramps, text formats and label settings from the selected project, allowing you to easily export the browse these symbols.

|image52|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

General
-------

Feature: Show news items on welcome page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A curated QGIS news feed is now shown on the welcome page. This finally gives us a direct channel to push project news to ALL our users! Expect to see lots of interesting QGIS news, tips, and events coming your way!

|image53|

This feature was funded by QGIS.org

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Milliradians (SI definition) and mil (NATO) units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 3.10 allows you to measure angles in two new units, milliradians (SI definition) and mil (NATO) units.

|image54|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Interface Customization dialog filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added a new "search" box to the Interface Customization dialog, which allows you to filter through the widgets and easily find the widget you are trying to customize...

|image55|

This feature was developed by DelazJ

Feature: Improved auto-fix broken layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a layer path is fixed in a project, QGIS 3.10 will automatically scan through all other broken paths and try to auto-fix any others which were also pointing to the same original broken file path. Any change which speeds up fixing broken layer paths is a welcome change in our view!

|image56|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Spatial bookmarks supercharged!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've totally revamped how spatial bookmarks are exposed and managed in QGIS 3.10. Spatial Bookmarks are now shown in the browser panel, and can be regrouped into custom, categorized folders. This offers a much easier way to navigate and manage your bookmarks.

We also added a brand new bookmark editor dialog, which features an extent widget that greatly facilitates bookmark editing.

Bookmarks can also now be dragged and dropped onto canvases, allowing secondary canvases to zoom to a particular bookmark. This allows bookmarks to play nice in multi-canvas projects, since you can drop them onto a specific canvas to zoom.

|image57|

This feature was developed by Mathieu Pellerin, Nyall Dawson

Feature: "Reselect Features" action in Edit -> Select menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ever spend 10 minutes painstakingly creating an interactive selection of features, only to accidentally deselect them all through an errant mouse click? If so, this feature is designed just for you! Now, you can restore a layer's selection following a selection clear operation via the new "Reselect Features" option in the Edit menu.

|image58|

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Parallelize snap index build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The idea was to parallelize for each layer the snap cache computing (sequential at the moment) and to make it non blocking. As a consequence it is still possible to use QGIS even if snap cache is currently building. User can for instance start to edit node while the snap cache build is in progress.

This feature was developed by Oslandia

Feature: Templates for QGIS Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 3.10 includes the ability to directly use Project Templates from the welcome page. Additionally, you can now ship project templates to your whole organisation by placing them in a system folder, next to the already existing possibility to put it into a user profile folder.

|image59|

This feature was funded by `The QGIS Project <https://www.qgis.org>`__

This feature was developed by `Matthias Kuhn (OPENGIS.ch) <https://www.opengis.ch>`__

Data Providers
--------------

Feature: Read-write support for .shz and .shp.zip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For QGIS builds based on GDAL 3.1, you can now open and edit single-layer ZIP compressed shapefiles (.shz), or multi-layer ones (.shp.zip). Regardless of where you sit on the Shapefile vs Geopackage battle, you'll welcome this ability to de-clutter your folders and store shapefiles as a single file!

This feature was developed by Even Rouault

Feature: Oracle provider authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've updated the Oracle database provider to add full support for QGIS built-in authentication system.

This feature was developed by Jürgen Fischer

Feature: Improved PostGIS raster support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PostGIS raster layers are now shown in the Browser panel and from the Data Source Manager dialog, allowing you to easily manage and add these layers to your projects. Currently only read support from browser is supported - you cannot drag rasters into a PostGIS database using the browser.

This feature was developed by Alessandro Pasotti

Feature: Oracle - Database transaction support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For version 3.10, we've enhanced the Oracle database provider and added support for editing layers via transactions.

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: Z/M dimensions in delimited text layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've added optional support for Z and M fields to QGIS' delimited text provider, allowing you to create Z or M enabled layers directly from CSV files.

|image60|

This feature was developed by `Mathieu Pellerin <http://www.imhere-asia.com/>`__

Feature: Static data providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One huge behind-the-scenes job we completed for QGIS 3.10 is a refactoring of the provider infrastructure. Now, providers allow both dynamic and static linking. This was a pre-requisite to be able to build QGIS libraries on platforms that do not support dynamic linkage (iOS), and allows for QGIS based tools like the Input data collection app to be distributed for iOS based devices!

This feature was funded by `Lutra Consulting Ltd. <http://www.lutraconsulting.co.uk>`__

This feature was developed by `Peter Petrik, Martin Dobias <http://www.lutraconsulting.co.uk/about>`__

QGIS Server
-----------

Feature: Using SVG in QGIS Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Earlier QGIS server versions had rendering issues when remote SVG files were used in a project (e.g. those hosted via external http servers). We've improved how QGIS Server fetches these resources, and it's now possible to use remote SVG paths in your layers and publish them as WMS without rendering issues in QGIS Server.

|image61|

This feature was funded by `Ifremer <https://sextant.ifremer.fr/>`__

This feature was developed by `René-Luc D'Hont (3Liz) <https://www.3liz.com/>`__

Feature: WMS dimension
~~~~~~~~~~~~~~~~~~~~~~

In QGIS 3.10 a WMS server can provide support for several type of dimensions such as time, elevation or other types of dimensions. The dimension has to be defined as the layer level and can be used by the WMS client to filter requested information. WMS Time is part of the WMS Dimension.

|image62|

This feature was funded by `Ifremer <https://sextant.ifremer.fr/>`__

This feature was developed by `René-Luc D'Hont (3Liz) <https://www.3liz.com/>`__

Feature: Server OAPIF (aka WFS3) support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 3.10 Server is one of the very first geospatial servers which supports the new `OGC API - Features - Part 1: Core <http://docs.opengeospatial.org/is/17-069r3/17-069r3.html>`__ standard (also known as WFS3)!

This is a completely new implementation that provides an HTML and JSON based service for your web mapping developments, including a simple WebGIS interface which is available out of the box and it is easily customizable through an HTML template system.

More information is available in the `documentation <https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/services.html#wfs3-ogc-api-features>`__

|image63|

This feature was developed by `Alessandro Pasotti <https://www.qcooperative.net>`__

Programmability
---------------

Feature: New class QgsBookmarkManager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Attached to QgsProject and QgsApplication, this new class provides a stable, supported method of managing project and global bookmarks (vs the old undocumented, not stable approach of directly manipulating project keys or a sqlite database). Now your plugins and scripts are capable of reading, modifying, and managing spatial bookmarks!

This feature was funded by `North Road <http://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road) <http://north-road.com>`__

Feature: New API for provider database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thanks to funding from the QGIS grant program, you can now use a `new API <https://github.com/qgis/QGIS/pull/31190>`__ aimed to manage DB connections in a unified way. The new connection API also provides a set of useful methods that can be used by plugin authors to access information about tables, schemas etc. and to run SQL arbitrary queries and get the results back into a handy Python array.

This feature was funded by QGIS

This feature was developed by `Alessandro Pasotti <https://www.qcooperative.net>`__

Notable Fixes
-------------

Feature: Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Bug Title                                                                                            | URL issues (if reported)                                 | URL PR or commit                                         | 3.4 backport PR or commit                                |
+======================================================================================================+==========================================================+==========================================================+==========================================================+
| Crash when deleting print layout items                                                               | `#31549 <https://github.com/qgis/QGIS/issues/31549>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| DB manager python error                                                                              | `#31457 <https://github.com/qgis/QGIS/issues/31457>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| QGIS 3.4.11: Clicking a PDF URL in GetFeatureInfo response generates error                           | `#31542 <https://github.com/qgis/QGIS/issues/31542>`__   | Already fixed (by me) on 3.8 and Master                  |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Watch file not adding new columns                                                                    | `#31452 <https://github.com/qgis/QGIS/issues/31452>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Loss of labels background from older project/style                                                   | `#31427 <https://github.com/qgis/QGIS/issues/31427>`__   | `PR #3164 <https://github.com/qgis/QGIS/pull/31647>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| "Text formats" dialog shows modifiable buffer properties while the "draw text buffer" is unchecked   | `#31428 <https://github.com/qgis/QGIS/issues/31428>`__   | `PR #3173 <https://github.com/qgis/QGIS/pull/31734>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Symbology tab widget does not horizontally expand in the layer properties dialog extent              | `#31449 <https://github.com/qgis/QGIS/issues/31449>`__   | `PR #3166 <https://github.com/qgis/QGIS/pull/31665>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Watch file not adding new columns                                                                    | `#31452 <https://github.com/qgis/QGIS/issues/31452>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Unreported but related to #31452                                                                     | `PR #3168 <https://github.com/qgis/QGIS/pull/31688>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Unable to add WMS service in QGIS, same URL works in other clients                                   | `#31661 <https://github.com/qgis/QGIS/issues/31661>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| QGIS Server - Download of capabilities failed: SSL handshake failed                                  | `#31675 <https://github.com/qgis/QGIS/issues/31675>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| apparent regression in raster calculator multiplying conditionals                                    | `#31193 <https://github.com/qgis/QGIS/issues/31193>`__   | `PR #3169 <https://github.com/qgis/QGIS/pull/31690>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Broken GPKG browser actions                                                                          | `#31730 <https://github.com/qgis/QGIS/issues/31730>`__   | `PR #3173 <https://github.com/qgis/QGIS/pull/31731>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Resizing the data source manager dialog fails to resize unfocused panels                             | `#31732 <https://github.com/qgis/QGIS/issues/31732>`__   | `PR #3174 <https://github.com/qgis/QGIS/pull/31741>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| In place processing multipart to singleparts does not handle unique constraints                      | `#31634 <https://github.com/qgis/QGIS/issues/31634>`__   | `PR #3175 <https://github.com/qgis/QGIS/pull/31750>`__   | `PR #3181 <https://github.com/qgis/QGIS/pull/31810>`__   |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| crash when adding legend via python                                                                  | `#31713 <https://github.com/qgis/QGIS/issues/31713>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| UI: Legend does not refresh after classifincation bounds updated                                     | `#31643 <https://github.com/qgis/QGIS/issues/31643>`__   | Not affected                                             | `PR #3183 <https://github.com/qgis/QGIS/pull/31834>`__   |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| UI: PostGIS layer error message not helpful, disappears and shouldn't happen                         | `#31799 <https://github.com/qgis/QGIS/issues/31799>`__   | `PR #3184 <https://github.com/qgis/QGIS/pull/31841>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Server GetLegendGraphics contextual (BBOX) fails if no WIDTH and HEIGHT are supplied                 | `#31846 <https://github.com/qgis/QGIS/issues/31846>`__   | `PR #3186 <https://github.com/qgis/QGIS/pull/31865>`__   | `PR #3188 <https://github.com/qgis/QGIS/pull/31882>`__   |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| extend/trim crash                                                                                    | `#31864 <https://github.com/qgis/QGIS/issues/31864>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| UI: any click on number of classes updown triggers twice                                             | `#31635 <https://github.com/qgis/QGIS/issues/31635>`__   | `PR #3187 <https://github.com/qgis/QGIS/pull/31871>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| GPKG project is not marked dirty after it is deleted from the storage                                | `#30550 <https://github.com/qgis/QGIS/issues/30550>`__   | `PR #3187 <https://github.com/qgis/QGIS/pull/31876>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Fix unreported issue with QVariantList to JSON conversion in QgsJsonUtils                            | unreported                                               | `PR #3192 <https://github.com/qgis/QGIS/pull/31920>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Crash on adding WMS                                                                                  | `#31927 <https://github.com/qgis/QGIS/issues/31927>`__   | `#31927 <https://github.com/qgis/QGIS/issues/31927>`__   | `PR #3197 <https://github.com/qgis/QGIS/pull/31979>`__   |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Raster calculator change sign does not work when OpenCL is on                                        | `#32023 <https://github.com/qgis/QGIS/issues/32023>`__   | `PR #3202 <https://github.com/qgis/QGIS/pull/32026>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Snapping map units always show "meters even when the project is in different units                   | `#31961 <https://github.com/qgis/QGIS/issues/31961>`__   | `PR #3201 <https://github.com/qgis/QGIS/pull/32018>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| QGIS Raster Calculator outputs nodata only rasters                                                   | `#32025 <https://github.com/qgis/QGIS/issues/32025>`__   | `PR #3202 <https://github.com/qgis/QGIS/pull/32026>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Opening projects from PostgreSQL issue                                                               | `#32050 <https://github.com/qgis/QGIS/issues/32050>`__   | `PR #3206 <https://github.com/qgis/QGIS/pull/32062>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| GetLegendGraphic shows all identical symbols for content based legend                                | `#32020 <https://github.com/qgis/QGIS/issues/32020>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| WFS doesn't recognize advertised GeoJSON outputFormat string                                         | `#32065 <https://github.com/qgis/QGIS/issues/32065>`__   | `PR #3210 <https://github.com/qgis/QGIS/pull/32106>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| creating indexes on geopackage failes (QGIS 3.8.3)                                                   | `#32094 <https://github.com/qgis/QGIS/issues/32094>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| DB manager import option "Create single-part geometries instead of multi-part" is broken             | `#32089 <https://github.com/qgis/QGIS/issues/32089>`__   | `PR #3210 <https://github.com/qgis/QGIS/pull/32108>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| GetLegendGraphic shows all identical symbols for content based legend                                | `#32020 <https://github.com/qgis/QGIS/issues/32020>`__   | `PR #3212 <https://github.com/qgis/QGIS/pull/32120>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| WFS contextual legend issue when canvas CRS is different than layer's CRS                            | unreported                                               | `PR #3212 <https://github.com/qgis/QGIS/pull/32120>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| PostGIS/geojson: Cannot input negative numbers in int fields                                         | `#32149 <https://github.com/qgis/QGIS/issues/32149>`__   | `PR #3216 <https://github.com/qgis/QGIS/pull/32161>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Information tab in WMS layer properties is unresponsive if a WMS service contains many layers        | `#32213 <https://github.com/qgis/QGIS/issues/32213>`__   | `PR #3226 <https://github.com/qgis/QGIS/pull/32269>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Data Source UI - PostgreSQL table multi-line comments make the grid table hard to read               | `#32257 <https://github.com/qgis/QGIS/issues/32257>`__   | `PR #3233 <https://github.com/qgis/QGIS/pull/32336>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| More null pointer dereferences when plugins are off                                                  | `#32347 <https://github.com/qgis/QGIS/issues/32347>`__   | `PR #3235 <https://github.com/qgis/QGIS/pull/32351>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| null pointer dereferences when plugins are off                                                       | `#32338 <https://github.com/qgis/QGIS/issues/32338>`__   | `PR #3234 <https://github.com/qgis/QGIS/pull/32345>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| "Merge features" and "merge feature attributes" have broken numerical functions                      | `PR #3236 <https://github.com/qgis/QGIS/pull/32360>`__   | `PR #3236 <https://github.com/qgis/QGIS/pull/32360>`__   |                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it/>`__

Feature: Bug fixes by Alexander Bruy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Bug Title                                                                                              | URL issues (if reported)                                 | URL PR or commit                                         | 3.4 backport PR or commit                                |
+========================================================================================================+==========================================================+==========================================================+==========================================================+
| GDAL scripts in Processing need quoting on attribute names                                             | `#30878 <https://github.com/qgis/QGIS/issues/30878>`__   | `PR #3171 <https://github.com/qgis/QGIS/pull/31712>`__   | `PR #3171 <https://github.com/qgis/QGIS/pull/31717>`__   |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Processing GDAL algorithms does not handle correctly WFS input layers                                  | `#29663 <https://github.com/qgis/QGIS/issues/29663>`__   | `PR #3173 <https://github.com/qgis/QGIS/pull/31735>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| shp files in zip files files cannot be used in Processing with 3rd party providers (SAGA, GRASS...)    | `#29001 <https://github.com/qgis/QGIS/issues/29001>`__   | `PR #3174 <https://github.com/qgis/QGIS/pull/31744>`__   | `PR #3178 <https://github.com/qgis/QGIS/pull/31787>`__   |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Not possible to toggle use selected features in the Processing layer combobox                          | `#30636 <https://github.com/qgis/QGIS/issues/30636>`__   | `PR #3173 <https://github.com/qgis/QGIS/pull/31739>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Connect to postgis database fails in "Layer - Add Postgis layer" on databases with weird table names   | `#27040 <https://github.com/qgis/QGIS/issues/27040>`__   | `PR #3176 <https://github.com/qgis/QGIS/pull/31763>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| GRASS v.build.polylines dosn't work in Qgis 3.4.10                                                     | `#31037 <https://github.com/qgis/QGIS/issues/31037>`__   |                                                          |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Processing Algorithms written with the @alg decorator don't get the gear icon                          | `#31252 <https://github.com/qgis/QGIS/issues/31252>`__   | `PR #3188 <https://github.com/qgis/QGIS/pull/31887>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| v.drape - no 25D export with SpatiaLite format                                                         | `#30066 <https://github.com/qgis/QGIS/issues/30066>`__   |                                                          |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Service url cannot include custom query parameters                                                     | `#26761 <https://github.com/qgis/QGIS/issues/26761>`__   |                                                          |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Processing: python error on startup                                                                    | `#29535 <https://github.com/qgis/QGIS/issues/29535>`__   |                                                          |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Saving Processing's Package Layers algorithm's output to default temporary output leaves no result     | `#30535 <https://github.com/qgis/QGIS/issues/30535>`__   |                                                          |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| [Georeferencer] GDAL script does not set target SR                                                     | `#31353 <https://github.com/qgis/QGIS/issues/31353>`__   | `PR #3189 <https://github.com/qgis/QGIS/pull/31898>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Processing "Build virtual vector" now fails in certain cases                                           | `#29336 <https://github.com/qgis/QGIS/issues/29336>`__   | `PR #3190 <https://github.com/qgis/QGIS/pull/31901>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Unreported issue with missed import in the Processing algorithms dialog                                | unreported                                               | `PR #3190 <https://github.com/qgis/QGIS/pull/31902>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| db manager: python error when clicking "edit table" if the table is a postgis raster                   | `#30214 <https://github.com/qgis/QGIS/issues/30214>`__   | `PR #3190 <https://github.com/qgis/QGIS/pull/31904>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| DB Manager: Renaming a PostGIS geometry column causes it to lose its geometry type and SRS             | `#27613 <https://github.com/qgis/QGIS/issues/27613>`__   | `PR #3192 <https://github.com/qgis/QGIS/pull/31929>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Georeferencer incorrectly shows last image when reopened                                               | `#26700 <https://github.com/qgis/QGIS/issues/26700>`__   | `PR #3193 <https://github.com/qgis/QGIS/pull/31932>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| DB Manager: Create Layer dialog should be closed or cleared once the new layer is generated            | `#25535 <https://github.com/qgis/QGIS/issues/25535>`__   | `PR #3195 <https://github.com/qgis/QGIS/pull/31956>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| [Vector Save As...] Extension is not replaced in filename when switching format                        | `#26054 <https://github.com/qgis/QGIS/issues/26054>`__   | `PR #3196 <https://github.com/qgis/QGIS/pull/31960>`__   |                                                          |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by Alexander Bruy

Feature: Bug fixes by Peter Petrik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Bug Title                                                                          | URL issues (if reported)                                 | URL PR or commit                                         | 3.4 backport PR or commit                                |
+====================================================================================+==========================================================+==========================================================+==========================================================+
| Reproducible Crash: retrieving QgsHighlight instance stored as a widget property   | `#30766 <https://github.com/qgis/QGIS/issues/30766>`__   | `PR #3173 <https://github.com/qgis/QGIS/pull/31733>`__   | `PR #3197 <https://github.com/qgis/QGIS/pull/31977>`__   |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Layer styling Mesh layer does not respond to change of Color ramp (first time)     | `#29188 <https://github.com/qgis/QGIS/issues/29188>`__   | `PR #3198 <https://github.com/qgis/QGIS/pull/31981>`__   |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| qgis crashed on close in QSortFilterProxyModel                                     | `#31721 <https://github.com/qgis/QGIS/issues/31721>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| QGIS freezes                                                                       | `#29742 <https://github.com/qgis/QGIS/issues/29742>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Crash when trying to save a project                                                | `#29896 <https://github.com/qgis/QGIS/issues/29896>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Crash on exit with advanced digitizing active                                      | `#29143 <https://github.com/qgis/QGIS/issues/29143>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| Renaming macOS app causes authentication error                                     | `#32163 <https://github.com/qgis/QGIS/issues/32163>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
| QGIS cannot be opened after updating to Mac OS Catalina                            | `#32167 <https://github.com/qgis/QGIS/issues/32167>`__   |                                                          |                                                          |
+------------------------------------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Peter Petrik <https://www.lutraconsulting.co.uk/>`__

Feature: Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Bug Title                                                                                   | URL issues (if reported)                                 | URL PR or commit                                          | 3.4 backport PR or commit                                                                           |
+=============================================================================================+==========================================================+===========================================================+=====================================================================================================+
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform   | `#31762 <https://github.com/qgis/QGIS/issues/31762>`__   | `PR #3176 <https://github.com/qgis/QGIS/pull/31764>`__    | `Commit 08bb3fe <https://github.com/qgis/QGIS/commit/08bb3fea3fc3f574755ecc0a7dc8381a9822e4cd>`__   |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform   | `#31762 <https://github.com/qgis/QGIS/issues/31762>`__   | `PR #3184 <https://github.com/qgis/QGIS/pull/31848>`__    | `PR #3185 <https://github.com/qgis/QGIS/pull/31850>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| QGIS WFS stripping of viewparam KVP from WFS Feature Requests                               | `#31026 <https://github.com/qgis/QGIS/issues/31026>`__   | `PR #3176 <https://github.com/qgis/QGIS/pull/31765>`__    | `PR #3188 <https://github.com/qgis/QGIS/pull/31883>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Crash: right click on image ->export ->save as->"save raster layer as"                      | `#30937 <https://github.com/qgis/QGIS/issues/30937>`__   | `PR #3176 <https://github.com/qgis/QGIS/pull/31766>`__    | `PR #3178 <https://github.com/qgis/QGIS/pull/31780>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| crash in discover relations for postgresql layers                                           | `#31213 <https://github.com/qgis/QGIS/issues/31213>`__   | `PR #3176 <https://github.com/qgis/QGIS/pull/31768>`__    | `PR #3177 <https://github.com/qgis/QGIS/pull/31779>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Exporting raster as raw data to GeoPackage fails silently                                   | `#30644 <https://github.com/qgis/QGIS/issues/30644>`__   | `PR #3177 <https://github.com/qgis/QGIS/pull/31771>`__    | `PR #3178 <https://github.com/qgis/QGIS/pull/31781>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| QGIS crashes after deactivating a GDAL driver in use in the project                         | `#29212 <https://github.com/qgis/QGIS/issues/29212>`__   | `PR #3177 <https://github.com/qgis/QGIS/pull/31772>`__    | `PR #3180 <https://github.com/qgis/QGIS/pull/31802>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Crash exporting to GS7BG format                                                             | `#31775 <https://github.com/qgis/QGIS/issues/31775>`__   | `PR #3178 <https://github.com/qgis/QGIS/pull/31785>`__    | `PR #3183 <https://github.com/qgis/QGIS/pull/31836>`__                                              |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| pgdump is no longer a recognized format for the GDAL/OGR convert format algorithm           | `#31421 <https://github.com/qgis/QGIS/issues/31421>`__   | `PR #3181 <https://github.com/qgis/QGIS/pull/31811>`__    | not worth                                                                                           |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| PBF files not loading correctly                                                             | `#31062 <https://github.com/qgis/QGIS/issues/31062>`__   | `PR #3181 <https://github.com/qgis/QGIS/pull/31812>`__    | `PR #31835 <https://github.com/qgis/QGIS/pull/31835>`__                                             |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Error importing cover from Geoserver WFS service                                            | `#29844 <https://github.com/qgis/QGIS/issues/29844>`__   | `PR #31813 <https://github.com/qgis/QGIS/pull/31813>`__   | `PR #31867 <https://github.com/qgis/QGIS/pull/31867>`__                                             |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Feature count from online Geojson not updated upon refresh                                  | `#30518 <https://github.com/qgis/QGIS/issues/30518>`__   | `PR #31860 <https://github.com/qgis/QGIS/pull/31860>`__   | not worth                                                                                           |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Edits in GeoJson datasources are not saved anymore                                          | `#28580 <https://github.com/qgis/QGIS/issues/28580>`__   | GDAL https://github.com/OSGeo/gdal/pull/1846              | Backported to GDAL 3.0 and 2.4 maintenance branches                                                 |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Even Rouault <http://www.spatialys.com/>`__

Feature: Bug fixes by Sandro Santilli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Bug Title                                                                                                      | URL issues (if reported)                                 | URL PR or commit                                                                                     | 3.4 backport PR or commit                                                                            |
+================================================================================================================+==========================================================+======================================================================================================+======================================================================================================+
| Adding Postgis rasters from DB Manager ask for password for each add                                           | `#31162 <https://github.com/qgis/QGIS/issues/31162>`__   |                                                                                                      |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] segmentizebymaxdistance puts qgis in endless CPU loop                                             | `#31832 <https://github.com/qgis/QGIS/issues/31832>`__   | `Commit 6942b4b9 <https://github.com/qgis/QGIS/commit/6942b4b93d252bc3a031db08a34f378d8d3c726d>`__   | `Commit 3225f491 <https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0>`__   |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| file INSTALL cannot find doc/api/html                                                                          | `#31842 <https://github.com/qgis/QGIS/issues/31842>`__   | `Commit 3225f491 <https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| QGIS died on signal 11 # at start up                                                                           | `#31350 <https://github.com/qgis/QGIS/issues/31350>`__   |                                                                                                      |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| repository files modified by ``make check``                                                                    | `#25830 <https://github.com/qgis/QGIS/issues/25830>`__   | `PR #31980 <https://github.com/qgis/QGIS/pull/31980>`__                                              |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| CMake Error at cmake/FindGEOS.cmake:162                                                                        | `#32170 <https://github.com/qgis/QGIS/issues/32170>`__   | `Commit bc9bb888 <https://github.com/qgis/QGIS/commit/bc9bb8880a3db5a05c697f5d56708757a2ce999d>`__   | `Commit 27f13936 <https://github.com/qgis/QGIS/commit/27f13936afd970d766f398584a1ea509dc15b907>`__   |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| False success from ogr provider's committChanges                                                               | `#32144 <https://github.com/qgis/QGIS/issues/32144>`__   | `Commit f421dc4f <https://github.com/qgis/QGIS/commit/f421dc4f92cfc019eec9823556d3c8f3e9589d95>`__   | `Commit 136cec24 <https://github.com/qgis/QGIS/commit/136cec244111748627c59db151002fddfc5f1708>`__   |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| TestSagaAlgorithms: line 139, in check\_algorithm: 'NoneType' object has no attribute 'checkParameterValues'   | `#32143 <https://github.com/qgis/QGIS/issues/32143>`__   | `Commit 76b39de1 <https://github.com/qgis/QGIS/commit/76b39de1b85375f48d7a5d35ebe39a52224d1809>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| PostGIS Data Loads Extemely Slow                                                                               | `#26186 <https://github.com/qgis/QGIS/issues/26186>`__   | `PR #31858 <https://github.com/qgis/QGIS/pull/31858>`__                                              |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Sandro Santilli <http://strk.kbt.io/>`__

Feature: Bug fixes by Matthias Kuhn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------+
| Bug Title                                           | URL issues (if reported)                                 | URL PR or commit                                          | 3.4 backport PR or commit   |
+=====================================================+==========================================================+===========================================================+=============================+
| Crash when opening symbology tab of invalid layer   | `#32041 <https://github.com/qgis/QGIS/issues/32041>`__   | `#32041 <https://github.com/qgis/QGIS/issues/32041>`__    | n/a                         |
+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------+
| PR reviews                                          | Many :D                                                  |                                                           |                             |
+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------+
| qgz are marked as temporary on windows              | `#32118 <https://github.com/qgis/QGIS/issues/32118>`__   |                                                           |                             |
+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------+
| Allow selecting geometry type in context            | `#32121 <https://github.com/qgis/QGIS/issues/32121>`__   | `PR #32125 <https://github.com/qgis/QGIS/pull/32125>`__   | n/a                         |
+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Matthias Kuhn <https://www.opengis.ch/>`__

Feature: Bug fixes by Paul Blottiere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Bug Title                                                                     | URL issues (if reported)                                 | URL PR or commit                                                | 3.4 backport PR or commit   |
+===============================================================================+==========================================================+=================================================================+=============================+
| Fixes invalid schemaLocation in GetCapabilities doc                           | `#32085 <https://github.com/qgis/QGIS/issues/32085>`__   | `PR #32352 <https://github.com/qgis/QGIS/pull/32352>`__         |                             |
+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Invalid WMS GetFeatureInfo response with json info\_format                    | `#32326 <https://github.com/qgis/QGIS/issues/32326>`__   | `PR #32386 <https://github.com/qgis/QGIS/pull/32386>`__/files   |                             |
+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| QGIS Server SELECTION doesn't work with Postgres ids of type bigint or text   | `#29779 <https://github.com/qgis/QGIS/issues/29779>`__   |                                                                 |                             |
+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Regression with opacities for the WMS GetPrint request                        | `#29317 <https://github.com/qgis/QGIS/issues/29317>`__   |                                                                 |                             |
+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+
| Unreported regression: Invalid renderer type after loading a QML style file   | unreported regression                                    | `PR #32388 <https://github.com/qgis/QGIS/pull/32388>`__         |                             |
+-------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------+-----------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by Paul Blottiere

Feature: Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Bug Title                                                                                                                                                | URL issues (if reported)                                                                             | URL PR or commit                                                                                     | 3.4 backport PR or commit                                                                            |
+==========================================================================================================================================================+======================================================================================================+======================================================================================================+======================================================================================================+
| Fix crash when deleting layouts from designer window                                                                                                     | `#32465 <https://github.com/qgis/QGIS/issues/32465>`__                                               | `Commit e643e7f6 <https://github.com/qgis/QGIS/commit/e643e7f6abe63aff123e07a0137afdda3987d4e6>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix model to python when model has no input parameters                                                                                                   | `Commit 6f1c42e7 <https://github.com/qgis/QGIS/commit/6f1c42e7bc9fa6ddfae3bbc1304ebeb53fe6a014>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix string escaping when converting models to python code                                                                                                | `#32451 <https://github.com/qgis/QGIS/issues/32451>`__                                               | `Commit e3eb4f54 <https://github.com/qgis/QGIS/commit/e3eb4f54abdd8c6d4f4de443e3517775e9e565e1>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix memory leak                                                                                                                                          | `Commit 5be31915 <https://github.com/qgis/QGIS/commit/5be319157f112a2fdbab7f03d0010d69f1e79157>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix potential overflow in raster renderer                                                                                                                | `Commit 1ba8db41 <https://github.com/qgis/QGIS/commit/1ba8db41b67c7c481affd5271864cc2318ce06e4>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Restore project variables early in the project read cycle                                                                                                | `#32382 <https://github.com/qgis/QGIS/issues/32382>`__                                               | `Commit d76835fe <https://github.com/qgis/QGIS/commit/d76835fec5a9217a5ea1996374d142f7319f8d08>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Improve docs for Join by Nearest, raise warning in log                                                                                                   | `#32317 <https://github.com/qgis/QGIS/issues/32317>`__                                               | `Commit 670c81f9 <https://github.com/qgis/QGIS/commit/670c81f9212ada60f56c1c70ee9d37280052622c>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Catch some reprojection exceptions during raster rendering                                                                                               | `#32301 <https://github.com/qgis/QGIS/issues/32301>`__                                               | `Commit 1dfc0c1e <https://github.com/qgis/QGIS/commit/1dfc0c1e4eb8be26bb7214e3978aa6d80974c221>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [labeling] Fix broken numeric formatting settings, add tests                                                                                             | `#32393 <https://github.com/qgis/QGIS/issues/32393>`__                                               | `Commit b58dd674 <https://github.com/qgis/QGIS/commit/b58dd6745fabf8bccd6dbeb684b37393d5953cb7>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix uncaught transform exception when determining AFS layer bounds                                                                                       | unreported                                                                                           | `Commit 857697dd <https://github.com/qgis/QGIS/commit/857697dd9919e80fc03e0c2059e56ce7311e9b49>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix qt warning thrown when converting a 2.18 project                                                                                                     | unreported                                                                                           | `Commit 12ad9fca <https://github.com/qgis/QGIS/commit/12ad9fca1ed5027129161ee5b5c764b8374d0b51>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Add option to take no action ("Leave as an unknown CRS") when a layer is loaded which has no CRS                                                         | #19762, #27634, #24815 (and probably others)                                                         | `Commit ffe66bff <https://github.com/qgis/QGIS/commit/ffe66bff82be16dd90cd95f13331e5be7ca2c628>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Don't force fallback to WGS84 for unknown layer CRSes                                                                                                    | unreported                                                                                           | `Commit 93741566 <https://github.com/qgis/QGIS/commit/937415663f609fa7e41056aeb1176a0a145accc1>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix memory layers cannot use non-EPSG CRS codes                                                                                                          | unreported, but likely a cause of many bugs                                                          | `Commit 2dad68f7 <https://github.com/qgis/QGIS/commit/2dad68f76396a419b25fa8dad2b7b16552086740>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix crash after deleting report sections                                                                                                                 | `#31302 <https://github.com/qgis/QGIS/issues/31302>`__                                               | `Commit 3356460c <https://github.com/qgis/QGIS/commit/3356460ce70af15105880d135271595dccfc397c>`__   | `Commit d3230ac0 <https://github.com/qgis/QGIS/commit/d3230ac0c545604a97fa3028ca3e846bff65004c>`__   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Ensure polygon rings generated for rendering are always closed                                                                                           | unreported                                                                                           | `Commit a69e38d9 <https://github.com/qgis/QGIS/commit/a69e38d9c358faea5ae4a8628add1e6721cc23e8>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Don't crash QgsTessellator when an empty polygon is added                                                                                                | unreported                                                                                           | `Commit 761b2e77 <https://github.com/qgis/QGIS/commit/761b2e778594f4051a72d02b898354f501e336fe>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix crash in topology checker plugin after a check is canceled                                                                                           | unreported                                                                                           | `Commit 606bcd35 <https://github.com/qgis/QGIS/commit/606bcd35143d09cca5b1ec45bdb5b13236e4376b>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix topology checker multipart check                                                                                                                     | `#28361 <https://github.com/qgis/QGIS/issues/28361>`__                                               | `Commit 5101386b <https://github.com/qgis/QGIS/commit/5101386b37fb4d180d32d31663404e3bcc647cec>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix crash on exit when topology checker dock is open with visible results                                                                                | unreported                                                                                           | `Commit 64375ad4 <https://github.com/qgis/QGIS/commit/64375ad4d28597eb97808f64e1481915df7a676c>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Don't load print layouts when opening project browser items                                                                                              | via email                                                                                            | `Commit 9f1ce084 <https://github.com/qgis/QGIS/commit/9f1ce08418db9545ed18d6711c472833f9889e1d>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Add QgsProject flag to avoid loading print layouts when reading a project file, avoids crashes when project is loaded in background thread               | via email                                                                                            | `Commit d0ed3746 <https://github.com/qgis/QGIS/commit/d0ed3746629ae9c9349fe2e9c75550679120026d>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Don't try to load HTML content when a layout is created in a background thread                                                                           | via email                                                                                            | `Commit 53252496 <https://github.com/qgis/QGIS/commit/532524961c0880b33e1d7ed4a3ce0805d7f0bc71>`__   | `Commit 5fcab0e7 <https://github.com/qgis/QGIS/commit/5fcab0e713a1e9ffde8b049f620d4a5cd6a81ff3>`__   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Huge speed up to QgsTessellator                                                                                                                          | `Commit 577e1e96 <https://github.com/qgis/QGIS/commit/577e1e962d4004f9cd11a169860e0b099216c963>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] Ensure all objects used by the model are correctly imported                                                                                 | `#32004 <https://github.com/qgis/QGIS/issues/32004>`__                                               | `Commit e5e3fe47 <https://github.com/qgis/QGIS/commit/e5e3fe473e8e6764f528b4a40095a7a047e9c357>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] Avoid confusing use of expression parameter type in Random Points in Polygon algorithm                                                      | `#27640 <https://github.com/qgis/QGIS/issues/27640>`__                                               | `Commit 196e15a0 <https://github.com/qgis/QGIS/commit/196e15a0ff974622bfa1e7dfdeb9fe8567a7f3b7>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Update map settings variables in UI when map extent/rotation changes                                                                           | `#24136 <https://github.com/qgis/QGIS/issues/24136>`__                                               | `Commit 86c83537 <https://github.com/qgis/QGIS/commit/86c83537f9b03816ba5b8f90c8cf8a2820077441>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix layout variables set programmatically do not show in GUI                                                                                   | `#28837 <https://github.com/qgis/QGIS/issues/28837>`__                                               | `Commit 1afdd935 <https://github.com/qgis/QGIS/commit/1afdd935cf84cbd702093935a676672d1e349da1>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Ensure variable panels are updated when layout or atlas properties change                                                                      | `#26402 <https://github.com/qgis/QGIS/issues/26402>`__                                               | `Commit 2b31e03a <https://github.com/qgis/QGIS/commit/2b31e03ad0659500a733d71c10c54e17e6817c10>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Move page background setting to a per-page option                                                                                              | `#25695 <https://github.com/qgis/QGIS/issues/25695>`__                                               | `Commit 45e847ef <https://github.com/qgis/QGIS/commit/45e847ef69b56b4c12774363e20a7a05f49e8618>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Optimize QgsContrastEnhancementFunction                                                                                                                  | `Commit f5c21a0f <https://github.com/qgis/QGIS/commit/f5c21a0fbd72fe840900e0ad35c4af285fbd8a79>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Prevent removal of the last remaining page in a layout                                                                                         | via email                                                                                            | `Commit e6ecfdd3 <https://github.com/qgis/QGIS/commit/e6ecfdd39bc2ae842c437700508899a9e1aa9dcd>`__   | `Commit b65f23f8 <https://github.com/qgis/QGIS/commit/b65f23f86b4630b4b5157400a713c36081bd56b9>`__   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix crash when exporting layout with no pages                                                                                                  | via email                                                                                            | `Commit b784d698 <https://github.com/qgis/QGIS/commit/b784d6982826039bd9fa35b7ecd1a362e29c0b04>`__   | `Commit f8355cbb <https://github.com/qgis/QGIS/commit/f8355cbbbe4bdbbae9c3f1b135ed59bbc51226a2>`__   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix conditional formatting panel high dpi issues                                                                                                         | `Commit 1f033fe8 <https://github.com/qgis/QGIS/commit/1f033fe83d63a2edb6ddc2b6d90169e3b814764e>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix loss of font setting when editing conditional format                                                                                                 | `Commit 72efc1ed <https://github.com/qgis/QGIS/commit/72efc1edde693800b6604e8ec3afcc892ea5239e>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Avoid overflow in QgsImageOperation                                                                                                                      | `Commit aefbf662 <https://github.com/qgis/QGIS/commit/aefbf6627256637cf455b2df409b3a4bf8171b33>`__   | `Commit 9f4d3a87 <https://github.com/qgis/QGIS/commit/9f4d3a8745b2d89faeb6a9272369eaa772e3638c>`__   |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] Extend api for retrieving a layer in a compatible format                                                                                    | via 3rd party plugin bug tracker                                                                     | `Commit 651c5071 <https://github.com/qgis/QGIS/commit/651c5071806d6f4f4dafc800e6b0d67f043a9ef0>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix conditional styles in feature list view do not update when the layer's conditional styles are changed                                                | `Commit bccd5a46 <https://github.com/qgis/QGIS/commit/bccd5a46106d7c5a63b3bd8c64ad1491a60205af>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix broken display of conditional styles in feature list view                                                                                            | `Commit 5f7264d4 <https://github.com/qgis/QGIS/commit/5f7264d4d18d6894c4d33017439dc517a932fd75>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix incorrect conditional styling applied to rows in some cases                                                                                          | `Commit c15c7271 <https://github.com/qgis/QGIS/commit/c15c72718909f4bce2d172b819c74ec7d8d4d9b3>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Use invalid colors, not transparent colors, to indict not set colors in conditional formats, fixes incorrect colors used for conditionally styled rows   | `Commit bc82cffd <https://github.com/qgis/QGIS/commit/bc82cffd85342d92435600547c220eb1eaf90257>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| "[labeling] When an extreme number of features are being labeled from a single layer, place additional limits on the maximum number of                   |                                                                                                      |                                                                                                      |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| labeling candidates to generate for features in this layer"                                                                                              | `Commit 61bfced6 <https://github.com/qgis/QGIS/commit/61bfced6a7ae109bc97a0924eae108c0e51916d5>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix incorrect alignment of items when the align or distribute tools are used with items with a non-top-left reference point                    | `#31900 <https://github.com/qgis/QGIS/issues/31900>`__                                               | `Commit b4550dc4 <https://github.com/qgis/QGIS/commit/b4550dc4c06eec23ace4cbc5c6f1f8b23c8ee14f>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] Respect user set default vector output format in vector split algorithm                                                                     | `Commit 90bac82f <https://github.com/qgis/QGIS/commit/90bac82f124ccb53e43bb99f5d483105bea1c967>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix GUI is not updated when layout atlas is set to use the default filename expression                                                                   | `#20786 <https://github.com/qgis/QGIS/issues/20786>`__                                               | `Commit a4da849e <https://github.com/qgis/QGIS/commit/a4da849e9d190ece1b748303cc8f68333f1e0e78>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [reports] Remove useless extra set of export actions                                                                                                     | `#26384 <https://github.com/qgis/QGIS/issues/26384>`__                                               | `Commit d6b41813 <https://github.com/qgis/QGIS/commit/d6b4181349a274e8d34196a340f4b806403af06b>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [reports] Fix crash when print button clicked before a report section is opened                                                                          | unreported                                                                                           | `Commit c93fd0a4 <https://github.com/qgis/QGIS/commit/c93fd0a4350ea14db9728ad17ada06e70eb9ffd6>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [reports] Reduce minimum width of report organiser dock                                                                                                  | `#25916 <https://github.com/qgis/QGIS/issues/25916>`__                                               | `Commit 7c490848 <https://github.com/qgis/QGIS/commit/7c4908481269f38e1b96c730542d5299903963fb>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Add a page number selection combo box at the top of the guide manager dock                                                                     | `#25700 <https://github.com/qgis/QGIS/issues/25700>`__                                               | `Commit 2f22aeaf <https://github.com/qgis/QGIS/commit/2f22aeaf276785867ed850f54c691a0a5b7c0aeb>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Show color button style "Pick color" and "Chooe Color" and symbol button menu                                                                            | `#25696 <https://github.com/qgis/QGIS/issues/25696>`__                                               | `Commit 39cfd0f9 <https://github.com/qgis/QGIS/commit/39cfd0f935bb8c6669237bc7abe6ca89c6a82a32>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix out of sync layout bounds after page removal                                                                                                         | `#26665 <https://github.com/qgis/QGIS/issues/26665>`__                                               | `Commit d498eed0 <https://github.com/qgis/QGIS/commit/d498eed0a5caf01b914a2c25f0c1d255d955b4a9>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix odd selection behavior when keyboard modifiers are pressed when rectangular selection ends                                                 | `Commit 37b5af54 <https://github.com/qgis/QGIS/commit/37b5af54d9423563d17422f5b90d6a7dbdfe0299>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix interaction with group members in items panel                                                                                                        | `#26674 <https://github.com/qgis/QGIS/issues/26674>`__                                               | `Commit 5154240f <https://github.com/qgis/QGIS/commit/5154240fa94401952329138300dd2035e5519d5e>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layout] Fix invalid svg exports when including metadata                                                                                                 | `#28130 <https://github.com/qgis/QGIS/issues/28130>`__                                               | `Commit cc94aebc <https://github.com/qgis/QGIS/commit/cc94aebc6fa2e53adc99902b7f7ac4f87e0361db>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [legends] Fix missing symbols for inverted polygon layers when using filter by map content                                                               | `#22718 <https://github.com/qgis/QGIS/issues/22718>`__                                               | `Commit abc9f47c <https://github.com/qgis/QGIS/commit/abc9f47ca471540c9b0f9dd6159d3ac7f9791a3c>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Use a slightly larger font size in CRS details on Windows                                                                                                | `#31297 <https://github.com/qgis/QGIS/issues/31297>`__                                               | `Commit 757017c2 <https://github.com/qgis/QGIS/commit/757017c2c29a0ea4b72527e4cd98e700c720022c>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [processing] Add warning when packaging a geopackage with no layers                                                                                      | `#31888 <https://github.com/qgis/QGIS/issues/31888>`__                                               | `Commit f11e6603 <https://github.com/qgis/QGIS/commit/f11e6603957f69a34ad7aa9893aa144cc5020ca4>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix crash when opening layout with dynamic image in html label                                                                                 | `#28996 <https://github.com/qgis/QGIS/issues/28996>`__                                               | `Commit 5db6165f <https://github.com/qgis/QGIS/commit/5db6165fb597c2db278e678953578992789fa38b>`__   | `Commit e29865cd <https://github.com/qgis/QGIS/commit/e29865cd485c3576db27aab4cad86614f3eff2f3>`__   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Expose report feature settings when an attribute table is used in an atlas                                                                               | `#28441 <https://github.com/qgis/QGIS/issues/28441>`__                                               | `Commit 9fd17c8f <https://github.com/qgis/QGIS/commit/9fd17c8f3cce8fb5864db137da71c3cb61b44510>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix attribute table ignores cell margin for top/bottom aligned text                                                                            | `#31259 <https://github.com/qgis/QGIS/issues/31259>`__                                               | `Commit 7b356fe4 <https://github.com/qgis/QGIS/commit/7b356fe4cde1b030ddfb589a22cb59229311074e>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix truncated legend symbol borders when layer has opacity set                                                                                           | `Commit 30e14938 <https://github.com/qgis/QGIS/commit/30e149387bcccbd14f057a16cb27729c57c9a210>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix adding/moving legend is very slow with large projects                                                                                                | `#29058 <https://github.com/qgis/QGIS/issues/29058>`__                                               | `Commit 758ac909 <https://github.com/qgis/QGIS/commit/758ac9092f9fac3f7533766f329f17832b2dcd35>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [reports] Fix predefined scale mode is incompatible with report outputs                                                                                  | `#29196 <https://github.com/qgis/QGIS/issues/29196>`__                                               | `Commit fcd21e48 <https://github.com/qgis/QGIS/commit/fcd21e485068d8082bdef0a5a7393b57fe5bf3c1>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Ensure atlas expression evaluation has access to coverage layer scope                                                                                    | `#31807 <https://github.com/qgis/QGIS/issues/31807>`__                                               | `Commit 3de05939 <https://github.com/qgis/QGIS/commit/3de059395706a225ca137b3d4a7a34b27d3cc9ae>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Resizing pages to content should not create empty page size if no items are present                                                                      | `#29034 <https://github.com/qgis/QGIS/issues/29034>`__                                               | `Commit 421e68cf <https://github.com/qgis/QGIS/commit/421e68cf5ae5637001765842e257caf6becdb876>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix map rotation does not immediately restore in reports                                                                                                 | `#31217 <https://github.com/qgis/QGIS/issues/31217>`__                                               | `Commit f5afebe5 <https://github.com/qgis/QGIS/commit/f5afebe5dd0228ceb612a9823a80c77ccd51a1e6>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Do not return nan values when an assistant is used with min val == max val                                                                               | `#31242 <https://github.com/qgis/QGIS/issues/31242>`__                                               | `Commit 97923751 <https://github.com/qgis/QGIS/commit/979237515ce2921b9552a99eda071e9e9a14297a>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| [layouts] Fix label items don't update when their opacity < 100                                                                                          | `#29079 <https://github.com/qgis/QGIS/issues/29079>`__                                               | `Commit f9a47738 <https://github.com/qgis/QGIS/commit/f9a47738aaaec7504f912b2442195662a216b9e3>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix project load status indicator can get "stuck" after project load                                                                                     | unreported                                                                                           | `Commit 40d95b69 <https://github.com/qgis/QGIS/commit/40d95b69d91ade71473f5ea0182040d8398cc668>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix corrupted expressions in filter indicator tooltips                                                                                                   | `Commit 393e623b <https://github.com/qgis/QGIS/commit/393e623ba7d278eabc4f09aeaabb92f56fa269c9>`__   | `Commit 8e0e368f <https://github.com/qgis/QGIS/commit/8e0e368f255ba10c530afd445ecd1ab53bf266bb>`__   |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix cannot use GPS panel to draw features in multi polygon/line                                                                                          | `#29144 <https://github.com/qgis/QGIS/issues/29144>`__                                               | `Commit dc2b209d <https://github.com/qgis/QGIS/commit/dc2b209da3609a47b1457c0cb12417afbcb36344>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix loss of label background settings when restoring projects.                                                                                           | `#31427 <https://github.com/qgis/QGIS/issues/31427>`__                                               | `Commit aa4a8da3 <https://github.com/qgis/QGIS/commit/aa4a8da3a713b6961fccce019c5e9b5778f68b23>`__   | n/a                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Fix crash in point displacement renderer                                                                                                                 | `Commit 7043933f <https://github.com/qgis/QGIS/commit/7043933ff2bed42df5ae3439867330e39fe60f53>`__   | n/a                                                                                                  |                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Nyall Dawson <https://north-road.com/>`__

.. |image1| image:: images/projects/ce6ba8fc893e51ec721c9dded4dd98d11806a223.png
   :class: img-responsive img-rounded center-block
.. |image2| image:: images/entries/b1aba6e9334ee1d862bde8f66f9ae4d30d945703.png
   :class: img-responsive img-rounded
.. |image3| image:: images/entries/07ae51e244cc5b1d6a971e386ea98f1314a3dfb1.png
   :class: img-responsive img-rounded
.. |image4| image:: images/entries/79f8365571da7b6c60f001f388d9c02d9e8920b2.png
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/c1f50067d50b909e38b7333ad5d8d415e763801d.png
   :class: img-responsive img-rounded
.. |image6| image:: images/entries/1ccab8f4328238f5275e41c3d466bf27a5d097a2.png
   :class: img-responsive img-rounded
.. |image7| image:: images/entries/bf657c21ba6deaff10ff80611a77b435e12155e5.png
   :class: img-responsive img-rounded
.. |image8| image:: images/entries/3a9fd11192cdbdaa2f139a28d63cc33e1d10c3bc.png
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/7bcc02d06eb7030a289e129b9bed2656d6c6fefb.png
   :class: img-responsive img-rounded
.. |image10| image:: images/entries/14b307efef5de1085e4c402d3e06e5dd10a64ae2.png
   :class: img-responsive img-rounded
.. |image11| image:: images/entries/4e53a6482dacb6e2d6d1ff2a8c4592d98f82430a.png
   :class: img-responsive img-rounded
.. |image12| image:: images/entries/0b830e5ea769aacfd9c5bf9d8028ed278590d803.gif
   :class: img-responsive img-rounded
.. |image13| image:: images/entries/9db2c54c0d65bc61da8c0c46cfefcbab96c833df.png
   :class: img-responsive img-rounded
.. |image14| image:: images/entries/737cd2f8bc569ee9ad7df9aee02eec83b4e6facd.png
   :class: img-responsive img-rounded
.. |image15| image:: images/entries/e49baccdb83da1b88433e2c7718642ae4a78810d.jpg
   :class: img-responsive img-rounded
.. |image16| image:: images/entries/b2a650a874e263173a56d93b046df7f031eb8d6e.png
   :class: img-responsive img-rounded
.. |image17| image:: images/entries/1030adf0c9c0c46ff5a38a09ae16a735bdff3684.png
   :class: img-responsive img-rounded
.. |image18| image:: images/entries/41ab256b477b0baf0971b398f882a6633cd12615.png
   :class: img-responsive img-rounded
.. |image19| image:: images/entries/bb6303d9589972781988549283ef150700ba5863.png
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/570ff6f8c365a78d05bb56cfdbd8647f83aac331.jpg
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/420b784c4fc79a09358201c8814cfe48b82dbbca.png
   :class: img-responsive img-rounded
.. |image22| image:: images/entries/78263d3350afd05147928378f81dddba13961acc.png
   :class: img-responsive img-rounded
.. |image23| image:: images/entries/69961f6faa732b683ccfb1ab539250b21ea5bd26.png
   :class: img-responsive img-rounded
.. |image24| image:: images/entries/ec2940b4222b8172403b20b0f70af0588c38f0cc.gif
   :class: img-responsive img-rounded
.. |image25| image:: images/entries/e571fc1811ccf58e007a7913600b65377e31ed41.jpg
   :class: img-responsive img-rounded
.. |image26| image:: images/entries/7eea84e316a148c6872369d3df5fb63a6bc2f043.png
   :class: img-responsive img-rounded
.. |image27| image:: images/entries/dac35ad47f56dd24456df6d318359a0d70efeb15.png
   :class: img-responsive img-rounded
.. |image28| image:: images/entries/8c6426a723b9fdc1cead1949f3304db4763ecb9c.png
   :class: img-responsive img-rounded
.. |image29| image:: images/entries/9f73cce9c3f3ff81c6b66adab654ff4e23524ae1.png
   :class: img-responsive img-rounded
.. |image30| image:: images/entries/e219a18e997a6506314c1777c94050bf4a69cf9b.png
   :class: img-responsive img-rounded
.. |image31| image:: images/entries/245ada907ba2e14ad291dae54b93adb327b64225.png
   :class: img-responsive img-rounded
.. |image32| image:: images/entries/4b8ed681a38435a2f0bf299fd28f299e2873848c.png
   :class: img-responsive img-rounded
.. |image33| image:: images/entries/4a7b306942755ac96cfa9bc97abbfd7815d17ad4.png
   :class: img-responsive img-rounded
.. |image34| image:: images/entries/6b2177a5781bc2d5cdfb63f121501a734897e4a1.png
   :class: img-responsive img-rounded
.. |image35| image:: images/entries/3b93e7b25eef3e3f149ba8db022e467258a74116.png
   :class: img-responsive img-rounded
.. |image36| image:: images/entries/0f24e8e2746cb4b7890d015c2ae476f1f1bf96ef.png
   :class: img-responsive img-rounded
.. |image37| image:: images/entries/d6791d32d649fdc3b2e86aa257a33796391e13e0.png
   :class: img-responsive img-rounded
.. |image38| image:: images/entries/8a0081e087a6f9ff9180615f34bb56ea6dccc649.png
   :class: img-responsive img-rounded
.. |image39| image:: images/entries/9f61759f0b8d6a61ea070a5328c4f641c582778e.PNG
   :class: img-responsive img-rounded
.. |image40| image:: images/entries/d9224e26da62b092d56fd091195942d4142e9bd7.PNG
   :class: img-responsive img-rounded
.. |image41| image:: images/entries/18f42d184246ed167be10dee72f5000671d7ac01.png
   :class: img-responsive img-rounded
.. |image42| image:: images/entries/471f15d2616ffc1531c8eef95d4d8ed87d161998.png
   :class: img-responsive img-rounded
.. |image43| image:: images/entries/87cae0401b93aa308c156a615e63a71e98d25980.png
   :class: img-responsive img-rounded
.. |image44| image:: images/entries/8d6075eb1c4fc38b76f9761836048e940be408f8.PNG
   :class: img-responsive img-rounded
.. |image45| image:: images/entries/94fe90f54308a81c5f031066c132e1ad5e8e6ac2.PNG
   :class: img-responsive img-rounded
.. |image46| image:: images/entries/479f2a711f8c4b254e72348eda3c79187d4117f2.PNG
   :class: img-responsive img-rounded
.. |image47| image:: images/entries/60aac076d447f244dd232a8e8766a109032a9540.png
   :class: img-responsive img-rounded
.. |image48| image:: images/entries/d0471bc7ea65e476537c8828a7850a64ca9120ef.png
   :class: img-responsive img-rounded
.. |image49| image:: images/entries/a0adf902641c8ace142d9749e632e114262342cd.png
   :class: img-responsive img-rounded
.. |image50| image:: images/entries/1b68212fa4a991c79f7d352b5ee3798d0e9a10a3.png
   :class: img-responsive img-rounded
.. |image51| image:: images/entries/6ef35bc88e69aaf92f5f223249bf792ffd4d28d5.png
   :class: img-responsive img-rounded
.. |image52| image:: images/entries/4c9dd54203cbce44f91e85ed1ff01f1cbb4a40c5.png
   :class: img-responsive img-rounded
.. |image53| image:: images/entries/d3822539302bcd15ae05ef697abafaa1aa5c3ae4.png
   :class: img-responsive img-rounded
.. |image54| image:: images/entries/f208b7c32bfe608a448dc2e9359de20e3e4397dd.png
   :class: img-responsive img-rounded
.. |image55| image:: images/entries/57f395b303ba963e67242e0f2cfe7104e61f2ad0.png
   :class: img-responsive img-rounded
.. |image56| image:: images/entries/0119e6f0b3d950d613d224d7bbd53a38575b3579.png
   :class: img-responsive img-rounded
.. |image57| image:: images/entries/8329961bfa04631c5a970888f9a21bad66ddc6fa.png
   :class: img-responsive img-rounded
.. |image58| image:: images/entries/e1234a3ca30866b91f64f97b83fdf0fb90838cb6.png
   :class: img-responsive img-rounded
.. |image59| image:: images/entries/5adaa5a973e0b232bae3a8dbab8739c8887ac70e.png
   :class: img-responsive img-rounded
.. |image60| image:: images/entries/bfaa5fc4c03d27e5345475172f5e7bdb20a4f6ff.png
   :class: img-responsive img-rounded
.. |image61| image:: images/entries/71d731c71f864fcb542f2f7ec52c68e4c03068d3.png
   :class: img-responsive img-rounded
.. |image62| image:: images/entries/45744c5a4a4c94e1c71a91bcfa7b672333002e75.png
   :class: img-responsive img-rounded
.. |image63| image:: images/entries/81af9beefcd8522ecc0f953b2a6b9b4895e35675.png
   :class: img-responsive img-rounded

