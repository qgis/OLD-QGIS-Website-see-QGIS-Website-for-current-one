.. _changelog316:

Changelog for QGIS 3.16
=======================

|image1|

Release date: 2020-10-27

Another great day for the QGIS project! The new long term support release brings a wide range of features to both QGIS Desktop and QGIS Server. This release brings a wealth of new options for 3D mapping, mesh generation from other data types, additional spatial analysis tools, symbology and user interface enhancements to name but a few! A host of tools have been incorporated into the ever-expanding processing framework, and the QGIS browser now supports advanced database interaction functionality that was previously reserved for the DB Manager plugin. These are a few of the improvements that have been introduced from this release, and users of the previous LTS will find a massive number of new features available since 3.10. We are pleased to detail some of the additional highlights of this new release below.

**Thanks**

We would like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to `QGIS.ORG <qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our `donors list <https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our `sustaining member page <https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships>`__ for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

:raw-html:`<div id="qgissustainingmembersatom"> <!-- to be filled via javascript loading of atom feed --> </div>`

QGIS is Free software and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision-making tools will result in a better society for all of humanity.

.. contents::
   :local:

General
-------

Add user groups easter egg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type the words "user groups" into the current coordinates window and watch the magic happen.

|image2|

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Temporal
--------

Ability to export temporal animation frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows exporting of temporal animation frames to successive images, for later stitching together in an external application. Users have precise control over the image size and map extent.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Map Tools
---------

Go-To locator
~~~~~~~~~~~~~~~~~~~~~~

We have added a new goto locator filter.

The goto indicator takes in the following strings:

-  A pair of x and y coordinates (separated by a comma or space).
-  An OSM, Leaflet, or OpenLayers formatted URL.
-  A Google maps URL.

The logic of the XY string is as follows:

-  If the canvas CRS isn't WGS84:

   -  If the coordinate fits within WGS84 bounds, add a WGS84 result (this is weighted to have higher priority than the canvas CRS result below).
   -  If the coordinate fits within the canvas CRS bounds, add a canvas CRS result.

-  If the canvas CRS is WGS84:

   -  If the coordinate fits within the WGS84 bounds, add a WGS84 result.

|image3|

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

User Interface
--------------

Add context menu to map canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The map canvas now has a right-click context menu. By default, it creates the "Copy Coordinate" menu that was introduced with QGIS 3.14, however, it is expected that this functionality will be extended to allow many more functionalities to be accessed with spatial context in the future.

|image4|

This feature was developed by `jakimowb <https://api.github.com/users/jakimowb>`__

Symbology
---------

Vector tile styling improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple enhancements were introduced for the editing of complex vector tiles styles:

-  Show tooltips in lists, so that full filter rules and names can be viewed without resizing columns
-  Show the current canvas zoom level in the widgets
-  Allow users to filter the list of styles to only show those which are currently visible
-  Set the correct canvas zoom level when editing symbols, so that expression previews work nicely

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Allow users to optionally specify the URL for the default style on vector tile connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When setting up a vector tile source connection, there's a new option to enter a URL to a MapBox GL JSON style configuration. If one has been entered, then that style will be applied whenever the layers from the connection are added to QGIS.

This also works also with ArcGIS Vector Tile Service connections which will the default style configuration specified in the server configuration.

|image5|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Allow data-defined offset for fill symbol layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any fill symbol layer which supports offsetting polygons, including simple fills, raster image fills, shapeburst and gradent fills, now allow data-defined offsets

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Import MapBox GL JSON styles for vector tile layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can now load MapBox GL JSON style configuration files when importing style files on vector tile layers

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Expose option to offset simple line dash patterns by a preset amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows for tweaking the positioning of dashes/spaces in the line, so that the dashes/spaces can be placed at nicer positions to account for corners in the line (also can be used potentially to "align" adjacent dash pattern borders).

The offset can be set in various units, including map units, and can also be data defined.

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add options to dynamically tweak dash pattern in simple line symbol layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Options have been added to allow the tweaking of dash patterns to allow more control for improving the rendered quality of line symbols. These options include:

-  Align dash pattern to line length: If checked, the dash pattern lengths will be subtly adjusted in order to ensure that when a line is rendered it will end with a complete dash element, instead of a gap element or partial dash element.

-  Tweak dash pattern at sharp corners: If checked, this option dynamically adjusts the dash pattern placement so that sharp corners are represented by a full dash element coming into and out of the sharp corner. It's designed to better represent the underlying geometry while rendering dashed lines, especially for jagged lines.

The following images illustrate the "Align dash pattern to line length" change in action, with yellow lines indicating the true start and end position of the line features being symbolised.

Before:

|image6|

After:

|image7|

|image8|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Manage 3D symbols through style manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support has been added for managing 3D symbols through the QGIS style manager, including support for importing and exporting libraries of 3d symbols, and completes the recent work in fully abstracting out 3D symbols and their widget handlers.

Unfortunately, there are no thumbnails generated for 3D symbols in the library, and a generic icon is used for all 3D symbols for the time being. Generating thumbnails is no trivial matter, so it has been deferred for the time being.

This feature addresses the issue raised in `31479 <https://github.com/qgis/QGIS/issues/31479>`__.

|image9|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Labelling
---------

Add option to allow users to control the placement of labels along line features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new "Label Anchoring" section in the line placement settings for labels allows users to specify whether labels should be placed at the center, start or end of lines. In addition, it allows offsets of these positions (based on the percentage of the feature length), which may be defined statically or by using a data-defined definition.

|image10|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Control anchor point for line labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new option is exposed which allows users to control whether the anchor point for the labeling of line features is a hint or a strict requirement. The resulting behavior modifications include the following:

-  Strict: Labels are placed exactly on the label anchor only, and no other fallback placements are permitted.
-  Hint: The label anchor is treated as a hint for the preferred label placement, but other placements close to the anchor point are permitted.

|image11|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Diagrams
--------

Render axis for stacked bar diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This adds support for rendering the axis on stacked bar diagrams if an axis has been set. The implementation is based on the axis rendering for the histogram diagram.

Negative values are not handled properly by stacked bar diagrams with or without the axis being displayed.

Addresses `Issue 34915 <https://github.com/qgis/QGIS/issues/34915>`__

|image12|

This feature was developed by `Dan Minor <https://api.github.com/users/dminor>`__

Mesh
----

In-memory mesh datasets with persistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature introduces the ability to create in-memory dataset groups for mesh layers. These dataset groups are temporary and are not kept once the project is closed.

A new option has been added to the mesh calculator which allows the creation of in-memory dataset groups.

This feature also introduces the ability to remove or save these memory dataset groups to a file with the specified driver.

|image13|

|image14|

This feature was funded by `Artelia Group <https://www.arteliagroup.com/en>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk>`__

Multi identify for mesh layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The identify tool has been adapted when used on mesh layers and now displays the dataset value corresponding to the current time of the temporal controller for all dataset groups. The active dataset groups (scalar and eventually vector) are first displayed, then the other dataset groups. There is also other information displayed, including:

-  Source where the dataset is stored
-  Time step of the dataset that is displayed (can be different than the time of the temporal controller). Displays nothing if the dataset group is not temporal
-  Centroid of the corresponding face
-  Coordinate of the snapped vertex (if one is snapped)
-  Center of the snapped edge (if one is snapped)

When the map canvas does not have temporal navigation enabled, the identify results contain only information about the active dataset groups which have static datasets defined in the mesh properties dialog.

|image15|

This feature was funded by `Artelia Group <https://www.arteliagroup.com/en>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk>`__

Virtual dataset groups for mesh layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to use "virtual" data set groups has been introduced for mesh layers. This replaces the "memory" dataset group used in `37389 <https://github.com/qgis/QGIS/pull/37389>`__.

With the mesh calculator, users may choose to create those "virtual" dataset groups that will be added to the layer. Values are not stored in memory but each dataset is rather calculated when needed with the formula entered in the mesh calculator.

Those virtual dataset groups are saved within the project and be removed or saved to file for persistence.

Persistent and virtual dataset groups are distinguished in the source tab of the mesh layer properties by changes in the color of the background for each item, indicated as follows:

Persistent: yellow

Virtual: purple

|image16|

|image17|

This feature was funded by `Artelia Group <https://www.arteliagroup.com/en>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk>`__

Add export to QgsMesh method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A method has been added to export a triangulation to a QgsMesh instance, with the possibility to construct mesh layer with triangulation from existing points and lines. This is the first step to allow the ability to obtain a QgsMesh from other map layers.

The Triangulation and DualEdgeTriangulation classes were also renamed and refactored to make them more consistent with QGIS code.

-  Add a method to export the triangulation to a QgsMesh instance.

This feature was developed by `Vincent Cloarec <https://api.github.com/users/vcloarec>`__

TIN Mesh creation
~~~~~~~~~~~~~~~~~~~~~~~~~~

TIN mesh layers can be created from vector layer data (vertices and/ or break lines). The resulting mesh is constructed with a constrained Delaunay triangulation. This mesh layer can be created using the python API or through an algorithm in the processing tool box.

|image18|

This feature was developed by `Vincent Cloarec <https://api.github.com/users/vcloarec>`__

Rendering
---------

Gamma correction filter for raster layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add gamma correction filter pipe for raster layers in addition to the existing brightness, contrast, hue, and saturation filters. Users can adjust the gamma value from the layer properties dialog, using styling panel and/or new buttons on the Raster toolbar. Default gamma value is 1.0 and it can be adjusted within the range 0.1 to 10.

Addresses `Issue 13512 <https://github.com/qgis/QGIS/issues/34915>`__

Also adds a rendering test for brightness and contrast filter which has no test at all and fixes some deprecation warnings in the Python test for ``QgsRasterLayer``.

|image19|

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

3D Features
-----------

Allow 3D material texture files to be embedded in style/project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some minor API and code cleanups were performed, as well as introducing the use of QgsImageCache for 3D texture files in order to allow them to be embedded within projects.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Shadow rendering
~~~~~~~~~~~~~~~~~~~~~~~~~

Shadows can now be rendered in 3D views.

|image20|

This feature was developed by `Nedjima Belgacem <https://api.github.com/users/NEDJIMAbelgacem>`__

Export 3D scenes
~~~~~~~~~~~~~~~~~~~~~~~~~

3D Scenes can now be exported for use in other 3D software, such as Blender. This export feature supports multiple additional functions including output model simplification by specifying the output resolution, optional model smoothing, and the exporting of 3D vector layers.

|image21|

This feature was developed by `Nedjima Belgacem <https://api.github.com/users/NEDJIMAbelgacem>`__

Directional lighting support for QGIS 3D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added directional lights to QGIS 3D

-  Now the user can add directional lights to the 3D views.
-  I added a tab widget under the lights section of the 3D configuration dialog.
-  The user can specify the direction of the light, its color and intensity.
-  This is just a duplication of the already existing point lights implementation with some changes.
-  Later it may be useful to add a way to visualize the light direction by displaying a mesh that is positioned at camera's view point like an arrow that displays how the sun lights the scene for example.

|image22|

.. raw:: html

   <div class="col-lg-8 col-md-offset-1">

.. raw:: html

   </div>

This feature was developed by `Nedjima Belgacem <https://api.github.com/users/NEDJIMAbelgacem>`__

Texturing support for vector layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Texturing support has been added for QGIS 3D with the following new functionalities:

-  Users can now select an image to be displayed on the surfaces of buildings as diffuse map from the symbol properties.
-  The user can also change the scale of textures from the symbol properties.

Some visual issues may appear when using textures. These issues relate to the normals of surfaces that you may be able to fix by checking "add back faces" and playing around with the invert normals and culling mode in the symbol properties.

|image23|

This feature was developed by `Nedjima Belgacem <https://api.github.com/users/NEDJIMAbelgacem>`__

Enable embedded and remote 3D models for 3D point symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can now utilise and embed remote 3D models for 3D point symbols.

|image24|

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Add option to show light source origins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A feature which allows users to toggle a visible sphere at light source origins in a 3D scene.

This allows for the easier repositioning and placement of light sources relative to the scene contents.

Addresses `Issue #37726 <https://github.com/qgis/QGIS/issues/37726>`__.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Improvements for material handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Further improvements for material handling were introduced, and a Gooch shading model was added. This improves the QgsAbstractMaterialSettings API, by:

-  Adding icon support for registered material types (for use in the material selector combo box).
-  Adds support for handling different rendering techniques to QgsAbstractMaterialSettings. Now material classes can indicate which rendering techniques they support (e.g. Triangles, Lines, InstancedPoints, etc.), and the material is only offered when it's compatible with the required technique.
-  The technique handling in the gooch material widget was improved to avoid showing settings that have no effect in a particular context (e.g. hiding all but the ambient color choice for simple 2D line symbols).
-  A new material, "Gooch", was added. This material gives a CAD style 3D render, where the shading is not dependent on appropriate lighting setup in a scene and where the 3D details are always visible, regardless of the lighting choice.

|image25|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Print Layouts
-------------

Expose control over text format and alignment for individual cells in manual text tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds control over setting the text format (e.g. bold/italic/buffer/shadow etc) and text alignment (horizontal and vertical) for the contents of individual cells in a manual text table.

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Use QgsTextRenderer to render attribute table text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows for the full range of text formatting options in layout attribute tables, including buffers, shadows, word spacing etc.

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Use QgsTextRenderer for drawing map grid text in layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows for grid annotations which use buffers, shadows, background shapes, etc.

|image26|

|image27|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Expose option to control PDF image compression method when exporting layouts to PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Options are for Lossy compression, which is the default JPEG compression used, and Lossless compression (which creates bigger files in most cases, but is much more suitable for professional printing outputs or for post-production in other products such as Illustrator etc)

The bad news is that this option is only available in builds based on Qt 5.13 or later.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add automatic clipping settings for atlas maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature allows users to enable map clipping for layout map items so that the maps are clipped to the boundary of the current atlas area feature.

Options exist for:

-  Enabling or disabling the clipping on a per-map basis
-  Specifying the clipping type:

   -  “Clip During Render Only”: applies a painter based clip, so that portions of vector features which sit outside the atlas feature become invisible
   -  “Clip Feature Before Render”: applies the clip before rendering features, so borders of features which fall partially outside the atlas feature will still be visible on the boundary of the atlas feature
   -  “Render Intersecting Features Unchanged”: just renders all features which intersect the current atlas feature, but without clipping their geometry

-  Controlling whether labels should be forced placed inside the atlas feature, or whether they may be placed outside the feature
-  Restricting the clip to a subset of the layers in the project, so that only some are clipped

|image28|

|image29|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add API to QgsMapSettings for specifying clipping regions to apply while rendering maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is currently API only functionality, but functionality has been added which provide the backend capabilities to specify clipping regions which may be used during map render operations.

Although primarily introduced in order to provide functionality which allows the automatic clipping of map elements to the current atlas feature geometry in print layouts, the API has been deliberately implemented in a manner that's very flexible to allow various use cases which require the clipping of regions during map render operations.

For non-vector layers, the clipping is applied through a QPainter clipping path. For vector layers, the API exposes various options in how the clipping should be applied:

#. As an "intersects" style test only: All vector features which intersect the path are rendered, without actually clipping the feature's geometry

#. By modifying the feature's geometry and clipping the geometry to the region: Any stroke or outline settings for the symbol will be rendered along the boundary of the clipping region, even if the feature actually partially falls outside this region.

or

#. Using a painter clip path: Features are clipped to the region, but only at painter time. Boundaries of the feature which fall outside the clip region will not be visible.

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Layout legend maximum marker size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds the possibility to enter the maximum marker size (in mm) to the layout legend widget.

In some cases, such as when point layers use a symbol size which is based on map units, the point markers on the layout legend can get quite big. This feature adds a setting to the layout legend widget which allows the restriction of the maximum marker symbol size while the automatic legend update is still active.

This feature was developed by `mhugent <https://api.github.com/users/mhugent>`__

Allow cells in manual text tables to have expression based contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows individual cells from a manual text table to take their contents from a preset expression. Expressions have access to the full layout item expression context, allowing cells to calculate and display metadata style values or aggregate based calculations.

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Clip layout maps to shape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New functionality was introduced which allows users to clip a map item to a shape or polygon item from their layout, allowing for non-rectangular maps within the layout.

|image30|

|image31|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Support for rotated ticks/annotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tick marks and annotations on a map frame in the print composer can now be rotated, allowing them to align with a rotated map frame as described in `issue 36904 <https://github.com/qgis/QGIS/issues/36904>`__. It works for both rotated maps and reprojected grids.

The following options have been added:

-  Ticks:

   -  Rotate ticks (if unchecked, ticks get drawn as before, not taking angle into account)
   -  Rotated ticks alignment (whether ticks should have a constant length, or be aligned orthogonaly)
   -  Skip low angled ticks (an angle threshold below which ticks aren't drawn, so you can skip ticks for grid lines that are, for example, too close to being parallel with the map edge)

-  Annotations:

   -  Parallel to Tick (Next To/ Horizontal / Vertical Ascending / Vertical Descending)
   -  Draw low angled (if checked, skipped ticks above will still get an annotation)

|image32|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Olivier Dalang, OPENGIS.ch <https://www.opengis.ch>`__

Add page offset expression for Y positions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``layout_pageoffsets`` expression was added for print layouts which returns an array of Y coordinates for the top of each page in the layout. this allows users to dynamically position items on pages in a context where page sizes may change.

For example, to set an item at 2.5mm from the top of page 2 (for the data-defined position Y of a map item) : ``@layout_pageoffsets[1] + 2.5``

This constitutes a workaround for `Issue 37567 <https://github.com/qgis/QGIS/issues/37567>`__.

This feature was funded by `BikePlan <https://www.bikeplan.swiss/>`__

This feature was developed by `Olivier Dalang, OPENGIS.ch <https://www.opengis.ch>`__

Expressions
-----------

Add to\_decimal() function to convert DMS to DD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``QgsCoordinateUtils::dmsToDecimal`` function has been added which exposes the ``to_decimal`` function in expressions. This allows the conversion of DMS (degree/minute/second) strings into DD (decimal degree) format.

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Add "main\_angle" function to return the estimated main angle of a geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Returns the angle of the oriented minimum bounding box which covers the geometry value.

Useful for data defined overrides in the symbology of label expressions, e.g. to rotate labels to match the overall angle of a polygon, and similar for line pattern fill. |image33|

|image34|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Port refFunctions to core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Various overlay operations have been added to the expression engine. This covers the functionality of the refFunctions plugin.

|image35|

The following new expression functions are implemented:: 

* overlay_intersects(layer[,expression][,filter][,limit][,cache])
* overlay_contains(layer[,expression][,filter][,limit][,cache])
* overlay_crosses(layer[,expression][,filter][,limit][,cache])
* overlay_equals(layer[,expression][,filter][,limit][,cache])
* overlay_touches(layer[,expression][,filter][,limit][,cache])
* overlay_disjoint(layer[,expression][,filter][,limit][,cache])
* overlay_within(layer[,expression][,filter][,limit][,cache])
* overlay_nearest(layer[,expression][,filter][,limit][,max_distance][,cache])

In all instances, the spatial operator is evaluated against the other layer. If an expression is provided, it returns an array of results. If no expression is provided, it returns a boolean indicating whether or not there is a match for at least one feature. Features can optionally be filtered by an expression, and optionally be limited to a certain count.

The ``overlay_nearest`` function has an additional max\_distance filter.

|image36|

This feature was developed by `Olivier Dalang, OPENGIS.ch <https://www.opengis.ch>`__

Digitising
----------

Add option to calculate bearing based on travel direction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For devices which report faulty bearing measurements, this option can be used to instead calculate the GPS bearing based on the previous two recorded locations.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Digitizing and splitting curved features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New functionality was introduced that adds the possibility to switch between linear or circular strings when digitizing or splitting vector layer features.

The user can use the keyboard shortcut **Ctrl+Shift+G** to switch between linear/circular.

For splitting features, new overloading methods have been added to the API. When splitting, curves are preserved. For this, the curve is segmentized before splitting, and all the split features are "de-segmentized" after splitting.

A toolbar button was added to enable switching between linear/circular: |image37|

|image38|

|image39|

|image40|

This feature was developed by `Vincent Cloarec <https://api.github.com/users/vcloarec>`__

Data Management
---------------

Rescale raster algorithm for Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a rescale raster algorithm to change raster value range, whilst preserving the shape of the raster's histogram. Useful for when rasters from different sources should be compared or processed together and their pixel values should be in the same range. By default, the algorithm preserves the NODATA value of the input raster but there is an option to override it.

The following image displays a histogram of a DEM (value range is 85-243) |image41| And the next image displays a histogram of same DEM rescaled to the range 100-1000 |image42|

Addresses `Issue 26099 <https://github.com/qgis/QGIS/issues/26099>`__.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Forms and Widgets
-----------------

Multiple widgets for a single relation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple relation widgets may now be created for a single relation, each with their own distinct configuration.

This feature changes the behavior of relation widgets created in the drag and drop interface and provides resolution for `Issue 37675 <https://github.com/qgis/QGIS/issues/37675>`__.

On reading a project configured with older QGIS versions, the config is taken over and written into the new widget configuration. Autogenerated forms no longer allow the configuration of relation editor widgets anymore, but if it has been configured in an older QGIS, the attribute form will still read this configuration.

|image44|

This feature was developed by `signedav <https://api.github.com/users/signedav>`__

Show related features in identify results tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will now be able to see related (child) features in the results window when using the identify tool. Under each identified parent feature, new groups will show containing any related child features, displaying their attributes, actions, and allowing the user to directly open the feature form for the child feature.

This feature addresses issue `18634 <https://github.com/qgis/QGIS/issues/18634>`__.

|image45|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Filter expressions in relation reference widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An option has been added for static filter expression to be used in the relation reference widget.

|image46|

This feature was developed by `Ivan Ivanov <https://api.github.com/users/suricactus>`__

Analysis Tools
--------------

Add project load profile times to debugging tools dock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modification of the QgsRuntimeProfiler class which performs the following functions: 1. Make the profiling thread-safe, so that it's possible to record times across multiple threads 2. Allows different profiling "groups"

The new groups API is used here to expose a breakdown of project load times in the debugging dock, alongside the existing QGIS startup profiling. It's possible now to get a breakdown of the various stages of project load, in order to identify the causes of slow project load times.

TODO: In the majority of cases, performance problems will be caused by one or more layers, so it would be nice to further break down the individual layer load times. For example, for an individual WFS layer, we may see the time taken for the initial "server capabilities" or other queries. Add a group with profile times for map rendering, so you can see exactly which layers in your project are causing slow map redraw times.

In its current form, only the overall load time of each individual layer is displayed.

|image47|

|image48|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Processing
----------

Add help string for parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Help strings can now be specified at the parameter level.

This will be visible in the tooltip, in the CLI and Python Processing API.

|image55|

This feature was developed by `Étienne Trimaille <https://api.github.com/users/Gustry>`__

New "Align points to features" algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm calculates the rotation required to align point features with their nearest feature from another reference layer. A new field is added to the output layer which is filled with the angle (in degrees, clockwise) to the nearest reference feature.

Optionally, the output layer's symbology can be set to automatically use the calculated rotation field to rotate marker symbols.

If desired, a maximum distance to use when aligning points can be set to avoid aligning isolated points to distant features.

An example use case for this is the aligning of building point symbols to follow the nearest road direction by using a data defined rotation value generated by this algorithm.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add modeler algorithm to create directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm allows models to create new file directories. Useful for models which have to output results to certain dynamically created paths (e.g. a folder containing the current date).

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add modeler algorithm to set a project expression variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows a model to set Project-level expression variables during execution. Especially useful with the new `Export Print Layout algorithms <https://github.com/qgis/QGIS/pull/36916>`__ to allow models which dynamically set variables used in a layout prior to export.

This functionality was ported from https://gis.stackexchange.com/questions/359386

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add processing algorithms to export a print layout as PDF/image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Models are able to export print layouts from the current project. One use case for this is allowing users to create an in-project model which exports a particular set of layouts from the project to certain folders, so that they can easily re-export the current project in a single operation instead of having to manually open multiple layouts and export one-by-one.

Additionally, with the new capabilities to have expression based output files inside models, you can automatically export the layouts to a folder with the current date tag and include this in the exported file names!

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Add a save features to file algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is now a native processing algorithm to save vector features to a file dataset within a model. It comes with a pair of advanced features to pass dataset and layer options on to GDAL.

|image56|

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Export layout atlas as PDF algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new QGIS processing algorithm was added which allows the export of a map atlas to PDF. This is the PDF counterpart to the recent export atlas layout to image algorithm.

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

New "Flatten Relationship" algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm flattens all relationships for a vector layer, exporting a single layer containing one master feature per related feature. This master feature contains all the attributes for the related features.

It's designed as a quick way to de-normalize a relation from a project, e.g. to allow exporting to CSV.

This feature was funded by SMEC/SJ

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Export atlas layout as image algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new native processing algorithm was added to export layout atlases as images.

This is useful in models where remote datasets are processed with the goal of being used as atlas coverage layers.

|image57|

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

New Cell statistics algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added a **Cell statistics** raster analysis algorithm. It performs cell-wise statistics on a stack of raster layers while accounting for NoData. The functions available in the current implementation are:

| 

-  Sum
-  Mean
-  Median
-  Standard Deviation
-  Variance
-  Maximum
-  Minimum
-  Majority (most frequent value)
-  Minority (least frequent value)
-  Range (max - min)
-  Variety (count of unique values)

|image49|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

New Equal to frequency algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have added some new raster algorithms that operate on a local cell-by-cell basis in a raster stack. The Equal to frequency algorithm evaluates on a cell-by-cell basis the frequency (number of times) the values of an input stack of rasters are equal to the value of a value raster.

|image50|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

New Greater than frequency algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have added some new raster algorithms that operate on a local cell-by-cell basis in a raster stack. The Greater than frequency algorithm evaluates on a cell-by-cell basis the frequency (number of times) the values of an input stack of rasters are greater than the value of a value raster.

|image51|

This feature was developed by `Clemens Raffler <https://github.com/root676>`__

New Less than frequency algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have added some new raster algorithms that operate on a local cell-by-cell basis in a raster stack. The Less than frequency algorithm evaluates on a cell-by-cell basis the frequency (number of times) the values of an input stack of rasters are less than the value of a value raster.

|image52|

This feature was developed by `Clemens Raffler <https://github.com/root676>`__

New Lowest position in raster stack algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added some raster value position analysis tools with this new QGIS version: The *Lowest position in raster stack* algorithm evaluates on a cell-by-cell basis the position of the raster with the lowest value in a stack of rasters. Position counts start with 1 and range to the total number input rasters. The order of the input rasters is relevant for the algorithm.

|image53|

This feature was developed by `Clemens Raffler <https://github.com/root676>`__

New Highest position in raster stack algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added some raster value position analysis tools with this new QGIS version: The *Highest position in raster stack* algorithm evaluates on a cell-by-cell basis the position of the raster with the highest value in a stack of rasters. Position counts start with 1 and range to the total number input rasters. The order of the input rasters is relevant for the algorithm.

|image54|

This feature was developed by `Clemens Raffler <https://github.com/root676>`__

Load processing results to layer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can now optionally set a group name which ensures that the resulting output layers added to the project when using the *Open output file after running algorithm* option are grouped together. This allows all outputs from several processing algorithms to be grouped so that they may be easily located in the layer tree and be removed, exported, or have their visibility toggled easily. |image58|

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Add zonal statistics algorithm which creates new output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously, when calculating zonal statistics, the algorithm always updated the original data source, adding additional fields. A new zonal statistics algorithm has been added which creates a new output instead. This functionality is an implementation of the `29504 feature request <https://github.com/qgis/QGIS/issues/29504>`__.

This feature was developed by `Matthias Kuhn <https://api.github.com/users/m-kuhn>`__

Add geometry processing parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added a new ``QgisProcessingParameterGeometry`` for passing geometries as a parameter to processing alogrithms.

This provides a way to pass simple geometries to algorithms without requiring an input layer.

The immediates use case are:

-  Algorithms that might need to manipulate geometries in an atomic way.
-  Delegation from parent algorithms.
-  Use with headless qgis processing in stand-alone processing tools.

Features:

-  The parameter is compatible with string parameters as it may pass Well-Known-Text as the value.
-  The current widget interaction is minimalistic as it only uses the input text widget for entering the value as WKT.

This feature was developed by `David Marteau <https://api.github.com/users/dmarteau>`__

Add an interface to determine whether it is safe for the application to exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An interface for plugins and scripts to register custom logic to prevent the QGIS application from exiting was added. This allows plugins to determine whether it is safe for the application to exit. This has made it possible to allow plugins to determine whether there are unsaved changes which should be saved or discarded before allowing QGIS to exit, functionality which has already been implemented in the console script editor, preventing data loss by prompting users when there are unsaved changes rather than silently shutting down the application.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Application and Project Options
-------------------------------

List available GDAL vector drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A *Vector Drivers* tab is now available within the QGIS GDAL Settings window, which lists all the available GDAL vector drivers and allows users to toggle their active state. Where several drivers may be used to open data of a specific type, users may now modify these settings to ensure that the intended driver is used when importing specific vector data types. For example, the FileGDB and OpenFileGDB drivers are both capable of being used to import .gdb files, but if the data file has a version of 9.x, the FileGDB won't be able to open it. In this instance, a user may disable the FileGDB driver and ensure that the data is loaded using the OpenFileGDB driver instead.

This functionality directly addresses the limitations outlined in `Issue 18738 <https://github.com/qgis/QGIS/issues/18738>`__.

|image59|

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Detect GRASS installation folder on MacOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MacOS previously had a platform-specific custom parameter setting Grass7Utils.GRASS\_FOLDER. This caused crashes for many users with multiple QGIS installations or who had some invalid folder settings. The parameter has been removed and a GISBASE environment variable has been introduced instead, which is commonly used in GRASS scripts as the "root" installation directory, emulating the behavior used for GRASS detection in Windows environments. If GISBASE is not present (default), a search is performed for grass folders in ``QgsApplication.prefixPath()`` (when packaged in bundle format). If not found, the standalone GRASS instance is searched for. The new behaviour for GRASS is in-line with the methodology used for the GDAL and SAGA processing tools.

This resolves `Issue 38595 <https://github.com/qgis/QGIS/issues/38595>`__.

|image60|

This feature was developed by `Lutra Consulting (Peter Petrik) <https://api.github.com/users/PeterPetrik>`__

Browser
-------

Expose fields in the Browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First part of QEP https://github.com/qgis/QGIS-Enhancement-Proposals/issues/171

Exposes field columns in the browser for providers that implement connections API:

-  PG
-  GPKG
-  Spatialite
-  MSSQL

The following operations are supported on fields:

-  add new field
-  delete field

|image61|

|image62|

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

Data Providers
--------------

ArcGIS Vector Tile Service connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An option to create connections for ArcGIS Vector Tile Services was added to allow users to easily load vector tile layers from ArcGIS Server vector tile services. It also added support for authentication, configuration, and custom referer string to vector tile connections.

This change adds explicit UI options for adding and configuring connections to ESRI vector tile services. While these services use the standard vector tile framework for data retrieval, they can be directly added by creating a connection using the VectorTileService API endpoint on the ArcGIS server.

After a user adds a layer from a VectorTileService, the server's default styling and labeling for the layer is automatically loaded.

|image63|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Trust layer metadata propagation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The trust flag at the project level is only used to read the vector layer extent from xml, not from the provider.

This flag was not available at the vector layer and data provider level. A new QgsMapLayer reading flag to propagate the trust layer metadata for the project's read flag and a new provider flag to trust the datasource config.

Trusting the datasource config allows the provider to use estimated metadata, ensures the primary key is unique and that the detectable geometry type and SRID are the same as the requested.

This feature was developed by `rldhont <https://api.github.com/users/rldhont>`__

Add support for virtual columns in Oracle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for virtual (generated) Oracle columns has been added and is defined this way:

``sql CREATE TABLE QGIS.GENERATED_COLUMNS ( "pk" INTEGER PRIMARY KEY, "generated_field" GENERATED ALWAYS AS ('test:' || "pk") VIRTUAL);``

**Note:** It's not possible to define a generated column on an SDO\_GEOMETRY field in Oracle.

For now, when creating a new feature, the generated field is editable and should not be. A new API method needs to be added to retrieve readonly field from the provider as discussed in `Issue 35995 <https://github.com/qgis/QGIS/pull/35995#issuecomment-633055700>`__.

This feature was developed by `Julien Cabieces <https://api.github.com/users/troopa81>`__

Add advanced options for data imports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New functionality has been introduced which allows advanced parameters to be specified when importing layers using the OGR data provider, opening a vast range of new possibilities, especially when working around expected dataset issues.

|image64|

|image65|

This feature was developed by `Even Rouault <https://api.github.com/users/rouault>`__

QGIS Server
-----------

QGIS Server WFS3 API Sorting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds sorting functionality to the QGIS Server WFS3 API

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

QGIS Server landing page plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Landing Page Plugin for QGIS Server was created, which is a C++ port of https://github.com/elpaso/qgis-server-landing-page-plugin

|image66|

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

Environment variable to disable GetPrint and to not load layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``QGIS_SERVER_DISABLE_GETPRINT`` environment variable was added to QGIS Server which prevents the loading of layouts when projects are read and disables the WMS GetPrint request, improving the read time of projects.

This feature was funded by `Ifremer <https://wwz.ifremer.fr>`__

This feature was developed by `3Liz <https://www.3liz.com>`__

Environment variable to trust layer metadata with server settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Trust layer metadata can be defined at the project level. A new project reading flag was added which allows the forcing of trust layer metadata.

For QGIS server, the trust layer metadata option can be overridden with ``QGIS_SERVER_TRUST_LAYER_METADATA`` environment variable.

This feature was funded by `Ifremer <https://wwz.ifremer.fr>`__

This feature was developed by `3Liz <https://www.3liz.com>`__

Notable Fixes
-------------

Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Bug Title                                                                                                                                      | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                                                        | 3.10 backport commit (GitHub)                                                       |
+================================================================================================================================================+==========================================================+============================================================================================================================================+=====================================================================================+
| Scrolling attribute table of a layer added with the "delimted text provider" is almost impossible                                              | `#38068 <https://github.com/qgis/QGIS/issues/38068>`__   | `PR #38735 <https://github.com/qgis/QGIS/pull/38735>`__                                                                                    | `PR #38745 <https://github.com/qgis/QGIS/pull/38745>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| support for API-keys via query for API implementing OGC API - Features                                                                         | `#38436 <https://github.com/qgis/QGIS/issues/38436>`__   | `PR #38738 <https://github.com/qgis/QGIS/pull/38738>`__                                                                                    | N/A                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Custom CRS does not always switch parameters correctly from wkt to proj string                                                                 | `#38689 <https://github.com/qgis/QGIS/issues/38689>`__   | cannot reproduce                                                                                                                           |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| OGC API Features client always use limit=1000                                                                                                  | `#38666 <https://github.com/qgis/QGIS/issues/38666>`__   | cannot reproduce                                                                                                                           |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Exporting to geopackage changes field type from DATE to DATETIME                                                                               | `#37857 <https://github.com/qgis/QGIS/issues/37857>`__   | not a bug                                                                                                                                  |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| CSV date field being interpreted as time type                                                                                                  | `#38091 <https://github.com/qgis/QGIS/issues/38091>`__   | `PR #38741 <https://github.com/qgis/QGIS/pull/38741>`__                                                                                    | N/A                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Coordinate Transformation Difference between QGIS and Proj                                                                                     | `#38190 <https://github.com/qgis/QGIS/issues/38190>`__   | usage issue                                                                                                                                |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| gdal\_rasterize not working when file has '&' symbol in name                                                                                   | `#38674 <https://github.com/qgis/QGIS/issues/38674>`__   | `PR #38743 <https://github.com/qgis/QGIS/pull/38743>`__                                                                                    | `PR #38747 <https://github.com/qgis/QGIS/pull/38747>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Core dump when using identify feature on a vector polygon                                                                                      | `#36213 <https://github.com/qgis/QGIS/issues/36213>`__   | already fixed                                                                                                                              |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Error of the raster histogram of QGIS 3.10.8(LTR)                                                                                              | `#38298 <https://github.com/qgis/QGIS/issues/38298>`__   | `PR #38769 <https://github.com/qgis/QGIS/pull/38769>`__                                                                                    | TODO                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| [Postgres] Cannot edit attribute when there is no primary key                                                                                  | `#37917 <https://github.com/qgis/QGIS/issues/37917>`__   | not a bug IMHO                                                                                                                             |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Switching between WMS info-output formats throws: CRITICAL QTableWidget: cannot insert an item that is already owned by another QTableWidget   | `#37215 <https://github.com/qgis/QGIS/issues/37215>`__   | `PR #38770 <https://github.com/qgis/QGIS/pull/38770>`__                                                                                    | `PR #38783 <https://github.com/qgis/QGIS/pull/38783>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| SaveAs Geopackage: TEXT fields are converted to TEXT(255)                                                                                      | `#25405 <https://github.com/qgis/QGIS/issues/25405>`__   | already fixed                                                                                                                              |                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| "Join attributes by nearest" tool defaults to "None" when using Max distance of 0                                                              | `#38761 <https://github.com/qgis/QGIS/issues/38761>`__   | `PR #38773 <https://github.com/qgis/QGIS/pull/38773>`__                                                                                    | No, not appropriate (see `PR #38778 <https://github.com/qgis/QGIS/pull/38778>`__)   |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Lost edits in layer of same transaction group                                                                                                  | `#38697 <https://github.com/qgis/QGIS/issues/38697>`__   | `PR #38779 <https://github.com/qgis/QGIS/pull/38779>`__ + `PR #38780 <https://github.com/qgis/QGIS/pull/38780>`__                          | `PR #38824 <https://github.com/qgis/QGIS/pull/38824>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Preview of Expression String Builder 'freezes' if Feature id higher then available                                                             | `#38646 <https://github.com/qgis/QGIS/issues/38646>`__   | `PR #38797 <https://github.com/qgis/QGIS/pull/38797>`__                                                                                    | N/A                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| VectorFileWriter/OGR provider: workaround GDAL 3.1.x bug regarding XLSX and ODS creation                                                       | not reported                                             | `PR #38837 <https://github.com/qgis/QGIS/pull/38837>`__                                                                                    | `PR #38853 <https://github.com/qgis/QGIS/pull/38853>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Coordinate operation widget: avoid repeating scope and remarks                                                                                 | not reported                                             | `PR #38847 <https://github.com/qgis/QGIS/pull/38847>`__                                                                                    | N/A                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Freeze when showing attribute table of WFS layer                                                                                               | `#37224 <https://github.com/qgis/QGIS/issues/37224>`__   | `PR #38952 <https://github.com/qgis/QGIS/pull/38952>`__                                                                                    | `PR #38956 <https://github.com/qgis/QGIS/pull/38956>`__                             |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| OGR Error when editing a kml file                                                                                                              | `#39087 <https://github.com/qgis/QGIS/issues/39087>`__   | `GDAL Commit 72e1a4d7c96e0381d2d335857697b5f8e1668450 <https://github.com/OSGeo/gdal/commit/72e1a4d7c96e0381d2d335857697b5f8e1668450>`__   | Backported to GDAL 3.1 branch too                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Even Rouault <http://www.spatialys.com/>`__

Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                                         | URL issues.qgis.org (if reported)                                                                                | URL Commit (Github)                                        | 3.10 backport commit (GitHub)                             |
+===================================================================================================================================+==================================================================================================================+============================================================+===========================================================+
| Loading PostGIS layers with no specified geometry loads all features in the attribute table.                                      | `PR #35367 <https://github.com/qgis/QGIS/pull/35367>`__ `#38565 <https://github.com/qgis/QGIS/issues/38565>`__   | Backport only                                              | `PR #38736 <https://github.com/qgis/QGIS/pull/38736>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Server API: current project is not settable anymore                                                                               | `#38755 <https://github.com/qgis/QGIS/issues/38755>`__                                                           | `PR #38758 <https://github.com/qgis/QGIS/pull/38758>`__    | `PR #38758 <https://github.com/qgis/QGIS/pull/38758>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| PostGIS layer saved in 3.10 project, fail to load correctly on 3.14                                                               | `#38567 <https://github.com/qgis/QGIS/issues/38567>`__                                                           | `PR #38763 <https://github.com/qgis/QGIS/pull/38763>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Server WFS-T 1.1.0 wrong case for totalUpdated, totalInserted, totalDeleted                                                       | `#38558 <https://github.com/qgis/QGIS/issues/38558>`__                                                           | `PR #38764 <https://github.com/qgis/QGIS/pull/38764>`__    | TODO                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Server crashes on GetLegendGraphics when RULE does not exists.                                                                    | `#38766 <https://github.com/qgis/QGIS/issues/38766>`__                                                           | `PR #38775 <https://github.com/qgis/QGIS/pull/38775>`__    | `PR #38794 <https://github.com/qgis/QGIS/pull/38794>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Form view gets stuck in the last shown not-NULL-value for some attributes when browsing through data                              | `#38552 <https://github.com/qgis/QGIS/issues/38552>`__                                                           | `PR #38801 <https://github.com/qgis/QGIS/pull/38801>`__    | TODO                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Marker line Simple marker rotation override not respecting follow line direction setting                                          | `#38716 <https://github.com/qgis/QGIS/issues/38716>`__                                                           | `PR #38815 <https://github.com/qgis/QGIS/pull/38815>`__    |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Unable to dock the "snapping options" widget                                                                                      | `#38604 <https://github.com/qgis/QGIS/issues/38604>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Can't read PG data sources when saved in version 3.10 and using service / auth combo                                              | `#38809 <https://github.com/qgis/QGIS/issues/38809>`__                                                           | `PR #38833 <https://github.com/qgis/QGIS/pull/38833>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| DB Manager "cancel" button to stop a query is not working                                                                         | `#38092 <https://github.com/qgis/QGIS/issues/38092>`__                                                           | `PR #38870 <https://github.com/qgis/QGIS/pull/38870>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| GDAL enhancement related to `#38092 <https://github.com/qgis/QGIS/issues/38092>`__                                                | `#38092 <https://github.com/qgis/QGIS/issues/38092>`__\ 2                                                        | https://github.com/OSGeo/gdal/pull/2953#event-3788638320   | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Shift values issue while creating new field under DB Manager                                                                      | `#38800 <https://github.com/qgis/QGIS/issues/38800>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Problem with VUV wms                                                                                                              | `#38924 <https://github.com/qgis/QGIS/issues/38924>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Data Source Manager: WMS/WMTS Window not resizable                                                                                | `#38903 <https://github.com/qgis/QGIS/issues/38903>`__                                                           | works for me, pending feedback                             |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Form tab option "Show as group box" won't save or apply                                                                           | `#38539 <https://github.com/qgis/QGIS/issues/38539>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Scale lock is ignored when panning the map                                                                                        | `#38953 <https://github.com/qgis/QGIS/issues/38953>`__                                                           | `PR #38954 <https://github.com/qgis/QGIS/pull/38954>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Zoom to layer overwrites locked scale bug                                                                                         | `#38417 <https://github.com/qgis/QGIS/issues/38417>`__                                                           | `PR #38954 <https://github.com/qgis/QGIS/pull/38954>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Repeated column names cause visualization issues in DB Manager                                                                    | `#38976 <https://github.com/qgis/QGIS/issues/38976>`__                                                           | `PR #38981 <https://github.com/qgis/QGIS/pull/38981>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| "show search\_path" returns 0 rows                                                                                                | `#38975 <https://github.com/qgis/QGIS/issues/38975>`__                                                           | `PR #38981 <https://github.com/qgis/QGIS/pull/38981>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| PG NOTIFY not accessible                                                                                                          | `#38986 <https://github.com/qgis/QGIS/issues/38986>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Fix PG db-manager rename schema                                                                                                   | `#38998 <https://github.com/qgis/QGIS/issues/38998>`__                                                           | `PR #39000 <https://github.com/qgis/QGIS/pull/39000>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Several PG browser items UX issues                                                                                                | `#39001 <https://github.com/qgis/QGIS/issues/39001>`__                                                           | `PR #39006 <https://github.com/qgis/QGIS/pull/39006>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Virtual vector does not load correctly on Windows                                                                                 | `#35016 <https://github.com/qgis/QGIS/issues/35016>`__                                                           | works for me on windows/current master                     |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| DB Manager: PostgreSQL field comments are not displayed correctly                                                                 | `#38394 <https://github.com/qgis/QGIS/issues/38394>`__                                                           | `PR #39026 <https://github.com/qgis/QGIS/pull/39026>`__    |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Only first row for Postgis raster table in DB Manager preview and when adding layer to Map canvas                                 | `#39017 <https://github.com/qgis/QGIS/issues/39017>`__                                                           | `PR #39039 <https://github.com/qgis/QGIS/pull/39039>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| erroneous postgis query when trying to discover relations                                                                         | `#39036 <https://github.com/qgis/QGIS/issues/39036>`__                                                           |                                                            |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| many additional tables that are already loaded in the project are loaded on project load because of layer dependencies            | `#39025 <https://github.com/qgis/QGIS/issues/39025>`__                                                           | `PR #39043 <https://github.com/qgis/QGIS/pull/39043>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Partial fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor                | `#39058 <https://github.com/qgis/QGIS/issues/39058>`__                                                           | `PR #39071 <https://github.com/qgis/QGIS/pull/39071>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Allow to set precision for raster single band presudocolor classification                                                         | not reported                                                                                                     | `PR #39079 <https://github.com/qgis/QGIS/pull/39079>`__    |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Complete fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor               | `#39058 <https://github.com/qgis/QGIS/issues/39058>`__                                                           | `PR #39088 <https://github.com/qgis/QGIS/pull/39088>`__    | Risky                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Failure with identifier sequence when adding feature                                                                              | `#39093 <https://github.com/qgis/QGIS/issues/39093>`__                                                           | works for me                                               |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Export report to PDF crashes QGIS if no layout is in edit mode                                                                    | `#39086 <https://github.com/qgis/QGIS/issues/39086>`__                                                           | `PR #39135 <https://github.com/qgis/QGIS/pull/39135>`__    | TODO                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| PG raster: float rasters do not show nodata values correctly in master/3.14                                                       | `#39142 <https://github.com/qgis/QGIS/issues/39142>`__                                                           | `#39142 <https://github.com/qgis/QGIS/issues/39142>`__     |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Python API call QgsAbstractDatabaseProviderConnection::TableProperty exceptions not converted to QgsProviderConnectionException   | `#39151 <https://github.com/qgis/QGIS/issues/39151>`__                                                           | `PR #39152 <https://github.com/qgis/QGIS/pull/39152>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| DB Manager unable to show PostGIS geography column                                                                                | `#37666 <https://github.com/qgis/QGIS/issues/37666>`__                                                           | `PR #39154 <https://github.com/qgis/QGIS/pull/39154>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| setting a field to NULL via field calculator freezes qgis                                                                         | `#39178 <https://github.com/qgis/QGIS/issues/39178>`__                                                           | `PR #39257 <https://github.com/qgis/QGIS/pull/39257>`__    | TODO                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Layer X: Feature has too many attributes (expecting 5, received 7) when "Automatic Creation of Transaction Group" is enabled      | `#39230 <https://github.com/qgis/QGIS/issues/39230>`__                                                           | `PR #39267 <https://github.com/qgis/QGIS/pull/39267>`__    | `PR #39278 <https://github.com/qgis/QGIS/pull/39278>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| unreported crash when calling data provider's lastError on no errors                                                              | not reported                                                                                                     | `PR #39267 <https://github.com/qgis/QGIS/pull/39267>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Crash digitizing a feature when transaction group is on (after save)                                                              | `#39265 <https://github.com/qgis/QGIS/issues/39265>`__                                                           | `PR #39283 <https://github.com/qgis/QGIS/pull/39283>`__    |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Transaction groups: not-current layers a set to not editable after save                                                           | `#39282 <https://github.com/qgis/QGIS/issues/39282>`__                                                           | `PR #39286 <https://github.com/qgis/QGIS/pull/39286>`__    | not critical                                              |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| OGR decodeUri: be tolerant on layerName case                                                                                      | not reported but impact the QGIS-Documentation                                                                   | `PR #39328 <https://github.com/qgis/QGIS/pull/39328>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Wrong extension handling in links when layer name has dots                                                                        | not reported                                                                                                     | `PR #39346 <https://github.com/qgis/QGIS/pull/39346>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| Passwords are URL-encoded before base64 encoding for HTTP Basic auth                                                              | `#39243 <https://github.com/qgis/QGIS/issues/39243>`__                                                           | `PR #39347 <https://github.com/qgis/QGIS/pull/39347>`__    | `PR #39382 <https://github.com/qgis/QGIS/pull/39382>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+
| QGIS crash in Settings menu if NOT in english                                                                                     | `#39430 <https://github.com/qgis/QGIS/issues/39430>`__                                                           | `PR #39434 <https://github.com/qgis/QGIS/pull/39434>`__    | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it/>`__

Bug fixes by Peter Petrik
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                                                  | URL issues.qgis.org (if reported)                                                  | URL Commit (Github)                                                                                                                                             | 3.10 backport commit (GitHub)                             |
+============================================================================================================================================+====================================================================================+=================================================================================================================================================================+===========================================================+
| Problem with displaying mesh and canvas rotation                                                                                           | `#35147 <https://github.com/qgis/QGIS/issues/35147>`__                             | `PR #38795 <https://github.com/qgis/QGIS/pull/38795>`__/files                                                                                                   | no, not critial                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash while attempting to use mesh                                                                                                         | `#31773 <https://github.com/qgis/QGIS/issues/31773>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Spatial Bookmark Manager Bad Behavior and Crashing App                                                                                     | `#35348 <https://github.com/qgis/QGIS/issues/35348>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Seqmentation fault 11 on QGIS shutdown on MacOS                                                                                            | not reported                                                                       | `PR #38806 <https://github.com/qgis/QGIS/pull/38806>`__                                                                                                         | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__   |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash when creating New MSSQL connexion on macOS                                                                                           | `#35026 <https://github.com/qgis/QGIS/issues/35026>`__                             | `PR #39084 <https://github.com/qgis/QGIS/pull/39084>`__                                                                                                         | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| qgis\_process is installed in the wrong place on MacOS                                                                                     | `#38447 <https://github.com/qgis/QGIS/issues/38447>`__                             | `Mac Packager Commit 97b0ec974e2309e447ebb69c4117580db27af6f0 <https://github.com/qgis/QGIS-Mac-Packager/commit/97b0ec974e2309e447ebb69c4117580db27af6f0>`__    | N/A                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Unable to run GRASS plugin on MacOS                                                                                                        | `#32511 <https://github.com/qgis/QGIS/issues/32511>`__                             | `Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae <https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Processing: GRASS r.drain fails on macOS: "No module named site", "Raster not found"                                                       | `#36126 <https://github.com/qgis/QGIS/issues/36126>`__                             | `Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae <https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| The Grass7 processing toolbox option dialogue should include a way to specify a path to the GRASS binary, overriding Grass7Utils.command   | `#29454 <https://github.com/qgis/QGIS/issues/29454>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Path error GRASS plugin QGIS 3.14                                                                                                          | `#38595 <https://github.com/qgis/QGIS/issues/38595>`__                             | `PR #38840 <https://github.com/qgis/QGIS/pull/38840>`__                                                                                                         | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| No Print dialog or Page Setup dialog in macOS                                                                                              | `#30791 <https://github.com/qgis/QGIS/issues/30791>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Splash Screen Persists While 'Handle Bad Layers' Dialog is Open                                                                            | `#34784 <https://github.com/qgis/QGIS/issues/34784>`__                             | `PR #38842 <https://github.com/qgis/QGIS/pull/38842>`__                                                                                                         | not appropriate                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| qgis terms of license pop up bug                                                                                                           | `#38588 <https://github.com/qgis/QGIS/issues/38588>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Cannot load pictures anymore in custom forms                                                                                               | `#30833 <https://github.com/qgis/QGIS/issues/30833>`__                             | already fixed by `Mac Packager Issue #3 <https://github.com/qgis/QGIS-Mac-Packager/issues/3>`__                                                                 | not appropriate                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
|                                                                                                                                            | `Mac Packager Issue #83 <https://github.com/qgis/QGIS-Mac-Packager/issues/83>`__   | `Mac Packager Commit 36f86759649abc4cb8f6875f6ad934070c13d56e <https://github.com/qgis/QGIS-Mac-Packager/commit/36f86759649abc4cb8f6875f6ad934070c13d56e>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Projections not reading in MacOS Nightly Build                                                                                             | `#38919 <https://github.com/qgis/QGIS/issues/38919>`__                             | `PR #38922 <https://github.com/qgis/QGIS/pull/38922>`__                                                                                                         | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| layers in .osm format are not loading                                                                                                      | `Mac Packager Issue #84 <https://github.com/qgis/QGIS-Mac-Packager/issues/84>`__   | cannot reproduce                                                                                                                                                | works in 3.10                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| missing metadata python package                                                                                                            | `Mac Packager Issue #87 <https://github.com/qgis/QGIS-Mac-Packager/issues/87>`__   | `Mac Packager Commit 7c94749579acaf059e9b6c5094c7a2cb74d17f7a <https://github.com/qgis/QGIS-Mac-Packager/commit/7c94749579acaf059e9b6c5094c7a2cb74d17f7a>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GeoPDF Export fails                                                                                                                        | `Mac Packager Issue #75 <https://github.com/qgis/QGIS-Mac-Packager/issues/75>`__   | works now with qgis-deps-0.5.5                                                                                                                                  | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GRASS Console not work on Mac                                                                                                              | `#38961 <https://github.com/qgis/QGIS/issues/38961>`__                             | `Mac Packager Commit bfc4ca0717de0e496d98f91e7a28e85216763ab1 <https://github.com/qgis/QGIS-Mac-Packager/commit/bfc4ca0717de0e496d98f91e7a28e85216763ab1>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Processing Plugin Crashes QGIS on MacOS Nightly Build                                                                                      | `#38960 <https://github.com/qgis/QGIS/issues/38960>`__                             | `PR #38973 <https://github.com/qgis/QGIS/pull/38973>`__                                                                                                         | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Program crash when pasting file name                                                                                                       | `#38939 <https://github.com/qgis/QGIS/issues/38939>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Wrong Python default path in QGIS server on macOS                                                                                          | `#29843 <https://github.com/qgis/QGIS/issues/29843>`__                             | `Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491 <https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| qgis\_map.fcgi on macOS doesn't find libraries                                                                                             | `#29399 <https://github.com/qgis/QGIS/issues/29399>`__                             | `Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491 <https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GRASS provider cannot get projection                                                                                                       | `#31397 <https://github.com/qgis/QGIS/issues/31397>`__                             | `Mac Packager Commit bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95 <https://github.com/qgis/QGIS-Mac-Packager/commit/bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS crashing on start on Mac                                                                                                              | `#38858 <https://github.com/qgis/QGIS/issues/38858>`__                             | corrupted user profile                                                                                                                                          | N/A                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Browser cannot open Volumes under macOS                                                                                                    | `#29702 <https://github.com/qgis/QGIS/issues/29702>`__                             | `PR #39096 <https://github.com/qgis/QGIS/pull/39096>`__                                                                                                         | no, not critial                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MetaSearch unexpected keyword argument 'auth'                                                                                              | `#38074 <https://github.com/qgis/QGIS/issues/38074>`__                             | cannot reproduce on master                                                                                                                                      | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| No QGIS plugins found in /Applications/QGIS3.10.app/Contents/MacOS/../PlugIns/qgis                                                         | `#39044 <https://github.com/qgis/QGIS/issues/39044>`__                             | cannot reproduce on master                                                                                                                                      | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Browser Panel: unable to find all the connected drives                                                                                     | `#24641 <https://github.com/qgis/QGIS/issues/24641>`__                             | duplicate of `#29702 <https://github.com/qgis/QGIS/issues/29702>`__ for MacOS                                                                                   |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Provider Settings for GRASS avoid to active OTB                                                                                            | `#39112 <https://github.com/qgis/QGIS/issues/39112>`__                             | cannot reproduce on master                                                                                                                                      |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Can't open GeoJSON vector via HTTP protocol on Windows and macOS                                                                           | `#37107 <https://github.com/qgis/QGIS/issues/37107>`__                             | "`Mac Packager Commit d06bc3ac933c75071f36937aaf8189920dccc503 <https://github.com/qgis/QGIS-Mac-Packager/commit/d06bc3ac933c75071f36937aaf8189920dccc503>`__   | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS 3.0.1 Crash - Zooming in while moving node crashes QGIS                                                                               | `#26509 <https://github.com/qgis/QGIS/issues/26509>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash when switching user profiles (too early?)                                                                                            | `#26993 <https://github.com/qgis/QGIS/issues/26993>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Aborted when debugging python plugin with pdb                                                                                              | `#27201 <https://github.com/qgis/QGIS/issues/27201>`__                             | cannot reproduce/not valid                                                                                                                                      |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Customization: the widget catcher can't select icon from a toolbar when it's under a group of icons                                        | `#22967 <https://github.com/qgis/QGIS/issues/22967>`__                             | `PR #39209 <https://github.com/qgis/QGIS/pull/39209>`__                                                                                                         | not critical                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS on macOS can save file in qgz-format, but won't open files in qgz format                                                              | `#39204 <https://github.com/qgis/QGIS/issues/39204>`__                             | cannot reproduce                                                                                                                                                |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Mouse pointer keeps switching type                                                                                                         | `#32947 <https://github.com/qgis/QGIS/issues/32947>`__                             | probably desired feature, not a bug                                                                                                                             |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Aggregate function bug on macOS version                                                                                                    | "`#32932 <https://github.com/qgis/QGIS/issues/32932>`__                            | cannot reproduce on master                                                                                                                                      | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Clear filter in Snapping Toolbar > Edit advanced configuration causes crash                                                                | `#29750 <https://github.com/qgis/QGIS/issues/29750>`__                             | cannot reproduce on master                                                                                                                                      |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Snapping Settings window with Night Mapping, low readability                                                                               | `#29751 <https://github.com/qgis/QGIS/issues/29751>`__                             | already fixed                                                                                                                                                   |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Merge raster fails in macOS                                                                                                                | `#39213 <https://github.com/qgis/QGIS/issues/39213>`__                             | cannot reproduce on master                                                                                                                                      | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Can't get info on WFS feature in MacOS nightly build                                                                                       | `#39223 <https://github.com/qgis/QGIS/issues/39223>`__                             | `Mac Packager Commit 54872e06a43ef61bf6dae8242e121bd5cec8be11 <https://github.com/qgis/QGIS-Mac-Packager/commit/54872e06a43ef61bf6dae8242e121bd5cec8be11>`__    | different packaging system...                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS 3.4.10 crashes - Python                                                                                                               | `#31304 <https://github.com/qgis/QGIS/issues/31304>`__                             | already fixed                                                                                                                                                   | already fixed                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Exporting GRASS vector (save as...) crashes QGIS                                                                                           | `#37508 <https://github.com/qgis/QGIS/issues/37508>`__                             | `PR #39284 <https://github.com/qgis/QGIS/pull/39284>`__                                                                                                         | TODO                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash when loading 3D project with DEM terrain and symbols that uses height value over the terrain                                         | `#35483 <https://github.com/qgis/QGIS/issues/35483>`__                             | `PR #39287 <https://github.com/qgis/QGIS/pull/39287>`__                                                                                                         | TODO                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Creating 3D View from raster                                                                                                               | `#37163 <https://github.com/qgis/QGIS/issues/37163>`__                             | duplicate of `#35483 <https://github.com/qgis/QGIS/issues/35483>`__                                                                                             | N/A                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash when moving camera in 3D                                                                                                             | "`#37881 <https://github.com/qgis/QGIS/issues/37881>`__                            | cannot reproduce on master                                                                                                                                      |                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Peter Petrik <https://www.lutraconsulting.co.uk/>`__

Bug fixes by Paul Blottiere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                               | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                        | 3.10 backport commit (GitHub)                             |
+=========================================================================+==========================================================+============================================================================================================+===========================================================+
| Linebreak issue with editing expression of "Title Label Decoration"     | `#37803 <https://github.com/qgis/QGIS/issues/37803>`__   | `PR #38817 <https://github.com/qgis/QGIS/pull/38817>`__                                                    | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__   |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS Server GetPrint: EXTERNAL\_WMS layer on top of QGIS layer          | `#35873 <https://github.com/qgis/QGIS/issues/35873>`__   | `PR #38548 <https://github.com/qgis/QGIS/pull/38548>`__                                                    | N/A                                                       |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fixes OGC API Features certification                                    | not reported                                             | `PR #37622 <https://github.com/qgis/QGIS/pull/37622>`__                                                    | N/A                                                       |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Outdated help for labels "data-defined" placement group options         | `#36680 <https://github.com/qgis/QGIS/issues/36680>`__   | `PR #37344 <https://github.com/qgis/QGIS/pull/37344>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Server GetFeatureInfo returns 0 where is should return NULL             | `#37781 <https://github.com/qgis/QGIS/issues/37781>`__   | `PR #38807 <https://github.com/qgis/QGIS/pull/38807>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| z function returns Nan when used with a 2d point geometry               | `#37772 <https://github.com/qgis/QGIS/issues/37772>`__   | `PR #38831 <https://github.com/qgis/QGIS/pull/38831>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| m function returns Nan when used with a 2d point geometry               | not reported                                             | `PR #38831 <https://github.com/qgis/QGIS/pull/38831>`__/commits/829ee25d431b2b3d1ea08fa8a930bb519ab2dd2f   |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| processing.algorithmHelp from terminal (outside QGIS desktop)           | `#37524 <https://github.com/qgis/QGIS/issues/37524>`__   | cannot reproduce                                                                                           |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Cache join layer in memory" not toggling when editing join properties   | `#37326 <https://github.com/qgis/QGIS/issues/37326>`__   | `PR #38838 <https://github.com/qgis/QGIS/pull/38838>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Map tips should not appear for invisible features                       | `#37066 <https://github.com/qgis/QGIS/issues/37066>`__   | `PR #38861 <https://github.com/qgis/QGIS/pull/38861>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Merge features: manual value is not respected                           | `#37659 <https://github.com/qgis/QGIS/issues/37659>`__   | `PR #39083 <https://github.com/qgis/QGIS/pull/39083>`__                                                    |                                                           |
+-------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Paul Blottiere <https://hytech-imaging.fr/>`__

Bug fixes by Matthias Kuhn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                               | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.10 backport commit (GitHub)   |
+=========================================================+==========================================================+===========================================================+=================================+
| Legend nodes overlapping each other after inserting     | `#38881 <https://github.com/qgis/QGIS/issues/38881>`__   | `PR #38882 <https://github.com/qgis/QGIS/pull/38882>`__   | not critical                    |
+---------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Poor legend performance with complex legends            | `#38890 <https://github.com/qgis/QGIS/issues/38890>`__   | `PR #38891 <https://github.com/qgis/QGIS/pull/38891>`__   | not critical                    |
+---------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| AMS layers cannot be added when no project CRS is set   | `#38892 <https://github.com/qgis/QGIS/issues/38892>`__   | `PR #38893 <https://github.com/qgis/QGIS/pull/38893>`__   | no intention                    |
+---------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Legend performance problems                             | `#38978 <https://github.com/qgis/QGIS/issues/38978>`__   | `PR #39066 <https://github.com/qgis/QGIS/pull/39066>`__   |                                 |
+---------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Matthias Kuhn <https://www.opengis.ch/>`__

Bug fixes by Julien Cabieces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Bug Title                                                                                                     | URL issues.qgis.org (if reported)                         | URL Commit (Github)                                       | 3.10 backport commit (GitHub)                                     |
+===============================================================================================================+===========================================================+===========================================================+===================================================================+
| QgsProcessingAlgRunnerTask started inside function crashes QGIS                                               | `#38583 <https://github.com/qgis/QGIS/issues/38583>`__    | Won’t fix                                                 |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Geometry generator symbol not rendered if the feature itself is not on the map canvas                         | `#38579 <https://github.com/qgis/QGIS/issues/38579>`__    | Feedback                                                  |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Relation widget in input form tabs - NULL value filled with data in form                                      | `#38549 <https://github.com/qgis/QGIS/issues/38549>`__    | Won’t backport (too risky)                                | (Closed) `#38549 <https://github.com/qgis/QGIS/issues/38549>`__   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Warning message: Missing layer form dependency : layer 'layerX' requires layer 'layerY' to be loaded          | `PR #38802 <https://github.com/qgis/QGIS/pull/38802>`__   | `PR #38802 <https://github.com/qgis/QGIS/pull/38802>`__   | N/A                                                               |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| When embedding a layer, the display expression of a relation reference is not taken over                      | `#38422 <https://github.com/qgis/QGIS/issues/38422>`__    | Closed (FeatureRequest)                                   |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| the keybord shortcut CTRL+C copy only the first cell, not the whole line                                      | `#37503 <https://github.com/qgis/QGIS/issues/37503>`__    | `PR #38810 <https://github.com/qgis/QGIS/pull/38810>`__   |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| if shortcut is set for copy features then Ctrl+C not working anymore                                          | `#37401 <https://github.com/qgis/QGIS/issues/37401>`__    | Duplicate #37503                                          |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Organize columns not working if the table is empty                                                            | `#38653 <https://github.com/qgis/QGIS/issues/38653>`__    | Upstream (Qt)                                             |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Copy and paste style for forms ignores edit widget type                                                       | `#37702 <https://github.com/qgis/QGIS/issues/37702>`__    | `PR #38836 <https://github.com/qgis/QGIS/pull/38836>`__   |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Keep order when drag and drop multiple widget                                                                 | `#37038 <https://github.com/qgis/QGIS/issues/37038>`__    | `PR #38844 <https://github.com/qgis/QGIS/pull/38844>`__   | `PR #39239 <https://github.com/qgis/QGIS/pull/39239>`__           |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| QGIS crash removing QgsAnnotation in python                                                                   | `#36098 <https://github.com/qgis/QGIS/issues/36098>`__    | Feedback                                                  |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Error in SQL statement for Virtual layers may lock layers in map canvas                                       | `#34378 <https://github.com/qgis/QGIS/issues/34378>`__    | `PR #38949 <https://github.com/qgis/QGIS/pull/38949>`__   | `PR #39023 <https://github.com/qgis/QGIS/pull/39023>`__           |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Virtual field in virtual layer not found                                                                      | `#38523 <https://github.com/qgis/QGIS/issues/38523>`__    | Feedback                                                  |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Closed ID column for temporary layer is not detected when creating virtual layers using data source manager   | `#34830 <https://github.com/qgis/QGIS/issues/34830>`__    | Won’t fix                                                 |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Boolean virtual field unusable in virtual layers                                                              | `#31798 <https://github.com/qgis/QGIS/issues/31798>`__    | `PR #38957 <https://github.com/qgis/QGIS/pull/38957>`__   | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__           |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| fails to generate virtual geometry layer based on virtual wkt field                                           | `#28265 <https://github.com/qgis/QGIS/issues/28265>`__    | Feedback                                                  |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Closed virtual fields can't be filtered                                                                       | `#28072 <https://github.com/qgis/QGIS/issues/28072>`__    | Not reproduced                                            |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Qgis crached after calculated field removed                                                                   | `#26486 <https://github.com/qgis/QGIS/issues/26486>`__    | Not reproduced                                            |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| sql "order by" does not work with the "Add/Edit Virtual Layer" feature                                        | `#29043 <https://github.com/qgis/QGIS/issues/29043>`__    | Won’t fix                                                 |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Form fails to initialize $geometry                                                                            | `#34791 <https://github.com/qgis/QGIS/issues/34791>`__    | `PR #39041 <https://github.com/qgis/QGIS/pull/39041>`__   |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Oracle - can't create or a modify a connection                                                                | `#38979 <https://github.com/qgis/QGIS/issues/38979>`__    | `PR #39131 <https://github.com/qgis/QGIS/pull/39131>`__   |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Test connection Oracle DB ready - OK greyed out !                                                             | `#39116 <https://github.com/qgis/QGIS/issues/39116>`__    | Duplicate #38979                                          |                                                                   |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+
| Scale dependent snapping does not activate as long as it displays the scale as "1:xxxxxx"                     | `#39031 <https://github.com/qgis/QGIS/issues/39031>`__    | `PR #39133 <https://github.com/qgis/QGIS/pull/39133>`__   | N/A                                                               |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Julien Cabieces <https://www.oslandia.com/>`__

Bug fixes by Denis Rouzaud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                                                                                            | URL issues.qgis.org (if reported)                         | URL Commit (Github)                                       | 3.10 backport commit (GitHub)   |
+======================================================================================================================+===========================================================+===========================================================+=================================+
| correctly determine if variables are static in aggregate expression and filter, give @parent in generic aggregates   | `#33382 <https://github.com/qgis/QGIS/issues/33382>`__    | `PR #39391 <https://github.com/qgis/QGIS/pull/39391>`__   | no                              |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Freeze when using aggregate in a virtual field                                                                       | `#39366 <https://github.com/qgis/QGIS/issues/39366>`__    | Won’t fix                                                 |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Fix SVG marker anchor calculation and improve bounds                                                                 | `PR #39336 <https://github.com/qgis/QGIS/pull/39336>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Improve SVG UI + remove duplicated code                                                                              | `PR #39421 <https://github.com/qgis/QGIS/pull/39421>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Improve SVG UI + remove duplicated code                                                                              | `PR #39519 <https://github.com/qgis/QGIS/pull/39519>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Improve SVG UI + remove duplicated code                                                                              | `PR #39524 <https://github.com/qgis/QGIS/pull/39524>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Fix duplicating features                                                                                             | `PR #39548 <https://github.com/qgis/QGIS/pull/39548>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| fix duplication of feature being stopped at 1 level deep                                                             | `PR #39550 <https://github.com/qgis/QGIS/pull/39550>`__   |                                                           |                                 |
+----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Denis Rouzaud <https://www.opengis.ch/>`__

Bug fixes by Olivier Dalang
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------+-------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                    | URL issues.qgis.org (if reported)   | URL Commit (Github)                                       | 3.10 backport commit (GitHub)   |
+==============================+=====================================+===========================================================+=================================+
| Core topology fixer issues   | not reported                        | `PR #39392 <https://github.com/qgis/QGIS/pull/39392>`__   |                                 |
+------------------------------+-------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Olivier Dalang <https://www.opengis.ch/>`__

Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Bug Title                                                                                                                                                                                   | URL issues.qgis.org (if reported)                                                                                | URL Commit (Github)                                                                                                                  | 3.10 backport commit (GitHub)                                                                                                        |
+=============================================================================================================================================================================================+==================================================================================================================+======================================================================================================================================+======================================================================================================================================+
| Fix crash in dbmanager                                                                                                                                                                      | `#38393 <https://github.com/qgis/QGIS/issues/38393>`__                                                           | `Commit 8c623b268ed94ef65aa19e2271be10b75e1ef36a <https://github.com/qgis/QGIS/commit/8c623b268ed94ef65aa19e2271be10b75e1ef36a>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix GeoPDF page size issues when opened in Acrobat reader                                                                                                                                   | `#33465 <https://github.com/qgis/QGIS/issues/33465>`__                                                           | `Commit 460bf8e534eb32ccba665918a615b55a8cbccadd <https://github.com/qgis/QGIS/commit/460bf8e534eb32ccba665918a615b55a8cbccadd>`__   | Delayed till more widespread user testing                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Improve default lighting of 3d scenes                                                                                                                                                       | not reported                                                                                                     | `Commit 350bc602e0ecd0f93dc2cc90ab34ce09993a687b <https://github.com/qgis/QGIS/commit/350bc602e0ecd0f93dc2cc90ab34ce09993a687b>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Allow conversion of QgsFeatureStoreList results to Python objects                                                                                                                           | `#39479 <https://github.com/qgis/QGIS/issues/39479>`__                                                           | `Commit 49c508921d7ccb59b1f1abaff4f890456cca1455 <https://github.com/qgis/QGIS/commit/49c508921d7ccb59b1f1abaff4f890456cca1455>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix preview symbol when offsetting point symbols isn't shown correctly                                                                                                                      | not reported                                                                                                     | `Commit 62409b92ce20a84dd92188cf42a98d7cdc0b08c3 <https://github.com/qgis/QGIS/commit/62409b92ce20a84dd92188cf42a98d7cdc0b08c3>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Use click-click behavior for rotate and offset marker tools                                                                                                                                 | not reported                                                                                                     | `Commit 00a3a6b8057f96dfa6c37943427a276cd3a5065d <https://github.com/qgis/QGIS/commit/00a3a6b8057f96dfa6c37943427a276cd3a5065d>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Avoid massive UI hangs when a layer has complicated actions defined                                                                                                                         | not reported                                                                                                     | `Commit 9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668 <https://github.com/qgis/QGIS/commit/9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Ensure display expression is used for map action tool, not raw feature ids                                                                                                                  | not reported                                                                                                     | `Commit e304d4d7e3eae0f48f336c7eb34542be6055df5d <https://github.com/qgis/QGIS/commit/e304d4d7e3eae0f48f336c7eb34542be6055df5d>`__   | Low priority                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Improve UX when configuring lights in a 3d scene, fixes confusing interface                                                                                                                 | not reported                                                                                                     | `Commit 3019b82100d4fc405f64cebcddf9aaae253c4293 <https://github.com/qgis/QGIS/commit/3019b82100d4fc405f64cebcddf9aaae253c4293>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix features with invalid geometries cannot be selected                                                                                                                                     | `#38460 <https://github.com/qgis/QGIS/issues/38460>`__                                                           | `Commit 22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d <https://github.com/qgis/QGIS/commit/22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Expose metadata tab for mesh layers                                                                                                                                                         | not reported                                                                                                     | `Commit 9482b1be70f36f778f6a409847244c5ff8a6a739 <https://github.com/qgis/QGIS/commit/9482b1be70f36f778f6a409847244c5ff8a6a739>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix missing text codecs on Windows installs                                                                                                                                                 | `#36871 <https://github.com/qgis/QGIS/issues/36871>`__                                                           | `Commit c3ca85e60bec73056bd87c426fd71c8f578363cb <https://github.com/qgis/QGIS/commit/c3ca85e60bec73056bd87c426fd71c8f578363cb>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't force a whole layout map to be rasterised just because one vector layer has non 100% opacity                                                                                          | not reported                                                                                                     | `Commit 2d15a4cfad6c732cf640fbb0eabd625856b643ca <https://github.com/qgis/QGIS/commit/2d15a4cfad6c732cf640fbb0eabd625856b643ca>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Ensure mesh layer properties follows same appearance as other layer types                                                                                                                   | not reported                                                                                                     | `Commit 3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac <https://github.com/qgis/QGIS/commit/3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Speed up mesh triangulation algorithm by avoiding a bunch of unnecessary QVector detachments                                                                                                | not reported                                                                                                     | `Commit 46ef391a7acf10515a11c19b69fafa4548046448 <https://github.com/qgis/QGIS/commit/46ef391a7acf10515a11c19b69fafa4548046448>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't allow users to set 3d terrain to mesh or DEM without selecting an elevation layer, instead show friendly warning                                                                      | not reported                                                                                                     | `Commit 0d9f1da846c70764fa6840309b5460f713b30e1f <https://github.com/qgis/QGIS/commit/0d9f1da846c70764fa6840309b5460f713b30e1f>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Avoid 3d map config dialog opening with initially out-of-sync selected pane                                                                                                                 | not reported                                                                                                     | `Commit 8b6477208f3c34e228734f7c04d32625965c48ed <https://github.com/qgis/QGIS/commit/8b6477208f3c34e228734f7c04d32625965c48ed>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix menu not shown when clicking 'add' item in style manager dialog and color ramp tab is active                                                                                            | not reported                                                                                                     | `Commit a085ce84b81a46896c9f00ee64eccaea63dad29a <https://github.com/qgis/QGIS/commit/a085ce84b81a46896c9f00ee64eccaea63dad29a>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix trying to create new color ramp from first page in style manager dialog does nothing                                                                                                    | not reported                                                                                                     | `Commit 34fb646f7ab69f20072b4d74ebec0595054089d7 <https://github.com/qgis/QGIS/commit/34fb646f7ab69f20072b4d74ebec0595054089d7>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix generated layers stored in geopackage always report a feature count of 0                                                                                                   | not reported                                                                                                     | `Commit 0675d99b34ee209a09857dfcba47cb5a92f55154 <https://github.com/qgis/QGIS/commit/0675d99b34ee209a09857dfcba47cb5a92f55154>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix Import Geotagged photos algorithm incorrectly assigns form widgets when saving the results to GPKG                                                                                      | not reported                                                                                                     | `Commit ff336ade18f4d6b307e4ed0e98fee77ee11a157c <https://github.com/qgis/QGIS/commit/ff336ade18f4d6b307e4ed0e98fee77ee11a157c>`__   | `PR #39563 <https://github.com/qgis/QGIS/pull/39563>`__                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Ensure driverName is passed to QgsVectorLayerExporter so that GPKG specific optimisations can be applied when saving outputs to geopackage                                     | not reported                                                                                                     | `Commit 501c63feb3887e18da35188062546186d8a767ac <https://github.com/qgis/QGIS/commit/501c63feb3887e18da35188062546186d8a767ac>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Update strings and UI regarding layer CRS override setting                                                                                                                                  | `#32101 <https://github.com/qgis/QGIS/issues/32101>`__                                                           | `Commit 06cfdd9563b15d8fbb27aee94b83d1b15773df77 <https://github.com/qgis/QGIS/commit/06cfdd9563b15d8fbb27aee94b83d1b15773df77>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Use proper SQL code editor in filter preview widget in vector layer properties, don't show filter as disabled                                                                               | not reported                                                                                                     | `Commit 0f4270cfe600e77f09db7727bd3ba965be7acb0e <https://github.com/qgis/QGIS/commit/0f4270cfe600e77f09db7727bd3ba965be7acb0e>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix boolean literal presentation in dox/PyQGIS docs                                                                                                                                         | not reported                                                                                                     | `Commit 746ee315bd0a4140f6e84617d547cc89103f79aa <https://github.com/qgis/QGIS/commit/746ee315bd0a4140f6e84617d547cc89103f79aa>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Speed up QGIS geometry validation                                                                                                                                                           | not reported                                                                                                     | `Commit 2a15c3b0a4a631db1b55ac7e46256fdbd89949f9 <https://github.com/qgis/QGIS/commit/2a15c3b0a4a631db1b55ac7e46256fdbd89949f9>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Correctly discard fid field values when running algorithms with the RegeneratePrimaryKey flag in in-place mode                                                                 | `#37761 <https://github.com/qgis/QGIS/issues/37761>`__, `#33816 <https://github.com/qgis/QGIS/issues/33816>`__   | `Commit db7b97705967041d4eaca7e7f69cbf49f5692aef <https://github.com/qgis/QGIS/commit/db7b97705967041d4eaca7e7f69cbf49f5692aef>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] When reporting that a feature is invalid, also mention the layer name                                                                                                          | `#26664 <https://github.com/qgis/QGIS/issues/26664>`__                                                           | `Commit a53bb3d49b59a3f814d862f30202ff156f74d6bc <https://github.com/qgis/QGIS/commit/a53bb3d49b59a3f814d862f30202ff156f74d6bc>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Allow expanding xls, ods, gpx, pdf files in browser so that layer sources can be repaired for these file types                                                                              | not reported                                                                                                     | `Commit 252976b739527e213f5d1c8c98a345911dfeab32 <https://github.com/qgis/QGIS/commit/252976b739527e213f5d1c8c98a345911dfeab32>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix "Split with lines" algorithm can get stuck in an endless loop                                                                                                              | not reported                                                                                                     | `Commit 05645b320d8547f50a308843e961e343c383036d <https://github.com/qgis/QGIS/commit/05645b320d8547f50a308843e961e343c383036d>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't show cascaded feature deletion warnings and feedback if joined deleted features came from an auxilary layer                                                                           | not reported                                                                                                     | `Commit 8c79b94fcc14e41d4442a018554e889f81b8e080 <https://github.com/qgis/QGIS/commit/8c79b94fcc14e41d4442a018554e889f81b8e080>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix crash in undo dock when clearing project/closing QGIS                                                                                                                                   | `#38157 <https://github.com/qgis/QGIS/issues/38157>`__                                                           | `Commit d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8 <https://github.com/qgis/QGIS/commit/d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8>`__   | `Commit 5c97ff66dd90d450a1ec60583da9626c14c9c08c <https://github.com/qgis/QGIS/commit/5c97ff66dd90d450a1ec60583da9626c14c9c08c>`__   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix copy/paste/select all shortcuts don't work when layer tree is selected                                                                                                                  | `#38849 <https://github.com/qgis/QGIS/issues/38849>`__                                                           | `Commit 02d7afae3f8699e83efacc781d3266700397d8b8 <https://github.com/qgis/QGIS/commit/02d7afae3f8699e83efacc781d3266700397d8b8>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix edited and new features no longer correctly show their corresponding color shading in the feature list view                                                                             | not reported                                                                                                     | `Commit a195b056624c2fabe231be7c0e96c3d63e052e5b <https://github.com/qgis/QGIS/commit/a195b056624c2fabe231be7c0e96c3d63e052e5b>`__   | Too risky/low priority                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ALWAYS load processing plugin in qgis\_process tool                                                                                                                                         | `#37989 <https://github.com/qgis/QGIS/issues/37989>`__                                                           | `Commit bc0df6d25e929a575d0821208f7d187737d80709 <https://github.com/qgis/QGIS/commit/bc0df6d25e929a575d0821208f7d187737d80709>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Add --json option to qgis\_process tool                                                                                                                                                     | https://github.com/paleolimbot/qgisprocess/issues/21                                                             | `Commit fc8d916b8dd444b3edaee3c18ec308e74a9bb91e <https://github.com/qgis/QGIS/commit/fc8d916b8dd444b3edaee3c18ec308e74a9bb91e>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Ensure all code editors in QGIS follow the same appearance and behavior                                                                                                                     | not reported                                                                                                     | (many)                                                                                                                               | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| When creating a CRS from WKT and the WKT has an embedded CRS name, correctly use this to set the QgsCoordinateReferenceSystem description                                                   | not reported                                                                                                     | `Commit 9a35b27630982d63101c57c3e3440dcbf1a7786f <https://github.com/qgis/QGIS/commit/9a35b27630982d63101c57c3e3440dcbf1a7786f>`__   | Possible after further user testing                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Big speed up for scripts which fire off many individual feature requests to a memory provider layer                                                                                         | not reported                                                                                                     | `Commit 1d2bb41752c51e6c9b84124a1ce1599d3d42b41c <https://github.com/qgis/QGIS/commit/1d2bb41752c51e6c9b84124a1ce1599d3d42b41c>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [console] Fix exception when running scripts                                                                                                                                                | not reported                                                                                                     | `Commit 5c8013df6129a2bc06d25a98ff20dbf27621bff5 <https://github.com/qgis/QGIS/commit/5c8013df6129a2bc06d25a98ff20dbf27621bff5>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [layouts] Fix resizing multiline label items to adjust to the size of their text                                                                                                            | not reported                                                                                                     | `Commit 6829e6351e1dab18f1fa0c0443107eb7617794c7 <https://github.com/qgis/QGIS/commit/6829e6351e1dab18f1fa0c0443107eb7617794c7>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Improve appearance of PyQGIS documentation for functions which return multiple values                                                                                                       | not reported                                                                                                     | `Commit 0001ec27a43cbf4c99d1525c3c5f75183e96f5c3 <https://github.com/qgis/QGIS/commit/0001ec27a43cbf4c99d1525c3c5f75183e96f5c3>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Don't raise a generic "something went wrong" exception when calling processing.run(), instead use proper descriptive exception                                                 | not reported                                                                                                     | `Commit 2207c30a247e5907a12185165b4bd220e255bbdc <https://github.com/qgis/QGIS/commit/2207c30a247e5907a12185165b4bd220e255bbdc>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix execution of "Eliminate selection" through Python                                                                                                                          | `#38808 <https://github.com/qgis/QGIS/issues/38808>`__                                                           | `Commit ee7bea2305253fd276a69c25bb5d308942dcb190 <https://github.com/qgis/QGIS/commit/ee7bea2305253fd276a69c25bb5d308942dcb190>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [3d] Fix crash when line feature cannot be buffered                                                                                                                                         | not reported                                                                                                     | `Commit f6eed85729a8cbf913155ae16df7499f688ba0fa <https://github.com/qgis/QGIS/commit/f6eed85729a8cbf913155ae16df7499f688ba0fa>`__   | `Commit d4c963e1c2fdc497dba038896caf2b3f975240ff <https://github.com/qgis/QGIS/commit/d4c963e1c2fdc497dba038896caf2b3f975240ff>`__   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix custom stroke patterns incorrectly scale when data defined stroke width is set                                                                                                          | `#39201 <https://github.com/qgis/QGIS/issues/39201>`__                                                           | `Commit 03fdc0cd7992a7883183704cd68506f32afe9ca3 <https://github.com/qgis/QGIS/commit/03fdc0cd7992a7883183704cd68506f32afe9ca3>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Allow columns to be resized in datum transformation table                                                                                                                                   | `#39169 <https://github.com/qgis/QGIS/issues/39169>`__                                                           | `Commit 1cd5a3358b235f67b6b4d95331ce561e9f8cb715 <https://github.com/qgis/QGIS/commit/1cd5a3358b235f67b6b4d95331ce561e9f8cb715>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix settings incorrectly show for wrong layer types in labeling dialog                                                                                                                      | `#39168 <https://github.com/qgis/QGIS/issues/39168>`__                                                           | `Commit 2e948884c029c9f79639201943ec4bc36dba3573 <https://github.com/qgis/QGIS/commit/2e948884c029c9f79639201943ec4bc36dba3573>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix error reporting from batch dialog                                                                                                                                          | `#39197 <https://github.com/qgis/QGIS/issues/39197>`__                                                           | `Commit 5243a8594cc39540f2c01201415633801a22ff43 <https://github.com/qgis/QGIS/commit/5243a8594cc39540f2c01201415633801a22ff43>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix crash when renaming conditional branch in modeler                                                                                                                          | `#39053 <https://github.com/qgis/QGIS/issues/39053>`__                                                           | `Commit ddae53b7b789467bf17b21d6f4b884e827fbd3c5 <https://github.com/qgis/QGIS/commit/ddae53b7b789467bf17b21d6f4b884e827fbd3c5>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix crash in model designer when a child algorithm contains hidden parameters                                                                                                  | not reported                                                                                                     | `Commit f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0 <https://github.com/qgis/QGIS/commit/f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Ensure True/False are treated as Python keywords in Python code editor                                                                                                                      | not reported                                                                                                     | `Commit 5f661045c078b7938550c2c9d0798664c6f65f5a <https://github.com/qgis/QGIS/commit/5f661045c078b7938550c2c9d0798664c6f65f5a>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't silently close QGIS with unsaved changes in the console script editors                                                                                                                | `#38529 <https://github.com/qgis/QGIS/issues/38529>`__                                                           | `Commit 9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9 <https://github.com/qgis/QGIS/commit/9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix dropping processing script algorithm .py file on QGIS no longer triggers the algorithm to execute                                                                                       | not reported                                                                                                     | `Commit 64bf347d7e1d664fc674c5ca602ce6c4bedecdf9 <https://github.com/qgis/QGIS/commit/64bf347d7e1d664fc674c5ca602ce6c4bedecdf9>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix message log dock causes havoc with other docks placed in the same area                                                                                                                  | `#31955 <https://github.com/qgis/QGIS/issues/31955>`__                                                           | `Commit 384f6a1d9257a05eaa58942921c94f1dd4941cd3 <https://github.com/qgis/QGIS/commit/384f6a1d9257a05eaa58942921c94f1dd4941cd3>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| When restoring a custom CRS from XML, if the CRS does NOT match any of the existing user defined CRS's on the QGIS profile then still restore the previously saved name of the custom CRS   | not reported                                                                                                     | `Commit e6d316ace7031821e04ca625e35f7c2c4d57f639 <https://github.com/qgis/QGIS/commit/e6d316ace7031821e04ca625e35f7c2c4d57f639>`__   | Possible after further user testing                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't refer to valid but custom CRSes as "Unknown CRS" and instead use "Custom CRS" phrasing                                                                                                | not reported                                                                                                     | `Commit d3833fd8d6c4b4f0673c4c2337044c224675185f <https://github.com/qgis/QGIS/commit/d3833fd8d6c4b4f0673c4c2337044c224675185f>`__   | Possible after further user testing                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Improve performance of processing batch process dialog with a large number of files                                                                                                         | `#38987 <https://github.com/qgis/QGIS/issues/38987>`__                                                           | `Commit 776768eb9f4ee2a8d13909b4ced5c175a0d05b3d <https://github.com/qgis/QGIS/commit/776768eb9f4ee2a8d13909b4ced5c175a0d05b3d>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Improve behavior of CRS selector and transformation widgets                                                                                                                                 | not reported                                                                                                     | many                                                                                                                                 | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [layouts] Use standard CRS selector widget for map grid CRS choice                                                                                                                          | `#26548 <https://github.com/qgis/QGIS/issues/26548>`__                                                           | `Commit 4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70 <https://github.com/qgis/QGIS/commit/4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [layouts] When selecting a CRS for a map item, don't show misleading no crs option at the top of the dialog                                                                                 | not reported                                                                                                     | `Commit c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad <https://github.com/qgis/QGIS/commit/c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix "layer has no CRS" message incorrectly show at the top of many projection selection dialog boxes                                                                                        | not reported                                                                                                     | `Commit c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c <https://github.com/qgis/QGIS/commit/c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix crash when editing style and opening a project                                                                                                                                          | `#38920 <https://github.com/qgis/QGIS/issues/38920>`__                                                           | `Commit 67ec244864ca6f9290e1f35a1a0c60b4888fe686 <https://github.com/qgis/QGIS/commit/67ec244864ca6f9290e1f35a1a0c60b4888fe686>`__   | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__/commits/ecf96231aefa5628539f0b63ca313ea8b20c9548                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Avoid qt warning when dragging a non-color object over color buttons                                                                                                                        | not reported                                                                                                     | `Commit fd771bba68da84b1ce8023898b9662b5dc619693 <https://github.com/qgis/QGIS/commit/fd771bba68da84b1ce8023898b9662b5dc619693>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix shift in geopdf feature positions when using geographic CRS at large scales                                                                                                             | `#37755 <https://github.com/qgis/QGIS/issues/37755>`__                                                           | `Commit 0b77f187ec5a14651457fd07f306cba2511fb854 <https://github.com/qgis/QGIS/commit/0b77f187ec5a14651457fd07f306cba2511fb854>`__   | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__/commits/b705d29c73e81fe87e2e301c7028e5e659d80364                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix constraint metadata is duplicated after opening layer properties                                                                                                                        | `#38916 <https://github.com/qgis/QGIS/issues/38916>`__                                                           | `Commit 6a002573c00a8a8e11443eaca28b57a8ad6de4c0 <https://github.com/qgis/QGIS/commit/6a002573c00a8a8e11443eaca28b57a8ad6de4c0>`__   | `PR #38748 <https://github.com/qgis/QGIS/pull/38748>`__/commits/49260b8f1f4b1ddd9a25c7160f32570221f3989e                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix PDF export includes vector information outside of the area of interest                                                                                                                  | `#38878 <https://github.com/qgis/QGIS/issues/38878>`__                                                           | `Commit f3f226aa69a19b31dd8a1b83c82319528e061cfe <https://github.com/qgis/QGIS/commit/f3f226aa69a19b31dd8a1b83c82319528e061cfe>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [layouts] Fix legend symbol rendering doesn't respect linked map scale when symbol uses map unit based sizes                                                                                | `#38326 <https://github.com/qgis/QGIS/issues/38326>`__                                                           | `Commit 426ee2120b33a8613f3e476da3c2eba0a00f65d7 <https://github.com/qgis/QGIS/commit/426ee2120b33a8613f3e476da3c2eba0a00f65d7>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't try to write empty rendered rings/geometries to GeoPDF outputs                                                                                                                        | not reported                                                                                                     | `Commit 96753cfd1b9e986841158675bda365e585c48c27 <https://github.com/qgis/QGIS/commit/96753cfd1b9e986841158675bda365e585c48c27>`__   | Possible after further user testing                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Correctly apply capitalization setting whenever QgsTextRenderer is used, not just in labeling                                                                                               | `#38898 <https://github.com/qgis/QGIS/issues/38898>`__                                                           | `Commit e1ca83b2c24c51e7ff67a53278ffd2601c0459be <https://github.com/qgis/QGIS/commit/e1ca83b2c24c51e7ff67a53278ffd2601c0459be>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix qgis\_process list raises exception if processing algorithm provider is activated                                                                                                       | `#38862 <https://github.com/qgis/QGIS/issues/38862>`__                                                           | `Commit 772181bc16820d7dd5ee8d967355dbdfde5a8efe <https://github.com/qgis/QGIS/commit/772181bc16820d7dd5ee8d967355dbdfde5a8efe>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Dramatic speed up for calling some frequently used methods from PyQGIS                                                                                                                      | not reported                                                                                                     | `Commit d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca <https://github.com/qgis/QGIS/commit/d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix certain characters show as HTML escaped in processing log                                                                                                                  | `#37934 <https://github.com/qgis/QGIS/issues/37934>`__                                                           | `Commit 965595d25bd0a69875ba8a405d3b365bedfe2a12 <https://github.com/qgis/QGIS/commit/965595d25bd0a69875ba8a405d3b365bedfe2a12>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix incorrect capitalization in title of new layout name dialog                                                                                                                             | not reported                                                                                                     | `Commit 92d0ec59a1c26c4ac33d35b9e6c93344845eddca <https://github.com/qgis/QGIS/commit/92d0ec59a1c26c4ac33d35b9e6c93344845eddca>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Add a new capitalization option for "Title Case", and rename the confusing "Capitalize First Letter" option to Force First Letter to Capital                                                | `#16539 <https://github.com/qgis/QGIS/issues/16539>`__                                                           | `Commit 484ba6f979cdcaabffe823c72b35b57d1b1c7aad <https://github.com/qgis/QGIS/commit/484ba6f979cdcaabffe823c72b35b57d1b1c7aad>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Add a Legend category to the style selection widgets and allow legend settings to be stored and restored in QML                                                                             | `#37683 <https://github.com/qgis/QGIS/issues/37683>`__                                                           | `Commit f018252023275f95c167d7f308d05c8819d6db0b <https://github.com/qgis/QGIS/commit/f018252023275f95c167d7f308d05c8819d6db0b>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix [Style] Export --> Save as QGIS Layer style File should allow to select style categories (and output format)                                                                            | `#29145 <https://github.com/qgis/QGIS/issues/29145>`__                                                           | `Commit 1ad2e78735e57cef218a7470d7eec645c2f45263 <https://github.com/qgis/QGIS/commit/1ad2e78735e57cef218a7470d7eec645c2f45263>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [browser] Correctly save expanded node state when closing QGIS                                                                                                                              | not reported                                                                                                     | `Commit 2eff061bf3cdcb3f36956e43098adfcb0359b5eb <https://github.com/qgis/QGIS/commit/2eff061bf3cdcb3f36956e43098adfcb0359b5eb>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| [browser] Gpkg and other container types can be dragged to the map to allow layers to be added from them                                                                                    | not reported                                                                                                     | `Commit 0234d4e9e10f3fbb5732f66e00eebd038f502ab0 <https://github.com/qgis/QGIS/commit/0234d4e9e10f3fbb5732f66e00eebd038f502ab0>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Don't prompt for CRS for annotation layers                                                                                                                                                  | `#38739 <https://github.com/qgis/QGIS/issues/38739>`__                                                           | `Commit 15975c1d5191933311d81a494d87806f4e73ce57 <https://github.com/qgis/QGIS/commit/15975c1d5191933311d81a494d87806f4e73ce57>`__   | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix reading saved color map file when an item's label contains a comma character                                                                                                            | `#24112 <https://github.com/qgis/QGIS/issues/24112>`__                                                           | `Commit 252149375c750d6a8f1ee281c1cc9d03de272170 <https://github.com/qgis/QGIS/commit/252149375c750d6a8f1ee281c1cc9d03de272170>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix diagram settings are not correctly restored when loading a QML file                                                                                                                     | `#35343 <https://github.com/qgis/QGIS/issues/35343>`__                                                           | `Commit 4668927ce432b198b3c572535ff234343c5042f5 <https://github.com/qgis/QGIS/commit/4668927ce432b198b3c572535ff234343c5042f5>`__   | Too risky                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Fix can no longer paste colors from text strings                                                                                                                                            | not reported                                                                                                     | `PR #39561 <https://github.com/qgis/QGIS/pull/39561>`__                                                                              | N/A                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Nyall Dawson <https://north-road.com/>`__

.. |image1| image:: images/projects/dbc0cef663f2f652e0961ac2ed168eb45ed2e182.png
   :class: img-responsive img-rounded center-block
.. |image2| image:: images/entries/079434bceb5004b0ee2c4ad5d62edd1290c28575.png
   :class: img-responsive img-rounded
.. |image3| image:: images/entries/acb9e856ac744d0e40d8de33c025deb075385856.gif
   :class: img-responsive img-rounded
.. |image4| image:: images/entries/f6e3ce9dca04583c9fa791204fe7e1a3c49c61d0.png
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/f93d5dca726eb94be82cc47479424b8fe42f5920.gif
   :class: img-responsive img-rounded
.. |image6| image:: images/entries/87635346-39f11c00-c782-11ea-88bc-369866d7f57a.png
.. |image7| image:: images/entries/87635368-44131a80-c782-11ea-95d9-07fb7d00ffcf.png
.. |image8| image:: images/entries/e1a4d82c248cdd0f04f236443897178c12574885.gif
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/7e4ee802abba7dfd7ec61cdd8b3db333b7a30fae.gif
   :class: img-responsive img-rounded
.. |image10| image:: images/entries/f5cc643fc4eafe75053c134b245e91d2e72e33d0.gif
   :class: img-responsive img-rounded
.. |image11| image:: images/entries/a6c67225ee3b55a021a395ffbf58bd05352ef6fb.gif
   :class: img-responsive img-rounded
.. |image12| image:: images/entries/09739c5bed021a99baec41c98b87f5335a4bf8ec.png
   :class: img-responsive img-rounded
.. |image13| image:: images/entries/85622744-4d9edc00-b635-11ea-91db-a02fa28e6bea.gif
.. |image14| image:: images/entries/b27519025102be3b07fc8241f0ff8f8f2f9b31c6.png
   :class: img-responsive img-rounded
.. |image15| image:: images/entries/c4974747f5bc0dcba02f30a97e68bb5edacc5f48.png
   :class: img-responsive img-rounded
.. |image16| image:: images/entries/86540129-a8a3bf00-bed0-11ea-94b8-bf29b5818cb8.gif
.. |image17| image:: images/entries/803983acbaec38e8df0fb4fd12d28beef7399520.png
   :class: img-responsive img-rounded
.. |image18| image:: images/entries/fc8a9633b87b29bba052dacd166c0735b4449c90.png
   :class: img-responsive img-rounded
.. |image19| image:: images/entries/bf6076062db63bc4c789bc18d3b029c14b2ddc8e.gif
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/ef724bf261c7740d3cc92238d71d5ecb32a190c3.jpeg
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/91c112ba42358124faec9c3427542524d6b593f9.png
   :class: img-responsive img-rounded
.. |image22| image:: images/entries/4dcd7d7f4bcfb71d765656bfe734ec32ddcaca9c.png
   :class: img-responsive img-rounded
.. |image23| image:: images/entries/1c4fc6ffc1b7a28aeff9c625fb6238998dd30b67.png
   :class: img-responsive img-rounded
.. |image24| image:: images/entries/d4deaabbeddcf5f4784f602f19dabfac22b2d100.png
   :class: img-responsive img-rounded
.. |image25| image:: images/entries/b6df518d57147bfdfd207d4499363c9d4653721b.png
   :class: img-responsive img-rounded
.. |image26| image:: images/entries/86863750-26550e00-c10f-11ea-8dd4-1b740017949e.gif
.. |image27| image:: images/entries/349efbc988ccbf3499e18ec4453b637abf893c38.png
   :class: img-responsive img-rounded
.. |image28| image:: images/entries/86433831-191ad680-bd3f-11ea-9289-cc6d2b3e2e11.gif
.. |image29| image:: images/entries/1f1343d09c75b0e1d131c25a79b905d7aaadbc35.png
   :class: img-responsive img-rounded
.. |image30| image:: images/entries/88761088-c1428480-d1b1-11ea-90c0-a391d00b084d.gif
.. |image31| image:: images/entries/7179282b09e8d196251f543a9c5f059f89c701e2.png
   :class: img-responsive img-rounded
.. |image32| image:: images/entries/0da542215cefcd2e3ca120dd0381b47611734dce.gif
   :class: img-responsive img-rounded
.. |image33| image:: images/entries/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif
.. |image34| image:: images/entries/03463ac0a8303444d94806fb2ff66d6a73c56ccb.png
   :class: img-responsive img-rounded
.. |image35| image:: images/entries/90797864-7bd92900-e311-11ea-945f-0c2ade14e801.gif
.. |image36| image:: images/entries/d4bb059729eecfc689e001f731d59fff25225615.png
   :class: img-responsive img-rounded
.. |image37| image:: images/entries/88101713-6505b200-cb6c-11ea-9feb-68a4130d6f52.gif
.. |image38| image:: images/entries/86938423-6a93de80-c10e-11ea-8511-489d8b4f006f.gif
.. |image39| image:: images/entries/86938444-7089bf80-c10e-11ea-8fd0-0f419f71b52e.gif
.. |image40| image:: images/entries/8145ccfa4e659f7d8315830cecfe2b2f391b9aa4.png
   :class: img-responsive img-rounded
.. |image41| image:: images/entries/86897604-53ee8700-c110-11ea-99ae-540d38f88154.png
.. |image42| image:: images/entries/86897671-67015700-c110-11ea-8183-e0d6bd013dbb.png
   :class: img-responsive img-rounded
.. |image44| image:: images/entries/d3a51f9b7ea6ffa3c8c8c457e3d6278d57bcf125.gif
   :class: img-responsive img-rounded
.. |image45| image:: images/entries/863b80851b995421b6f2ea455faf6b1c41211cd5.gif
   :class: img-responsive img-rounded
.. |image46| image:: images/entries/8048bb8df64e31bb733eea239c527f8be631ce6f.gif
   :class: img-responsive img-rounded
.. |image47| image:: images/entries/85852208-7bca1a80-b7f3-11ea-8882-b3253622b1b6.png
.. |image48| image:: images/entries/943a79db68aee3458cb88cacd7a69b66fda3caea.png
   :class: img-responsive img-rounded
.. |image49| image:: images/entries/fca13f48b118ed13ebe84191a226ca0e20c37bfa.png
   :class: img-responsive img-rounded
.. |image50| image:: images/entries/e368e10cfa5e19992176930121e0cb846c3d1ca8.png
   :class: img-responsive img-rounded
.. |image51| image:: images/entries/97228db861367c2875dab0533ab616bb2ac2432c.png
   :class: img-responsive img-rounded
.. |image52| image:: images/entries/114853cd3d7c245b56edea0024704c853997275c.png
   :class: img-responsive img-rounded
.. |image53| image:: images/entries/f3383f5583c9096b1b8d1873679e1a495fac0485.png
   :class: img-responsive img-rounded
.. |image54| image:: images/entries/a730b8c1566c99bdebff09c783ae320b0c138d76.png
   :class: img-responsive img-rounded
.. |image55| image:: images/entries/2196bcb0123ced5e180ffb2b9469a65a38dcc41b.png
   :class: img-responsive img-rounded
.. |image56| image:: images/entries/b238631365830b019300700cf59c3a8dd3d05a4f.png
   :class: img-responsive img-rounded
.. |image57| image:: images/entries/e4f315e60743577c9f45ad44643fd5ba9778c040.png
   :class: img-responsive img-rounded
.. |image58| image:: images/entries/414c68839518d5b658d6e6f1565f6c27e1f4336f.gif
   :class: img-responsive img-rounded
.. |image59| image:: images/entries/5cc48d8ea8bc276446f8eae4a1c838e0d1f91a40.png
   :class: img-responsive img-rounded
.. |image60| image:: images/entries/e59bb83513293830df8ec4dcf825247b14dacc98.png
   :class: img-responsive img-rounded
.. |image61| image:: images/entries/87223743-a4b7e700-c37f-11ea-88a3-4b371bfadf89.gif
.. |image62| image:: images/entries/d4e761ad977a712aa1fc1fbc65d61c886e6e79fb.png
   :class: img-responsive img-rounded
.. |image63| image:: images/entries/e31c882fa9552ed6bd247f0092305ae8c153948a.gif
   :class: img-responsive img-rounded
.. |image64| image:: images/entries/e1c7474d19828b39f5872b289a1e8ba994556a10-1.png
.. |image65| image:: images/entries/4a2d99c6ef6ec12e5f63a29ad00d9ebc3cd534e2.png
   :class: img-responsive img-rounded
.. |image66| image:: images/entries/a2254bbef892835317a9f608afd8bd3722ee4b38.gif
   :class: img-responsive img-rounded

