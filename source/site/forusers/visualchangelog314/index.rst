.. _changelog314:

Changelog for QGIS 3.14
=======================

|image1|

Release date: 2020-06-25

Another awesome release in the trail of great QGIS releases we have made across 18 years of development. This release is so jam-packed with new features and improvements big and small, it is hard to know where to start. Some of the marquee features include vector tile support, huge advances in mdal / mesh support, native support for temporal data in WMS-T, PG Raster, vector providers, and mesh layers. Users focussed on cartography and digitising haven't been left out either, with many new options for you!

**Thanks**

We would like to thank the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to `QGIS.ORG <qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our `donors list <https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our `sustaining member page <https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships>`__ for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

:raw-html:`<div id="qgissustainingmembersatom"> <!-- to be filled via javascript loading of atom feed --> </div>`

QGIS is Free software and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision-making tools will result in a better society for all of humanity.


.. contents::
   :local:


General
-------

Feature: New grid decoration annotations font settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Annotations for the map canvas' grid decoration are now fully customizable including font color, buffer, etc.

|image8|

This feature was funded by iMHere Asia

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__


Temporal
--------

Feature: Cumulative temporal range setting in temporal controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a setting in the temporal controller to set the animation temporal range to cumulative. This means that all animation frames will have the same start date-time but different end dates and times.

This is useful is you wish to accumulate data in your temporal visualisation instead of showing a 'moving time window' across your data.

|image2|

This feature was funded by `Meteorological Service of Canada <https://weather.gc.ca>`__

This feature was developed by `Kartoza / Samweli Mwakisambwe <https://kartoza.com>`__

Feature: Add a new "Redraw Layer Only" mode for temporal vector layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When set to this mode, the layer will automatically be redrawn whenever the temporal range is changed, but no time based filtering will be applied to the features.

This configuration is useful when the layer has symbology settings which vary based on the temporal range. For instance, when a layer is using time-dependent rule-based renderer expressions or data-defined symbology expressions.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add basic temporal handling support for vector layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exposes some basic native temporal capabilities for vector layers:

-  Static time range for layer (to match raster layer possibilities), this sets a single static time range that applies to the whole layer. All features from the layer will be shown whenever the canvas time overlaps the layer time range
-  "Single field with DateTime": Allows selection of a single Date or DateTime field from the layer. Features will be shown whenever this field value is within the canvas time range
-  "Separate Fields for Start and End Date/Time": Allows selection of start and end Date/DateTime fields from the layer. Features will be shown whenever the time interval calculated from these fields overlaps the canvas time range

We should consider extending this in future, e.g. to add modes like "start time + fixed duration", "start time + duration from field", "start and end time via expressions", etc.

Some known limitations/inefficiencies:

-  Currently only Date/DateTime fields can be used. This was done to simplify the format handling and avoid the need to worry about string fields with different DateTime formats. In future, we should allow selection of string fields and allow users to enter a custom DateTime format string
-  Unlike the Time Manager plugin approach, the approach taken here is to rely completely on QGIS expressions and feature requests to do the filtering (Time Manager uses layer filter strings and attempts to set a native SQL filter syntax so that filtering is done on the backend). This is intentional because it provides a unified filter approach regardless of the provider used (i.e. we don't need to worry about the different SQL syntaxes used natively by the different providers). The beauty of feature request expression compilation **should** mean that the QGIS expressions are magically turned into native backend queries, BUUUUUUUUUUUT... because we lack QGIS expression support for DateTime literals, we currently rely on the "to\_datetime" expression function and coerce everything through strings. None of the expression compilers handle this function, so currently \*all\* filtering is done on the QGIS side. We need to add functions for optimised DateTime literal creation and then ensure that the different compilers correctly map these literals across to the backend filter syntax to allow all the filtering work to be done on the database side...

So, currently, performance is much worse with large layers compared to Time Manager (and the exposed feature set is smaller, e.g. no interpolation handling) but the advantage is that we can use the native temporal framework and have vector layers animated alongside mesh and raster layers!

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Postgres raster temporal API support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added temporal capabilities integration for Postgres rasters.

|image3|

|image4|

This feature was funded by ARPA Piemonte

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

Feature: QGIS Project temporal settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds project time settings functionality.

You will be able to set the project temporal range either by using manual input or by calculating it from the current project's temporal layers. The latter can be done by clicking the provided "Calculate from Layers" button.

This implementation sets the stage for adding an animation feature for temporal layers in QGIS.

Here's an example of setting the project temporal range. |image5|

Prior discussions about QGIS temporal support can be found `here <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/161>`__ and `here <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/128>`__.

This feature was funded by `Meteorological Service of Canada <https://weather.gc.ca>`__

This feature was developed by `Kartoza / Samweli Mwakisambwe <https://kartoza.com>`__

Feature: WMS-T layers temporal constraints support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds the ability to constrain WMS Temporal (WMS-T) layers inside QGIS. You will be able to constrain the DateTime range for any temporal layer from WMS-T providers.

This implementation lets the user specify the required DateTime range on the layer from the source tab on the layer properties dialog.

Below is an example of the workflow. |image6|

**Note:** *For instant point in time requests, specifying a range with equal begin and end DateTime will result into using the specified DateTime instant and not a range.*

|image7|

This feature was funded by `Meteorological Service of Canada <https://weather.gc.ca>`__

This feature was developed by `Kartoza / Samweli Mwakisambwe <https://kartoza.com>`__

Feature: Temporal API
~~~~~~~~~~~~~~~~~~~~~

This feature provides an API implementation for temporal support in QGIS.

You can find the API for Python by searching for 'Temporal' in the python docs (`link <https://qgis.org/pyqgis/master/search.html?q=Temporal&check_keywords=yes&area=default>`__).

This feature was funded by `Meteorological Service of Canada <https://weather.gc.ca>`__

This feature was developed by `Kartoza / Samweli Mwakisambwe <https://kartoza.com>`__


Map Tools
---------

Feature: Identify Tool Support for QGIS vector tile layers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The identify map tool is now able to inspect attributes of features in vector tiles.

|image9|

This feature was funded by `Many funders <https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/>`__

This feature was developed by `Lutra Consulting (Martin Dobias) <https://www.lutraconsulting.co.uk/>`__

Feature: Show a menu next to scale widget buttons, to allow setting the widget directly to a scale from a print layout map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A screencast says a thousand words:

|image10|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add tool button to "Deselect Features from the Current Active layer"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image11|

This feature was developed by `Ivan Ivanov <https://api.github.com/users/suricactus>`__

User Interface
--------------

Feature: Allow the drag and drop of a layer across several QGIS instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image12|

This feature was funded by `QGIS Swiss user group <https://www.qgis.ch>`__

This feature was developed by `Denis Rouzaud <https://api.github.com/users/3nids>`__

Feature: Open attribute tables as tabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the option "Open new attribute tables as dock windows" is active, new attribute tables will be opened as tabs on top of existing attribute tables.

|image13|

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Symbology
---------

Feature: Raster Layer Contour Renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new renderer draws contour lines that are calculated on the fly from the source raster band. It is possible to set the interval of the contour lines and the symbol used for drawing.

In addition there is support for "index contours" - contour lines with higher intervals, typically drawn with a wider line symbol.

If we generate contour lines on input raster blocks with the same size as our output raster block, the generated lines would contain too much detail. This detail can be reduced by the "downscale" factor - this will request lower resolution of the source raster.

|image14|

This feature was developed by `Martin Dobias <https://api.github.com/users/wonder-sk>`__

Feature: Add percentage size unit for Raster Image Marker and Raster fill layers symbology.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to the `Feature Request <https://github.com/qgis/QGIS/issues/30057>`__ this patch adds a new percentage (of original image size) value for size units of **Raster Image Marker** and **Raster fill** (by `nirvn <https://github.com/qgis/QGIS/pull/34869#issuecomment-595090465>`__ suggestion) layers.

For example a layer contains raster images of various sizes and aspect ratios:

|image15| |image16|

If we use an existing Raster image marker **size unit** values the layer will look like this (with a normal croc, but huge giraffe):

|image17|

or like this (with a normal giraffe but tiny croc):

|image18|

The new **percentage** value of size units is intended to fix this issue.

Both unit tests "qgis\_rasterfilltest" and "qgis\_rastermarkertest" were rewritten with a set of new control images for testing the proposed **percentage** value of size units.

This feature was developed by `beketata <https://api.github.com/users/beketata>`__

Feature: Add data-defined property to font family/style for font markers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data-defined properties were added for the font markers' font family and the brand new font style properties. This can come in handy for a number of scenarios, including multilingual context where a data-defined property can avoid duplicating datasets.

|image19|

This feature was funded by iMHere Asia

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Feature: New font style setting for font markers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this brand new font style setting, users can pick non-default style of font families previously not available.

|image20|

This feature was funded by iMHere Asia

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Labelling
---------

Feature: Respect HTML colors in labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enabled, this option will treat label contents as HTML, and any FOREGROUND COLOR RELATED html formatting options will be respected in the rendered label.

Note: ONLY HTML COLOR TAGS ARE RESPECTED. This is NOT a bug, rather this feature has been designed as a "test of the waters" with HTML formatting in labels, and accordingly only formatting options which do not alter the font shape were considered.

On the plus side, it works correctly with ALL other label settings, including shadows, buffers, curved labels, etc!

Now some pretty pictures:

|image21|

|image22|

This feature was funded by `geoProRegio AG <http://www.geoproregio.ch>`__

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Automatic placement of labels outside polygons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds the ability to automatically place labels outside of polygon features.

This is exposed in a number of ways:

#. A new placement mode which always places polygon labels for the layer outside the features: |image23| |image24|
#. When using other polygon placement modes, a new checkbox "Allow placing labels outside of polygons" can be checked to allow labels to be placed outside when it isn't possible to place them inside the polygon: |image25| |image26|

The "allow placing labels outside" checkbox can be data defined, allowing users to either allow outside labels, prevent outside labels, or force outside labels on a feature-by-feature basis.

The placement algorithm is based on a modification of Rylov & Reimer (2016) "*A practical algorithm for the external annotation of area features*". While Rylov & Reimer propose a horizontal sweep-line based approach for selection of candidate label points, in practice I found that this delivered inferior results (and was slower) then just traversing the exterior ring of the polygon and generating candidate point at regular intervals (especially for narrow, nearly horizontal polygons).

As shown in the islands screenshot above, the outside placement mode works as expected with the "Follow label placement" multiline alignment mode.

This feature was funded by `Swiss QGIS user group <https://www.qgis.ch/>`__

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Vector tile layer - part 4 (labeling)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continued work on vector tile layer implementation.

This adds labeling support for vector tile layers. So far this is just working on qgis\_core... GUI support will come next. Labeling uses the same concepts as the rendering of vector tiles: we have a list of labeling styles, each one is defined by sub-layer name, geometry type, filter expression, zoom range and of course label style configuration (QgsPalLayerSettings).

Note there is a "chicken-and-egg problem" with labeling: For vector tiles, we create QgsFields for a sub-layer based on fields that renderer and labeling request, but with labeling it was impossible to get required fields if they were not already available in the expression context (hence some small additions to QgsProperty, QgsPropertyCollection, QgsPalLayerSettings to be able to get required field names by not preparing internal expressions at the same time).

|image27|

An example how to set the above labeling in Python console::

 s = QgsVectorTileBasicLabelingStyle()
 s.setLayerName("place")
 s.setGeometryType(QgsWkbTypes.PointGeometry)
 s.setFilterExpression("rank = 1 AND class = 'country'")
 ls=QgsPalLayerSettings()
 ls.drawLabels=True
 ls.fieldName="name"
 ls.placement = QgsPalLayerSettings.OverPoint s.setLabelSettings(ls)
 labeling = QgsVectorTileBasicLabeling()
 labeling.setStyles([s])
 iface.activeLayer().setLabeling(labeling)


This feature was funded by `Many funders <https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/>`__

This feature was developed by `Lutra Consulting (Martin Dobias) <https://www.lutraconsulting.co.uk/>`__

Feature: Add control over anchor point for callout on label
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This gives users control over where a callout should join to the label text (previously, you only had control over where the callout would join to the corresponding feature geometry).

Choices include:

-  Closest point (previous behavior)
-  Label Centroid
-  Fixed corners: Top left/top right/bottom left/bottom right/etc

Data defined control over the label anchor is also possible.

Helps fix some callout ugliness!

Previous result (closest point mode):

|image28|

With new "centroid" placement:

|image29|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Mesh
----

Feature: Use only specified dataset group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature allows the user to choose the dataset groups that are used. This can be done in the mesh layer properties dialog in the source tab.

A new tree view displays all the available dataset groups from the data provider. The dataset groups can be checked/unchecked and renamed.

This widget also provides buttons to load extra dataset groups from files, to expand/collapse the tree, to check/uncheck all items and to reset the defaults from the provider (for now, only the original name).

Only the checked dataset group will be displayed in the active dataset widget in renderer settings.

|image30|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Scalar color settings depending on classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this feature, MDAL reads classified scalar values in the dataset. When values are classified, the default scalar rendering settings has the color ramp shader and labels set according to the classified values.

|image31|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Snap on mesh elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a method to the API to snap on mesh elements.

The method returns the position of the snapped point on the closest mesh element :

-  For a vertex, the snapped position is the vertex position
-  For an edge, the snapped position is the projected point on the edge, or the extremity of edge if outside the edge
-  For a face, the snapped position is the centroid of the face

The returned position is in map coordinates.

|image32|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: 1D mesh width/color varying
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature provides a new way to render a 1D mesh with edge widths that can vary depending on value. So now, width and color vary depending on the value on the edges or on vertices.

The user can define min/max value and min/max width to set the rendering.

For color, the user can define a color ramp shader (as for 2D mesh and raster).

For this new rendering, new generic classes are introduced that could be used outside the mesh framework.

|image33|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Support for multiple mesh (since MDAL 0.5.91)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to updating to MDAL 0.5.91, this feature allows several meshes to be loaded from one file.

The file is parsed and a sub layer dialog is launched using the same logic as for vector or raster layers.

|image34|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Plug mesh layer to QGIS temporal framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image35|

Time handling in mesh layer
...........................

The time in a mesh layer is defined by :

-  A reference time provided by the data, the project or the user
-  Each dataset is associated with relative times
-  Time extent is defined by the first time and the last time of all datasets

::

 Reference time :          AT
 Dataset 1 time            o---RT------RT-----RT-----------RT
 Dataset 2 time            o-------RT------RT--------RT
 Dataset 3 time            o--------------------------RT-------RT------RT
 Time extent of layer      o----<---------------------------------------->

 -  AT : absolute time (QDateTime)
 -  RT : relative time (qint64)

The class **QgsMeshDataprovidertemporalCapabilities** stores the reference time provided by the data and all the relative times of the dataset. This class has the ability to return dataset index from a dataset group index and a relative time since the reference time. The reference time (which can be different than the provider reference time) and the absolute time extent are stored in the class **QgsMeshTemporalProperties**

The temporal settings in the properties widget are only the reference time and the provider time unit: |image36|

The default reference time of the layer is set by (sorted by priority):

-  From the data provider if defined in data
-  From the project if defined
-  From current date with time 00h00

The user can change it if he wants.

Rendering principle
...................

The 2D and 3D renderers access the active dataset index from the layer with the time range stored in the ``QgsContextRenderer`` and in the ``Qgs3DMapSettings`` : Relative time is calculated as the difference between the time range of ``QgsContextRenderer`` and the reference time stored by ``QgsMeshTemporalProperties``. The dataset index comes from the ``QgsMeshDataproviderTemporalCapabilities`` that maps the relative time with dataset index.

The data are brought from the provider with the dataset index.

Static dataset
..............

There is also the option to set a static dataset, that is to choose a dataset that will be rendered independently of the QGIS time controller. To do that the user can check the check box at the bottom of the temporal page of the properties widget: |image37| For now, as it was simpler to implement and allows the required dataset to be chosen directly, the user can independently choose scalar dataset and vector dataset from combo boxes with the time associated for each dataset (relative time for data without reference time). If required, a unique time could be implemented but that could lead to inconsistent results with non synchronous datasets. The static dataset settings are in the temporal page but can be easily put in the source page if wanted.

This feature was funded by `Lutra Consulting <https://www.lutraconsulting.co.uk>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Resampling from vertex values to face values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resampling is available for datasets defined on faces, e.g. the value on vertices is calculated from values on faces.

This feature implements resampling from values on vertices to values on faces using the neighbor average method.

The default method is set to "none" for resampling from vertices to faces and to "neighbor average" for resampling from faces to vertices. Then the default rendering is always smooth. |image38|

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Coloring mesh vector dataset with color ramp shader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature allows the user to color the mesh layer vector dataset (arrow, stream lines, traces) with the color ramp shader depending on the magnitude of the vector.

|image39|

|image40|

|image41|

This feature was funded by `Deltares <https://www.deltares.nl/en/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Save style for mesh layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds the option for saving a mesh layer style in a qml file, as utilised for vector and raster layers.

The feature also refactors the raster and vector layer properties menu style. |image42|

This feature was funded by `Artelia Group <https://www.arteliagroup.com/en>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Mesh 1D Renderer
~~~~~~~~~~~~~~~~~~~~~~~~~

Update to `MDAL 0.5.90 <https://github.com/lutraconsulting/MDAL/releases/tag/0.5.90>`__

Initial implementation of `Support of 1D elements in Mesh Layers <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/164>`__

1D Meshes consist of vertices and edges. An edge connects two vertices and can have assigned data (scalars or vectors) on it. The 1D mesh network can, for example, be used for modelling an urban drainage system.

There are new options to display 1D mesh (edges) in the mesh frame tab |image43|

Also for data on 1D mesh (edges or vertices) there are new options in the contours tab

|image44|

Note that not all functionality available for 2D meshes is available, notably

-  Support for Mesh Calculator for 1D meshes
-  3D rendering of 1D meshes
-  Identify and Plots in Crayfish (will be added later in the following PR)

Some functions are not necessary for 1D meshes, especially

-  Export of mesh contours

This feature was developed by `Peter Petrik <https://api.github.com/users/PeterPetrik>`__

Feature: Mesh simplification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a mesh layer could have millions of triangles, rendering can be very slow, especially as all the triangles are displayed in the view even when triangles are too small to be seen.

For those situations, this feature provides an option to simplify the mesh. Simplification leads to one or more simplified meshes that represent levels of detail. When rendering the mesh, the appropriate level of detail is chosen to provide an adequate rendering depending on the view.

A new tab in the mesh layer properties widget allows the user to change the settings :

-  The reduction factor is used to simplify a mesh; the number of triangles for each level of detail is approximately equal to the number of triangles of the previous level of detail, divided by the reduction factor
-  Maximum mesh resolution: this is the average size (in pixels) of the triangles that are allowed to be displayed; if the average size of the mesh is lower than this value, a mesh with a lower level of detail is displayed, i.e. a mesh with an average size just greater than the maximum mesh resolution.

|image45|

This feature allows the speeding up of rendering as shown in these tables (result in milliseconds) : |image46|

Demo GIF Before: |image47|

After: |image48|

This feature was funded by `BMT <https://www.bmt.org/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

3D Features
-----------

Feature: Arrows for 3D mesh layer dataset rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds an option for displaying arrows on a mesh layer dataset 3D entity, depending on vector dataset.

The dataset used to render arrows is the one chosen for rendering vectors on 2D rendering.

In the same way, the color of arrows are defined in the 2D rendering settings for vector dataset.

In 3D settings, the user can define the spacing of arrows and if size is fixed or scaled on magnitude.

This spacing setting also defines the maximum size of arrows because arrows can't overlap. |image49|

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Print Layouts
-------------

Feature: Temporal settings for layout map items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds a collapsible section to the layout map item widget that allows users to enable and set a temporal range to be used when rendering map content.

The start and end datetime value can be data-defined, which comes in handy when used alongside atlas features.

|image50|

This feature was funded by iMHere Asia

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Feature: Allow sorting attribute table by field not listed in the table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using the same data model for the displayed and the sorting columns, two data models are now used. They use the same API / base class as they are very similar.

This feature was developed by `Denis Rouzaud <https://api.github.com/users/3nids>`__

Feature: Expose control over layer legend splitting behavior on a layer-by-layer basis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This allows users to manually override the legend's default setting for "split layers" on a layer-by-layer basis, by double clicking a layer in the layout legend panel and choosing whether that layer:

-  Follows the default legend setting for splitting
-  Can ALWAYS be split over multiple columns (regardless of the legend's setting)

or

-  Can NEVER be split over multiple columns (regardless of the legend's setting)

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow customisation of division and subdivision symbols as distinct from scalebar tick horizontal symbol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows for styling division and subdivision symbols in a different way compared with the horizontal line symbol in a tick scalebar

Sponsored by SLYR

Builds off the hard work done by @agiudiceandrea!

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow overriding the default symbol for a legend node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This allows users to (optionally) customise the symbol appearance for a legend node, e.g. to tweak the colors or symbol sizes to better provide a "representative" patch symbol compared with how those corresponding features actually appear on the map.

It's useful for exaggerating symbol widths, or for manually tweaking the colors of semi-transparent symbols so that the colors represent the actual appearance of the symbols when rendered on top of the map content. Or to tweak the marker interval/offset in marker lines so that the markers are nicely spaced in the legend patch.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow placing manual column breaks in legends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds the option when configuring a legend item to place a column break before the item, causing it to be placed into a new column.

This allows user control over the column content, for cases when the automatic column generation doesn't result in the desired results.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add subdivisions in ticks scalebar right segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds the ability to create subdivisions for segments included in the right part of the ticks scalebar.

Line Ticks Up |image51|

Line Ticks Middle |image52|

Line Ticks Down |image53|

Scalebar item properties - Segments groupbox |image54|

The behaviour related to the segments on the left side of the scalebar is unchanged.

This feature was developed by `Andrea Giudiceandrea <https://api.github.com/users/agiudiceandrea>`__

Feature: Allow overriding the legend patch size on a per-item basis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows users to override the symbol patch size for individual legend nodes, by double clicking the node

Width and height can be individually overridden, with the node falling back to the default width or height when the override isn't set.

Sponsored by SLYR |image55|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow control over the horizontal spacing before legend group/subgroup/symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gives flexibility to allow "nesting" legend groups/subgroups/symbols and much greater control over legend item placement.

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Manage legend patch shapes through style manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update finalises the recent legend patch shape customisation work, by adding in support for custom legend patch shapes to style manager!

Now we just need a really nice set of default patch shapes to ship!!

|image56|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow configuring legend patch shapes by double-clicking on legend items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows users to set custom legend patch shapes for items by entering a WKT string representing the patch geometry.

Sponsored by SLYR

|image57|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Support pasting pictures directly into layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Embeds the pasted picture into the layout.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow marker items to sync rotation with maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This allows creation of north arrows from marker symbols, exposing the same options as exist for picture items acting as north arrows.

When a marker acts as a north arrow, the map rotation is ADDED to any existing marker symbol rotation (e.g. if you have to rotate the triangle marker 90% to get it pointing straight up, it will still work nicely in north arrow mode!)

|image58|

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: New item type for marker symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows marker symbols to be placed directly on layouts, e.g. for manually placing markers over a map item or for creation of advanced custom legends.

Previously you had to hack support for these, e.g. by drawing rectangles using centroid fill symbols. Much nicer to have a dedicated item type for it, allowing more specific customisation options (coming soon!)

Sponsored by SLYR

|image59|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add import content from clipboard for fixed table items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new import content from clipboard feature has been added to QGIS' table editor to enable quicker layout fixed table item editing and creation.

|image60|

This feature was funded by iMHere Asia

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Feature: Add numeric formatter "fraction" style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This style represents decimal numbers as vulgar fractions, e.g. "3/4" instead of 0.75.

Options include using Unicode superscript and subscript characters for nicer typography, e.g. ¹⁷/₂₃ (this is the default mode, disabling this option uses the "17/23" format). An option also exists for using dedicated unicode characters for specific fractions (where a unicode character exists), e.g. ½ or ¾.

Ultimately this allows for creation of scalebars with fractional representations of distances, e.g. 0 ----- ½ ----- 1 km (instead of 0 ------ 0.5 ------ 1km)

Sponsored by SLYR

|image61|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add "stepped line" and "hollow" scalebar styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds two new scalebar styles (which are available in ArcMap, but previously impossible to reproduce in QGIS)

Stepped line style:

|image62|

Hollow (aka "South African") style:

|image63|

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow scalebar line style to be set using standard QGIS line symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of the previous settings of scalebar line color/width/cap styles, we now expose the option as a full line symbol for more advanced styling.

Also some code cleanups.

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Rework picture item UI and behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds an explicit choice between SVG or raster image sources, which allows us to clean up the configuration panel for layout pictures by hiding options which don't apply to a certain picture source. Also permits us to:

-  Reuse the standard SVG selector tree widget, which loads images in a background thread
-  Uses the standard SVG and image selector line edit, which permits drag and drop of images and exposes options to embed images and link to online sources

Ultimately this is motivated by a desire to allow users to embed images in layouts and layout templates

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Make CRS controlable by a variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This makes the Map CRS controllable by a variable.

|image64|

Related to #34547

This feature was developed by `Alex <https://api.github.com/users/roya0045>`__

Expressions
-----------

Feature: New expressions
~~~~~~~~~~~~~~~~~~~~~~~~

-  ``ascii``
-  ``make_interval`` Allows direct construction of interval values from years/months/weeks/days/hours/minutes/second values, without having to construct a string representation of the interval first
-  ``maptip``
-  ``layer_property('distance_units')``
-  ``display_expression``
-  ``eval_template``
-  ``make_date``
-  ``make_time``
-  ``make_datetime``
-  ``close_line``
-  ``is_multipart``
-  geometry Z and M minimum and maximum
-  ``@frame_number``
-  ``@frame_rate``
-  ``@frame_duration``
-  ``@map_start_time`` Start of the map's temporal time range (as a datetime value)
-  ``@map_end_time`` End of the map's temporal time range (as a datetime value)
-  ``@map_interval:`` Duration of the map's temporal time range (as an interval value)
-  ``@animation_start_time``
-  ``@animation_end_time``

This feature was developed by Etienne Trimaille, Jan Caha, Julien Monticolo, Nyall Dawson

Feature: Feature browser for preview in expression builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This adds a feature browser to the expression builder so one can browse features to see the result of the expression |image65|

A new widget is added: ``QgsFeaturePickerWidget``. For the moment, it's a simple combobox (but inherits widget so we can add a map picker button later on). It behaves the same way than the one in the relation reference widget (an editable combobox).

It relies on the same base model (``QgsFeatureFilterModel``). A new abstract class ``QgsFeaturePickerModelBase`` regroups the logic of the, and the new model is called ``QgsFeaturePickerModel``. Basically the ``QgsFeaturePickerModel`` used the feature id to identify the features while ``QgsFeatureFilterModel`` use a list of attributes (the foreign keys of a relation). It declutters a bit the former model which was quite...cluttered.

As a side note, I tried to use templates for ``QgsFeaturePickerModelBase``, but since templates cannot be mixed with Q\_OBJECT, the alternatives sounded like the code would be less readable.

Tests have been added.

Sponsored by the **QGIS Swiss User Group**!

This feature was developed by `Denis Rouzaud <https://api.github.com/users/3nids>`__

Feature: Ability to remove custom functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a remove button to the Functions Editor tab in the Expression builder dialog to allow the removal of user functions from QGIS without needing to navigate to the user profile directory.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Add ability to edit, import and export user expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new button is added that allows editing of saved expressions. It is only active when a user expression is selected in the expressions tree. When pressed, it opens a window that allows the currently selected user expression to be edited. Changing the label of the expression makes a copy of the currently existing one. `Demo <https://imgur.com/w3UEOoR>`__

**Import/Export**

A new button with a menu is added, that allows the import/export of user expressions to/from a JSON file. Clicking on either of the menu entries opens a file selector dialog for the expressions JSON file source/destination. In the case of label conflicts, an additional dialog asks how to proceed - either to overwrite or to skip the current expression. `Import/Export Demo <https://imgur.com/0eiaFfu>`__

This feature was developed by `Ivan Ivanov <https://api.github.com/users/suricactus>`__

Digitising
----------

Feature: Dedicated avoid geometry intersection/overlap mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This version of QGIS comes with a new dedicated avoid geometry intersection/overlap mode setting when digitizing features.

| The three available modes are:

| 

Allow intersections/overlaps

| 

Avoid intersections/overlaps on active layer

| 

Avoid intersections/overlaps on user-defined layers list.

| 

The third mode's layers list is setup by the user via the advanced snapping configuration widgets.

|image66|

This feature was funded by `OpenGIS.ch <http://www.opengis.ch/>`__

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

Feature: New snapping modes: Centroid and middle of a segment (midpoint)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature is aimed at improving `snapping modes in QGIS <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/107>`__ by getting closer to the experience of CAD tools.

It adds two new modes. Snapping on the center of a geometry (centroid) and the middle of a segment.

To allow the selection of these new modes, several snapping modes can be selected at the same time.

|image67|

The order of preference for snapping is as follows: - Vertex, Intersection - Middle - Centroid - Edge - Area

|image68|

Sponsored by: Qwat group / Ville de Lausanne ( @ponceta @dsavary ) / Oslandia and some spare time

This feature was developed by `lbartoletti <https://api.github.com/users/lbartoletti>`__

Feature: Snapping to the currently digitized feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Snapping can now also supports snapping to the feature currently being digitised. This option is enabled/disabled a new button in the snapping toolbar.

This enables some really nice CAD-like editing abilities, such as closing features at a 90° angle or precisely aligning segments inside a feature. It's very efficient once one is accustomed to using the alt+a shortcut to lock the angle.

|image69|

This feature was funded by Kanton Solothurn and Land Vorarlberg

This feature was developed by `Olivier Dalang <https://api.github.com/users/olivierdalang>`__

Feature: Tracing now supports curved geometries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tracing tool now creates curved geometries when working on a layer that supports curved geometries.

|image70|

The support is still experimental, so this feature must be enabled in the digitizing options.

This feature was funded by ecoptima and Planteam

This feature was developed by `Olivier Dalang (OPENGIS.ch) <https://api.github.com/users/olivierdalang>`__

Forms and Widgets
-----------------

Feature: Allow editing of links in file widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a form, links can now be edited in the file widget (when the widget is not readonly).

|image71|

Sponsored by the QGIS Swiss user group

This feature was developed by `Denis Rouzaud <https://api.github.com/users/3nids>`__

Feature: Expression controlled labels (aliases)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new feature allows form labels (aliases) to be evaluated in the form context.

|image72|

|image73|

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Add description to value relation widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds an option for adding a description to each value in a value relation widget. The description will show up as tooltip

Please excuse the different languages in the demo video.

|image74|

This feature was developed by `Matthias Kuhn <https://api.github.com/users/m-kuhn>`__

Feature: New database table name widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new widget was added to QGIS to select a new table from an existing DB connection:

|image75|

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

Feature: Get current parent form values in child forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds the option of using current values from the "parent" form in filter expressions (for now only in value-relation widgets: to be used in drill-down filters).

A new "parentForm" scope was added as well as a new set of functions and variables to access the parent from within an embedded child form. The new functions and variables were modelled on the existing "current\_value", "current\_feature" etc.

The new functions and variables are also available when the parent form is opened from a new (unsaved, unbuffered) feature, making it easier to create drill-down filters based on the parent's values when adding children from an unsaved parent form.

Example
~~~~~~~

|image76|

New functions and variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image77| |image78| |image79|

Funded by: **ARPA Piemonte**

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Relation widget: add checkbox to hide save child edits button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is very useful for embedded forms.

Funded by: **ARPA Piemonte**

|image80|

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Relation widget force suppress popup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds an option to the relation widget configuration to suppress form popup open when new features are added in an embedded form context.

This option overrides the form-level option (that might still be the desired behavior when the form is used as a standalone form).

|image81|

Note: the final label is **Force hide form on add feature**

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Layer Legend
------------

Feature: Added move to bottom in layertreeview context menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Moving around layers on big projects was made easier with *Move to top* but one still had to manually move basemaps to the bottom of the layer list, a cumbersome task in big layer trees. This feature adds a *Move to bottom* option to the layer tree context menu that works in the same way as Move to top.

This feature was developed by `uclaros <https://api.github.com/users/uclaros>`__

Feature: Make Add Group button act as Group Selected if selected layers >= 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When there is more than one layer selected and the user presses the *Add Group* button, create a new group and put the selected layers in it too! |image82|

This feature was developed by `uclaros <https://api.github.com/users/uclaros>`__

Feature: Allow renaming of the current map theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This adds the option of renaming a map theme from the map theme drop-down menu.

|image83|

This feature was developed by `Harrissou Sant-anna <https://api.github.com/users/DelazJ>`__

Feature: Turn on/off ALL selected layers with "Space" button
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Toggles the visibility of the currently selected layers or groups using the space button: |image84|

This feature was developed by `Ivan Ivanov <https://github.com/suricactus>`__

Analysis Tools
--------------

Feature: Network logger - more functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds some more useful tools to the network logger:

-  Copy URL
-  Copy request as JSON
-  Save log to file (after a big warning to users that the log may contain sensitive information and should be treated as confidential)

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Inbuilt network logging tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tool, which is available from the new F12 "dev tools" panel, is a native port of @rduivenvoorde's network logger plugin.

It shows a list of ongoing and completed network requests, along with a whole load of useful detail like request and reply status, headers, errors, SSL configuration errors, timeouts, cache status, etc.

Also has loads of polish and useful capabilities, such as the ability to filter requests by URL substrings and status, and you can right-click requests to open the URL in a browser or copy them as a cURL command.

Why do we want this as a native tool instead of a plugin? Well:

-  It's extremely useful, so is nice to have available out-of-the-box
-  By moving it to c++, we can startup the logging process much earlier than a plugin gets the opportunity to. This allows the log to include additional information, such as requests fired off by other plugins which occur before the network logger plugin has been loaded (also other in-built requests, e.g. news feed)
-  Performance has been an ongoing struggle with the Python plugin. While this is about as close as a 1:1 port as you can get, the performance issues have all been magically solved. The classes have some very intensive list operations, which is likely the cause of the poor performance under Python.

|image85|

This feature was funded by `Meteorological Service of Canada <https://weather.gc.ca>`__

This feature was developed by `Nyall Dawson (for Kartoza) <https://api.github.com/users/nyalldawson>`__

Processing
----------

Feature: Collection of random raster generation algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this feature we added a large collection of random number raster generation algorithms. The algorithms are capable of outputting random rasters following specific random number distributions. The following distributions are available:

#. Create random raster layer (binomial distribution)
#. Create random raster layer (exponential distribution)
#. Create random raster layer (gamma distribution)
#. Create random raster layer (negative binomial distribution)
#. Create random raster layer (normal distribution)
#. Create random raster layer (poisson distribution)
#. Create random raster layer (uniform distribution)

|image86|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

Feature: Vector tile layer - part 8 (writer in Processing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature adds Processing integration for vector tile writing. It is just a wrapper around the existing QgsVectorTileWriter class.

New algorithms in the Processing toolbox:

|image87|

Algorithm's parameters for XYZ:

|image88|

Algorithm's parameters for MBTiles:

|image89|

List of input layers:

|image90|

Input layer details:

|image91|

This feature was funded by `QGIS Community <https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/>`__

This feature was developed by `Lutra Consulting (Martin Dobias) <https://www.lutraconsulting.co.uk/>`__

Feature: New modeler algorithm for creating conditional branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm allows users to setup multiple conditions (via qgis expressions), which cause their corresponding branch of the model to be run or skipped depending on the result of the expression evaluation.

|image92|

This feature was funded by Andreas Neumann

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow reordering model inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of forcing a quasi-random ordering of inputs for models, this feature exposes a new "Reorder Model Inputs" option in the model designer which allows users control over the exact order of inputs to show users for their model.

No more illogical ordering like showing a field choice before the layer choice it's based on!

Sponsored by NaturalGIS

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Defer model validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of forcing all child algorithms to be immediately valid and have all parameters correctly filled, this feature defers model validation until run time or when a new "Validate model" action is triggered.

A common frustration with the QGIS model designer is that it constantly forces models to be valid, even work-in-progress models. This means it’s impossible to add a component to a model and only partially populate its settings — you have to fill in everything upfront. If you realise mid way through this that you need to make a change somewhere else in your model, it’s impossible to do without canceling and losing all the settings you’ve already configured.

This change sees the model validation deferred until run time. Models can be temporarily invalid (e.g. having algorithm components which are only partially configured). The missing required values can now be filled at a later stage, without losing any existing settings. If a non-valid model is run, the user gets a descriptive warning informing them of the changes they need to make in order to finish configuration of the model.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Added support for different raster data types in Create constant raster layer algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this feature we added a new advanced **OUTPUT\_TYPE** parameter for the *Create constant raster layer* algorithm. Via this parameter, you can now specify an output data type for your constant raster layers.

-  Byte
-  Integer16
-  Unsigned Integer16
-  Integer32
-  Unsigned Integer32
-  Float32
-  Float64

|image93|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

Feature: Added Round raster algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this new processing algorithm we enable QGIS to **round Raster values**.

The main functionality of the algorithm is either standard up/nearest/down-rounding of floating point cell values or rounding to powers of a user specified base *n*. The algorithm can be used with rasters of all types (even byte/integer rasters when rounding to powers of n) and outputs the same raster data type. A standard floating point rounding of an integer raster will copy it and raise a warning.

The example shows an output raster rounded to multiples of 10

|image94|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

Feature: Allow copying/cut/paste of model components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature allows users to copy and paste model components, both within the same model and between different models

|image95|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow appending processing results to existing layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When appending results, users are given a field mapping panel choice to allow them to manually set how fields are mapped to the destination layer's fields:

|image96|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow creation of group boxes in models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds the following functions to the model designer:

-  The ability to customise the color of individual comments in a model
-  Allow creation of "Group Boxes" in models, which are a visual indicator of logically linked model components (e.g. 'Data Preparation Steps', 'NDVI Calculation Steps', ... etc). Users can customise the color and title for group boxes.
-  Allow navigation direct to group boxes from the View menu, aiding navigation of complex models.

|image97|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Processing: show input and output values for children after running model through designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A picture explains this best! After running the algorithm through the designer, you now see the values calculated for the inputs and outputs for each child algorithm:

|image98|

This is very useful for debugging models -- you can see a much clearer visual picture of the flow of values through the model.

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add "Save Log to File" algorithm for models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm saves the contents of the execution log (right up to the point in the model at which the 'save log' algorithm executes) to a file.

It can be used to automatically store the debugging log when running models for later reference and transparency.

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow running algorithms directly on database (and other non-disk) sources without loading into projects first
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This change allows users to directly browse to non disk-based layer sources for any processing feature source inputs. It allows these inputs to be taken direct from postgres, sql server, oracle, wfs, afs, etc layers directly without having to first load them into a project!

We take full advantage of the QGIS browser to enable this:

|image99|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Expose per-feature-source advanced options for processing inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature exposes per-feature-source advanced options, such as:

-  The ability to limit the number of features read from the source. (Useful in model development, you can easily test run models using a small subset of an input layer)
-  The ability to override on a per-input basis the global processing option for how to handle invalid geometries. Now you can safely leave the default processing setting at the conservative "Stop algorithm execution when a geometry is invalid" setting while easily temporarily overriding this for one particular input!

|image100|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Enable snapping to grid for models in designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update implements two "snapping" features in the Processing model designer:

#. Users can enable a new "Enable Snapping" option from the view menu, which will cause all component moving or resizing operations to automatically snap to grids

#. After selecting some components, users can select Edit -> Snap Selected Components to Grid to manually snap just those selected components.

Additionally, I've added a helpful "select all" action for quickly selecting all components in a model.

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add "filter by geometry type" and "filter by layer type" algorithms to processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update adds two new algorithms to processing:

-  "Filter by geometry type": This algorithm filters features by their geometry type. Incoming features will be directed to different outputs based on whether they have a point, line or polygon geometry. It allows for model creation which responds to different input layer geometry types by applying different logic depending on the input geometry type.

-  "Filter by layer type": This algorithm allows conditional model branching based on an input layer type. For instance, it allows a model to adapt to the actual layer type of a generic "map layer" parameter input, and decide which branch of the model to run as a result.

It also adds in the required API to allow algorithms to "prune" model branches based on their calculated results. For example, a model which returns the new *FlagPruneModelBranchesBasedOnAlgorithmResults* flag will cause any remaining parts of the model which are dependent on the outputs of that algorithm to be entirely skipped IF the algorithm does not return that particular output. (This is a prerequisite component for a future generic "conditional branching by expression" algorithm, and also used by "filter by layer type" to control the model flow based on the input layer type)

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: "Remove Null Geometries" algorithm can also remove EMPTY geometries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Empty geometries do not contain coordinates. Thus, like *null* geometries, empty geometries are not spatial data in a strict sense. To make it easier for users to clean a vector layer, the *Remove Null Gometries* algorithm now has an "**Also remove empty geometries**" option.

|image101|

This feature was funded by `SwissTierras Colombia <https://swisstierrascolombia.com/>`__

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Feature: Add multi-selection handling to model designer, interactive resizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds:

-  The ability to select multiple items at once in the model designer
-  The ability to resize individual or multiple items
-  The ability to delete multiple selected items
-  Improved model designer "tool" interaction, following the layout designer approach (e.g. alt + space = zoom drag mode, and selection tools follow their counterparts in layouts so shift+selection adds to selection, ctrl+selection removes, etc)
-  Selected items can be moved by the cursor keys

Refs NRCan Contract#3000707093

Here's how it looks in action (with a particular ugly looking test model I use!)

|image102|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add undo/redo support to model designer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Makes QGIS more forgiving for users!

Refs NRCan Contract#3000707093

Works just like you'd expect:

|image103|

Note that we save the whole model definition in the undo stack, not just the affected component changes.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Remember parameter values between model designer runs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When designing a model, users typically will need to run the model many times as they tweak its structure.

This change causes the parameters used when running the model from the designer to be remembered and saved into the model, so that each time you run the model from the designer you don't have to re-set all the input parameter values to the desired test ones.

Makes iterative model design SO much easier!

Sponsored by Alta Ehf

Also includes a partial port of the model designer dialog from Python to c++, because c++ >> Python.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Comments in Processing Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This allows users to create comments attached to model components (inputs, algorithms or outputs). Comments are shown linked to the associated component, and can be freely moved around the model.

|image104|

Funded by Fisel + König

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: New standalone console tool for running processing algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new qgis\_process tool allows users to run processing algorithms (both built-in, and those provided by plugins) directly from the console.

Running:

-  ``qgis_process list`` will output a complete list of all available algorithms, grouped by provider.
-  ``qgis_process plugins`` lists available and activated plugins which advertise the hasProcessingProvider metadata option (only these plugins are loaded by the tool)
-  ``qgis_process help algid`` outputs the help and input descriptions for the specified algorithm, e.g. ``qgis_process help native:centroids``

``qgis_process run``: runs an algorithm. Parameters are specified by a ``--param=value`` syntax. E.g.

::

    qgis_process run native:centroids --INPUT="my_shapefile.shp" --OUTPUT="centroids.kml"

or

::

    qgis_process run native:buffer --INPUT=/home/me/my.shp --DISTANCE=20 --OUTPUT=/home/me/buffered.shp

While running an algorithm a text-based feedback bar is shown, and the operation can be cancelled via CTRL+C

Sponsored by the Swedish User Group

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: New parameter type for datetime (or date, or time) values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a new parameter type QgsProcessingParameterDateTime for handling date/datetime/time values.

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add algorithms for raising warnings and exceptions from models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These algorithms raise either a custom warning in the processing log OR raise an exception which causes the model execution to terminate.

An optional condition expression can be specified to control whether or not the warning/exception is raised, allowing logic like "if the output layer from another algorithm contains more than 10 features, then abort the model execution".

Sponsored by Fisel + König

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add Fill NoData cells algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the new QGIS version we introduce a new processing algorithm for filling NoData cells in a raster dataset with a constant numerical input.

The algorithm scans an input raster dataset for NoData cells and fills them with the user defined fill value. Doing so, the algorithm respects the data type of the input raster so that e.g. floating point numbers will be dealt with appropriately for an integer raster. The resulting dataset will not contain any NoData cells.

|image105|

This feature was developed by `Clemens Raffler <https://api.github.com/users/root676>`__

Feature: Various fixes for Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Finalize work on range parameters support in GRASS algorithms;
-  Fix broken r.series algorithm
-  Minor fixes to r.rescale and r.rescale.eq
-  Fix for rasterize tool
-  GRASS GIS tests cleanup

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Show "template layer" field constraints in the "Refactor Fields" algorithm interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you are migrating data, it is important to be aware of constraints on target (a.k.a. template) layers.

The "Refactor Fields" algorithm now highlights constraints, and even lets you know more about them via tool-tips.

|image106|

This feature was funded by `SwissTierras Colombia <https://swisstierrascolombia.com/>`__

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Feature: New convert to curves algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We added a new algorithm to convert segmentized geometries to curved geometries.

The algorithm considers successive points to represent a curve if they are evenly spaced and within a tolerance.

|image107|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Application and Project Options
-------------------------------

Feature: Add @layers, @layer\_ids project scope variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add @layers, @layer\_ids project scope variables which contain lists of map layers and map layers ids for all layers from the current project

This mimics the existing @map\_layers, @map\_layer\_ids, but unlike the @map variants these return ALL project layers, not just those associated with the current context's map settings.

Sponsored by SLYR

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Data Providers
--------------

Feature: Allow adding attributes in the New Scratch Layer dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows the user to add attributes directly in the New Scratch Layer dialog making it more consistent with other dialogs like New Shapefile/Geopackage. |image108|

It is still possible to create a scratch layer without any attributes by not adding any fields to the list.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Allow creating geometryless DBF tables from the New Shapefile dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allow creating "plain" DBF files without associated geometries from the New Shapefile dialog.

|image109|

Creating DBF tables can be useful in some cases and having to use third-party tools for this instead of doing it from within QGIS is inconvenient. This also makes the New Shapefile dialog more consistent with the New Geopackage dialog, which already allows "geometryless" tables to be created.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Allow filtering WM(T)S list in source dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add ability to filter between lists of WMS or WMTS from the source dialog

WMS |image110|

WMTS |image111|

Sponsored by the QGIS Swiss user group

This feature was developed by `Denis Rouzaud <https://api.github.com/users/3nids>`__

Feature: Add vector tiles to Datasource manager dialog and Layers menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a new tab to the Datasource Manager dialog allowing the user to manage/add vector tile connections, including import/export. Also adds a corresponding entry to Layers menu.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Import/export for ArcGIS Map and FeatureServer connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add missed import/export functionality for ArcGIS MapServer and FeatureServer connections.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Add XYZ tiles to Datasource manager dialog and Layers menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds new tab to Datasource Manager dialog allowing to manage/add XYZ connections. Also add corresponding entry to Layers menu.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Spatialite transaction group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transactions implementation for the native SpatiaLite provider.

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Allowing saving outputs direct to more database formats (and other nice stuff)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update allows users to save processing vector outputs directly to more database formats.

Previously outputs could only be written directly to postgres databases. With this change, this functionality has been made more flexible and now supports direct writing to any database provider which implements the connections API (currently postgres, geopackage, spatialite and sql server)

Ultimately this exposes the new ability to directly save outputs to SQL Server or Spatialite databases (alongside the previous GPKG+Postgres options which already existed)

(As soon as oracle, db2, ... have the connections API implemented we'll instantly gain direct write support for those too!)

We do this via a nice inline version of the new "new database table name" widget.

|image112|

Other nice stuff includes:

-  You can now drag and drop file or folders from explorer or the qgis browser to output parameters in order to easily overwrite these files (or save to the folder), matching the behavior possible with inputs
-  You can actually write scripts which output direct to ANY qgis data provider (including oracle and db2)... it's just that these don't get exposed in the UI because they don't yet support the connections API

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Add dedicated parameter type for database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows selection from the registered database connections for a specific database provider type (the provider must implement the connections API).

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: PG: expose foreign tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Expose foreign tables to the browser and data source select dialog.

This feature was developed by `Alessandro Pasotti <https://api.github.com/users/elpaso>`__

Feature: PG raster expose set filter to app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This should be the final change to the PG raster data provider and exposes the set filter options:

-  Filter can be set in the data source dialog (as for vector layers)
-  Filter can be set from the legend tree's context menu (as for vector layers)
-  The renderer, the extent and the min/max stats are also updated when the filter changes
-  New tests for the new behavior

|image113|

This feature was funded by `ARPA Piemonte <http://www.arpa.piemonte.it/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Postgres: save features into tables with generated fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allow updating/inserting features in PostgreSQL tables with generated fields. GENERATED columns is a feature introduced by PostgreSQL 12, which allows column values to be generated from other columns in the same table; this replaces the creation of triggers to, for instance, automatically populate and keep up-to-date a column of centroids or areas for the polygons in the main geometry column.

This feature was developed by `José de Paula Rodrigues N. Assis <https://api.github.com/users/espinafre>`__

Feature: Date and DateTime field types support added to Spatialite and Delimited Text providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Spatialite and Delimited Text providers now support Date and DateTime field types.

This feature was developed by `Mathieu Pellerin <https://api.github.com/users/nirvn>`__

QGIS Server
-----------

Feature: Add QGIS\_SERVER\_IGNORE\_BAD\_LAYERS config option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows the overriding of the default behavior in the case of bad layers (which is to invalidate the whole project).

When set to TRUE, bad layers are skipped and the remainder of the project becomes available.

This feature was funded by `Geoinformatikbüro Dassau GmbH <https://www.gbd-consult.de/home.html>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it>`__

Feature: Server project settings, add 'expanded' attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the 'visible' and 'mutuallyExclusive' attribute, this update adds 'expanded' to the GetProjectSettings response of the server. The update allows a web client to see which layer tree elements are expanded / collapsed and to then present them the same way in the web map layer list.

This feature was developed by `mhugent <https://api.github.com/users/mhugent>`__

Feature: Add DXF server export params NO\_MTEXT and FORCE\_2D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS server now supports the new parameters ``NO_MTEXT`` and ``FORCE_2D`` to control text and line symbology for generated DXF files.

Adds missing parameters to GetDxf request.

This feature was developed by `Matthias Kuhn <https://api.github.com/users/m-kuhn>`__

Feature: WMS project validator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS Server validator has been reviewed. This tool is useful when you want to publish a QGIS project using the WMS protocol.

For programmers, the validator is also now callable from PyQGIS, so plugins can now use it too.

This feature was funded by `3Liz <https://www.3liz.com>`__

This feature was developed by `Etienne Trimaille <https://github.com/Gustry>`__

Feature: Webp
~~~~~~~~~~~~~

    WebP is a modern image format that provides superior lossless and lossy compression for images on the web. WebP creates smaller, richer images that make the web faster.

    WebP lossless images are 26% smaller in size compared to PNGs. WebP lossy images are 25-34% smaller than comparable JPEG images at equivalent SSIM quality index.

Source: https://developers.google.com/speed/webp

With webp QGIS server now supports a format that provides smaller file sizes for the same quality and even provides transparency.

This feature was funded by `OPENGIS.ch <https://www.opengis.ch>`__

This feature was developed by `Matthias Kuhn (OPENGIS.ch) <https://www.opengis.ch>`__

Plugins
-------

Feature: Allow plugins to register custom "Project Open" handlers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These allow plugins to extend the "Open Project" dialog by adding in support for new file filters, which appear in the formats drop down list alongside the existing "QGS Projects" entry.

Custom project open handlers then get first chance at loading project files.

This allows plugins to extend QGIS support by adding integrated support for opening projects from non QGS/QGZ formats, e.g. allowing users to open ArcGIS MXD documents or MapInfo WOR Workspaces direct from the project open dialog.

These non-native projects are also added to the recent projects list and welcome screen, giving them a truly first-class experience within QGIS.

Sponsored by SLYR

|image114|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Allow users to install stable or experimental plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update improves the plugin manager by allowing users to choose between installing the stable or the experimental version of a plugin.

This makes it possible to have pre-releases of plugins in the repository for power-users to test, while still allowing them to switch back easily to stable versions, without having to untick the global *enable experimental* option.

This change makes no difference for users who haven't checked the *enable experimental* option.

|image115|

This feature was funded by `Swiss QGIS User Group <https://www.qgis.ch/>`__

This feature was developed by `Olivier Dalang <https://api.github.com/users/olivierdalang>`__

Programmability
---------------

Feature: Support for adding dock widgets as tabs: addTabifyDockWidget()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dock widgets are great for displaying complex interfaces that extend QGIS functionality.

Now, both core and plugin devs have the option to tabify their dock widgets on top of existing ones. They can even choose on top of which dock widget they want their own dock widget appear.

|image116|

This feature was funded by `SwissTierras Colombia <https://swisstierrascolombia.com/>`__

This feature was developed by `Germán Carrillo <https://github.com/gacarrillor>`__

Feature: Port output parameter wrappers to new API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ports the output parameter wrappers (sinks, vector, raster, file and folder destinations) to the new c++ API for dialog and modeler.

This allows a range of new possibilities, including:

-  Models with static outputs for child algorithms, e.g. always saving a child algorithm's output to a geopackage or postgres layer
-  Models with expression based output values for child algorithms, e.g. generating an automatic file name based on today's date and saving outputs to that file

|image117|

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Port last remaining input parameters to new API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update ports the Raster Band input parameter and Multi Layer input parameter to the new C++ API.

Benefits include:

-  Expression based band/layer lists in models
-  Inline (non-blocking) lists for multi selection parameters (fields, bands, layer lists, enums)
-  Rearrangement of inputs for multi-layer parameters in models, to set specific layer orders

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Port Feature Source, Raster, Vector and Mesh Layer parameters to new API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's now possible to use expression-based layer sources in processing models.

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Vector tile layer - part 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the initial work on vector tile layer support.

|image118| (The red lines are not rendering artifacts, they are drawn intentionally to show tile borders.)

Summary
~~~~~~~

So far this only includes changes to the qgis\_core library.

Main additions to the public API:

-  QgsVectorTileLayer - the main map layer class
-  QgsVectorTileRenderer - base class for renderer class implementations for vector tiles
-  QgsVectorTileBasicRenderer - default renderer implementation

New private classes (may be added to public API if needed):

-  QgsVectorTileLoader - handles fetching of tiles from network / mbtiles
-  QgsVectorTileMVTDecoder - handles decoding of raw tile data to features
-  QgsVectorTileLayerRenderer - takes care of overall rendering (fetch + decode + draw)
-  QgsVectorTileUtils - various useful functions

Some new classes that may be shared by vector and raster tiles:

-  QgsTileXYZ - position of a tile in tile matrix set (zoom level, column, row)
-  QgsTileRange - rectangular selection in a tile matrix (start/end column and row)
-  QgsTileMatrix - description of a tile matrix (map extent, zoom level, scale, number of rows/columns)

(also QgsTileMatrixSet to be added later when we support other tile matrix sets than just GoogleCRS84Quad)

Testing
~~~~~~~

You can load a vector tile layer from Python console, e.g.::

 ds = QgsDataSourceUri() ds.setParam("type","xyz")
 ds.setParam("url", "https://api.maptiler.com/tiles/v3/{z}/{x}/{y}.pbf?key=YOUR_FREE_API_KEY") 
 uri = bytes(ds.encodedUri()).decode('utf-8')
 vtl = QgsVectorTileLayer(uri, "Vector Tiles Test")
 QgsProject.instance().addMapLayer(vtl)


It is also possible to load vector tiles from a local MBTiles file - for "type" use "mbtiles" and for "url" use a local path (e.g. "/home/martin/x.mbtiles").

There is currently no support for labeling.

Thanks
~~~~~~

Huge thanks to all funders who have contributed to the crowdfunding and made this possible - https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors

This feature was funded by `QGIS Community <https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/>`__

This feature was developed by `Lutra Consulting (Martin Dobias) <https://www.lutraconsulting.co.uk>`__

Feature: Port processing extent parameter to new api, many other improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This update ultimately ports the extent parameter to the new c++ api, but along the way it:

-  Refactors the existing gui widget "QgsExtentGroupBox" to move the guts out to "QgsExtentWidget" (allowing it to be used in places where a group box is inappropriate/looks bad). It also adds a new "condensed" mode for the widget, because the default appearance is very space heavy.
-  The new parameter widget utilises this common QgsExtentWidget, so that we remove all the duplicate code which was previously used by the old python wrapper
-  Allows drag and drop of project map layers from the layer tree to a QgsExtentWidget to auto-set the extent to match
-  Allows QgsExtentWidget to be optionally nullable
-  Allows QgsGeometry values to be set for extent parameter values. This is done to aid use of extent parameters with the "precalculated value" mode in models -- you can now use all the expression geometry functions to calculate a geometry and the bounding box of this is used for the parameter value in the child algorithm

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Interface and API for unified development/debugging tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds interface hooks to allow plugins (and c++) to register "development/debugging" tools

These tools appear in a new Development/Debugging Tools dock, and provide a unified handling and place for these tools in the UI.

The intention here is that specialised development/debugging tools will be moved to this common interface, e.g.

-  Network logger
-  First aid style Python local variables inspector
-  Startup time debugging tools
-  Layer load and rendering time debugging tools ... ?

Here's an example demo showing a "Python locals" dev tool:

|image119|

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Feature: Data type support for QgsProcessingParameterMapLayer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allow the definition of accepted layer types for ``QgsProcessingParameterMapLayer``. This is useful when an algorithm can work with different layer types (for example, points and rasters) and avoids duplication of the same algorithm with different inputs.

This is an API improvement and is not visible for the vast majority of users.

This feature was developed by `Alexander Bruy <https://api.github.com/users/alexbruy>`__

Feature: Add processing parameter types for database schema and table name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Replaces the previous ad-hoc Python postgis widget wrappers with proper first class c++ dedicated parameters for schemas and tables, with wrappers built off the core connections api.

Refs NRCan Contract#3000707093

This feature was developed by `Nyall Dawson <https://api.github.com/users/nyalldawson>`__

Notable Fixes
-------------

Feature: Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                   | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                                | 3.10 backport commit (GitHub)                             |
+=============================================================================================================+==========================================================+====================================================================================================================+===========================================================+
| Getfeatureinfo does not show relation reference items for QGIS Server                                       | `#36549 <https://github.com/qgis/QGIS/issues/36549>`__   | Turned out to be a feature request                                                                                 | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| OGR provider QgsOgrProvider::changeAttributeValues returns true on errors                                   | `#36583 <https://github.com/qgis/QGIS/issues/36583>`__   | `PR #36620 <https://github.com/qgis/QGIS/pull/36620>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GPKG transaction groups are stored with empty second pair of the key                                        | `#36525 <https://github.com/qgis/QGIS/issues/36525>`__   | `PR #36660 <https://github.com/qgis/QGIS/pull/36660>`__                                                            | `PR #37157 <https://github.com/qgis/QGIS/pull/37157>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Symbology using relations does not propagate in QGIS Server                                                 | `#36614 <https://github.com/qgis/QGIS/issues/36614>`__   | cannot reproduce                                                                                                   | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| "Loading PostGIS raster with QGIS 3.12.3 crashes"                                                           | `#36689 <https://github.com/qgis/QGIS/issues/36689>`__   | `PR #36702 <https://github.com/qgis/QGIS/pull/36702>`__                                                            | not relevant                                              |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GetFeatureInfo Fid value is different between application/json and application/vnd.ogc.gml                  | `#36262 <https://github.com/qgis/QGIS/issues/36262>`__   | `PR #36733 <https://github.com/qgis/QGIS/pull/36733>`__                                                            | `PR #37158 <https://github.com/qgis/QGIS/pull/37158>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GPKG (and spatialite) DB-level unique constraints are not supported by OGR (and spatialite) provider        | `#36468 <https://github.com/qgis/QGIS/issues/36468>`__   | `PR #36802 <https://github.com/qgis/QGIS/pull/36802>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| no value in the attribute form if value missing in the value map                                            | `#32756 <https://github.com/qgis/QGIS/issues/32756>`__   | `PR #36804 <https://github.com/qgis/QGIS/pull/36804>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| DB Manager does not show anymore query results                                                              | `#36205 <https://github.com/qgis/QGIS/issues/36205>`__   | `PR #36823 <https://github.com/qgis/QGIS/pull/36823>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| DB Manager does not show anymore query results                                                              | `#36205 <https://github.com/qgis/QGIS/issues/36205>`__   | `PR #36831 <https://github.com/qgis/QGIS/pull/36831>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GPKG browser drag&drop not working                                                                          | unreported                                               | `PR #36972 <https://github.com/qgis/QGIS/pull/36972>`__                                                            | `PR #37159 <https://github.com/qgis/QGIS/pull/37159>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| it is not possible to save a project in the geopackage                                                      | `#36832 <https://github.com/qgis/QGIS/issues/36832>`__   | `PR #36980 <https://github.com/qgis/QGIS/pull/36980>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| It is possible to store text into a numeric field, while it shouldn't be, using the Date/Time edit widget   | `#36715 <https://github.com/qgis/QGIS/issues/36715>`__   | `#36715 <https://github.com/qgis/QGIS/issues/36715>`__                                                             | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Feature creation very slow when using joins                                                                 | `#36167 <https://github.com/qgis/QGIS/issues/36167>`__   | `PR #36866 <https://github.com/qgis/QGIS/pull/36866>`__, `PR #36963 <https://github.com/qgis/QGIS/pull/36963>`__   | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS Server: WFS Request does not use SrsName on the geometry                                               | `#36398 <https://github.com/qgis/QGIS/issues/36398>`__   | `PR #36926 <https://github.com/qgis/QGIS/pull/36926>`__, `PR #37071 <https://github.com/qgis/QGIS/pull/37071>`__   | not critical                                              |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Unable to delete a stored geopackage connection from browser                                                | `#36930 <https://github.com/qgis/QGIS/issues/36930>`__   | `PR #36937 <https://github.com/qgis/QGIS/pull/36937>`__                                                            | `PR #37166 <https://github.com/qgis/QGIS/pull/37166>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Constraints: unique constraint not correctly evaluated when 0                                               | `#36962 <https://github.com/qgis/QGIS/issues/36962>`__   | `PR #36967 <https://github.com/qgis/QGIS/pull/36967>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| PyQgis: OriginJoin fields arte not present into QgsLayerVector QgsFields container for GeoPackage layers    | `#36977 <https://github.com/qgis/QGIS/issues/36977>`__   | not reproducible                                                                                                   | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Joined tables cannot be edited even if the "editable join layer" option is checked                          | `#36934 <https://github.com/qgis/QGIS/issues/36934>`__   | not reproducible/in progress                                                                                       | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Removal of unused 'allowMethod' from qgisservice/qgisserverapi                                              | `#36163 <https://github.com/qgis/QGIS/issues/36163>`__   | `PR #36997 <https://github.com/qgis/QGIS/pull/36997>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Omogenize window title                                                                                      | `#35761 <https://github.com/qgis/QGIS/issues/35761>`__   | `PR #36998 <https://github.com/qgis/QGIS/pull/36998>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Labeling: data-defined alignment grey-out activation issue                                                  | `#37003 <https://github.com/qgis/QGIS/issues/37003>`__   | `PR #37006 <https://github.com/qgis/QGIS/pull/37006>`__                                                            | `PR #37167 <https://github.com/qgis/QGIS/pull/37167>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS reports "no layers" in GeoPackage when geopackage directory is write protected                         | `#36574 <https://github.com/qgis/QGIS/issues/36574>`__   | `PR #37018 <https://github.com/qgis/QGIS/pull/37018>`__                                                            | not critical (UX only)                                    |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Joined tables cannot be edited even if the "editable join layer" option is checked                          | `#36934 <https://github.com/qgis/QGIS/issues/36934>`__   | won't fix                                                                                                          | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Postgis Timestamps from query in DB Manager displayed as \`PyQT5.QTCore.QDateTime(2020, 3, 17               | `#35140 <https://github.com/qgis/QGIS/issues/35140>`__   | `PR #37042 <https://github.com/qgis/QGIS/pull/37042>`__                                                            | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Wrong image preview and image preview size in form                                                          | `#33682 <https://github.com/qgis/QGIS/issues/33682>`__   | `PR #37093 <https://github.com/qgis/QGIS/pull/37093>`__                                                            | `PR #37168 <https://github.com/qgis/QGIS/pull/37168>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| can't change value in vertex editor if "locale" settings use commas as decimal separator                    | `#29682 <https://github.com/qgis/QGIS/issues/29682>`__   | `PR #37135 <https://github.com/qgis/QGIS/pull/37135>`__                                                            | `PR #37169 <https://github.com/qgis/QGIS/pull/37169>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Identifying a WMS layer with format "feature" crashes QGIS                                                  | `#29443 <https://github.com/qgis/QGIS/issues/29443>`__   | `PR #37171 <https://github.com/qgis/QGIS/pull/37171>`__                                                            | `PR #37210 <https://github.com/qgis/QGIS/pull/37210>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Attempting to create a new feature in Spatialite with transaction group and NOT NULL constraint fails       | `#37236 <https://github.com/qgis/QGIS/issues/37236>`__   | won't fix                                                                                                          | N/A                                                       |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Using "Add feature" to create feature and child feature with transaction group causes foreign key error     | `#37222 <https://github.com/qgis/QGIS/issues/37222>`__   | `PR #37249 <https://github.com/qgis/QGIS/pull/37249>`__                                                            | not critical                                              |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Vectorlayer from spatialite missing features and inconsistent feature count                                 | `#29264 <https://github.com/qgis/QGIS/issues/29264>`__   | `PR #37277 <https://github.com/qgis/QGIS/pull/37277>`__                                                            | TODO                                                      |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Alessandro Pasotti <https://www.itopen.it/>`__

Feature: Bug fixes by Loïc Bartoletti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                       | URL issues.qgis.org (if reported)                                                                                | URL Commit (Github)                                       | 3.10 backport commit (GitHub)                             |
+=================================================================+==================================================================================================================+===========================================================+===========================================================+
| Fix error when vector layer has Z                               | `#32016 <https://github.com/qgis/QGIS/issues/32016>`__                                                           | `PR #36553 <https://github.com/qgis/QGIS/pull/36553>`__   | `PR #36595 <https://github.com/qgis/QGIS/pull/36595>`__   |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix rectangle from 3 points                                     | `#35043 <https://github.com/qgis/QGIS/issues/35043>`__, `#35671 <https://github.com/qgis/QGIS/issues/35671>`__   | `PR #36523 <https://github.com/qgis/QGIS/pull/36523>`__   | `PR #36560 <https://github.com/qgis/QGIS/pull/36560>`__   |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Allow to search qmlplugindump in different paths                | N/A                                                                                                              | `PR #36513 <https://github.com/qgis/QGIS/pull/36513>`__   | N/A                                                       |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix the absence of words in the advanced configuration widget   | `PR #35643 <https://github.com/qgis/QGIS/pull/35643>`__\ #issuecomment-610215386                                 | `PR #36511 <https://github.com/qgis/QGIS/pull/36511>`__   | N/A                                                       |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix interpolation on split geometry                             | `PR #36514 <https://github.com/qgis/QGIS/pull/36514>`__                                                          | `#33489 <https://github.com/qgis/QGIS/issues/33489>`__    | N/A                                                       |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Loïc Bartoletti <https://www.oslandia.com/>`__

Feature: Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Bug Title                                                                                    | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                       | 3.10 backport commit (GitHub)                                                                             |
+==============================================================================================+==========================================================+===========================================================================================================+===========================================================================================================+
| Wrong interpretation of EPSG code from a PRJ file in QGIS-dev (proj v7.1.0)                  | `#36111 <https://github.com/qgis/QGIS/issues/36111>`__   | `PROJ PR 2240 <https://github.com/OSGeo/PROJ/pull/2240>`__                                                | N/A: PROJ issue                                                                                           |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS crashes when adding file to geopackage -> layer -> field(BLOB)                          | `#30210 <https://github.com/qgis/QGIS/issues/30210>`__   | `PR #36722 <https://github.com/qgis/QGIS/pull/36722>`__                                                   | `PR #36737 <https://github.com/qgis/QGIS/pull/36737>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Bad error message on WFS connection fail                                                     | `#29866 <https://github.com/qgis/QGIS/issues/29866>`__   | `PR #36717 <https://github.com/qgis/QGIS/pull/36717>`__                                                   | `PR #36735 <https://github.com/qgis/QGIS/pull/36735>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS crashes during map re-rendering after CRS switch                                        | `#29672 <https://github.com/qgis/QGIS/issues/29672>`__   | cannot reproduce                                                                                          | N/A                                                                                                       |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS crashes when "open directory" is selected from the recent projects contextual menu      | `#31630 <https://github.com/qgis/QGIS/issues/31630>`__   | `PR #36738 <https://github.com/qgis/QGIS/pull/36738>`__                                                   | `PR #36755 <https://github.com/qgis/QGIS/pull/36755>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Problem reprojecting rasters in 54019 and 54042 CRSs                                         | `#35512 <https://github.com/qgis/QGIS/issues/35512>`__   | `PROJ PR 2243 <https://github.com/OSGeo/PROJ/pull/2243>`__                                                | N/A: PROJ issue                                                                                           |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| WFS Provider WARNING - Cannot create temporary SpatiaLite cache when using flatpak install   | `#36545 <https://github.com/qgis/QGIS/issues/36545>`__   | `PR #36745 <https://github.com/qgis/QGIS/pull/36745>`__                                                   | N/A                                                                                                       |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| WFS Transaction operation using GetCapabilities URI                                          | `#34307 <https://github.com/qgis/QGIS/issues/34307>`__   | `PR #36746 <https://github.com/qgis/QGIS/pull/36746>`__                                                   | N/A                                                                                                       |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGis 3.10.2 crashes when displaying two PostGIS raster layers                                | `#34456 <https://github.com/qgis/QGIS/issues/34456>`__   | -                                                                                                         | N/A                                                                                                       |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS 3.4.10 crashes - Python                                                                 | `#31304 <https://github.com/qgis/QGIS/issues/31304>`__   | already fixed in master                                                                                   | `PR #36751 <https://github.com/qgis/QGIS/pull/36751>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| WMS provider expects SERVICE=WMTS keyword in uppercase to detect WMTS                        | `#36659 <https://github.com/qgis/QGIS/issues/36659>`__   | `PR #36752 <https://github.com/qgis/QGIS/pull/36752>`__                                                   | `PR #36766 <https://github.com/qgis/QGIS/pull/36766>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| WCS DescribeCoverage response origin always empty                                            | `#36504 <https://github.com/qgis/QGIS/issues/36504>`__   | `PR #36754 <https://github.com/qgis/QGIS/pull/36754>`__                                                   | `PR #36781 <https://github.com/qgis/QGIS/pull/36781>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Extent wrong if layer contains point at 0,0                                                  | `#33823 <https://github.com/qgis/QGIS/issues/33823>`__   | Not a QGIS bug. Fixed in GDAL 3.1                                                                         | N/A                                                                                                       |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Projection not recognised from Mapinfo converstion                                           | `#34471 <https://github.com/qgis/QGIS/issues/34471>`__   | `PR #36758 <https://github.com/qgis/QGIS/pull/36758>`__                                                   | `PR #36783 <https://github.com/qgis/QGIS/pull/36783>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS crashes/freezes when adding a large CSV file as delimited text layer                    | `#36392 <https://github.com/qgis/QGIS/issues/36392>`__   | `PR #36778 <https://github.com/qgis/QGIS/pull/36778>`__                                                   | `PR #36810 <https://github.com/qgis/QGIS/pull/36810>`__                                                   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| QGIS 3.12 unknown CRS or Select Transformation                                               | `#36837 <https://github.com/qgis/QGIS/issues/36837>`__   | `GDAL Commit 68133b8 <https://github.com/OSGeo/gdal/commit/68133b8b6f724a581a5dcb19fbdcd657ddbd6c4c>`__   | `GDAL Commit 6ae7f60 <https://github.com/OSGeo/gdal/commit/6ae7f60a5914a2f16b8b1a94758f10e6621e4aca>`__   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| BIGTIFF error is not obvious in processing log                                               | `#36867 <https://github.com/qgis/QGIS/issues/36867>`__   | `GDAL Commit cfc8e61 <https://github.com/OSGeo/gdal/commit/cfc8e613ad86dd4b00604dd64df239916ccda135>`__   | `GDAL Commit fb88e3c <https://github.com/OSGeo/gdal/commit/fb88e3ca5c8905fbcaab79e96a2bfc1c36f72d08>`__   |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Even Rouault <http://www.spatialys.com/>`__

Feature: Bug fixes by Paul Blottiere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                     | URL issues.qgis.org (if reported)                                                           | URL Commit (Github)                                       | 3.10 backport commit (GitHub)                             |
+===============================================================+=============================================================================================+===========================================================+===========================================================+
| Fix segfault when adding a layer                              | `Mailing list <https://lists.osgeo.org/pipermail/qgis-developer/2020-June/061421.html>`__   | `PR #36910 <https://github.com/qgis/QGIS/pull/36910>`__   | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix signal connection                                         | Unreported issue                                                                            | `PR #35836 <https://github.com/qgis/QGIS/pull/35836>`__   | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Update the API to export a legend in JSON                     | Unreported binding issue                                                                    | `PR #36370 <https://github.com/qgis/QGIS/pull/36370>`__   | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Core dump if vector tile layer (file) becomes unavailable     | `#36821 <https://github.com/qgis/QGIS/issues/36821>`__                                      | cannot reproduce                                          | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Crash on project open when mapcanvas extents = nan            | `#35899 <https://github.com/qgis/QGIS/issues/35899>`__                                      | cannot reproduce                                          | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Using some functions in raster calulator crashes QGIS         | `#35583 <https://github.com/qgis/QGIS/issues/35583>`__                                      | `PR #37273 <https://github.com/qgis/QGIS/pull/37273>`__   | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Auxiliary storage not usable in non editable layer            | `#30376 <https://github.com/qgis/QGIS/issues/30376>`__                                      | Already fixed. Closed.                                    | N/A                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix compilation with GCC 10, Qt/PyQt 5.15.0 and SIP 4.19.23   | `#37072 <https://github.com/qgis/QGIS/issues/37072>`__                                      | `PR #37116 <https://github.com/qgis/QGIS/pull/37116>`__   | `PR #37250 <https://github.com/qgis/QGIS/pull/37250>`__   |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Paul Blottiere <https://hytech-imaging.fr/>`__

Feature: Bug fixes by Julien Cabieces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                               | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                                | 3.10 backport commit (GitHub)                             |
+=========================================================================================================+==========================================================+====================================================================================================================+===========================================================+
| Reproducible crash using QgsMapCanvas.items() with Oracle layers                                        | `#33791 <https://github.com/qgis/QGIS/issues/33791>`__   | `PR #36240 <https://github.com/qgis/QGIS/pull/36240>`__                                                            | `PR #36246 <https://github.com/qgis/QGIS/pull/36246>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Line breaks are ignored in the user expression help panel                                               | `#36191 <https://github.com/qgis/QGIS/issues/36191>`__   | `PR #36249 <https://github.com/qgis/QGIS/pull/36249>`__                                                            | `PR #36387 <https://github.com/qgis/QGIS/pull/36387>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| "Edit user expression" does not allow to rename the user expression                                     | `#36192 <https://github.com/qgis/QGIS/issues/36192>`__   | `PR #36349 <https://github.com/qgis/QGIS/pull/36349>`__                                                            | N/A                                                       |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Cannot change labels of raster symbology classes                                                        | `#36172 <https://github.com/qgis/QGIS/issues/36172>`__   | `PR #36376 <https://github.com/qgis/QGIS/pull/36376>`__                                                            | `PR #36533 <https://github.com/qgis/QGIS/pull/36533>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Crash when layer not available                                                                          | `#33300 <https://github.com/qgis/QGIS/issues/33300>`__   | Cannot reproduce                                                                                                   | N/A                                                       |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Select by expression returns erroneous results with integer field division for shapefiles               | `#35449 <https://github.com/qgis/QGIS/issues/35449>`__   | `PR #2531 <GDAL%20https://github.com/OSGeo/gdal/pull/2531>`__                                                      | N/A                                                       |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Using concat(field1, field2) concatenates 0 instead of empty string ('') if any of the fields is NULL   | `#36112 <https://github.com/qgis/QGIS/issues/36112>`__   | `PR #36521 <https://github.com/qgis/QGIS/pull/36521>`__                                                            | `PR #36529 <https://github.com/qgis/QGIS/pull/36529>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Stuck at Recent Project window when opening blank file in 3.10.3                                        | `#34809 <https://github.com/qgis/QGIS/issues/34809>`__   | Cannot reproduce                                                                                                   | N/A                                                       |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS crashes on getting items of mapCanvas scene if features are identified                             | `#34457 <https://github.com/qgis/QGIS/issues/34457>`__   | `PR #36439 <https://github.com/qgis/QGIS/pull/36439>`__                                                            | `PR #36450 <https://github.com/qgis/QGIS/pull/36450>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| sorting on a column that has a value relation is inconsistent                                           | `#36114 <https://github.com/qgis/QGIS/issues/36114>`__   | `PR #36776 <https://github.com/qgis/QGIS/pull/36776>`__                                                            | `PR #36887 <https://github.com/qgis/QGIS/pull/36887>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Missing points (depending on canvas scale) in virtual layer based on sqlite file                        | `#36054 <https://github.com/qgis/QGIS/issues/36054>`__   | `PR #36792 <https://github.com/qgis/QGIS/pull/36792>`__                                                            | `PR #36718 <https://github.com/qgis/QGIS/pull/36718>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Project is modified as soon as you move cursor on canvas                                                | `#36796 <https://github.com/qgis/QGIS/issues/36796>`__   | `PR #36797 <https://github.com/qgis/QGIS/pull/36797>`__                                                            | `PR #36718 <https://github.com/qgis/QGIS/pull/36718>`__   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Set filter applied to wrong "version" of table when multiple geometry types                             | `#34982 <https://github.com/qgis/QGIS/issues/34982>`__   | `PR #36801 <https://github.com/qgis/QGIS/pull/36801>`__\ `PR #36718 <https://github.com/qgis/QGIS/pull/36718>`__   |                                                           |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Julien Cabieces <https://www.oslandia.com/>`__

Feature: Bug fixes by Bertrand Rix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                                  | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.10 backport commit (GitHub)   |
+============================================================+==========================================================+===========================================================+=================================+
| Vertex tool override global snapping parameters            | `#36229 <https://github.com/qgis/QGIS/issues/36229>`__   | `PR #36231 <https://github.com/qgis/QGIS/pull/36231>`__   | N/A                             |
+------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| QGIS crashes with QgsGeometry method on empty collection   | `#36142 <https://github.com/qgis/QGIS/issues/36142>`__   | `PR #36351 <https://github.com/qgis/QGIS/pull/36351>`__   | N/A                             |
+------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Selective masking: phantom lines on dark background        | `#34650 <https://github.com/qgis/QGIS/issues/34650>`__   | `PR #36697 <https://github.com/qgis/QGIS/pull/36697>`__   | N/A                             |
+------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Selective masking: issue with mask opacity                 | `#34947 <https://github.com/qgis/QGIS/issues/34947>`__   | `PR #36697 <https://github.com/qgis/QGIS/pull/36697>`__   | N/A                             |
+------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Bertrand Rix <https://www.oslandia.com/>`__

Feature: Bug fixes by Sebastien Peillet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                                                                              | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.10 backport commit (GitHub)   |
+========================================================================================================+==========================================================+===========================================================+=================================+
| [Oracle]Error on save geometries because wrong default values #34482                                   | `#34482 <https://github.com/qgis/QGIS/issues/34482>`__   | `PR #36769 <https://github.com/qgis/QGIS/pull/36769>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Invalid query for default value of date column of an oracle layer                                      | `#32401 <https://github.com/qgis/QGIS/issues/32401>`__   | `PR #36769 <https://github.com/qgis/QGIS/pull/36769>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Fields missing in Visibility by expression for a group in drag/drop form                               | `#35196 <https://github.com/qgis/QGIS/issues/35196>`__   | `PR #36824 <https://github.com/qgis/QGIS/pull/36824>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Project custom scales are displayed with scientific notation                                           | `#36859 <https://github.com/qgis/QGIS/issues/36859>`__   | `PR #36860 <https://github.com/qgis/QGIS/pull/36860>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries   | `#32521 <https://github.com/qgis/QGIS/issues/32521>`__   | `PR #34358 <https://github.com/qgis/QGIS/pull/34358>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Can't set min/max values to decimal in raster symbology with QGis Linux versions                       | `#33859 <https://github.com/qgis/QGIS/issues/33859>`__   | `PR #37136 <https://github.com/qgis/QGIS/pull/37136>`__   | N/A                             |
+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Sebastien Peillet <https://www.oslandia.com/>`__

Feature: Bug fixes by Alexander Bruy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                             | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                                | 3.10 backport commit (GitHub)                             |
+=======================================================================================================================+==========================================================+====================================================================================================================+===========================================================+
| Copy of truncated variable copies truncated text, not original                                                        | `#30641 <https://github.com/qgis/QGIS/issues/30641>`__   | `PR #36554 <https://github.com/qgis/QGIS/pull/36554>`__                                                            | `PR #36576 <https://github.com/qgis/QGIS/pull/36576>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Turning Multi edit mode off does not go back to table view                                                            | `#25099 <https://github.com/qgis/QGIS/issues/25099>`__   | `PR #36541 <https://github.com/qgis/QGIS/pull/36541>`__                                                            | `PR #36630 <https://github.com/qgis/QGIS/pull/36630>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| GRASS processing: missing parameter name                                                                              | `#36520 <https://github.com/qgis/QGIS/issues/36520>`__   | `PR #36644 <https://github.com/qgis/QGIS/pull/36644>`__                                                            | `PR #36690 <https://github.com/qgis/QGIS/pull/36690>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix redirection of the stdout results to temporary files in GRASS Processing algorithms                               | unreported                                               | `PR #36618 <https://github.com/qgis/QGIS/pull/36618>`__                                                            | `PR #36684 <https://github.com/qgis/QGIS/pull/36684>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix GRASS r.tileset algorithm                                                                                         | unreported                                               | `PR #36645 <https://github.com/qgis/QGIS/pull/36645>`__                                                            | `PR #36695 <https://github.com/qgis/QGIS/pull/36695>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QgsRasterTerrainAnalysisPlugin: check QgsRelief::processRaster() returned value                                       | `#17452 <https://github.com/qgis/QGIS/issues/17452>`__   | `PR #36731 <https://github.com/qgis/QGIS/pull/36731>`__                                                            | `PR #36740 <https://github.com/qgis/QGIS/pull/36740>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Histogram for graduated style in layer properties disappears when the layer properties window is too small            | `#25197 <https://github.com/qgis/QGIS/issues/25197>`__   | `PR #36732 <https://github.com/qgis/QGIS/pull/36732>`__                                                            | `PR #36749 <https://github.com/qgis/QGIS/pull/36749>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Exporting image with atlas option "Save World file" lead to incorrect world file naming (text after dot is missing)   | `#34523 <https://github.com/qgis/QGIS/issues/34523>`__   | `PR #36742 <https://github.com/qgis/QGIS/pull/36742>`__                                                            | `PR #36748 <https://github.com/qgis/QGIS/pull/36748>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| "Reloading QGIS" from the crash report dialog fails to reopen the project                                             | `#25532 <https://github.com/qgis/QGIS/issues/25532>`__   | `PR #36736 <https://github.com/qgis/QGIS/pull/36736>`__                                                            | `PR #36750 <https://github.com/qgis/QGIS/pull/36750>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Exporting raster style to SLD only works when output file has .sld suffix                                             | `#35944 <https://github.com/qgis/QGIS/issues/35944>`__   | `PR #36774 <https://github.com/qgis/QGIS/pull/36774>`__                                                            | `PR #36795 <https://github.com/qgis/QGIS/pull/36795>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| [Style Manager] Missing Favorites category in the "select by group" dialog from "Export symbols"                      | `#27315 <https://github.com/qgis/QGIS/issues/27315>`__   | `PR #36793 <https://github.com/qgis/QGIS/pull/36793>`__                                                            | not critical                                              |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| TIN Interpolation - output raster format and size issues                                                              | `#31970 <https://github.com/qgis/QGIS/issues/31970>`__   | `PR #36822 <https://github.com/qgis/QGIS/pull/36822>`__                                                            | `PR #36844 <https://github.com/qgis/QGIS/pull/36844>`__   |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Layer panel: "Edit Symbol" does nothing if no symbol defined for a rule (in rule-based rendering)                     | `#23048 <https://github.com/qgis/QGIS/issues/23048>`__   | `PR #36954 <https://github.com/qgis/QGIS/pull/36954>`__                                                            | not critical                                              |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Attributes shift in the Service area algorithm results                                                                | unreported                                               | `PR #37074 <https://github.com/qgis/QGIS/pull/37074>`__, `PR #37097 <https://github.com/qgis/QGIS/pull/37097>`__   | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Processing testing framework does not apply rounding to values casted to numbers                                      | unreported                                               | `PR #37234 <https://github.com/qgis/QGIS/pull/37234>`__                                                            | N/A                                                       |
+-----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by Alexander Bruy

Feature: Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Bug Title                                                                                                                                                                                 | URL issues.qgis.org (if reported)                                          | URL Commit (Github)                                                                                  | 3.10 backport commit (GitHub)                                                                                            |
+===========================================================================================================================================================================================+============================================================================+======================================================================================================+==========================================================================================================================+
| Fix leak in mesh 3d renderer                                                                                                                                                              | unreported                                                                 | `Commit 4b5a63d <https://github.com/qgis/QGIS/commit/4b5a63d11b7ea5baf6931c8abf86e132c706c1be>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix hang when rendering symbol previews using Meters in Map Unit sizes                                                                                                                    | `#28690 <https://github.com/qgis/QGIS/issues/28690>`__                     | `Commit 7c6286f <https://github.com/qgis/QGIS/commit/7c6286f8dfb7cc24e5b06c9ab950d9dd55fac517>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix font in CSS code editor                                                                                                                                                               | unreported                                                                 | `Commit 63cb42c <https://github.com/qgis/QGIS/commit/63cb42c298ef5ab732274bce205e49171b797ae4>`__    | not critical                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix rendering of geometry generator expressions which return geometry collection results                                                                                                  | `#35356 <https://github.com/qgis/QGIS/issues/35356>`__                     | `Commit be281c49 <https://github.com/qgis/QGIS/commit/be281c49b7932a1d0d0e3cb4dce7af17f5b201a9>`__   | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Correctly expose date time inputs (and a bunch of others) as inputs for in-model expressions                                                                                 | `#37219 <https://github.com/qgis/QGIS/issues/37219>`__                     | `Commit 281356a <https://github.com/qgis/QGIS/commit/281356aa4e951db5cd2782b53a7261c7343c4ca7>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix all Qt 5.14 deprecation warnings                                                                                                                                                      | unreported                                                                 | `Commit 3717adc <https://github.com/qgis/QGIS/commit/3717adcef6315f4b9a0089bfc2393cede937b644>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [symbology] When rendering a multipart geometry, ensure that geometry generator symbol is only rendered once, instead of once per part                                                    | `#23730 <https://github.com/qgis/QGIS/issues/23730>`__                     | `Commit d98fe9f <https://github.com/qgis/QGIS/commit/d98fe9f989f3b0677282acdf2ba99f4aa4fa08cc>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [layout] Make "show feature count" button apply to all selected indexes                                                                                                                   | `#37194 <https://github.com/qgis/QGIS/issues/37194>`__                     | `Commit 671cebc <https://github.com/qgis/QGIS/commit/671cebcf817e2b6fc17ce0307edf7fa377b665d3>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix for container "show as group box" setting is lost when closing layer properties dialog                                                                                                | `#37205 <https://github.com/qgis/QGIS/issues/37205>`__                     | `Commit 803f507 <https://github.com/qgis/QGIS/commit/803f507d45f99534dbc03ab5300e6137da36cd59>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Use even more forceful language to dissuade users from creating custom projections using Proj strings                                                                                     | `#37204 <https://github.com/qgis/QGIS/issues/37204>`__                     | `Commit 7ec4968 <https://github.com/qgis/QGIS/commit/7ec4968aa9dcb2107b00c1caaeb6ae575498bc3c>`__    | No -- string change                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Use "markers" terminology consistently in centroid fill widget                                                                                                                            | `#37106 <https://github.com/qgis/QGIS/issues/37106>`__                     | `Commit 2596b6b <https://github.com/qgis/QGIS/commit/2596b6be858a17533d1e16fca8ff8afc5d222564>`__    | No -- string change                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fixes to numbered list handling in dox/PyQGIS API                                                                                                                                         | unreported                                                                 | `Commit 74400c7 <https://github.com/qgis/QGIS/commit/74400c7ff88d563dad74dad41860f9b603214973>`__    | No                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix cross references in PyQGIS docs                                                                                                                                                       | unreported                                                                 | `Commit 81a9db9 <https://github.com/qgis/QGIS/commit/81a9db9f57706cba9b11e4372dd1bf50fcd7bc6a>`__    | No                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [layouts] Fix attribute table sort order combined with feature filter results in empty tables                                                                                             | `#36341 <https://github.com/qgis/QGIS/issues/36341>`__                     | `Commit 24897ab <https://github.com/qgis/QGIS/commit/24897ab86a7f11be196d8d705fa3307b05e0e53d>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix callout rendering to rotated labels                                                                                                                                                   | `#36681 <https://github.com/qgis/QGIS/issues/36681>`__                     | `Commit 2bb4aad <https://github.com/qgis/QGIS/commit/2bb4aad8c9b7238bd6ff6dc9a90a28c8625e859e>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix grass output handling in Processing models                                                                                                                                            | `#36379 <https://github.com/qgis/QGIS/issues/36379>`__                     | `Commit ef19911 <https://github.com/qgis/QGIS/commit/ef19911f1132dc5720a4068f059a0322d7511e2b>`__    |                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix vector datasets incorrectly simplify to rectangles in some CRS views                                                                                                                  | `#36898 <https://github.com/qgis/QGIS/issues/36898>`__                     | `Commit 47fba10 <https://github.com/qgis/QGIS/commit/47fba106dd9d057e6691dcca392efacbe31ad9ff>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix list item formatting in PyQGIS docs                                                                                                                                                   | unreported                                                                 | `Commit 84ec481 <https://github.com/qgis/QGIS/commit/84ec481aa8f3d3bb487272122414c765e77a2ea2>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix manual entry of extent values in widget                                                                                                                                  | `#36787 <https://github.com/qgis/QGIS/issues/36787>`__                     | `Commit ccc34c7 <https://github.com/qgis/QGIS/commit/ccc34c76e714e5f6f87d2a329ca048896eb4c87f>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [decorations] Use a proper ellipsoidal length calculation when calculating the size of the scalebar decoration                                                                            | `#28407 <https://github.com/qgis/QGIS/issues/28407>`__                     | `Commit af19cea <https://github.com/qgis/QGIS/commit/af19cea5acc90a6cc19d116dd35739059d0c5f83>`__    | `PR 36718 Commit a91309d <https://github.com/qgis/QGIS/pull/36718/commits/a91309ddbc0a430dc3bbcf48070bc565296ac551>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix collecting Triangle geometry types after tesselation                                                                                                                                  | `#36638 <https://github.com/qgis/QGIS/issues/36638>`__                     | `Commit df46fba <https://github.com/qgis/QGIS/commit/df46fba33823415b8310c986795f8c51550a0fa6>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix writing triangle geometry type via QgsVectorFileWriter fails                                                                                                                          | `#36638 <https://github.com/qgis/QGIS/issues/36638>`__                     | `Commit e0c03f9 <https://github.com/qgis/QGIS/commit/e0c03f9f0848490f358876ae5be6973961700bc9>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix degradation in Tesselation results                                                                                                                                                    | `#37077 <https://github.com/qgis/QGIS/issues/37077>`__                     | `Commit 61e7a5f <https://github.com/qgis/QGIS/commit/61e7a5fc90154bd4d35fea7d6cbd413ce61fa02e>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix layer subset string is ignored when OGR refuses to accept a compiled feature request expression                                                                                       | `#37073 <https://github.com/qgis/QGIS/issues/37073>`__                     | `Commit b5b4221 <https://github.com/qgis/QGIS/commit/b5b42218af5cbfca82f3b0a4d5a521e3d330f550>`__    | `PR 36718 Commit f486cf6 <https://github.com/qgis/QGIS/pull/36718/commits/f486cf6e6dadb2d0690f167620c90f4efddb3c4a>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [legends] Fix corrupted data defined legend rendering in layout designer                                                                                                                  | `#36765 <https://github.com/qgis/QGIS/issues/36765>`__                     | `Commit 8d00ae8 <https://github.com/qgis/QGIS/commit/8d00ae8638a09cb9a4c9ecd5d1fec3b352050cdd>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Avoid some QGIS startup warnings                                                                                                                                                          | unreported                                                                 | `Commit 013f682 <https://github.com/qgis/QGIS/commit/013f682bd3c6addd163a78d3776c578ae37377c6>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Place 3d tab in vector properties at the correct position                                                                                                                                 | `#35010 <https://github.com/qgis/QGIS/issues/35010>`__                     | `Commit ce9f5194 <https://github.com/qgis/QGIS/commit/ce9f519468d46bb6fe6dd0bc68efd7d58129be68>`__   | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix 3d tab is not activated when reopening vector layer properties                                                                                                                        | `#35011 <https://github.com/qgis/QGIS/issues/35011>`__                     | `Commit 3c0ecbf <https://github.com/qgis/QGIS/commit/3c0ecbfd79e1924cd01143324cdc26fe4a68f748>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [labeling] Fix incorrect label placement after moving an 'unplaced' label                                                                                                                 | unreported                                                                 | `Commit cbfb7f4 <https://github.com/qgis/QGIS/commit/cbfb7f4ce25e10aab5f7b8cee147afb801042704>`__    | `PR 36718 Commit 9189dec <https://github.com/qgis/QGIS/pull/36718/commits/9189dec7633b2eb6a1075bb35c2f90f6b90ba63a>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Don't block creation of new geopackages in vector save as dialog                                                                                                                          | unreported                                                                 | `Commit 8ccd127 <https://github.com/qgis/QGIS/commit/8ccd127f4d8bf66fb04b6484147ed116acf66d91>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [browser] Refine refreshConnections method to avoid triggering a full refresh of ALL browser content                                                                                      | `#37007 <https://github.com/qgis/QGIS/issues/37007>`__                     | `Commit a9d6b04 <https://github.com/qgis/QGIS/commit/a9d6b04f776b80acd1a97f48c7ed10e3599618b6>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [3d] When showing edges, data defined polygon height was not accounted for                                                                                                                | unreported                                                                 | `Commit e516231 <https://github.com/qgis/QGIS/commit/e516231bb2854405ea78a0cec40ad96295e9f8c6>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fixes for "Show all" labeling mode                                                                                                                                                        | unreported                                                                 | `Commit 2b91bd0 <https://github.com/qgis/QGIS/commit/2b91bd0cafff66f14ceb49b104bf2f2cc6ae714d>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [3d] Fix reprojection of features shows no features                                                                                                                                       | `#34824 <https://github.com/qgis/QGIS/issues/34824>`__                     | `Commit 62bd026 <https://github.com/qgis/QGIS/commit/62bd0267439a65f94a5cd9cb886bbb4e4780cdf0>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Add metadata setting for file destination parameters to avoid file overwrite confirmation prompt                                                                             | `#37011 <https://github.com/qgis/QGIS/issues/37011>`__                     | `Commit e81af2c <https://github.com/qgis/QGIS/commit/e81af2c9e10dc2a2e220c815cb9e531f7dba838d>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Avoid incorrectly antialiasing rendering of certain objects (such as map labels) when not wanted                                                                                          | `#36964 <https://github.com/qgis/QGIS/issues/36964>`__                     | `Commit bab83844 <https://github.com/qgis/QGIS/commit/bab838444cb55fc479d2f3dfa3b19d8ce80e73af>`__   | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Ensure that fields required by marker symbol backgrounds for labels are fetched when rendering                                                                                            | `#36944 <https://github.com/qgis/QGIS/issues/36944>`__                     | `Commit 8fb8e45 <https://github.com/qgis/QGIS/commit/8fb8e45d516611f09bf28e3832c3c6214f16c4a2>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| "Fix ""zoom"" and ""flash"" features buttons have no effect when opening filter mode in attribute form"                                                                                   | `#34506 <https://github.com/qgis/QGIS/issues/34506>`__                     | `Commit 6b2795 <https://github.com/qgis/QGIS/commit/6b27958948db2c88ae72b0b9ff99fc8aa8522bf2>`__     | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Avoid corrupted project thumbnail images in some circumstances                                                                                                                            | unreported                                                                 | `Commit f404e6e <https://github.com/qgis/QGIS/commit/f404e6e162df954ffb200d550b6c32375b7270c1>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Auto focus search box when opening "add layer to legend" dialog                                                                                                                           | `#36905 <https://github.com/qgis/QGIS/issues/36905>`__                     | `Commit 019e494 <https://github.com/qgis/QGIS/commit/019e494f1d61851ea192900a2cc9cce460d1ea73>`__    | not critical                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Set correct output layer type for Point to Layer algorithm                                                                                                                   | `#36941 <https://github.com/qgis/QGIS/issues/36941>`__                     | `Commit 7ee85cd <https://github.com/qgis/QGIS/commit/7ee85cd93cb5e0b623feaad2ef1ce9ea8f654bac>`__    | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| "Limit scope of Ctrl+C shortcut for copy features to canvas and for python console to console widget"                                                                                     | `#27035 <https://github.com/qgis/QGIS/issues/27035>`__ (many others too)   | `Commit 873716c <https://github.com/qgis/QGIS/commit/873716c6fa17298868060a6517205ad7bea78a72>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Remember layout designer window positions                                                                                                                                                 | `#36907 <https://github.com/qgis/QGIS/issues/36907>`__                     | `Commit 97d31d0 <https://github.com/qgis/QGIS/commit/97d31d025fe2264afadcf6afcb3eb6ebcfe9e91d>`__    | not critical                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix crash when zooming in too far to labels                                                                                                                                               | `#36346 <https://github.com/qgis/QGIS/issues/36346>`__                     | `Commit 3aa5e56 <https://github.com/qgis/QGIS/commit/3aa5e56d3c3dbb61f2a28c4874593aa401957ed3>`__    | `Commit a22635b <https://github.com/qgis/QGIS/commit/a22635bb64ae6d2a46715bd1208463e22b6080ae>`__                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Allow parent layer to be specified for field mapping inputs in models                                                                                                        | `#26493 <https://github.com/qgis/QGIS/issues/26493>`__                     | `Commit b8d4a39 <https://github.com/qgis/QGIS/commit/b8d4a39b58465f93f45ed886e77411c194f44132>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix placement of message bar 'clear all' menu arrow on hidpi screens                                                                                                                      | unreported                                                                 | `Commit 8a9975b <https://github.com/qgis/QGIS/commit/8a9975b4ff6b7a8a79bef05230db28754500fa40>`__    | not critical                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Always refresh plugin repositories when manually triggered by user                                                                                                                        | `#34351 <https://github.com/qgis/QGIS/issues/34351>`__                     | `Commit 98603b7 <https://github.com/qgis/QGIS/commit/98603b78660e05334c7b34ea3722533164f9553b>`__    | `PR 36718 Commit 0fcf6dc <https://github.com/qgis/QGIS/pull/36718/commits/0fcf6dc08289fb549c9bace24a70ed4a50bdd959>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [3d] Expose 3d algorithms provider to Python                                                                                                                                              | `#36661 <https://github.com/qgis/QGIS/issues/36661>`__                     | `Commit 1f835df <https://github.com/qgis/QGIS/commit/1f835dfa9af51204ea1182df7bf722d84b223645>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [symbology] Don't force rasterized output when exporting point pattern fills                                                                                                              | `#16100 <https://github.com/qgis/QGIS/issues/16100>`__                     | `Commit 23396b7c <https://github.com/qgis/QGIS/commit/23396b7c864d00fc164db8c80d704a1ffc430ac1>`__   | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [layouts] Don't refresh the map canvas multiple times during atlas exports                                                                                                                | `#30144 <https://github.com/qgis/QGIS/issues/30144>`__                     | `Commit 57519e9 <https://github.com/qgis/QGIS/commit/57519e9faa95fbfe6196134d9128caee48cb4b84>`__    | not critical                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| [processing] Fix double-evaluation of warp output parameter                                                                                                                               | `#30095 <https://github.com/qgis/QGIS/issues/30095>`__                     | `Commit adeca2f <https://github.com/qgis/QGIS/commit/adeca2f586203913ae3702531b32579ed4c14344>`__    |                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix incorrect warning message when turning off atlas preview                                                                                                                              | unreported                                                                 | `Commit 3b0af960 <https://github.com/qgis/QGIS/commit/3b0af960dd90af15cbe32e2fd7642408031e70f5>`__   | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Speed up message bar operations when many messages are shown                                                                                                                              | `#29698 <https://github.com/qgis/QGIS/issues/29698>`__                     | `Commit 5dd29f0 <https://github.com/qgis/QGIS/commit/5dd29f065e57fde532a21ae1bc9311aef9378455>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix oriented minimum bounding box calculation is wrong in some cases                                                                                                                      | `#36632 <https://github.com/qgis/QGIS/issues/36632>`__                     | `Commit 97d0988 <https://github.com/qgis/QGIS/commit/97d098884a7889346739d61bd9048e9dcf942d11>`__    | `PR 36718 Commit 68c6a0e <https://github.com/qgis/QGIS/pull/36718/commits/68c6a0e31dc58fa23621e872739df9efded6e6b7>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Ensure symbol opacity is always ignored for selections                                                                                                                                    | `#27859 <https://github.com/qgis/QGIS/issues/27859>`__                     | `Commit 4de6a53 <https://github.com/qgis/QGIS/commit/4de6a53235a6f7bd657c60d4f4d7160ed371d9df>`__    | `PR 36718 Commit 99eb710 <https://github.com/qgis/QGIS/pull/36718/commits/99eb710f89be0c6adc9acfdd888e366e6f2b796f>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix random sort order of symbols in Symbol Export dialog                                                                                                                                  | `#20572 <https://github.com/qgis/QGIS/issues/20572>`__                     | `Commit 987310f <https://github.com/qgis/QGIS/commit/987310fe90de2b21deb5c2564eb051e1d72548b2>`__    | `PR 36718 Commit bfa6058 <https://github.com/qgis/QGIS/pull/36718/commits/bfa60586e10735a6b670cd349dd8b9efd2ab2762>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Allow clearing heatmap weighting field                                                                                                                                                    | `#20256 <https://github.com/qgis/QGIS/issues/20256>`__                     | `Commit 3961fa2 <https://github.com/qgis/QGIS/commit/3961fa26f53e411c5c83b50e006df739ebda4c3e>`__    | `PR 36718 Commit d2600d6 <https://github.com/qgis/QGIS/pull/36718/commits/d2600d6d2cb765cb0641347ac342a74f663e4ba5>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Flag SAGA 'Merge Layers' algorithm as having known issues                                                                                                                                 | `#36375 <https://github.com/qgis/QGIS/issues/36375>`__                     | `Commit f676c821 <https://github.com/qgis/QGIS/commit/f676c821d9d9ff2d6e509d881ba2ea1853a34051>`__   | N/A                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Workaround odd upstream Qt issue where a painter with a semi-transparent brush with no solid pattern incorrectly applies the brush opacity to the pen when exporting to printer devices   | `#36580 <https://github.com/qgis/QGIS/issues/36580>`__                     | `Commit 38c8218 <https://github.com/qgis/QGIS/commit/38c82187a65d8b4833f2c633a69a4d937a8725eb>`__    | `PR 36718 Commit a562b67 <https://github.com/qgis/QGIS/pull/36718/commits/a562b678438d26c1f80486fdfff422d70c8c6329>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Improve plugin watchdog message and UX                                                                                                                                                    | unreported                                                                 | `Commit 150b373 <https://github.com/qgis/QGIS/commit/150b373c7ae61c0548ab0803f9b30a36b15e7ab4>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| "[layouts] Warn when previewing an atlas and a feature with no geometry is encountered, when one or more maps are set to be driven by atlas feature"                                      | `#36556 <https://github.com/qgis/QGIS/issues/36556>`__                     | `Commit 6ce84d2 <https://github.com/qgis/QGIS/commit/6ce84d2c347f49c9aae0c1953e2b2529228db430>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Avoid proj 'object is not a concatenated operation' warnings                                                                                                                              | unreported                                                                 | `Commit 6baa209 <https://github.com/qgis/QGIS/commit/6baa209285f452e5996537b1b0f1b5d924d5c59b>`__    |                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| "Fix memory layers lose CRS definition if it does not have an authority associated with it"                                                                                               | `#36241 <https://github.com/qgis/QGIS/issues/36241>`__                     | `Commit e23a49a <https://github.com/qgis/QGIS/commit/e23a49a6b858cad9373c3bfb9ad66525622ce9ee>`__    | `PR 36718 Commit c9350eb <https://github.com/qgis/QGIS/pull/36718/commits/c9350eb7439a29ac8ff3734cd7866f2403e3646e>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Implement spatial index detection for OGR provider                                                                                                                                        | `#30530 <https://github.com/qgis/QGIS/issues/30530>`__                     | `Commit f20801a <https://github.com/qgis/QGIS/commit/f20801a8bb3f23576e5e0d2abc6d3229e5044200>`__    | `PR 36718 Commit 536906e <https://github.com/qgis/QGIS/pull/36718/commits/536906ec6375b70d88767e58a08550369a25d1a0>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Fix incorrect dialog title for raster layer properties                                                                                                                                    | `#35510 <https://github.com/qgis/QGIS/issues/35510>`__                     | `Commit 2099261 <https://github.com/qgis/QGIS/commit/2099261230f82c5cd4439538e38754947c8f6bd6>`__    | `PR 36718 Commit e809f48 <https://github.com/qgis/QGIS/pull/36718/commits/e809f48cb9aaf03dfe8671c2d885f99b4a91922b>`__   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Don't try to identify CRSes created just for ellipsoid definitions                                                                                                                        | unreported                                                                 | `Commit 15b318b <https://github.com/qgis/QGIS/commit/15b318b50de9131ed1dd6bbf73ae5eb7572579a7>`__    | No -- too intrusive                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Nyall Dawson <https://north-road.com/>`__

Feature: Bug fixes by Denis Rouzaud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                        | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.10 backport commit (GitHub)                             |
+==================================================================================================+==========================================================+===========================================================+===========================================================+
| allow sorting attribute table by field not listed in the table                                   | `#25671 <https://github.com/qgis/QGIS/issues/25671>`__   | `PR #36236 <https://github.com/qgis/QGIS/pull/36236>`__   | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| fix layer tree dependencies (showinf symbols and main layer)                                     | unreported                                               | `PR #37000 <https://github.com/qgis/QGIS/pull/37000>`__   | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| fix Expression editor: syntax check fails if table is empty                                      | `#37100 <https://github.com/qgis/QGIS/issues/37100>`__   | `PR #37137 <https://github.com/qgis/QGIS/pull/37137>`__   | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| fix setting of feature in expression preview widget                                              | `#37214 <https://github.com/qgis/QGIS/issues/37214>`__   | `PR #37221 <https://github.com/qgis/QGIS/pull/37221>`__   | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Freeze when showing attribute table of WFS layer                                                 | `#37224 <https://github.com/qgis/QGIS/issues/37224>`__   | not yet fixed                                             | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Lookups in tables with more than 100 entries show wrong value in Relation Reference form parts   | `#37266 <https://github.com/qgis/QGIS/issues/37266>`__   | `PR #37280 <https://github.com/qgis/QGIS/pull/37280>`__   | `PR #37286 <https://github.com/qgis/QGIS/pull/37286>`__   |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

This feature was developed by `Denis Rouzaud <https://www.opengis.ch/>`__


Feature: Bug fixes by Audun Ellertsen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                        | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.10 backport commit (GitHub)                             |
+==================================================================================================+==========================================================+===========================================================+===========================================================+
| SpatiaLite support for importing layers with binary fields                                       | `#36705 <https://github.com/qgis/QGIS/issues/36705>`__   | `PR #36744 <https://github.com/qgis/QGIS/pull/36744>`__   | N/A                                                       |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| PostGIS support for importing layers with binary fields                                          | `#36705 <https://github.com/qgis/QGIS/issues/36705>`__   | `PR #36708 <https://github.com/qgis/QGIS/pull/36708>`__   | `PR #36720 <https://github.com/qgis/QGIS/pull/36720>`__   |
+--------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `Kongsberg Digital <https://www.kongsberg.com/digital/>`__

This feature was developed by `Audun Ellertsen <https://github.com/audun/>`__


.. |image1| image:: images/splash.jpeg
   :class: img-responsive img-rounded center-block
.. |image2| image:: images/entries/90da13821bfde46aa6d9d951fb9a31bf27d85656.gif
   :class: img-responsive img-rounded
.. |image3| image:: images/entries/78421839-37e3d100-765b-11ea-83e5-e7e3e519155e.png
.. |image4| image:: images/entries/a8347da9570ae597bc17e23236e4eb4d57efb1d1.gif
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/74980472-93f2ed00-5441-11ea-8765-f35d1f69b144.gif
.. |image6| image:: images/entries/74638436-ee0f5c00-517c-11ea-938e-cec23c61ba29.gif
.. |image7| image:: images/entries/b86eea9111e33e6aea345b0e0759de48eaceade9.gif
   :class: img-responsive img-rounded
.. |image8| image:: images/entries/14b7cf800ef293ac3ea3f00d12a30022876e713c.png
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/79157425-d3501100-7dd4-11ea-8395-5c8ff1dce449.png
.. |image10| image:: images/entries/78198825-34bada80-74cd-11ea-803a-90afea085b38.gif
.. |image11| image:: images/entries/76692569-26616780-6661-11ea-9071-fd4c712860db.gif
.. |image12| image:: images/entries/77666018-b5834f00-6f80-11ea-971e-c6d7d996d37d.gif
.. |image13| image:: images/entries/80049561-d8017d00-84d8-11ea-826e-d7092ac7a5c6.gif
.. |image14| image:: images/entries/77861880-17111b00-7218-11ea-95ba-410c97830b93.png
.. |image15| image:: images/entries/77845535-6e3fcd00-71d1-11ea-8760-b477e75f7a3a.jpg
.. |image16| image:: images/entries/77845539-726bea80-71d1-11ea-9512-0a8e6cde7b3c.jpg
.. |image17| image:: images/entries/77846711-bfec5580-71d9-11ea-9afe-a52af9b2784e.jpg
.. |image18| image:: images/entries/77846764-1eb1cf00-71da-11ea-9d6d-f468708ea726.jpg
.. |image19| image:: images/entries/1ded1a8bbec9eeebafad96b7616e963847961e14.png
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/e387c3745d49a36116908dffc1126befae7d1b1f.png
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/81377287-84359b80-9148-11ea-95f4-9d7917d62cf9.png
.. |image22| image:: images/entries/81377294-88fa4f80-9148-11ea-9036-2a597b064bbc.png
.. |image23| image:: images/entries/80680381-faf7e680-8b01-11ea-8612-b0f543bfd943.png
.. |image24| image:: images/entries/80680391-00553100-8b02-11ea-8e56-21b57964f765.png
.. |image25| image:: images/entries/80680478-30043900-8b02-11ea-8bd5-3325fc0a5021.png
.. |image26| image:: images/entries/80680488-37c3dd80-8b02-11ea-98bb-e0882e6ab9ab.png
.. |image27| image:: images/entries/78723460-bf676380-792b-11ea-9cab-a6732e20033a.png
.. |image28| image:: images/entries/76173692-5a660400-61ed-11ea-87dd-74a4db5cf0ce.png
.. |image29| image:: images/entries/76173706-6d78d400-61ed-11ea-89c1-ce4e2477dfef.png
.. |image30| image:: images/entries/81516813-3a46e400-9307-11ea-9621-a27d5a8c86f2.gif
.. |image31| image:: images/entries/81480226-42fbc500-91f6-11ea-91fd-3d430693d551.png
.. |image32| image:: images/entries/f11b278c71fecee8445ff29077bfddef543b564d.gif
   :class: img-responsive img-rounded
.. |image33| image:: images/entries/80013358-bb475400-849c-11ea-95c8-71b04382a927.gif
.. |image34| image:: images/entries/78789841-b1413380-797b-11ea-9c7b-f31cb9756809.gif
.. |image35| image:: images/entries/77872855-31e29000-7216-11ea-80fb-82e351dbb4a2.gif
.. |image36| image:: images/entries/77871643-bf23e580-7212-11ea-9b92-82c906c19c22.png
.. |image37| image:: images/entries/77871772-20e44f80-7213-11ea-8988-a51ec78c1320.png
.. |image38| image:: images/entries/77320848-acc41c00-6ce7-11ea-85af-2bff553ecbb5.gif
.. |image39| image:: images/entries/77156534-ed1c6380-6a75-11ea-8b97-a13d3ea27ede.png
.. |image40| image:: images/entries/77156669-2c4ab480-6a76-11ea-9209-d0144fbfc3f0.png
.. |image41| image:: images/entries/77156736-5bf9bc80-6a76-11ea-827b-bb55ce52b814.png
.. |image42| image:: images/entries/76421493-1fdda200-637a-11ea-9e4b-71a596b18dd9.png
.. |image43| image:: images/entries/75885078-2aea7c80-5e26-11ea-8435-eef74afce7b7.png
.. |image44| image:: images/entries/75885122-3b9af280-5e26-11ea-96a3-f4a4e48c040e.png
.. |image45| image:: images/entries/74750757-9e936380-5242-11ea-98cf-a0e3e6694831.png
.. |image46| image:: images/entries/74750903-d69aa680-5242-11ea-9be3-0af7b2beacaf.png
.. |image47| image:: images/entries/74751034-0cd82600-5243-11ea-8a02-de78a337f299.gif
.. |image48| image:: images/entries/74751042-12357080-5243-11ea-80cb-2a3217d03a78.gif
.. |image49| image:: images/entries/76225819-6a80e200-61f3-11ea-88da-43e70c358530.png
.. |image50| image:: images/entries/265d07738c1cec8a398ce5503330a520f98d4526.gif
   :class: img-responsive img-rounded
.. |image51| image:: images/entries/80860629-47116b00-8c69-11ea-83d8-61f27cb77e68.png
.. |image52| image:: images/entries/80860663-6c9e7480-8c69-11ea-94a3-8d0e8544867d.png
.. |image53| image:: images/entries/80860675-7b852700-8c69-11ea-984d-584eff1e3c95.png
.. |image54| image:: images/entries/81009703-653bbe80-8e55-11ea-9286-4850b32edb23.png
.. |image55| image:: images/entries/80325577-0edce780-8879-11ea-82bd-8f323a4c68ab.gif
.. |image56| image:: images/entries/79927419-0c4a4e80-8483-11ea-9b87-7ed8b393d349.gif
.. |image57| image:: images/entries/79714030-ea31be80-8312-11ea-8b6f-f40e3eea04b1.gif
.. |image58| image:: images/entries/78468312-2c2b0400-775a-11ea-926e-2acf7ec15aa4.png
.. |image59| image:: images/entries/78419618-c885d580-768a-11ea-959a-8459e19e05df.png
.. |image60| image:: images/entries/e7f2b64e48b0726bc03e2d4fa9424feabde1808d.gif
   :class: img-responsive img-rounded
.. |image61| image:: images/entries/77267662-0c71f580-6cef-11ea-9956-917e1d6ef496.png
.. |image62| image:: images/entries/77247015-c1b59680-6c78-11ea-92a9-7bbb2ba8638a.png
.. |image63| image:: images/entries/77247024-dc880b00-6c78-11ea-827a-344645cec248.png
.. |image64| image:: images/entries/74844265-348ac500-52fb-11ea-9198-78f4f9022ac1.PNG
.. |image65| image:: images/entries/80604352-e6e4b400-8a31-11ea-8f3b-8c864e124c78.png
.. |image66| image:: images/entries/caa646295d6f1cf6297864810637e9f8ceddc102.png
   :class: img-responsive img-rounded
.. |image67| image:: images/entries/71798125-35201280-3051-11ea-959d-a5897ca3391a.png
.. |image68| image:: images/entries/71799417-7e726100-3055-11ea-8e07-3792dbc741c2.gif
.. |image69| image:: images/entries/81065380-a37bc100-8edb-11ea-8aed-6fd52d843a26.gif
.. |image70| image:: images/entries/79769829-e3b04080-832c-11ea-9029-981e3a3ecf1b.gif
.. |image71| image:: images/entries/81038564-bcb64a80-8ea6-11ea-8289-46340dee9a88.gif
.. |image72| image:: images/entries/78998144-46912300-7b48-11ea-9fbf-232d11fbeff6.png
.. |image73| image:: images/entries/78904645-26486200-7a7d-11ea-84b0-b9e96c0c9797.gif
.. |image74| image:: images/entries/76538031-f195ba80-647e-11ea-9a41-271576e315bc.gif
.. |image75| image:: images/entries/76504669-70233580-6448-11ea-9194-173ae0d344ce.gif
.. |image76| image:: images/entries/75692656-28f9af80-5ca6-11ea-8dd6-9a4bf454f5b7.gif
.. |image77| image:: images/entries/75693398-2ba8d480-5ca7-11ea-8be0-9643f8841c89.png
.. |image78| image:: images/entries/75693402-2cda0180-5ca7-11ea-9d65-f0c00e26180e.png
.. |image79| image:: images/entries/75693404-2d729800-5ca7-11ea-889d-5aa73bc131ce.png
.. |image80| image:: images/entries/75524592-82e04800-5a0e-11ea-9333-461a0d02a1c0.png
.. |image81| image:: images/entries/75249972-9786cb00-57d7-11ea-8100-3426d32831db.png
.. |image82| image:: images/entries/76710403-f624d200-670f-11ea-9a41-13420c7940e3.gif
.. |image83| image:: images/entries/78195435-e29f9800-747f-11ea-95d2-604be58cf229-1.gif
.. |image84| image:: images/entries/77874799-cff64a80-7256-11ea-974b-c4084d1e01ae.gif
.. |image85| image:: images/entries/77712469-95ef3380-701f-11ea-8fec-3eded258b4e9.gif
.. |image86| image:: images/entries/6304472935d29f8292cf24c7cb0198e95a4de137.png
   :class: img-responsive img-rounded
.. |image87| image:: images/entries/81117303-224a1b80-8f27-11ea-851d-f4271ce66ed3.png
.. |image88| image:: images/entries/81117371-4279da80-8f27-11ea-9d8b-bbe1c78d9bf1.png
.. |image89| image:: images/entries/81117466-6ccb9800-8f27-11ea-85e7-9c9a1df87920.png
.. |image90| image:: images/entries/81117708-d6e43d00-8f27-11ea-866a-0c3bdbd97291.png
.. |image91| image:: images/entries/81117621-ae5c4300-8f27-11ea-993b-782d7de4a10e.png
.. |image92| image:: images/entries/79409609-b6d4f400-7fe1-11ea-8f7a-f42542f3fbfe.gif
.. |image93| image:: images/entries/b7b0b73f7d48104cb49f33ed2d453a70d188cbd6.png
   :class: img-responsive img-rounded
.. |image94| image:: images/entries/650983141141fc954abc96f79e5255e4634c5051.png
   :class: img-responsive img-rounded
.. |image95| image:: images/entries/78641463-a099aa80-78f4-11ea-8c0b-c6b6b72f0e7d.gif
.. |image96| image:: images/entries/78631098-b9976100-78de-11ea-8f18-f7c7473e0945.gif
.. |image97| image:: images/entries/78090538-bba87e00-740d-11ea-9476-144163d8f1ca.gif
.. |image98| image:: images/entries/77991113-5d749000-7366-11ea-986c-652f6e2229e7.png
.. |image99| image:: images/entries/77508685-fca50d80-6eb6-11ea-8190-a447847f55d9.gif
.. |image100| image:: images/entries/77395930-64dbec80-6dee-11ea-9590-b7fadcd242c1.gif
.. |image101| image:: images/entries/76703713-81b34a00-66a1-11ea-9818-ebf771885206.png
.. |image102| image:: images/entries/76388083-f9d4f380-63b3-11ea-8f06-97249e85ac2e.gif
.. |image103| image:: images/entries/76176510-c8fe8e00-61fc-11ea-90e1-91cbeadcbd4f.gif
.. |image104| image:: images/entries/75851342-26799000-5e35-11ea-8895-a310f01b3823.gif
.. |image105| image:: images/entries/6cbf249116a09b4d342729da1e09060b9f0ec52f.png
   :class: img-responsive img-rounded
.. |image106| image:: images/entries/75100644-6079a500-559e-11ea-91b6-f99fa05451de.png
.. |image107| image:: images/entries/c747d86081f3862d9d4bbb2ab067103daceab724.png
   :class: img-responsive img-rounded
.. |image108| image:: images/entries/81394331-76711d80-912a-11ea-8b86-4f2789adff08.png
.. |image109| image:: images/entries/81068877-be553200-8ee9-11ea-9a06-a4d30e773cf6.png
.. |image110| image:: images/entries/80964825-d0fc3800-8e11-11ea-9961-34edb623458c.png
.. |image111| image:: images/entries/80964191-b4abcb80-8e10-11ea-8b80-395dbb37b45c.png
.. |image112| image:: images/entries/77608752-dab89300-6f69-11ea-9c48-eefca7a4d199.gif
.. |image113| image:: images/entries/75894983-49a43f80-5e35-11ea-95a8-a86276b39bbc.gif
.. |image114| image:: images/entries/78514331-1833e080-77f4-11ea-9c8d-a5e9ead7dc1a.gif
.. |image115| image:: images/entries/75906887-b1638600-5e47-11ea-98c6-06fb664ab177.PNG
.. |image116| image:: images/entries/80051225-4b0cf280-84dd-11ea-9016-84a4303f230f.gif
.. |image117| image:: images/entries/78028688-bbbf6400-73a2-11ea-9b7f-a7d81133d321.gif
.. |image118| image:: images/entries/77539757-2d2e7c80-6ea2-11ea-9098-c6c0924f9d59.png
.. |image119| image:: images/entries/77492080-55f74780-6e8b-11ea-9141-1b96c42c29eb.png

