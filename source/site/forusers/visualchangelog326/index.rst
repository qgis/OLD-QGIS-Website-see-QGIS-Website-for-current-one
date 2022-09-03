.. _changelog326:

Changelog for QGIS 3.26
=======================

|image1|

Release date: 2022-06-17

The feature-packed release of QGIS 3.26 Buenos Aires includes a vast number of enhancements to a range of advanced core functionalities. This includes numerous improvements to 3D capabilities, improved tooling for point clouds, and the introduction of a new profile plotting framework for the creation of cross-sections and elevation profiles. Best of all, the new plotting framework uses the native QGIS rendering capabilities and comes with all the styling, symbology, and data driven properties we all know and love baked right in!

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at https://youtu.be/pZmrw_zR7sA

:raw-html:`<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/pZmrw_zR7sA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>`

The QGIS Community has also been active in various crowd-funding campaigns, `Open Day events <https://github.com/qgis/QGIS/wiki#qgis-open-day>`__, and the growth of the `STAC Ecosystem <https://medium.com/radiant-earth-insights/stac-updates-february-2022-e02a194861e>`__ has led to inter-agency collaboration initiatives which include outcomes such as the `STAC Browser QGIS Plugin <https://stac-utils.github.io/qgis-stac-plugin/>`__, which make it nearly trivial to produce `Raster Mosaics <https://www.youtube.com/watch?v=se2Xd7CKhHg>`__ from Earth Observation data using Open Source and Open Data. There is also a new `online analytics dashboard <https://blog.qgis.org/2022/06/16/qgis-userbase-analytics/>`__ which collects information from the QGIS Feed in an attempt to show how and where QGIS is being used, providing valuable insight to developers and the QGIS community.

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to `QGIS.ORG <https://qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our `list of donors <https://qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

:raw-html:`<div id="qgissustainingmembersatom"> <!-- to be filled via javascript loading of atom feed --> </div>`

QGIS is free software and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of what their financial or social status is - we believe that empowering people with spatial decision-making tools will result in a better society for all of humanity.

.. contents::
   :local:

Breaking Changes
----------------

Feature: DB2 Support Removed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DB2 provider has been marked deprecated and hidden from the QGIS UI for a number of releases. As no maintainers have come forward to support the maintenance of this data provider, it has been removed and will no longer be available for use in QGIS.

Map Tools
---------

Feature: Selecting all features by attribute value from Identify Results panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The identify results tools now provides an option available from the context menu of an attribute field value which allows for the quick selection of all features in that layer with matching values to be selected.

|image3|

This feature was funded by `Camptocamp <https://www.camptocamp.com>`__

This feature was developed by `Ismail Sunni <https://github.com/ismailsunni>`__

User Interface
--------------

Feature: Coordinate ordering according to CRS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS will now use the correct coordinate ordering for the project CRS when displaying coordinates in status bar (and identify results). A setting has been added in the project properties to allow users to override this with a specific coordinate ordering if desired (x/y or y/x).

Specifically, this means that projects in geographic CRS like EPSG:4326 will now show coordinates in latitude/longitude order instead of longitude/latitude (unless the specific CRS has different native ordering).

|image4|

This feature was funded by SevenCs GmbH

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Select features from expression based symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A "Select Features" action has been added to the right click context menu on legend class symbols. This allows you to rapidly select all features within a layer that match the associated symbol class in categorized, graduated, and rule based renderers.

|image5|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Copy preview expression value to clipboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new button has been added to the expression builder interface which allows the copying of the value in the expression preview field to the clipboard.

|image6|

This feature was funded by `Camptocamp <https://www.camptocamp.com/>`__

This feature was developed by `Ismail Sunni <https://github.com/ismailsunni>`__

Feature: Option to synchronize statistics panel with layer selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A "Keep synchronized with TOC" checkbox has been added to the statistics panel, which allows the statistics panel to automatically synchronize with the table of contents layer list, ensuring that the active layer is selected for the computed statistics displayed in the statistics panel.

The most recently defined expression used for defining the statistics calculation on a layer will be retained for each layer independently.

|image7|

This feature was developed by `Jacky Volpes <https://github.com/Djedouas>`__

Feature: Implement scroll wheel action for color and symbol buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Triggering a mouse wheel action while hovering a symbol layers will now automatically adjust one of the style attributes, making it more efficient to adjust common symbology rules. This feature affects different symbol styles in various ways, based on which UI control is selected.

-  For marker symbols, the marker size increases / decreases
-  For line symbols, the line width increases / decreases

In addition, when triggering a mouse wheel action while hovering a color symbol, the color opacity will increase / decrease.

|image8|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Accessibility
-------------

Feature: Horizontal table scroll with shift+wheel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Attribute tables can now be scrolled horizontally using the key combination of Shift+ Mouse wheel, switching from the default vertical scroll operation.

This matches the behavior exposed by LibreOffice, and provides a convenient way to quickly horizontally scroll tables when a mouse doesn't have a dedicated horizontal scroll wheel.

|image9|

This feature was funded by the City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Symbology
---------

Feature: New "Animated Marker" symbol type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new marker symbol type allows points to be rendered using an animated marker, sourced from an animated gif, webp or mng animation. Options are present for marker file, size, angle and frame rate.

There are two ways in which animated symbols are handled.

-  If the map is NOT considered an animation (i.e. a regular QGIS project), then the frame to render will be based on the current timestamp alone.
-  If the map itself is considered an animation, then the frame rendered for the animated marker is based on the map animation frame and frame rate. This is the case when the temporal controller is set to the Animation mode. In this case, the animated markers will follow the temporal controller animation, e.g. pausing when the animation is paused, advancing frames with the animation, etc. This mode also applies when exporting an animation from the temporal controller and is used when a plugin specifically sets the frame rate and current frame properties.

|image10|

This feature was funded by `North Road Consulting <https://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Allow any symbol to be an animated symbol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can now indicate that a symbol should be treated as an animated symbol, through the new "Animation Settings" option in the symbol widget's Advanced menu.

This settings panel allows users to enable animation for the symbol and set a specific frame rate at which the symbol should be redrawn. When enabled, the @symbol\_frame variable can be used in any symbol data defined property in order to animate that property.

For instance, setting the symbol's rotation to the following data defined expression will cause the symbol to rotate over time, with rotation speed dictated by the symbol's refresh rate.

::

    @symbol_frame % 360


|image11|

This feature was funded by `North Road Consulting <https://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Add a new classification method for "Fixed interval"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows users to create graduated breaks using a specific interval width for classes (instead of the total number of classes).

|image13|

This feature was funded by `SLYR <https://north-road.com/slyr/>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Custom dash pattern panel shows total pattern length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The custom dash pattern panel now displays the total dash pattern length, enhancing the ability for users to match the overall pattern length with sizes from other parts of a symbol.

|image14|

This feature was funded by `North Road Consulting <https://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Select style categories when storing styles in database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS supports the storing of layer styles in the source database, or in the local style database. QGIS then provides the ability to use those styles as the default style for a layer, or provide access to the style via the style manager.

In prior releases of QGIS, this process stored all available style categories in the database, however new functionality allows users to select which specific style categories should be stored, providing a similar level of flexibility for storing styles in database sources as was previously available only for the QML and SLD style formats.

|image15|

This feature was developed by `Jacky Volpes <https://github.com/Djedouas>`__

Labelling
---------

Feature: Allow data-defined control over line anchor type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allows data-defined control over whether the 'hint' or 'strict' anchoring type is used.

This feature was funded by City of Freiburg im Breisgau

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Control label anchor placement relative to text position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A control is now provided for defining what part of the text (start, middle, or end) of line labels correspond to the anchor position defined in label placement. This allows for more precise placement of labels according to specific requirements, such as lining up the end of a labels text with a specific point on a line feature.

In prior releases of QGIS, labels would always be centered over the anchor position of lines, unless it was a curved label, which used the start of the label for determining the anchor orientation.

A new option for "Follow placement" has also been added, which means that the text anchor will depend on the placement along line setting. This control attempts to determine the appropriate alignment option automatically according to the label placement on the feature and exhibits the following behaviors:

-  For labels anchored near the start of the line (0-25%), the anchor placement will be the **start** of the label text
-  For labels anchored near the end of the line (75-100%), the anchor placement will be the **end** of the label text
-  For anchor placements between 25 and 75%, the anchor placement will be the **center** of the label text

This feature was funded by City of Freiburg im Breisgau

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com/slyr/>`__

Feature: Interactively move curved line labels along their line features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Placement of curved label text can now be manipulated by using the interactive "Move Labels" tool.

|image16|

This feature was funded by City of Freiburg im Breisgau

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Rendering
---------

Feature: WMS provider resampling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following the ability of QGIS 3.24 to convert WMS raster tiles to elevation data, QGIS has further been enhanced to include various resampling methods to reduce rendering artifacts in WMS DEM sources, such as pixelation encountered with hillshade rendering.

|image17|

This feature was funded by `Maptiler <https://www.maptiler.com/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <http://www.lutraconsulting.co.uk>`__

Feature: Selective masking vectorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS introduced a selective masking feature in `version 3.12 <https://changelog.qgis.org/en/qgis/version/3.12/#selective-masking>`__, however the implementation relied on the rasterization of the map products and made it unsuitable for some cartographic work.

This long awaited feature implements selective masking in a way that vectorizes appropriate masked or clipped features wherever possible, allowing high quality vector outputs for SVG and PDF maps which use the masking features of QGIS.

This is implemented in line with `QEP 186 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/186>`__.

|image18|

This feature was developed by `Julien Cabieces <https://github.com/troopa81>`__

3D Features
-----------

Feature: Transparency support for 3D Phong material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides support for rendering semi transparent objects in 3D. An opacity slider is provided for the phong material widget, which defaults to 100% (fully opaque).

|image19|

This feature was funded by `Swedish QGIS user group. <https://www.qgis.se/>`__

This feature was developed by `Lutra Consulting (Nedjima Belgacem) <http://www.lutraconsulting.co.uk>`__

Feature: 3D Maps inherit terrain settings from project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a new 3D map is created in the project, the map will default to using the same terrain settings as are defined for the project. This makes it easier to create and destroy 3D maps, without having to re-setup their terrain settings each time.

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Sync 2D and 3D navigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new "Navigation sync" setting for 3D map frames provides the ability to automatically synchronize the 2D main map canvas extent and the 3D viewport based on various navigation options.

-  Option 1: Whenever the camera is moved in the 3D view, the main map (2D) canvas extent will be set to the viewed area
-  Option 2: Every change in position on the main map canvas (2D) will result in the 3D camera orientation being shifted to view approximately the same extent from the top (Nadir view position)
-  Option 3: A trapezoid area representing the field of view from the 3D map frame will be drawn on the main map (2D) canvas

Actions are also available for quickly turning these options on and off.

|image20|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Lutra Consulting (Nedjima Belgacem) <http://www.lutraconsulting.co.uk>`__

Feature: 3D axis in 3D map viewer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 3D axis annotation has been added to the 3D map viewer allowing users to better orient their view with their data.

This various additional includes controls and options for:

-  Displaying axis for X/Y/Z or using North/East/South/West based on the frame coordinate reference system (CRS)
-  Displaying a face-labeled cube instead of typical axis arrows

|image21|

This feature was developed by `benoitdm-oslandia <https://github.com/benoitdm-oslandia>`__

Point Clouds
------------

Feature: Point cloud triangulation in 3D views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS can now render point cloud layers in the 3D view as a solid surface, which is obtained by 2.5D triangulation.

Triangulation is configured using a checkbox in the 3D styling options, and configuration options allow exclusion of triangles which surpass user defined thresholds for width or height.

This triangulation is available for all the 3D point cloud renderer styles, including unique color, ramp color, classification, and RGB.

|image22|

This feature was developed by `Vincent Cloarec <https://github.com/vcloarec>`__

Feature: Cloud Optimized Point Clouds (COPC) support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now provides support for reading Cloud Optimized Point Clouds from local and remote data sources.

For more information on the COPC format, visit https://copc.io/.

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Lutra Consulting (Nedjima Belgacem) <https://www.lutraconsulting.co.uk/>`__

Feature: Point cloud filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filtering support has been added for point cloud layers, including a graphical query tool. Using filter expressions, point cloud points on both 2d and 3d canvases may be conditionally displayed based on xyz and/or LAS attributes.

|image23|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Lutra Consulting (Stefanos Natsis) <http://www.lutraconsulting.co.uk>`__

Feature: Point cloud style synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new "Follow 2d renderer" style for 3D point cloud symbology allows for a point cloud layer's 3D symbol to be kept in sync with its 2D counterpart. Any changes to the 2D symbology will be automatically applied to the 3D symbology.

|image12|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Lutra Consulting (Stefanos Natsis) <http://www.lutraconsulting.co.uk>`__

Feature: Improvements to the classified renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Classified renderer for point clouds has been improved to:

- Show only classes that are in the dataset (instead of hard-coded list) & show also non-standard classes
- Show percentage of points for each class
- Work also for other attributes (return number, number of returns, point source and few other classes)

|image55|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Lutra Consulting (Stefanos Natsis) <http://www.lutraconsulting.co.uk>`__


Print Layouts
-------------

Feature: Apply font settings from layer conditional styling to layout attribute tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously, only the font color and background color settings from the conditional styling rules were applied to attribute tables in layouts. Additional styling settings such as font family, bold, italic, strikeout, and underline are now applied from conditional rules.

|image24|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Scalebar Data Defined Overrides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds data defined overrides to the Scalebar layout item. This feature is useful when generating an atlas with the atlas feature containing the scale as a field. The map can be driven by this value, but the scalebar cannot. This implements #48084, which allows the scalebar properties to be data driven by the atlas feature.

|image56|


This feature was developed by `Ethan Snyder <https://github.com/esnyder-rve>`__


Expressions
-----------

Feature: Between/Not between operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now includes support for SQL-like ``BETWEEN`` and ``NOT BETWEEN`` operators in expression clauses.

|image25|

This feature was funded by Kanton Solothurn

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Static parent variable in aggregate expression functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In prior releases of QGIS, aggregate expressions did not pass the parent object parameters as static variables, preventing them from being executed by the data provider (e.g. PostgreSQL). This change will result in significant performance increases for a number of aggregate expressions. For example, in the aggregate expression:

``IF(aggregate(layer:='parks',aggregate:='count', expression:= 't_id', filter:=intersects( $geometry, geometry(@parent))) < 1, 'FALSE', 'TRUE')``

The execution of the ``intersects( $geometry, geometry(@parent))`` filter will be performed on the data provider directly.

This feature was funded by `Amt für Geoinformation Kanton Schaffhausen <https://agi.sh.ch>`__

This feature was developed by `David Signer <https://github.com/signedav>`__

Digitising
----------

Feature: Add a checkbox to disable vertex tool dock auto-opening behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The vertex tool dock now has a new checkbox for "Auto-open table", which is checked by default and retains the existing behavior.

If a user opts to uncheck this, then the vertex editor dock auto open/close behavior will be disabled, leaving the dock as regular QGIS dock which behaves the same as any other dock.

This is desirable in situations when:

-  The user is editing in a full screen session with docks hidden, and doesn't want the vertex editor dock to keep opening itself
-  The user has a heavily customized setup of stacked/tabbed/rearranged docks, and doesn't want the vertex editor dock to keep appearing and disappearing and causing other docks to be rearranged

If a user has opted out of the auto-open table behavior, then the dock can be closed and won't show immediately when switching to the vertex tool. The dock can then be re-opened either through the standard Views - Panels menu (or by right clicking a toolbar), OR through a new "Show Vertex Editor" action which has been added to the dropdown menu for the vertex editor toolbar button.

|image26|

This feature was funded by SevenCs GmbH

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Integrate shape map tools into feature digitizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Shape Tools have been extended and integrated with the features from digitizing tools, allowing the use of map tools to use shapes for digitizing operations.

This includes digitizing support for items such as:

-  StraightSegments
-  CircularStrings
-  Streaming
-  Shapes

This results in the ability to use the add part, add ring, or any other digitizing operations with the shape tools for hybrid digitizing operations, for example using the circular string or rectangle shape tools to create rings in existing area features.

This required significant refactoring and the porting of code from ``QgsMapToolDigitizeFeature`` to ``QgsMapToolCapture``.

|image27|

This feature was developed by `Denis Rouzaud <https://github.com/3nids>`__

Feature: New constraints for advanced digitizing panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The advanced digitizing panel now includes two additional soft constraints (snapping guides) for allowing users to capture positions relative to existing features. These constraints are optionally enabled and include:

-  **Line extension**: QGIS will provide a constraint that traces the extension of a line, based on the segment orientation defined by the selected vertex
-  **Xy vertex**: QGIS will provide a constraint that runs perpendicular to an existing vertex in vertical or horizontal orientation.

|image28|

This feature was funded by Métropole Européenne de Lille @Jean-Roc

This feature was developed by `Antoine Facchini <https://github.com/Koyaani>`__

Data Management
---------------

Feature: Add a "filter rules" search box to vector tile renderer and labeling widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users may now filter the visible rules by a portion of their label, layer or filter strings. This can greatly help with finding rules in complex vector tile styles.

|image29|

This feature was funded by `North Road Consulting <https://north-road.com>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: User defined field names in export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When exporting layers, users may now override the field names in the resulting layers.

The export dialog fields interface includes the following changes:

-  A new "Export names" column has been introduced to the fields table
-  A convenience checkbox is provided to automatically generate aliases, or revert to original field names
-  When field names are modified by the user, the checkbox will display a "PartiallyChecked" state indicator

|image30|

This feature was funded by the Swiss QGIS User Group

This feature was developed by `Damiano Lombardi <https://github.com/domi4484>`__

Feature: Georeferencing vector layers in georeferencer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now supports georeferencing vector layers in the georeferencer tool. This allows vector layers without spatial referencing to be interactively georeferenced, or layers with referencing to be re-referenced, in a similar manner to raster data. Georeferencing occurs in a task, so QGIS should remain responsive, even with large datasets.

Based on `#41386 <https://github.com/qgis/QGIS/pull/41386>`__

|image31|

This feature was funded by the Danish QGIS Usergroup

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Add field domain management capabilities to browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new API has been added to manage field domains through database connections, and QGIS now exposes this functionality through the browser panel.

This functionality is currently exposed only for GeoPackages, but support for other providers could potentially be exposed in future.

Included in this functionality is the ability to create new field domains, as well as set the field domain for GeoPackage table fields.

|image32|

This feature was funded by Provincie Gelderland

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Buffered Transactional Editing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this edit mode, all editable layers are toggled synchronously and all edits are saved in a local edit buffer. Saving changes is executed within a single transaction on all layers (per provider).

This new edit mode attempts to provide a hybrid alternative for managing the data editing approaches used in the current editing modes, local edit buffers and transactional editing, and is implemented in line with `QEP 203 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/203>`__

|image33|

This feature was funded by Kanton Glarus

This feature was developed by `Damiano Lombardi <https://github.com/domi4484>`__

Forms and Widgets
-----------------

Feature: Access form reference in python form actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The form instance, or ``QgsAttributeForm`` object, has now been exposed to the Python API for Drag and drop form actions.

This means that QGIS users can now reference the current form and produce actions that change values within the form itself, such as resetting default values or quick actions for applying other user defined presets.

This implementation has been done in line with `QEP 251 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/251>`__

|image34|

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Allow drag and drop forms label font and color customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The font and color of form labels and group or tabs titles can now be customized in the Drag & Drop from designer interface.

|image35|

This feature was funded by ARPA Piemonte

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Collapse form group by expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New configuration options are now available for Drag & Drop form group boxes which allow specifying an expression to define whether a form group should be collapsed.

|image36|

This feature was funded by ARPA Piemonte

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Analysis Tools
--------------

Feature: "Keep disjoint features separate" option for dissolve algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A "Keep disjoint features separate" option has been added for the dissolve algorithm which will cause features and parts that do not overlap or touch to be exported as separate features instead of parts of a single multipart feature. This makes it much simpler to perform simple aggregation based dissolves on a single class.

|image37|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Processing
----------

Feature: Raise message model tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A raise message algorithm has been added to the model tools which allows users to output additional information in models logs. This prevents the abuse of the raise error/warning algorithms and provides more granular control of model logging levels.

|image38|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Run batch processing steps in tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Individual steps from the batch processing dialog now run as a separate task whenever possible. Although individual steps are still run sequentially rather than parallel, this keeps the UI responsive, and permits responsive cancellation and progress reporting.

This feature was funded by NRCan Contract#3000739399

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Background processing of model algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously, any graphical models designed in Processing would be forced to run on the main thread, and did not support background execution. QGIS now supports running model algorithms off the main thread so that they can safely be run in background tasks.

This feature was funded by NRCan Contract#3000739399

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Allow setting Examples in graphical model help
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new 'Examples' section has been added to the graphical model help editor dialog, allowing users to enter their own custom examples to help explain usage of the model.

More instructive help is now shown for models in the qgis\_process tool, including outputting any example help which has been set.

|image39|

This feature was funded by NRCan Contract#3000739399

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Overlay tools with multiple overlay layers support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds new Intersect, Union and Difference tools which support multiple "overlay" inputs instead of a single overlay layer. The current workflow includes selecting the order of overlay layers used in the operation, which are used in an iterative process by using the output of an operation between two layers as an input for the same operation with the next layer.

This is a useful abstraction which can be utilized in various scenarios, such as processing models where iterative processes or loops may be limited.

|image40|

This feature was developed by `Alexander Bruy <https://github.com/alexbruy>`__

Application and Project Options
-------------------------------

Feature: Project elevation properties framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Elevation/terrain settings are now project-level settings, which are defined through the Project Properties, Terrain tab, in line with `QEP 246 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/246>`__ and in order to support the new elevation profile tools.

This framework provides configuration options for:

-  **Flat terrain** with a configurable terrain height setting
-  **DEM (Raster Layer)** with settings for defining the source raster layer, vertical scale and offset
-  **Mesh** with settings for defining the source mesh layer, vertical scale and offset

|image41|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Optionally store UI configuration in projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An opt-in setting for projects has been added for "Remember attribute table windows and docks between sessions". If checked for a project, then any opened attribute tables will be saved into the project and immediately restored when loading that project.

This has been designed to improve workflows when a user has constructed a project with a particular set of attribute table configurations for their requirements, and re-setting up these attribute tables is a hassle.

|image42|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Optionally store layer edit state in projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An opt-in setting has been added to project properties for "Remember editable layer status between sessions". If checked, then any layers which are editable will be remembered when saving that project and immediately made editable whenever the project is restored to make it simpler for users who are making complex, data-editing focused projects to store their configurations on a project by project basis.

|image43|

This feature was funded by City of Canning

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Project style databases support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new feature allows users to set a list of QGIS style databases for a project. This allows projects to link to multiple style databases, and then show all symbols and entities from those databases in the layer styling interface.

The style paths can point to style .db databases or .xml exports. When a project is loaded, symbol and label style selectors will show ALL symbols from ALL styles linked to the project. Additionally, every project now has a project-specific style database (which is stored alongside the project), for storing project-specific symbols, text formats, etc.

**This functionality requires a QGIS build based on Qt 5.13 or later, and is hidden on older builds (e.g. on Ubuntu 20.04)**

|image44|

This feature was funded by the QGIS Swiss user group.

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Added setting to show feature counts by default for newly added layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If enabled, this option will cause the feature count to be enabled for any newly added/created map layers. This setting will remain disabled by default.

|image45|

This feature was funded by SevenCs GmbH

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Add a "Skip" option for custom environmental variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS settings allow a particular user profile to modify the system environment variables for enhanced flexibility, in Settings --> Options --> Environment.

This functionality included options for "Overwrite", "If Undefined", "Unset", "Prepend", and "Append", which allowed users to perform various functions from configuring credentials to extending their PATH variables.

A new "Skip" option is now provided which allows users to ignore values from an existing field, without losing the stored values or having to remove them from the settings to disable them.

|image46|

This feature was developed by `Andrea Giudiceandrea <https://github.com/agiudiceandrea>`__

Feature: Revamped projects' default symbols, color ramp, and text format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new version of QGIS has revamped the way default projects symbols are handled, aiming at upgrading its UI/UX as well as behaving correctly in multi-user environments. The changes include:

-  Projects' default symbols and color ramps are now stored as symbology XML rather than references, improving portability and integration with external applications and services
-  A new project-level default text format setting has been added to allow user defined configuration of the default project font for newly-added vector layers
-  The user interface has been upgraded to make use of QGIS' symbol and color ramp buttons

|image47|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Profile Plots
-------------

Feature: Elevation profile plotting tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now includes a native elevation profile plotting tool.

The tool includes the following features:

-  Support for vector, raster, mesh, and point cloud layers, based on the corresponding layer's elevation settings.
-  Drawing profile lines interactively using a map tool, which supports snapping, tracing, stream digitizing and curves
-  Picking an existing line feature to use as the profile line. When this tool is active, users can click any line feature on the map to generate a profile curve along that line. If multiple features are present at the clicked point then a popup menu will appear allowing users to select from the available features.
-  Plots can be exported to PDF (as high quality vector objects) or various image formats
-  Profiles are rendered using standard QGIS line symbols, and so include support for advanced design and configuration, including support for geometry generators and paint effects.
-  Measuring distances on the plots
-  Identifying features in the plot via either a single click, or click-and-drag rectangle. Results are shown in the standard identify results dock, and support vector, raster, mesh, and point cloud layers.

Interactive navigation of the plot canvas is supported using the standard QGIS pan/zoom shortcuts, such as:

-  Middle mouse button: Pan
-  Space: Pan
-  Ctrl + Space: Zoom
-  Ctrl + Mouse wheel: Fine zoom

Shortcuts are available for nudging the elevation profile curve left and right, which allows users to "scrub" the curve across the map frame and find the optimal profile line. The step distance is set to match the chart's tolerance distance, so that a single step will result in a different set of point and point cloud features shown in the chart.

Keyboard shortcuts for nudging are:

-  Ctrl+Alt+,: Scrub left
-  Ctrl+Alt+.: Scrub right

For more information on this awesome feature and framework, be sure to watch the `QGIS Elevation Profiles Deep Dive <https://www.youtube.com/watch?v=AknJjNPystU>`__ presentation on YouTube.

|image48|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Flexible vector layer symbology in elevation profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vector layers added to profile charts will default to respecting their layer symbology. A checkbox has been added to disable this in the layer elevation properties.

This means that vector results in elevation profile charts will default to showing features using their corresponding 2D renderer, so custom styles such as categorized classes will be visible on the profile chart by default.

There's also options to change the interpretation of the elevation profile for vector layers. By default, the elevation profile tool will use an "individual features" option, which samples discrete positions where the cross section profile line intersects the vector features. There's also a "continuous surface" option which will generate an interpretation of the surface by interpolating across the sample positions for enhanced visualization, such as the production of a continuous surface line from contour lines or surveyed elevation points.

Additional rendering capabilities are provided for the "continuous surface" interpretation option, such as a "fill below" symbol style. This can be easier to interpret in some cases, and helps match expected symbology conventions in certain disciplines.

|image49|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Flexible symbology for point cloud profile plotting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Point cloud layers in profile charts include the following symbology features:

-  Single color display of points or a setting to inherit classification and coloring from the 2D symbology (e.g. RGB colors)
-  Respecting the profile curve distance tolerance setting
-  Option to reduce the opacity of points which are further from the profile curve
-  Automatic refinement based on plot visible area and scale, with a user controllable max screen error
-  Control over appearance of points (color, size and shape)

|image50|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: Vector feature extrusion for profile charts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The elevation profile tool provides support for vector feature extrusion and offset heights for incorporation of 2D vector in profile charts. These propertied can be data defined, and will also be used as the default offset/extrusion settings for any new 3D polygon symbols created for that layer.

|image51|

This feature was funded by `Crowdfunding for raster and point clouds improvements <https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Browser
-------

Feature: Rename bookmark groups context menu control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating new spatial bookmarks from the browser will now default to the "project bookmark" category, and a new context menu option has been added for renaming of bookmark groups. The existing behavior of renaming bookmark groups using the F2 key remains unchanged.

|image52|

This feature was funded by `Camptocamp <https://www.camptocamp.com>`__

This feature was developed by `Ismail Sunni <https://github.com/ismailsunni>`__

Data Providers
--------------

Feature: Support reading ESRI vector tile packages (.vtpk) files directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ESRI vector tile packages (VTPK files) can now be opened directly as vector tile layers via drag and drop, including support for style translation.

This feature was funded by `North Road Consulting, thanks to SLYR <https://north-road.com/slyr/>`__

This feature was developed by `Nyall Dawson (North Road Consulting) <https://north-road.com>`__

Feature: SQL Logging in the Debugging/Development panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The debugging/development panel now includes support for logging the SQL queries made by QGIS to backend data providers.

This provides an effective method of debugging algorithms and data providers, as well as capturing the SQL statements made to perform specific actions against particular providers.

Note that this is specifically designed to be used as a debugging and development tool and is not designed to be a replacement for any logging capabilities on the backend databases systems.

This has been implemented in line with `QEP 242 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/242>`__.

|image53|

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

QGIS Server
-----------

Feature: Alternate periodic check strategy for detecting project updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS Server now provides an alternate lastModified() strategy for invalidating the internal project cache, addressing concerns about the ability of QGIS server to invalidate the cache when a project file is updated on atypical file systems, such as NFS, or when the project file is stored in a database system like PostgreSQL.

An asynchronous periodic check strategy using the last modified value of a project is now provided for checking project configuration for changes.

The ``QGIS_SERVER_PROJECT_CACHE_STRATEGY`` environment variable may be used to configure the server caching strategy using the following values:

-  ``periodic`` for the alternative strategy
-  ``filesystem`` to use the file system watcher strategy
-  ``off`` to disable internal caching completely.

``QGIS_SERVER_PROJECT_CACHE_CHECK_INTERVAL`` is used for controlling the periodic strategy interval.

The ``QFileSystemWatcher`` strategy remains the default configuration.

This feature was funded by `3Liz <https://3liz.com>`__

This feature was developed by `David Marteau <https://github.com/dmarteau>`__

Feature: Add more server highlight label parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New parameters have been added to better control the placement of highlight labels on the WMS server, including:

-  ``HIGHLIGHT_LABELDISTANCE``: Distance between the feature and the label, defined in mm
-  ``HIGHLIGHT_LABELROTATION``: Label rotation, defined in degrees
-  ``HIGHLIGHT_LABELVALI``: Vertical alignment for placing the label directly on a point
-  ``HIGHLIGHT_LABELHALI``: Horizontal alignment for placing the label directly on a point

This feature was developed by `mhugent <https://github.com/mhugent>`__

Feature: Temporal properties support for WMS Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior releases of QGIS Server only provided support for the dimensions of time and elevation for vector layers and provided no integration with the updated temporal properties API provided by QGIS.

QGIS Server has now been extended to support the time dimension in the ``GetCapabilities`` response for WMS services, and accept a ``TIME`` query string parameter which provides capacity for temporal data filtering.

Parsing time values will be performed with the implementation specification provided by OGC API - Features (OAPIF) and use the following structure:

\| interval\| syntax \| \|---\|---\| \| interval-closed \| date-time "/" date-time \| \| interval-open-start \| [".."] "/" date-time \| \| interval-open-end \| date-time "/" [".."] \| \| interval \| interval-closed / interval-open-start / interval-open-end \| \| datetime \| date-time / interval \|

Note that this filtering applies to single values only, and a list of instants or ranges is not currently supported.

To prevent conflict with existing TIME dimension stipulations on legacy projects, if a ``TIME`` dimension was explicitly defined for a vector layer, the temporal properties for that layer will not be activated and the explicitly set ``TIME`` dimension will be considered instead.

This feature was funded by Gis3W

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Programmability
---------------

Feature: Add a QgsScaleCalculator function to calculate canvas width from a given extent, scale, and dpi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``calculateCanvasWidth( extent, scale )`` was added to the ``QgsScaleCalculator`` class to derive canvas width in pixel unit when providing an extent, a scale, and a DPI.

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Clear current symbol action in symbol button widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A set to null / clear current symbol action has been added to clear the current symbol attached to a symbol button widget.

|image54|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Notable Fixes
-------------

Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Bug Title                                                                              | URL Issues (if reported, Github)                         | URL Commit (Github)                                          | 3.22 backport commit (GitHub)                                |
+========================================================================================+==========================================================+==============================================================+==============================================================+
| WFS provider doesn't recognize CRS strings other than OGC URNs                         | `#46485 <https://github.com/qgis/QGIS/issues/46485>`__   | `PR #48550 <https://github.com/qgis/QGIS/pull/48550>`__      | N/A                                                          |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| QgsMapCanvas::showEvent access violation / QGIS crash                                  | `#48438 <https://github.com/qgis/QGIS/issues/48438>`__   | `PR #48551 <https://github.com/qgis/QGIS/pull/48551>`__      | `PR #48558 <https://github.com/qgis/QGIS/pull/48558>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| [GDAL provider] Minimal support for GDT\_Int64/GDT\_UInt64 of GDAL 3.5.0               | (not reported)                                           | `PR #48553 <https://github.com/qgis/QGIS/pull/48553>`__      |                                                              |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| access to QgsRubberBand-methods crashes QGis                                           | `#48471 <https://github.com/qgis/QGIS/issues/48471>`__   | `PR #48554 <https://github.com/qgis/QGIS/pull/48554>`__      | `PR #48561 <https://github.com/qgis/QGIS/pull/48561>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| annotationManager with access to canvas-items crashes QGis                             | `#48436 <https://github.com/qgis/QGIS/issues/48436>`__   | `PR #48554 <https://github.com/qgis/QGIS/pull/48554>`__      | `PR #48561 <https://github.com/qgis/QGIS/pull/48561>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Can not import excel File with new version of QGIS                                     | `#47838 <https://github.com/qgis/QGIS/issues/47838>`__   | N/A - freexl bug. Patch submitted to upstream                | N/A                                                          |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Layers added by QGIS are not correct if datasource is a collection                     | `#47610 <https://github.com/qgis/QGIS/issues/47610>`__   | `PR #48556 <https://github.com/qgis/QGIS/pull/48556>`__      | `PR #48572 <https://github.com/qgis/QGIS/pull/48572>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| SQLite: No Spatial Index Creation though QGIS misleadingly reports success             | `#44513 <https://github.com/qgis/QGIS/issues/44513>`__   | `PR #48557 <https://github.com/qgis/QGIS/pull/48557>`__      | `PR #48565 <https://github.com/qgis/QGIS/pull/48565>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Saving a large edited point layer takes far too long                                   | `#46355 <https://github.com/qgis/QGIS/issues/46355>`__   | `GDAL PR 5730 <https://github.com/OSGeo/gdal/pull/5730>`__   | `GDAL PR 5753 <https://github.com/OSGeo/gdal/pull/5753>`__   |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Non-existent but registered attribute table in GPKG is added as empty table            | `#30670 <https://github.com/qgis/QGIS/issues/30670>`__   | `GDAL PR 5752 <https://github.com/OSGeo/gdal/pull/5752>`__   | Not appropriate                                              |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Accents displayed incorrectly when saving metadata to geopackage                       | `#47435 <https://github.com/qgis/QGIS/issues/47435>`__   | `PR #48625 <https://github.com/qgis/QGIS/pull/48625>`__      | `PR #48631 <https://github.com/qgis/QGIS/pull/48631>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Raster tiles are clipped based on the gpkg\_contents bounding box of a GeoPackage      | `#45530 <https://github.com/qgis/QGIS/issues/45530>`__   | Not a bug                                                    |                                                              |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Pan-action freeze after use of middle mouse button and 'copy coordinate'               | `#48645 <https://github.com/qgis/QGIS/issues/48645>`__   | `PR #48666 <https://github.com/qgis/QGIS/pull/48666>`__      | `PR #48684 <https://github.com/qgis/QGIS/pull/48684>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| New GeoPackage layer cannot be loaded (QGIS thinks it's invalid but it isn't really)   | `#48671 <https://github.com/qgis/QGIS/issues/48671>`__   | `PR #48692 <https://github.com/qgis/QGIS/pull/48692>`__      | `PR #48774 <https://github.com/qgis/QGIS/pull/48774>`__      |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| [regression] New filter for duplicated WFS layer is also applied on source layer       | `#48465 <https://github.com/qgis/QGIS/issues/48465>`__   | `PR #48998 <https://github.com/qgis/QGIS/pull/48998>`__      | N/A                                                          |
+----------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+

These bugfixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

Bugs fixed by `Even Rouault <https://www.spatialys.com/>`__

Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                                                | URL Issues (if reported, Github)                                                                       | URL Commit (Github)                                                                     | 3.22 backport commit (GitHub)                             |
+==========================================================================================================================================+========================================================================================================+=========================================================================================+===========================================================+
| @project\_keywords are no longer tested on Rule based filters                                                                            | `#48480 <https://github.com/qgis/QGIS/issues/48480>`__                                                 | Not a bug                                                                               |                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| No more styles after duplicate layer and change filter in query builder in 3.22.6                                                        | `#48467 <https://github.com/qgis/QGIS/issues/48467>`__                                                 | Works for me on 3.24.2 and master                                                       |                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| MSSQL Add Connection Dialog never enables OK button                                                                                      | `#48462 <https://github.com/qgis/QGIS/issues/48462>`__                                                 | Works for me on master                                                                  |                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Highlight of identified feature not displaying correctly on "geometry generator" marker from different CRS                               | `#48439 <https://github.com/qgis/QGIS/issues/48439>`__                                                 | `PR #48579 <https://github.com/qgis/QGIS/pull/48579>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Cannot past copied features as temporary scratch layer                                                                                   | `#48401 <https://github.com/qgis/QGIS/issues/48401>`__                                                 | `PR #48611 <https://github.com/qgis/QGIS/pull/48611>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS crash by opening a form with relation content                                                                                       | `#48443 <https://github.com/qgis/QGIS/issues/48443>`__                                                 | `PR #48616 <https://github.com/qgis/QGIS/pull/48616>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Relation reference widget: filter expression does not work with variables                                                                | `#48190 <https://github.com/qgis/QGIS/issues/48190>`__                                                 | `PR #48619 <https://github.com/qgis/QGIS/pull/48619>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Random order of attributes in oracle feature query                                                                                       | `#35309 <https://github.com/qgis/QGIS/issues/35309>`__                                                 | `PR #48668 <https://github.com/qgis/QGIS/pull/48668>`__                                 | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| CSV datasource not converted from 3.16 to 3.22 correctly - projects not usable anymore                                                   | `#48587 <https://github.com/qgis/QGIS/issues/48587>`__                                                 | Works for me on 3.24 and master                                                         |                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Documentation doctest failure                                                                                                            | `QGIS developer mail list <https://lists.osgeo.org/pipermail/qgis-developer/2022-May/064720.html>`__   | `QGIS Documentation PR 7581 <https://github.com/qgis/QGIS-Documentation/pull/7581>`__   | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| "Add to group" option in sub layer window always add at top of layer tree                                                                | `#48694 <https://github.com/qgis/QGIS/issues/48694>`__                                                 | `PR #48696 <https://github.com/qgis/QGIS/pull/48696>`__                                 | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Name/id of map objects in GetProjectSettings follows an order that is the inverse of the order used to add the map objects in a layout   | `#46143 <https://github.com/qgis/QGIS/issues/46143>`__                                                 | `PR #48728 <https://github.com/qgis/QGIS/pull/48728>`__                                 | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Aborted inserts in Postgis geometryless tables are saved anyway                                                                          | `#48171 <https://github.com/qgis/QGIS/issues/48171>`__                                                 | `PR #48741 <https://github.com/qgis/QGIS/pull/48741>`__                                 | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Inconsistent coordinate rounding in Raster "Layer Properties"                                                                            | `#48767 <https://github.com/qgis/QGIS/issues/48767>`__                                                 | `PR #48790 <https://github.com/qgis/QGIS/pull/48790>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Drag and Drop Postgis-Table in QGIS Browser alters name of Geometry-Column                                                               | `#48748 <https://github.com/qgis/QGIS/issues/48748>`__                                                 | `PR #48796 <https://github.com/qgis/QGIS/pull/48796>`__                                 | no                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Layer filter does not work on multiline strings values with linebreaks                                                                   | `#47530 <https://github.com/qgis/QGIS/issues/47530>`__                                                 | `PR #48818 <https://github.com/qgis/QGIS/pull/48818>`__                                 | no need                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| QGIS Crashes while searching in the expression builder                                                                                   | `#48189 <https://github.com/qgis/QGIS/issues/48189>`__                                                 | `PR #48856 <https://github.com/qgis/QGIS/pull/48856>`__                                 | `PR #48864 <https://github.com/qgis/QGIS/pull/48864>`__   |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Server GetPrint with multiple maps following map themes apply prefixed LAYERS (map0:LAYERS) to all maps                                  | `PR #48923 <https://github.com/qgis/QGIS/pull/48923>`__                                                | `PR #48923 <https://github.com/qgis/QGIS/pull/48923>`__                                 | TODO                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------+

These bugfixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

Bugs fixed by `Alessandro Pasotti <https://www.qcooperative.net/>`__

Bug fixes by Alex Bruy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                     | URL Issues (if reported, Github)                         | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+===============================================================================================+==========================================================+===========================================================+===========================================================+
| QgsProcessingParameterMultipleLayers adds an extra list element when reordering inputs        | `#45634 <https://github.com/qgis/QGIS/issues/45634>`__   | Works for me on 3.24 and master                           |                                                           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| GDAL Vector to Raster (gdal\_rasterize) fail to produce ESRI ASCII as output                  | `#39140 <https://github.com/qgis/QGIS/issues/39140>`__   | Not a bug                                                 |                                                           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Processing: Drape / qgis:setzfromraster inconsistent NODATA behaviour                         | `#43650 <https://github.com/qgis/QGIS/issues/43650>`__   | Works for me on master                                    |                                                           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Algorithm output node is placed half outsize model canvas                                     | `#48132 <https://github.com/qgis/QGIS/issues/48132>`__   | `PR #48600 <https://github.com/qgis/QGIS/pull/48600>`__   | `PR #48661 <https://github.com/qgis/QGIS/pull/48661>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Inconsequence in CRS-names/id's in Copy Coordinate in MapCanvas                               | `#37226 <https://github.com/qgis/QGIS/issues/37226>`__   | `PR #48599 <https://github.com/qgis/QGIS/pull/48599>`__   |                                                           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QGIS Batch Mode Populating Form are producing gaps between rows                               | `#43869 <https://github.com/qgis/QGIS/issues/43869>`__   | `PR #48601 <https://github.com/qgis/QGIS/pull/48601>`__   | `PR #48636 <https://github.com/qgis/QGIS/pull/48636>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Processing settings dialog cleared after a search is done in Settings dialog                  | `#34543 <https://github.com/qgis/QGIS/issues/34543>`__   | `PR #48602 <https://github.com/qgis/QGIS/pull/48602>`__   | `PR #48633 <https://github.com/qgis/QGIS/pull/48633>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QgsProcessingAlgorithm with FlagHideFromModeler flag is still visible in the Model Designer   | `#48586 <https://github.com/qgis/QGIS/issues/48586>`__   | `PR #48603 <https://github.com/qgis/QGIS/pull/48603>`__   | `PR #48632 <https://github.com/qgis/QGIS/pull/48632>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Batch Nominatim Geocoder output directly saved to file has no CRS                             | `#48385 <https://github.com/qgis/QGIS/issues/48385>`__   | `PR #48618 <https://github.com/qgis/QGIS/pull/48618>`__   | `PR #48708 <https://github.com/qgis/QGIS/pull/48708>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Iterating over features in processing algorithm not creating correct destination folder       | `#48383 <https://github.com/qgis/QGIS/issues/48383>`__   | `PR #48646 <https://github.com/qgis/QGIS/pull/48646>`__   | `PR #48657 <https://github.com/qgis/QGIS/pull/48657>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Dragging multiple layers in processing algorithm layer selection widget crashes QGIS          | `#47728 <https://github.com/qgis/QGIS/issues/47728>`__   | `PR #48649 <https://github.com/qgis/QGIS/pull/48649>`__   | `PR #48656 <https://github.com/qgis/QGIS/pull/48656>`__   |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

These bugfixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

Bugs fixed by `Alex Bruy <https://www.qcooperative.net/>`__

Bug fixes by Sandro Santilli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                | URL Issues (if reported, Github)                                                    | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+==========================================================================================+=====================================================================================+===========================================================+===========================================================+
| Add simple bash script to run tests as done by CI                                        | `QGIS QEP #244 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/244>`__   | `PR #48617 <https://github.com/qgis/QGIS/pull/48617>`__   | Not appropriate                                           |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| test\_provider\_eptprovider occasionally aborts                                          | `#48778 <https://github.com/qgis/QGIS/issues/48778>`__                              | `PR #48793 <https://github.com/qgis/QGIS/pull/48793>`__   | not needed                                                |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Issue with QgsVectorLayerUndoCommand class (QGIS crashes)                                | `#23243 <https://github.com/qgis/QGIS/issues/23243>`__                              | `PR #48700 <https://github.com/qgis/QGIS/pull/48700>`__   | `PR #48934 <https://github.com/qgis/QGIS/pull/48934>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Check that source files are not overridden                                               | `#25830 <https://github.com/qgis/QGIS/issues/25830>`__                              | `PR #48654 <https://github.com/qgis/QGIS/pull/48654>`__   | Not appropriate                                           |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| TestQgsGdalProvider failures in absence of netcdf support                                | `#48906 <https://github.com/qgis/QGIS/issues/48906>`__                              | `PR #48907 <https://github.com/qgis/QGIS/pull/48907>`__   | `PR #48926 <https://github.com/qgis/QGIS/pull/48926>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| test\_core\_gdalprovider modifies tests/testdata/zip/landsat\_b1.zip source file         | `#48846 <https://github.com/qgis/QGIS/issues/48846>`__                              | `PR #48917 <https://github.com/qgis/QGIS/pull/48917>`__   | `PR #48926 <https://github.com/qgis/QGIS/pull/48926>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Drop gpkg\_metadata\_reference\_column\_name\_update trigger generated by GDAL < 2.4.0   | N/A                                                                                 | `PR #48953 <https://github.com/qgis/QGIS/pull/48953>`__   | `PR #48957 <https://github.com/qgis/QGIS/pull/48957>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix test analysis processing modification of source files                                | `#48937 <https://github.com/qgis/QGIS/issues/48937>`__                              | `PR #48959 <https://github.com/qgis/QGIS/pull/48959>`__   | `PR #48961 <https://github.com/qgis/QGIS/pull/48961>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| ctest: No module named 'qgis.server'                                                     | `#48958 <https://github.com/qgis/QGIS/issues/48958>`__                              | `PR #48993 <https://github.com/qgis/QGIS/pull/48993>`__   | `PR #48999 <https://github.com/qgis/QGIS/pull/48999>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| PyQgsLocalServer test fails: AttributeError: module 'platform' has no attribute 'dist'   | `#48962 <https://github.com/qgis/QGIS/issues/48962>`__                              | `PR #48976 <https://github.com/qgis/QGIS/pull/48976>`__   | `PR #49028 <https://github.com/qgis/QGIS/pull/49028>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix old GDAL triggers in geopackage files                                                | N/A                                                                                 | `PR #49037 <https://github.com/qgis/QGIS/pull/49037>`__   | `PR #49039 <https://github.com/qgis/QGIS/pull/49039>`__   |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

These bugfixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

Bugs fixed by `Sandro Santilli (strk) <https://strk.kbt.io/>`__

Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                      | URL Issues (if reported, Github)                                          | URL Commit (Github)                                                                                    | 3.22 backport commit (GitHub)                             |
+================================================================================================================+===========================================================================+========================================================================================================+===========================================================+
| layer\_property(..., 'path') should work for all layer types                                                   | `#49011 <https://github.com/qgis/QGIS/issues/49011>`__                    | `PR #49042 <https://github.com/qgis/QGIS/pull/49042>`__                                                | `PR #49046 <https://github.com/qgis/QGIS/pull/49046>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Improve UX for virtual layer creation dialog                                                                   | unreported                                                                | `PR #49015 <https://github.com/qgis/QGIS/pull/49015>`__                                                | Not appropriate                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| [db manager] Don't load preview layers into project                                                            | `#47159 <https://github.com/qgis/QGIS/issues/47159>`__                    | `PR #49016 <https://github.com/qgis/QGIS/pull/49016>`__                                                | `PR #49019 <https://github.com/qgis/QGIS/pull/49019>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Don't hang when an error occurs while trying to build a virtual layer                                          | `#48908 <https://github.com/qgis/QGIS/issues/48908>`__                    | `Commit 988edc8700 <https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5>`__   | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Don't offer non-vector layer providers as options for virtual layer                                            | `#48908 <https://github.com/qgis/QGIS/issues/48908>`__                    | `Commit 988edc8700 <https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5>`__   | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix selecting/deselecting all in offline editing dialog when some layers are in unchecked groups               | `#48971 <https://github.com/qgis/QGIS/issues/48971>`__                    | `PR #48985 <https://github.com/qgis/QGIS/pull/48985>`__                                                | `PR #49002 <https://github.com/qgis/QGIS/pull/49002>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix hovering features in attribute table in dark themes selects them                                           | `#48914 <https://github.com/qgis/QGIS/issues/48914>`__                    | `PR #48986 <https://github.com/qgis/QGIS/pull/48986>`__                                                | `PR #49001 <https://github.com/qgis/QGIS/pull/49001>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix atlas expression context is not available when rendering item overview frames                              | `#48963 <https://github.com/qgis/QGIS/issues/48963>`__                    | `PR #48967 <https://github.com/qgis/QGIS/pull/48967>`__                                                | `PR #48984 <https://github.com/qgis/QGIS/pull/48984>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix regression where layout attribute table conditional styles don't apply                                     | `#48965 <https://github.com/qgis/QGIS/issues/48965>`__                    | `PR #48968 <https://github.com/qgis/QGIS/pull/48968>`__                                                | `PR #48973 <https://github.com/qgis/QGIS/pull/48973>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Review and finish open PR `PR #48314 <https://github.com/qgis/QGIS/pull/48314>`__                              |                                                                           |                                                                                                        |                                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix geometry based expression attributes for diagrams                                                          | `#47800 <https://github.com/qgis/QGIS/issues/47800>`__                    | `PR #48893 <https://github.com/qgis/QGIS/pull/48893>`__                                                | `PR #48911 <https://github.com/qgis/QGIS/pull/48911>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix loss of precision when an extent is manually entered in processing extent widgets                          | `#48887 <https://github.com/qgis/QGIS/issues/48887>`__                    | `PR #48895 <https://github.com/qgis/QGIS/pull/48895>`__                                                | `PR #48910 <https://github.com/qgis/QGIS/pull/48910>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix some undersized icons on hidpi displays                                                                    | unreported                                                                | `PR #48875 <https://github.com/qgis/QGIS/pull/48875>`__                                                | Not appropriate                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Make atlas coverage layer available to expression builder for custom grid format                               | `#48833 <https://github.com/qgis/QGIS/issues/48833>`__                    | `PR #48839 <https://github.com/qgis/QGIS/pull/48839>`__                                                | `PR #48894 <https://github.com/qgis/QGIS/pull/48894>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix regression where user defined default style doesn't apply to MapInfo TAB files                             | `#48667 <https://github.com/qgis/QGIS/issues/48667>`__                    | `PR #48840 <https://github.com/qgis/QGIS/pull/48840>`__                                                | `PR #48892 <https://github.com/qgis/QGIS/pull/48892>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix picking values from QgsFeatureListComboBox                                                                 | `#48459 <https://github.com/qgis/QGIS/issues/48459>`__                    | `PR #48841 <https://github.com/qgis/QGIS/pull/48841>`__                                                | `PR #48881 <https://github.com/qgis/QGIS/pull/48881>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix clear values for offset along line spin boxes                                                              | unreported                                                                | `PR #48872 <https://github.com/qgis/QGIS/pull/48872>`__                                                | `PR #48878 <https://github.com/qgis/QGIS/pull/48878>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix ambiguous "show all labels" setting and address regressions in label when this setting is misinterpreted   | `#41043 <https://github.com/qgis/QGIS/issues/41043>`__                    | `PR #48771 <https://github.com/qgis/QGIS/pull/48771>`__                                                | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Main annotation layer should follow project crs unless it has items added                                      | `#42378 <https://github.com/qgis/QGIS/issues/42378>`__                    | `PR #48815 <https://github.com/qgis/QGIS/pull/48815>`__                                                | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix some misleading warnings about transformations for non-earth crs                                           | `#42378 <https://github.com/qgis/QGIS/issues/42378>`__                    | `PR #48815 <https://github.com/qgis/QGIS/pull/48815>`__                                                | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Never show the transformation selection dialog for the first layer added to a project                          | unreported                                                                | `PR #48811 <https://github.com/qgis/QGIS/pull/48811>`__                                                | `PR #48814 <https://github.com/qgis/QGIS/pull/48814>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Ensure layer level expressions work correctly for diagrams                                                     | `#47800 <https://github.com/qgis/QGIS/issues/47800>`__\ 0                 | `PR #48803 <https://github.com/qgis/QGIS/pull/48803>`__                                                | `PR #48813 <https://github.com/qgis/QGIS/pull/48813>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix handling of WMTS sources with dimensions in browser                                                        | `#36264 <https://github.com/qgis/QGIS/issues/36264>`__                    | `PR #48800 <https://github.com/qgis/QGIS/pull/48800>`__                                                | `PR #48812 <https://github.com/qgis/QGIS/pull/48812>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Ensure that all units are changed when setting output unit for a symbol                                        | `#45961 <https://github.com/qgis/QGIS/issues/45961>`__                    | `PR #48786 <https://github.com/qgis/QGIS/pull/48786>`__                                                |                                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix loss of mesh layer styling when fixing a broken path to a mesh layer                                       | unreported                                                                | `PR #48765 <https://github.com/qgis/QGIS/pull/48765>`__                                                | `PR #48768 <https://github.com/qgis/QGIS/pull/48768>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Show pinned label highlights also for pinned curved labels                                                     | `#48753 <https://github.com/qgis/QGIS/issues/48753>`__                    | `PR #48764 <https://github.com/qgis/QGIS/pull/48764>`__                                                | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Don't hide parts of the mesh renderer widget if the layer is invalid                                           | unreported                                                                | `PR #48757 <https://github.com/qgis/QGIS/pull/48757>`__                                                |                                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Add layer opacity widget in mesh layer renderer properties widget                                              | unreported                                                                | `PR #48756 <https://github.com/qgis/QGIS/pull/48756>`__                                                |                                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Review and finish open PR `PR #44941 <https://github.com/qgis/QGIS/pull/44941>`__                              |                                                                           |                                                                                                        |                                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix a crash when QgsProject::instance() is accessed when no QgsApplication exists                              | unreported                                                                | `PR #48721 <https://github.com/qgis/QGIS/pull/48721>`__                                                | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Better approach to filtering lists by tags which works across different styles                                 | `#48659 <https://github.com/qgis/QGIS/issues/48659>`__                    | `PR #48689 <https://github.com/qgis/QGIS/pull/48689>`__                                                | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix slow layout view when atlas is enabled with legend filter enabled                                          | `#47033 <https://github.com/qgis/QGIS/issues/47033>`__                    | `PR #48686 <https://github.com/qgis/QGIS/pull/48686>`__                                                | `PR #48704 <https://github.com/qgis/QGIS/pull/48704>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix crash after running model from history dialog                                                              | `#40258 <https://github.com/qgis/QGIS/issues/40258>`__                    | `PR #48687 <https://github.com/qgis/QGIS/pull/48687>`__                                                | `PR #48709 <https://github.com/qgis/QGIS/pull/48709>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix crash on QGIS exit                                                                                         | likely solves a number of open tickets, but needs end user confirmation   | `Commit 5b052730b5 <https://github.com/qgis/QGIS/commit/5b052730b5c10f12570dd5e68fca1962f113b3f3>`__   | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Add support for map field types to memory provider, avoid data loss in models/processing                       | unreported                                                                | `PR #48638 <https://github.com/qgis/QGIS/pull/48638>`__                                                | Too intrusive                                             |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix crash when convertng a curved geometry to curves                                                           | `#48045 <https://github.com/qgis/QGIS/issues/48045>`__                    | `#48045 <https://github.com/qgis/QGIS/issues/48045>`__                                                 | `PR #49024 <https://github.com/qgis/QGIS/pull/49024>`__   |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix many memory leaks                                                                                          | unreported                                                                | `PR #48590 <https://github.com/qgis/QGIS/pull/48590>`__                                                | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Fix ctrl modifier scrolling on symbol buttons                                                                  | unreported                                                                | `PR #48581 <https://github.com/qgis/QGIS/pull/48581>`__                                                | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

These bugfixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

Bugs fixed by `Nyall Dawson <https://north-road.com/>`__

.. |image1| image:: images/projects/916ce336f8f5939eb158506ea38290af6f1ce0f0.png
   :class: img-responsive img-rounded center-block
.. |image3| image:: images/entries/d2f2d4bf5b05b7e21aa6ff0957ad8be8ccda082f.gif
   :class: img-responsive img-rounded
.. |image4| image:: images/entries/7dada94231069c7f647d9a4a239d57506ad14bfd.gif
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/965a5e626ced053fd00fc33288c17330b7f920a0.gif
   :class: img-responsive img-rounded
.. |image6| image:: images/entries/0ecfdc2b0f6dae82ab5650f4d1d97d37df33aee4.gif
   :class: img-responsive img-rounded
.. |image7| image:: images/entries/0075fa6cc3b8410072eeec8bb43ac4cef4c38e61.png
   :class: img-responsive img-rounded
.. |image8| image:: images/entries/ab668355973259b389bd2623c4b1ba01b5e8f237.gif
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/7bf2a8d0d0500149ed7b1cb5edb22b8cd6258c86.gif
   :class: img-responsive img-rounded
.. |image10| image:: images/entries/e5330839c8c13220ccbbb2ea1c5fc556548a21be.gif
   :class: img-responsive img-rounded
.. |image11| image:: images/entries/c5c8938147137d9264d57a56c00548cc535cdaa2.gif
   :class: img-responsive img-rounded
.. |image12| image:: images/entries/9fde94a418b67018b72ad7d0e71c01cf9bc19afa.png
   :class: img-responsive img-rounded
.. |image13| image:: images/entries/5f4efe2866e8ba166c3948fb22946ec1ed3fa02b.gif
   :class: img-responsive img-rounded
.. |image14| image:: images/entries/201cc3be8689d55102c675c4af0ffdf4204c2a2b.png
   :class: img-responsive img-rounded
.. |image15| image:: images/entries/0bd238b2326485fe91d8dd6f2aa8956e5534a5e3.png
   :class: img-responsive img-rounded
.. |image16| image:: images/entries/31ad531d280be178c752850a8860a95f2b8c3bf2.gif
   :class: img-responsive img-rounded
.. |image17| image:: images/entries/60b9ae3354e9c6e2086986aee3b0828dc738187f.gif
   :class: img-responsive img-rounded
.. |image18| image:: images/entries/c717fac5bdd68a9f803738c77a5637fc070823e0.png
   :class: img-responsive img-rounded
.. |image19| image:: images/entries/38a2c9b60971a3056d2749373b2153e59eb0b3e1.png
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/9438a5861c6891d7123bdba4918fd4cd9da82343.png
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/bc7d732eed29aa4c9cd5a3888d2b80262960f41a.gif
   :class: img-responsive img-rounded
.. |image22| image:: images/entries/4b103066398ae065f4e3eb1e898356fceda8ef1d.png
   :class: img-responsive img-rounded
.. |image23| image:: images/entries/a86ac2e8e5f5f1dbdc9630e2b71d4e62686362d9.png
   :class: img-responsive img-rounded
.. |image24| image:: images/entries/a15e95f80ef5f86dd2de37e4e1642984db89f8a9.gif
   :class: img-responsive img-rounded
.. |image25| image:: images/entries/01fbc5c6454d48b126daa9597332ca8e94811608.gif
   :class: img-responsive img-rounded
.. |image26| image:: images/entries/b8569c513e1dffa0fabb253e8074588d44cce5eb.gif
   :class: img-responsive img-rounded
.. |image27| image:: images/entries/c0a8faef50107305ea8a04e92f68f9d7518507ff.gif
   :class: img-responsive img-rounded
.. |image28| image:: images/entries/4a68cb3c6e9a4f55c5f95ca4b827405ce0aed526.gif
   :class: img-responsive img-rounded
.. |image29| image:: images/entries/1cb1d1557bac8d4552a3ef617a27e0fcf9c082ff.gif
   :class: img-responsive img-rounded
.. |image30| image:: images/entries/77669a9cc8355f9fae0e331a28de7ace46e730d6.gif
   :class: img-responsive img-rounded
.. |image31| image:: images/entries/b6e89fcd31aec118497af05f94586d2bbf6f4491.gif
   :class: img-responsive img-rounded
.. |image32| image:: images/entries/e5f0feb4e3c4d925c98336d8938170ac9bb9fc1c.gif
   :class: img-responsive img-rounded
.. |image33| image:: images/entries/c7c3eea32a0cf34a07a9325fd87fdefcf8afb280.png
   :class: img-responsive img-rounded
.. |image34| image:: images/entries/8f71244038218dae15182ee507699de0050b405d.gif
   :class: img-responsive img-rounded
.. |image35| image:: images/entries/df03bff457eac65712cad54d0acee177526a3f13.png
   :class: img-responsive img-rounded
.. |image36| image:: images/entries/d601af9dff97189a63c0c9d7125ad9d50de3ff66.png
   :class: img-responsive img-rounded
.. |image37| image:: images/entries/350b223b3d7b647643338f57158c2b139df11f87.png
   :class: img-responsive img-rounded
.. |image38| image:: images/entries/e2433bb4fe23b076129ea4accd516e3b7939d64f.gif
   :class: img-responsive img-rounded
.. |image39| image:: images/entries/64e788f716481fbb085a0ba70e8cc4f2333ad744.gif
   :class: img-responsive img-rounded
.. |image40| image:: images/entries/419403e295be2748e89100cb31117685b151e409.png
   :class: img-responsive img-rounded
.. |image41| image:: images/entries/c58fa193b00b77b743b17b9ef50336f1b13d1b9f.png
   :class: img-responsive img-rounded
.. |image42| image:: images/entries/a9b8aad7c60417bb1d7a811da40af7a1b763efbe.gif
   :class: img-responsive img-rounded
.. |image43| image:: images/entries/04bf91d7cd37549d0949e2d3c67be6e7a809a3a5.png
   :class: img-responsive img-rounded
.. |image44| image:: images/entries/6172a0a8196db373e0eac8edbcbf790ae9532ba8.png
   :class: img-responsive img-rounded
.. |image45| image:: images/entries/3706248ef1ca50af9877d04df93d6f3455bce9ca.png
   :class: img-responsive img-rounded
.. |image46| image:: images/entries/31251db3a673149dcd900737dd9aada0fafb93ff.gif
   :class: img-responsive img-rounded
.. |image47| image:: images/entries/5fca0da47e4af53c46a12dcd5b68a1982afff16b.png
   :class: img-responsive img-rounded
.. |image48| image:: images/entries/6c530f4bfd565313f515ae9f6a79662d1682bfc7.png
   :class: img-responsive img-rounded
.. |image49| image:: images/entries/50ff18ed7962a0fbc09ca17f3b0688db6ed33bd3.png
   :class: img-responsive img-rounded
.. |image50| image:: images/entries/c8cf49088468d798190f56a32c0e6c6d1cefe72f.png
   :class: img-responsive img-rounded
.. |image51| image:: images/entries/3bfe2bcf8051167fd7729ef3c5a2a4f5249f823b.png
   :class: img-responsive img-rounded
.. |image52| image:: images/entries/79d5021866775b2eb429eb60c96f697ac0c6af49.gif
   :class: img-responsive img-rounded
.. |image53| image:: images/entries/62594ee3295e3276fe9510f42e2ba54d05153ebd.png
   :class: img-responsive img-rounded
.. |image54| image:: images/entries/e7c6ed595485dd51c3bccb87f2a31f9691ad4aae.png
   :class: img-responsive img-rounded
.. |image55| image:: images/entries/74d4c97f9c4d402e928893c88f331e9.png
   :class: img-responsive img-rounded
.. |image56| image:: images/entries/d3e680f3e4facc9078e4755045152d57f7dc680f.png
   :class: img-responsive img-rounded
