.. _changelog328:

Changelog for QGIS 3.28
=======================

|image1|

Release date: 2022-10-21

QGIS 3.28 Firenze introduces various feature updates, UX modifications, usability enhancements, and improved integration with various proprietary services and data backends. It is also set to introduce the long-awaited features provided by previous releases into the long-term support release, as outlined in the `QGIS Roadmap <https://www.qgis.org/en/site/getinvolved/development/roadmap.html>`__.

The splash screen features a rare and extraordinary 1847 map of Firenze, or Florence, Italy by Giuseppe Molini. This magnificently engraved map was originally drawn in 1731 by the Florentine architect Ferdinando Ruggieri. Oriented to the south, the map covers the old walled center of Florence as it extends on both sides of the Arno River. The upper right quadrant features the lily symbol of Florence. Though printed in 1847, this map has been prepared in the 17th-century style by copperplate engraving on thick-laid paper. Firenze in 1847 was on the cusp of political transformation. One year following the production of this rare map the Grand Duke of Tuscany, responding to political demonstrations throughout Florence, granted Tuscany its first constitution.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at https://youtu.be/IEkOhQezQMk

:raw-html:`<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/IEkOhQezQMk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>`

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to `QGIS.ORG <https://qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our `list of donors <https://qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

:raw-html:`<div id="qgissustainingmembersatom"> <!-- to be filled via javascript loading of atom feed --> </div>`

QGIS is free software and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of their financial or social status - we believe that empowering people with spatial decision-making tools will result in a better society for all of humanity.

.. contents::
   :local:

Breaking Changes
----------------

Feature: Drop project backward compatibility for symbology with QGIS 3.16 and older
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous releases of QGIS would write significant amounts of compatibility objects into the XML structure of project files to maintain backward compatibility for symbologies in order to allow project files to be opened with QGIS 3.16 and older. This compatibility has been removed from future releases.

This feature was developed by `Denis Rouzaud <https://github.com/3nids>`__

Temporal
--------

Feature: Add temporal manager support for WMTS layers with TIME dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This enhancement exposes any WMTS "time" dimensions for use in the temporal framework, including allowing these layers to be animated and controlled via the temporal controller.

When we do detect a time dimension on a WMTS layer, we no longer expose this in the same way as other non-time dimensions. The browser panel does not show the dimension values, and adding the layer via Data Source Manager no longer prompts the user to pick from the available time values. Instead, these layers are indicated with a new "time capable raster layer" icon, and are added to a project without the user specifying a time value.

Just like a WMS(T) layer, when a time-dimension enabled WMTS layer is added to the project, it will default to the "automatic" temporal mode, meaning that the layer will follow the temporal controller's current time range by default. A user can then opt to show a specific static time value for the layer through the layer's Temporal properties page, by unchecking "Dynamic Temporal Control" and picking a specific available time range from the "Predefined date" option.

This should unify the user experience so that the usage of WMTS time-enabled layers is essentially identical to the usage of WMS(T) layers.

|image3|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Map Tools
---------

Feature: Allow selecting features in vector tile layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for selecting features from vector tile layers has been added, which allows users to use the standard map-based selection tools to interactively select features from these sources.

When a vector tile layer has a selection, a user can:

-  Copy the features and paste them to other layers, or paste them into a scratch layer
-  Use other (non-editing) tools which operate on selections, such as "zoom to selected features"/"pan to selected features"

Selections can be made using any of the interactive map-based selection tools, e.g. select by rectangle, freehand, polygon, or radius. All the shortcuts which apply to vector selections for adding/subtracting/intersecting selections also apply.

Selecting features is made using the tile zoom level of the canvas, and then the features selected at this zoom level persist even if the user changes the map scale to another vector tile zoom level. This means a user can zoom in and select a small/ detailed feature, then zoom out and still see the selected feature on the map.

This feature was funded by Toitū Te Whenua Land Information New Zealand

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

User Interface
--------------

Feature: Exclusive window based UX for data source manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data source manager dialog is now ALWAYS non modal, and options to set it as such have been removed. The dialog now functions just like other "manager" type windows in QGIS, such as the style manager or layout manager.

The data source manager will instead be treated as its own window, which is raised to the foreground whenever the Data Source Manager button is pressed.

|image4|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add a Show in Attribute Table action to the right click menu of legend class symbols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new "Show in Attribute Table" action has been added to the right-click context menu of legend class symbols in the table of contents. This allows users to open the attribute table with a filter applied to match only the features relevant to a particular symbol group. This provides a significant performance improvement for certain datasets, such as large vector layers loaded from a remote source.

|image5|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Add setting to hide NULL values on identify result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "Identify Features" utility now provides the capability to hide NULL values from the returned results

|image6|

This feature was funded by `Camptocamp <https://www.camptocamp.com/>`__

This feature was developed by `Ismail Sunni <https://github.com/ismailsunni>`__

Symbology
---------

Feature: Allow control over GPS location marker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new general GPS options page has been introduced which includes new settings for controlling the marker symbol used for the current GPS location, and whether this symbol should be rotated to match the GPS direction.

|image7|

This feature was funded by Tiwi Resources, Bush Heritage, Australian Wildlife Conservancy

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Added new ellipse marker shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The symbol styles for the ellipse marker type now include additional shape types for:

-  Pentagon
-  Hexagon
-  Octagon
-  Third Circle
-  Quarter Circle
-  Star

|image8|

This feature was funded by North Road

This feature was developed by `ZayneTomlins <https://github.com/ZayneTomlins>`__

Labelling
---------

Feature: Add support for HTML bold/italic/font size and font family to labelling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for additional HTML formatting tags have been added for use within labeling (and everywhere else the text renderer is used).

Supported tags specifically include:

-  font family
-  font size
-  bold
-  italic

|image9|

This feature was funded by the Swiss QGIS user group

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add option to use absolute units for line height
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously, the line height was always set in multiples of the text line spacing, however, it is now possible to use absolute units for line height (useful in contexts where mixed text sizes are used within a single document).

|image10|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Mesh
----

Feature: Add option to reload mesh layer temporal properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An "Always take reference time from data source" option has been added for mesh layers that when checked, will ensure that the reference time is reloaded from the data source, and each time the layer is reloaded or the project reopened the time properties will be updated from the file automatically.

In previous releases, when a mesh layer file had a reference time and time extent that changed, the time layer properties would not be updated when the projector layer are reloaded, and the user would be required to manually navigate to the "Reload from provider" feature in the temporal tab of the layer properties.

|image11|

This feature was developed by `Vincent Cloarec <https://github.com/vcloarec>`__

3D Features
-----------

Feature: Ambient Occlusion 3D Effect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ambient occlusion effect is available for rendering data in 3D views that is useful for improving depth perception of the data in 3D. This is a post-processing effect and it can be even combined with eye dome lighting (EDL) for quite interesting results. An oversimplification of the effect is that features that are not visible to the camera are used to texture and darken neighboring elements, with the benefit of improving contrast, feature definition, and differentiation.

There is a new item for controlling the state of Ambient Occlusion in the configuration menu for 3D views, as well as extra parameters in the advanced section of the configuration dialog for fine-grained control over:

-  Radius: The distance threshold for calculating ambient occlusion
-  Intensity: The strength of the effect should be (higher values make things darker)
-  Occlusion threshold: Number of neighboring points that need to be occluded for the effect to appear (values lower than 50% will make the output darker, but possibly provide a greater range of occlusion)

|image12|

This feature was developed by `Martin Dobias & Belgacem Nedjima <https://github.com/wonder-sk>`__

Point Clouds
------------

Feature: Point Cloud Layer Export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Point Cloud layers now support being exported to vector or point cloud data formats, with optional filtering.

Supported formats include:

-  Temporary scratch layer (memory layer)
-  GeoPackage
-  Shapefile
-  DXF
-  LAZ (requires build WITH\_PDAL)
-  Uncompressed LAS files

Export operations support filtering by:

-  Extent
-  Filtering by Z Range
-  Limiting the number of exported points
-  Filtering spatially by polygon layer

In addition, output CRS definition and re-projection are also supported.

|image13|

This feature was funded by State of Vorarlberg and Swiss QGIS user group

This feature was developed by `Stefanos Natsis <https://github.com/uclaros>`__

Feature: Eye Dome Lighting for point clouds in 2D map canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The eye dome lighting effect is now available for point clouds in 2D renderers

|image14|

This feature was developed by `Nedjima Belgacem <https://github.com/NEDJIMAbelgacem>`__

Print Layouts
-------------

Feature: Add FORCE\_RASTER and IMAGE\_COMPRESSION parameters to PDF algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``FORCE_RASTER`` and ``IMAGE_COMPRESSION`` parameters have been added to the various "Export print layout as PDF" algorithms, including support for Atlas and multifile exports.

``FORCE_RASTER`` is mutually exclusive with and takes precedence over the ``FORCE_VECTOR`` parameter.

|image15|

This feature was developed by `Andrea Giudiceandrea <https://github.com/agiudiceandrea>`__

Expressions
-----------

Feature: Add new variable form of current feature expression functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The newer style variable form has been added for referencing the current feature and its attributes in expressions.

The newly introduced variables are:

-  ``@feature``: a replacement for $currentfeature, contains the current feature
-  ``@id``: a replacement for $id, contains the current feature id
-  ``@geometry``: a replacement for $geometry, contains the current feature geometry

This is a step towards eventually deprecating the older ``$`` style functions, and providing a more consistent approach to expressions instead of an unpredictable mix of ``@``/``$``.

Older functions and variable references will continue to work (and will likely continue working indefinitely for the sake of compatibility with older projects). They will also continue (for the time being) to be exposed in the UI to avoid user confusion.

|image16|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add new shared\_paths function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``shared_paths`` function has been added which returns a collection containing paths shared by the two input geometries. Those going in the same direction are in the first element of the collection, and those going in the opposite direction are in the second element. The paths themselves are given in the direction of the first geometry.

|image17|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Make\_valid and geom\_to\_array functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additional functions have been added for:

-  ``make_valid``: Repair broken input geometries and returns the corrected geometries
-  ``geometries_to_array``: This converts a geometry collection into an array for easier handling and iteration

|image18|

This feature was developed by `Alex <https://github.com/roya0045>`__

Feature: Concave hull function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``concave_hull`` function is now available in QGIS expressions (GEOS 3.11+)

|image19|

This feature was developed by `Loïc Bartoletti <https://github.com/lbartoletti>`__

Feature: Ask for confirmation when discarding expression changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new confirmation dialog is now safeguarding users against accidentally discarding their unapplied changes in expression editor dialogs. This safeguard is used in the Expression String Builder, the Expression Dialog (Epsilon icon, e. g. for Geometry Generators or for Pre-calculated Values in the model builder) and the Expression Based Filter (Attribute Table -> Advanced filter expression).

|image36|

This feature was funded by `WhereGroup GmbH <https://wheregroup.com/>`__

This feature was developed by `Johannes Kröger <https://github.com/kannes>`__

Data Management
---------------

Feature: Ask for confirmation when deleting features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new confirmation dialog appears by default when users perform an action that would delete records, such as using the DEL key or toolbar actions, to further reduce the risks of accidental feature deletion. Additionally, the feature count is now included in the dialog message itself (and is also still displayed in the title bar), making the total number of features deleted more clear to users.

In previous releases, similar confirmation prompts would only be displayed when some features fell out of the extent of the map canvas, or the deletion triggered the removal of child relation features. The new behavior is for the prompt to be enabled by default and disabled by using the "Don't show this message again" checkbox.

|image20|

This feature was funded by `QGIS user group Switzerland <https://www.qgis.ch/>`__

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Metadata and Metasearch
-----------------------

Feature: Layer metadata data provider search and storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation of elements from the `QEP #250 "Database metadata storage" <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/250>`__ initiative have been completed and this functionality includes the creation of a new layer metadata API and GUI components.

The following data providers/formats are supported for storing and managing layer metadata in QGIS:

-  GPKG (it was implemented already, I just wrapped it into the new API)
-  Postgres
-  Postgres Raster

In addition, a new layer metadata search tab is available from the data source manager, and an interactive layer metadata search is available using the QGIS locator.

|image21|

This feature was funded by ARPA Piemonte

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Processing
----------

Feature: Fixed precision support for select processing tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new advanced parameter is available for some processing tools which allows the use of the `fixed precision <https://blog.cleverelephant.ca/2020/12/waiting-postgis-31-3.html#fixed-precision-overlay>`__ parameter provided by GEOS >= 3.9.0. This parameter is listed under advanced parameters as "Grid Size" and is currently supported in the following tools:

-  Overlap
-  Intersection
-  Difference
-  Symmetrical Difference
-  Union

|image22|

This feature was funded by Orange Telecom FR

This feature was developed by `Loïc Bartoletti <https://github.com/lbartoletti>`__

Feature: Improved "Make Valid" Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS can now use the newer refined GEOS 3.10+ methods for validating and repairing geometry features.

|image23|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Default option to show feature count for vector outputs from processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``Show feature count for output vector layers`` setting is available (but disabled by default for performance reasons), which will automatically enable the "show feature count" option on output layers loaded from QGIS processing. This is able to give users a first glimpse of what to expect as an output from a Processing algorithm.

|image24|

This feature was developed by `Germap <https://github.com/gacarrillor>`__

Feature: Add relations export option to package layers algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "Package Layers" processing tool now supports optionally following project relations and exporting related tables following the hierarchy both upstream and downstream, whilst also taking selected features into account.

|image25|

This feature was funded by ARPA Piemonte

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Add "Offset" parameter to "Drape" algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds the "Offset" parameter to the "Drape (set Z value from raster)" and "Set M value from raster" algorithms. The "Offset" value is algebraically added to the band values after applying the "Scale factor".

|image26|

This feature was developed by `Andrea Giudiceandrea <https://github.com/agiudiceandrea>`__

Application and Project Options
-------------------------------

Feature: Modified project coordinate and bearing display settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Coordinate and Bearing Display options in the project settings have been updated in line with the following:

-  Map Units (behavior is the same as previous releases)
-  Map Geographic (modified behavior)
-  Custom Projection Units (new type)

The legacy Geographic (Latitude/ Longitude) option would display values in the map CRS coordinates *if* the CRS was geographic, otherwise, it would transform coordinates to a hard-coded WGS84 CRS value.

The updated Map Geographic (degrees) option, which supersedes the legacy approach, will display values in the map CRS coordinates *if* the CRS is geographic, however in instances where it is not, the internal ``QgsCoordinateReferenceSystem::toGeographicCrs()`` API will be used to transform the coordinates into the map CRS' associated geographic CRS. This is helpful in various contexts, such as when analyzing non-earth celestial bodies.

The Custom Projection Units type is a new addition that defaults to WGS84 and allows users to set any CRS they desire as display coordinates.

|image27|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Add support for "user" fonts, and automatic downloading of freely licensed fonts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new "Fonts" panel has been added to the settings dialog, which provides support for the following functionalities:

-  The ability for users to populate a list of automatic font replacements to apply when loading projects or styles, allowing better support for projects and styles to be used across different operating systems (e.g. replace "Arial" with "Helvetica").
-  Users can now place TTF or OTF fonts in the "fonts" subfolder of their user profile. These fonts will automatically be loaded at QGIS startup time. This provides a way for users to use fonts without requiring them to be installed on an operating system level, which is often blocked in enterprise environments. The Fonts setting panel lists all installed user fonts and allows users to manage (i.e. remove) previously installed user fonts
-  An API is provided for other tools, such as plugins and other clients, to specify additional user font folders which should be scanned during QGIS startup
-  Automatic downloading of missing fonts is now supported in certain circumstances. If a user opens a project or style, or they try to load a vector tile layer that references fonts that aren't currently available, then a hard-coded list of freely licensed fonts to download via URL is consulted to determine whether it's possible to automatically download the font to the user font directory (and notify the user of the font license). A setting to opt out of this behavior is provided in the Fonts panel if so desired.

|image28|

This feature was funded by Toitū Te Whenua Land Information New Zealand

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Browser
-------

Feature: Implement relationship discovery for OGR layers, and show relationships in browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Project Properties → Relations → Discover Relations feature is now able to support OGR layers that support relationships, such GeoPackage (via the related tables extension) and ESRI FileGeodatabases.

The QGIS Browser Panel now includes the ability to show detailed relationship information for these data sources.

|image29|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Modified UX for Geopackage and ESRI File Geodatabase creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A "New ESRI File Geodatabase" action has been added to the QGIS Browser right-click context menu on directories, and a new "vacuum" action is available for GDB files. (requires GDAL 3.6+)

Additionally, creating a new Geopackage from the same menu will now immediately create an empty GPKG, rather than the legacy behavior of opening a table creation dialog by default (and requiring table creation or users to input dummy data).

https://user-images.githubusercontent.com/1829991/178902332-0e112e73-0140-45b9-84bf-fc7875cb7b98.gif

|image30|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Allow drag and drop of vector layers to non-GPKG OGR database datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now allows drag and drop of vector layers between OGR database datasets that are not stored in GPKG format, for instance, the dragging of a layer onto a GDB to import that dataset into the geodatabase

|image31|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Expose field domain management for non-gpkg OGR sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS browser now supports more advanced functionalities for OGR databases that are not in GPKG format, including Field domain management capabilities (creation and listing domains) and table creation. This means that users can manage field domains and create new tables in an existing ESRI FileGeodatabase database from the QGIS Browser interface.

|image32|

This feature was funded by Provincie Gelderland

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Data Providers
--------------

Feature: Define session role for PostgreSQL connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``session_role`` setting can now be specified for PostgreSQL connections to set the user identifier of the active SQL session. Permissions checking for SQL commands are then carried out with the associated named role.

This is highly useful in instances where it is desirable to automatically give ownership of new objects (Tables/ Views/ Functions etc.) to the ``session_role`` group, and share ownership and the associated rights with all members of the ``session_role`` group.

The specified ``session_role`` must be a role that the current session user is a member of, or if the session user is a superuser, any role can be selected.

This feature was funded by `3liz <https://3liz.com/>`__

This feature was developed by `rldhont <https://github.com/rldhont>`__

Feature: Automatically add related tables when adding layers from GDAL datasets with embedded relationship information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For GDAL data formats with embedded relationship information, whenever a table is added QGIS is now able to discover relationships and immediately add all the related tables to the current project (if they don't already exist). Additionally, when adding these related layers QGIS will automatically configure the corresponding QGIS relationships.

This works for all formats which support the GDAL relationship API, which include:

-  Geopackage (via the related tables extension)
-  ESRI FileGDB/ OpenFileGDB
-  ESRI Personal Geodatabase
-  SQLite/ Spatialite formats.

This feature was funded by University of Uppsala

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add subset string (filter) support for arcgis REST layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can **greatly** improve the performance on large layers!

This feature was funded by `Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment <https://eng.naturstyrelsen.dk/>`__

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Abstract database provider for renaming fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``QgsAbstractDatabaseProviderConnection`` interface has been added for supporting renaming fields, and implemented for OGR connections along with the ability to rename existing fields for supported database connections via the QGIS Browser interface.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: WFS performing binary spatial operations in expressions on server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS used to be able to perform the expression filters of binary spatial operations on the server when the geometry was provided as WKT or in the GML format. This change converts the geometry from being a static variable in the expression to an OGC filter. The WFS URL is then created by combining a bounding box rectangle, layer filter, and the filtering expression.

A feature request computes the expression in advance to find out if it can be performed on the server, then it's stored in ``QgsBackgroundCachedSharedData`` where a new download is triggered.

When a filter request is not a pure binary spatial operation, it will not be evaluated on the server.

This feature was funded by Kanton Schaffhausen

This feature was developed by `signedav <https://github.com/signedav>`__

Feature: Editing ArcGIS REST Layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now supports the editing of ArcGIS feature server layers, such as those hosted on ArcGIS online. Assuming the user has appropriate permissions granted for editing a layer, it will unlock the ability to use the native QGIS tools to edit that layer. These changes include support for the following operations:

-  Deleting features
-  Adding new features
-  Curved geometries (only supported for enterprise ArcGIS server, as `ArcGIS online currently has no support for curves <https://support.esri.com/en/technical-article/000014684>`__)
-  Modifying existing features
-  Modifying attributes (creating fields, deleting fields, creating attribute indexes)

This feature was funded by `Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment <https://eng.naturstyrelsen.dk/>`__

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Load raster sublayers from vector tile styles automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When loading a new vector tile source into a project, if the associated MapBox GL style includes any raster sublayers, then also load those into the project with converted styles.

Fixes https://github.com/qgis/QGIS/issues/46593

|Peek 2022-06-20 12-31|

This feature was funded by Toitū Te Whenua Land Information New Zealand

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add WMS layers individually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In previous releases, the selection of layers from WMS Servers would be loaded into QGIS as a single project layer. This new functionality provides an optional checkbox to load each of the selected WMS layers into QGIS as distinct project layers.

|image34|

This feature was funded by `Camptocamp <https://www.camptocamp.com/>`__

This feature was developed by `Ismail Sunni <https://github.com/ismailsunni>`__

Feature: Save projects to Oracle Database Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now supports saving projects to Oracle databases.

|image35|

This feature was developed by `Julien Cabieces <https://github.com/troopa81>`__

QGIS Server
-----------

Feature: QGIS\_SERVER\_ALLOWED\_EXTRA\_SQL\_TOKENS settings variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new feature allows specifying extra tokens which may be used for a WMS FILTER definition. The current list of accepted tokens is rather small and this setting will allow system administrators to easily enlarge the list of allowed tokens.

This feature was funded by Zweckverband Grevesmühlen

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Open layers in a read only mode with QGIS Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``QGIS_SERVER_FORCE_READONLY_LAYERS`` environment variable to force QGIS Server to open layers in read-only mode.

This includes various underlying API changes to support read-only configuration for data provider construction, project structure, and layer properties.

This feature was funded by `Ifremer <https://wwz.ifremer.fr/>`__

This feature was developed by `rldhont <https://github.com/rldhont>`__

Plugins
-------

Feature: Changes to plugin automatic updates behaviour
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This change moves the old ``app/plugin_installer/checkOnStart`` setting key to a new ``plugins/automatically-check-for-updates`` key, and switches the default value to enable automatic checks.

This is designed to switch all existing QGIS users to the new default behavior of checking for plugin updates at startup (at a maximum of once every 3 days).

It is intended to offer a better QGIS experience to our users, by proactively informing all users when plugins should be updated, ensuring that ALL users are more likely to upgrade plugins and get the bug fixes for plugins promptly.

**Enterprise users who have customised this setting in their deployments will need to adapt their scripts for the new setting key.**

Additionally, the option to control the number of days between plugin startup checks has been removed and is hardcoded at 3 days.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Programmability
---------------

Feature: Add temporal handling to maps in QGIS Quick
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new implementation has been added to allow the Canvas and Map Settings in `QGIS Quick <https://api.qgis.org/api/qgsquick.html>`__ to handle temporal functionality.

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Addition of py-args command line parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running QGIS from the command line with the ``--code`` parameter, a new ``--py-args`` utility allows the passing of arguments to the python interpreter.

Arguments between ``--py-args`` and ``--`` are passed to the python interpreter and ignored by QGIS, so for example, when using the following command:

::

    qgis --code /home/user/example.py --py-args --specialScriptArguments "arg1" 'arg2' -- layer1 layer2

The ``example.py`` script will have ``--specialScriptArguments``, ``arg1``, and ``arg2`` passed as system arguments to the python interpreter, whilst ``layer1`` and ``layer2`` will be handled by QGIS normally and loaded as map layers

This feature was funded by Landesamt für Vermessung und Geoinformation Vorarlberg

This feature was developed by `Damiano Lombardi <https://github.com/domi4484>`__

Notable Fixes
-------------

Feature: Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                              | URL issues.qgis.org (if reported)                           | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+========================================================================================================+=============================================================+===========================================================+===========================================================+
| GetPrint request of Atlas Template doesn't respect Project scales                                      | `#49900 <https://github.com/qgis/QGIS/issues/49900>`__      | `PR #50199 <https://github.com/qgis/QGIS/pull/50199>`__   | `PR #50214 <https://github.com/qgis/QGIS/pull/50214>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Attribute Table Integer entries not showing due to window size                                         | `#50181 <https://github.com/qgis/QGIS/issues/50181>`__      | `PR #50201 <https://github.com/qgis/QGIS/pull/50201>`__   | Not recommended                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| WFS3 collections field name/displayName mix in request/response                                        | `#49399 <https://github.com/qgis/QGIS/issues/49399>`__      | `PR #50203 <https://github.com/qgis/QGIS/pull/50203>`__   | Not recommended                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QGIS Server WMS GetFeatureInfo does not evaluate represent\_value expression in maptip                 | `#30719 <https://github.com/qgis/QGIS/issues/30719>`__      | `PR #50216 <https://github.com/qgis/QGIS/pull/50216>`__   | `PR #50223 <https://github.com/qgis/QGIS/pull/50223>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| "evaluate default value on providers side" block insert on table in the schema with autoincrement      | `#50168 <https://github.com/qgis/QGIS/issues/50168>`__      | `PR #50230 <https://github.com/qgis/QGIS/pull/50230>`__   | `PR #50333 <https://github.com/qgis/QGIS/pull/50333>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QGIS not responding when entering page size using custom width or height fields                        | `#50104 <https://github.com/qgis/QGIS/issues/50104>`__      | Cannot reproduce                                          |                                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| "Add Directory..." inputs files from previous selected directory at first instance, then the corret.   | `#50055 <https://github.com/qgis/QGIS/issues/50055>`__      | `PR #50232 <https://github.com/qgis/QGIS/pull/50232>`__   | `PR #50241 <https://github.com/qgis/QGIS/pull/50241>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Layer style panel and Layer panel do not show same visibility settings for layer style                 | `#49998 <https://github.com/qgis/QGIS/issues/49998>`__      | Cannot reproduce                                          |                                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Crash while opening Options dialog after switching locale                                              | `#50239 <https://github.com/qgis/QGIS/issues/50239>`__\ 9   | `PR #50263 <https://github.com/qgis/QGIS/pull/50263>`__   | Not needed                                                |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| unreported MSSQL connections API error                                                                 | Unreported                                                  | `PR #50194 <https://github.com/qgis/QGIS/pull/50194>`__   | `PR #50454 <https://github.com/qgis/QGIS/pull/50454>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Identify and select tools don't work with geometry-based query layers                                  | `#50242 <https://github.com/qgis/QGIS/issues/50242>`__      | Cannot reproduce                                          |                                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Problem with Reloading SLD file in QGIS                                                                | `#50152 <https://github.com/qgis/QGIS/issues/50152>`__      | `PR #50266 <https://github.com/qgis/QGIS/pull/50266>`__   | queued                                                    |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Unreported endless alg splitwithlines                                                                  | Unreported                                                  | `PR #50279 <https://github.com/qgis/QGIS/pull/50279>`__   | Not recommended                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Processing algorithm "Split with lines" does not split polygon                                         | `#50227 <https://github.com/qgis/QGIS/issues/50227>`__      | Not a bug                                                 |                                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Expression do not split string in multiple lines                                                       | `#49666 <https://github.com/qgis/QGIS/issues/49666>`__      | `PR #50295 <https://github.com/qgis/QGIS/pull/50295>`__   | `PR #50455 <https://github.com/qgis/QGIS/pull/50455>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Problem with exportation of complex SLD                                                                | `#42348 <https://github.com/qgis/QGIS/issues/42348>`__      | `PR #50342 <https://github.com/qgis/QGIS/pull/50342>`__   | `PR #50354 <https://github.com/qgis/QGIS/pull/50354>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Wrong interpretation of SLD color opacity                                                              | `#44657 <https://github.com/qgis/QGIS/issues/44657>`__      | Not a bug                                                 |                                                           |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Wrong label size for SLD export/import                                                                 | `#35561 <https://github.com/qgis/QGIS/issues/35561>`__      | `PR #50347 <https://github.com/qgis/QGIS/pull/50347>`__   | Not needed                                                |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Exporting SLD doesnt include fill-opacity                                                              | `#33376 <https://github.com/qgis/QGIS/issues/33376>`__      | `PR #50349 <https://github.com/qgis/QGIS/pull/50349>`__   | `PR #50436 <https://github.com/qgis/QGIS/pull/50436>`__   |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| SpatiaLite - Added feature vanishes, attribute dialog does not show required fields                    | `#50523 <https://github.com/qgis/QGIS/issues/50523>`__      | `PR #50573 <https://github.com/qgis/QGIS/pull/50573>`__   | queued                                                    |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Alessandro Pasotti <https://www.qcooperative.net/>`__

Feature: Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| Bug Title                                                                                                                              | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                                        |
+========================================================================================================================================+==========================================================+===========================================================+======================================================================+
| GML import is missing one feature without geometry                                                                                     | `#50215 <https://github.com/qgis/QGIS/issues/50215>`__   | `PR #50231 <https://github.com/qgis/QGIS/pull/50231>`__   | Not appropriate                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account                                                           | `#49404 <https://github.com/qgis/QGIS/issues/49404>`__   | `PR #50236 <https://github.com/qgis/QGIS/pull/50236>`__   | Not needed                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| [WFS] Layer is added incorrectly as mixed geometry collection                                                                          | `#49335 <https://github.com/qgis/QGIS/issues/49335>`__   | `PR #50237 <https://github.com/qgis/QGIS/pull/50237>`__   | `PR #50353 <https://github.com/qgis/QGIS/pull/50353>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques                                   | `#49121 <https://github.com/qgis/QGIS/issues/49121>`__   | `PR #50249 <https://github.com/qgis/QGIS/pull/50249>`__   | `PR #50351 <https://github.com/qgis/QGIS/pull/50351>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| [Processing] Fix typo in smoothing parameter name of gdal\_grid algorithms                                                             | Unreported                                               | `PR #50261 <https://github.com/qgis/QGIS/pull/50261>`__   | `PR #50331 <https://github.com/qgis/QGIS/pull/50331>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS client shows wrong CRS                                                                                                             | `#42627 <https://github.com/qgis/QGIS/issues/42627>`__   | `PR #50272 <https://github.com/qgis/QGIS/pull/50272>`__   | `PR #50328 <https://github.com/qgis/QGIS/pull/50328>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS doesn't work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. http://www.opengis.net/def/crs/EPSG/0/xxxx)   | `#29391 <https://github.com/qgis/QGIS/issues/29391>`__   | `PR #50281 <https://github.com/qgis/QGIS/pull/50281>`__   | `PR #50386 <https://github.com/qgis/QGIS/pull/50386>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS ignores field inherited from parent feature type in WFS 2.0 services                                                              | `#42660 <https://github.com/qgis/QGIS/issues/42660>`__   | `PR #50300 <https://github.com/qgis/QGIS/pull/50300>`__   | Not appropriate                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| Loading and displaying CADRG/NITF data is slower than it used to be                                                                    | `#49439 <https://github.com/qgis/QGIS/issues/49439>`__   | `PR #50302 <https://github.com/qgis/QGIS/pull/50302>`__   | `PR #50352 <https://github.com/qgis/QGIS/pull/50352>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| world\_map.gpkg: little fix to avoid warning with recent GDAL versions                                                                 | Unreported                                               | `PR #50304 <https://github.com/qgis/QGIS/pull/50304>`__   | Not needed                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic                                                                                    | `#48052 <https://github.com/qgis/QGIS/issues/48052>`__   | https://github.com/OSGeo/gdal/pull/6426                   | `PR #50328 <https://github.com/qgis/QGIS/pull/50328>`__\ Bug Title   |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| --                                                                                                                                     | --                                                       | --                                                        | --                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| GML import is missing one feature without geometry                                                                                     | `#50215 <https://github.com/qgis/QGIS/issues/50215>`__   | `PR #50231 <https://github.com/qgis/QGIS/pull/50231>`__   | Not appropriate                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account                                                           | `#49404 <https://github.com/qgis/QGIS/issues/49404>`__   | `PR #50236 <https://github.com/qgis/QGIS/pull/50236>`__   | Not needed                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| [WFS] Layer is added incorrectly as mixed geometry collection                                                                          | `#49335 <https://github.com/qgis/QGIS/issues/49335>`__   | `PR #50237 <https://github.com/qgis/QGIS/pull/50237>`__   | `PR #50353 <https://github.com/qgis/QGIS/pull/50353>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques                                   | `#49121 <https://github.com/qgis/QGIS/issues/49121>`__   | `PR #50249 <https://github.com/qgis/QGIS/pull/50249>`__   | `PR #50351 <https://github.com/qgis/QGIS/pull/50351>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| [Processing] Fix typo in smoothing parameter name of gdal\_grid algorithms                                                             | Unreported                                               | `PR #50261 <https://github.com/qgis/QGIS/pull/50261>`__   | `PR #50331 <https://github.com/qgis/QGIS/pull/50331>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| WFS client shows wrong CRS                                                                                                             | `#42627 <https://github.com/qgis/QGIS/issues/42627>`__   | `PR #50272 <https://github.com/qgis/QGIS/pull/50272>`__   | `PR #50328 <https://github.com/qgis/QGIS/pull/50328>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS doesn't work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. http://www.opengis.net/def/crs/EPSG/0/xxxx)   | `#29391 <https://github.com/qgis/QGIS/issues/29391>`__   | `PR #50281 <https://github.com/qgis/QGIS/pull/50281>`__   | `PR #50386 <https://github.com/qgis/QGIS/pull/50386>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS ignores field inherited from parent feature type in WFS 2.0 services                                                              | `#42660 <https://github.com/qgis/QGIS/issues/42660>`__   | `PR #50300 <https://github.com/qgis/QGIS/pull/50300>`__   | Not appropriate                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| Loading and displaying CADRG/NITF data is slower than it used to be                                                                    | `#49439 <https://github.com/qgis/QGIS/issues/49439>`__   | `PR #50302 <https://github.com/qgis/QGIS/pull/50302>`__   | `PR #50352 <https://github.com/qgis/QGIS/pull/50352>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| world\_map.gpkg: little fix to avoid warning with recent GDAL versions                                                                 | Unreported                                               | `PR #50304 <https://github.com/qgis/QGIS/pull/50304>`__   | Not needed                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic                                                                                    | `#48052 <https://github.com/qgis/QGIS/issues/48052>`__   | https://github.com/OSGeo/gdal/pull/6426                   | `PR #50328 <https://github.com/qgis/QGIS/pull/50328>`__              |
+----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Even Rouault <https://www.spatialys.com/>`__

Feature: Bug fixes by Julien Cabieces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                        | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+==================================================================================================================+==========================================================+===========================================================+===========================================================+
| QGIS not retrieving sequence from postgis in 3.26                                                                | `#49463 <https://github.com/qgis/QGIS/issues/49463>`__   | `PR #50247 <https://github.com/qgis/QGIS/pull/50247>`__   | no need to bp                                             |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| SVG is not rendered for SVG Marker symbol                                                                        | `#50208 <https://github.com/qgis/QGIS/issues/50208>`__   | Cannot fix, Qt issue                                      |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| If "estimated metadata" option is checked, feature count for tables/postgis do not work                          | `#46790 <https://github.com/qgis/QGIS/issues/46790>`__   | `PR #50256 <https://github.com/qgis/QGIS/pull/50256>`__   | `PR #50425 <https://github.com/qgis/QGIS/pull/50425>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Variable raster image source in composer not working                                                             | `#47981 <https://github.com/qgis/QGIS/issues/47981>`__   | `PR #50277 <https://github.com/qgis/QGIS/pull/50277>`__   | `PR #50332 <https://github.com/qgis/QGIS/pull/50332>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Print Layout Picture Box reverting to SVG                                                                        | `#38031 <https://github.com/qgis/QGIS/issues/38031>`__   | `PR #50277 <https://github.com/qgis/QGIS/pull/50277>`__   | `PR #50332 <https://github.com/qgis/QGIS/pull/50332>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Layout picture can not change SVG image to Raster image                                                          | `#37804 <https://github.com/qgis/QGIS/issues/37804>`__   | `PR #50277 <https://github.com/qgis/QGIS/pull/50277>`__   | `PR #50332 <https://github.com/qgis/QGIS/pull/50332>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QgsOptionsPageWidget - helpKey and helpSearchPath are not working                                                | `#49421 <https://github.com/qgis/QGIS/issues/49421>`__   | `PR #50282 <https://github.com/qgis/QGIS/pull/50282>`__   | `PR #50330 <https://github.com/qgis/QGIS/pull/50330>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Freeze when opening WFS attribute table from HTTPS server with SSL exception                                     | `#42615 <https://github.com/qgis/QGIS/issues/42615>`__   | `PR #50443 <https://github.com/qgis/QGIS/pull/50443>`__   | no bp                                                     |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| News feed not loading when using MSI installer                                                                   | `#49097 <https://github.com/qgis/QGIS/issues/49097>`__   | `PR #50443 <https://github.com/qgis/QGIS/pull/50443>`__   | no bp                                                     |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| .ci/run\_tests.sh: test\_core\_networkaccessmanager (Timeout)                                                    | `#50234 <https://github.com/qgis/QGIS/issues/50234>`__   | `PR #50443 <https://github.com/qgis/QGIS/pull/50443>`__   |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| SVG Symbol on newer version of QGIS (3.22.7/8/10 tested) make the software lag a lot (and not on 3.4 version).   | `#49818 <https://github.com/qgis/QGIS/issues/49818>`__   | Feedback, not sure it’s a bug                             |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Empty Options drop-down menu in Query Logger tab                                                                 | `#50403 <https://github.com/qgis/QGIS/issues/50403>`__   | `PR #50527 <https://github.com/qgis/QGIS/pull/50527>`__   | no bp                                                     |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Build fails with WITH\_POSTGRESQL=OFF                                                                            | `#50075 <https://github.com/qgis/QGIS/issues/50075>`__   | Feedback                                                  |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Build fails with WITH\_GSL=OFF                                                                                   | `#50076 <https://github.com/qgis/QGIS/issues/50076>`__   | `PR #50555 <https://github.com/qgis/QGIS/pull/50555>`__   |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QGIS master exports out of bounds in layout                                                                      | `#48624 <https://github.com/qgis/QGIS/issues/48624>`__   | Cannot fix, Qt issue                                      |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Layout bleeding to edge outside map window                                                                       | `#49638 <https://github.com/qgis/QGIS/issues/49638>`__   | Cannot fix, Qt issue                                      |                                                           |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Freeze with virtual field on $area used as parameter in sum                                                      | `#49589 <https://github.com/qgis/QGIS/issues/49589>`__   | `PR #50533 <https://github.com/qgis/QGIS/pull/50533>`__   | `PR #50565 <https://github.com/qgis/QGIS/pull/50565>`__   |
+------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Julien Cabieces <https://oslandia.com/>`__

Feature: Bug fixes by Paul Blottiere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                             | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+=======================================================================================================+==========================================================+===========================================================+===========================================================+
| QGIS Server WFS 1.1.0 GetFeature response - properties with xsi:nil="true"                            | `#45243 <https://github.com/qgis/QGIS/issues/45243>`__   | `PR #50495 <https://github.com/qgis/QGIS/pull/50495>`__   |                                                           |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Cannot move labels                                                                                    | `#47542 <https://github.com/qgis/QGIS/issues/47542>`__   | Cannot reproduce                                          |                                                           |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Auxiliary storage and removed layers                                                                  | `#44667 <https://github.com/qgis/QGIS/issues/44667>`__   | `PR #50479 <https://github.com/qgis/QGIS/pull/50479>`__   | Not recommended                                           |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| OPACITIES parameter not handled with Vector Tile layer in GetMap/GetPrint                             | `#50364 <https://github.com/qgis/QGIS/issues/50364>`__   | `PR #50374 <https://github.com/qgis/QGIS/pull/50374>`__   | `PR #50539 <https://github.com/qgis/QGIS/pull/50539>`__   |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fixes log messages when a job error is not related to a specific layer                                | Unreported                                               | `PR #50372 <https://github.com/qgis/QGIS/pull/50372>`__   | Not needed                                                |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Labels: Data defined override of "Show Label" always wants the auxiliary storage option               | `#47993 <https://github.com/qgis/QGIS/issues/47993>`__   | `PR #50496 <https://github.com/qgis/QGIS/pull/50496>`__   | `PR #50538 <https://github.com/qgis/QGIS/pull/50538>`__   |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Auxiliary storage rotation or offset fields for symbols are visible by default while labels are not   | `#28548 <https://github.com/qgis/QGIS/issues/28548>`__   | `PR #50498 <https://github.com/qgis/QGIS/pull/50498>`__   |                                                           |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Improve selection of PostGIS raster overviews                                                         | Unreported                                               | `PR #50554 <https://github.com/qgis/QGIS/pull/50554>`__   | `PR #50575 <https://github.com/qgis/QGIS/pull/50575>`__   |
+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Paul Blottiere <https://hytech-imaging.fr/>`__

Feature: Bug fixes by Sandro Santilli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                                                                       | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.22 backport commit (GitHub)   |
+=================================================================================================+==========================================================+===========================================================+=================================+
| Crash with offline-editing-core-plugin converting to offline project layer with empty polygon   | `#50466 <https://github.com/qgis/QGIS/issues/50466>`__   | `PR #50577 <https://github.com/qgis/QGIS/pull/50577>`__   |                                 |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Cleanup temporary python test config path when requested                                        | `#48884 <https://github.com/qgis/QGIS/issues/48884>`__   | `PR #50608 <https://github.com/qgis/QGIS/pull/50608>`__   |                                 |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Include type name in message about unsupported qfield validations                               | Unreported                                               | `PR #50589 <https://github.com/qgis/QGIS/pull/50589>`__   |                                 |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Sandro Santilli (strk) <https://strk.kbt.io/>`__

Feature: Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                                                                             | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.22 backport commit (GitHub)                             |
+=======================================================================================================================================================================+==========================================================+===========================================================+===========================================================+
| Fix regression in column break calculations in legends                                                                                                                | `#42672 <https://github.com/qgis/QGIS/issues/42672>`__   | `PR #50597 <https://github.com/qgis/QGIS/pull/50597>`__   | Not suitable -- too risky                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix tracing fails when layer crs differs from map crs                                                                                                                 | `#49247 <https://github.com/qgis/QGIS/issues/49247>`__   | `PR #50612 <https://github.com/qgis/QGIS/pull/50612>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Show only available CRS in WMS layer selection widget                                                                                                                 | `#45918 <https://github.com/qgis/QGIS/issues/45918>`__   | `PR #50572 <https://github.com/qgis/QGIS/pull/50572>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix some overlay algorithms output multipoint geometries but output layer is single point, causing insertion errors                                                   | `#49456 <https://github.com/qgis/QGIS/issues/49456>`__   | `PR #50567 <https://github.com/qgis/QGIS/pull/50567>`__   | `PR #50641 <https://github.com/qgis/QGIS/pull/50641>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix missing information in crash reports on Windows                                                                                                                   | `#50472 <https://github.com/qgis/QGIS/issues/50472>`__   | `PR #50595 <https://github.com/qgis/QGIS/pull/50595>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix regression where attribute table dialogs do not open as proper top level windows with their own taskbar entries                                                   | `#49286 <https://github.com/qgis/QGIS/issues/49286>`__   | `PR #50594 <https://github.com/qgis/QGIS/pull/50594>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [georeferencer] Fix options ignored when "create world file only" is active                                                                                           | `#49331 <https://github.com/qgis/QGIS/issues/49331>`__   | `PR #50566 <https://github.com/qgis/QGIS/pull/50566>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Ensure identify tool uses correct labels for x/y values when coordinate axis order for project is y/x                                                                 | `#50540 <https://github.com/qgis/QGIS/issues/50540>`__   | `PR #50548 <https://github.com/qgis/QGIS/pull/50548>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Ensure coordinate display in status bar updates immediately when related settings change, and update the tooltip to match the actual values displayed in the widget   | `#50540 <https://github.com/qgis/QGIS/issues/50540>`__   | `PR #50548 <https://github.com/qgis/QGIS/pull/50548>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix rendering of linestrings with nan z values                                                                                                                        | `#50510 <https://github.com/qgis/QGIS/issues/50510>`__   | `PR #50549 <https://github.com/qgis/QGIS/pull/50549>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix broken logic in clearing python console history                                                                                                                   | Not reported                                             | `PR #50504 <https://github.com/qgis/QGIS/pull/50504>`__   | `PR #50515 <https://github.com/qgis/QGIS/pull/50515>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix QgsFileWidget does not reactivate widget's window after selecting a file/folder via the browse button on mac                                                      | Not reported                                             | `PR #50501 <https://github.com/qgis/QGIS/pull/50501>`__   | `PR #50502 <https://github.com/qgis/QGIS/pull/50502>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix code folding not shown for non-python code editor classes                                                                                                         | Not reported                                             | `PR #50492 <https://github.com/qgis/QGIS/pull/50492>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix leak in GEOS geometry library use                                                                                                                                 | Not reported                                             | `PR #50379 <https://github.com/qgis/QGIS/pull/50379>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix raster contour renderer ignores opacity setting                                                                                                                   | `#41663 <https://github.com/qgis/QGIS/issues/41663>`__   | `PR #50382 <https://github.com/qgis/QGIS/pull/50382>`__   | Not suitable -- too risky                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix truncation of recent project list removes too many items, raises a warning                                                                                        | Not reported                                             | `PR #50394 <https://github.com/qgis/QGIS/pull/50394>`__   | `PR #50397 <https://github.com/qgis/QGIS/pull/50397>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix dizzy easter egg                                                                                                                                                  | `#50345 <https://github.com/qgis/QGIS/issues/50345>`__   | `PR #50380 <https://github.com/qgis/QGIS/pull/50380>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix point pattern fill sometimes ignores symbol opacity setting                                                                                                       | `#48031 <https://github.com/qgis/QGIS/issues/48031>`__   | `PR #50384 <https://github.com/qgis/QGIS/pull/50384>`__   | Not suitable -- too risky                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix broken path in svg raises Qt warnings while rendering                                                                                                             | Not reported                                             | `PR #50383 <https://github.com/qgis/QGIS/pull/50383>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Ensure correct expression context is used when generating symbol preview icons                                                                                        | `#49106 <https://github.com/qgis/QGIS/issues/49106>`__   | `PR #50393 <https://github.com/qgis/QGIS/pull/50393>`__   | Not suitable -- too risky                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [spatialite] Fix corrupted default attribute values when fields are loaded using gaiaVectorLayer                                                                      | Privately reported                                       | `PR #50360 <https://github.com/qgis/QGIS/pull/50360>`__   | `PR #50361 <https://github.com/qgis/QGIS/pull/50361>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix handling of vector tiles when zoom level 0 is not available                                                                                                       | `#47934 <https://github.com/qgis/QGIS/issues/47934>`__   | `PR #50337 <https://github.com/qgis/QGIS/pull/50337>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix drag and drop of files to georeferencer window                                                                                                                    | `#49175 <https://github.com/qgis/QGIS/issues/49175>`__   | `PR #50338 <https://github.com/qgis/QGIS/pull/50338>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Never try to handle base parameter type values as map layers in QgsProcessingParameterDefinition::valueAs\* methods                                                   | `#48598 <https://github.com/qgis/QGIS/issues/48598>`__   | `PR #50327 <https://github.com/qgis/QGIS/pull/50327>`__   | Not required                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Avoid a redundant calculation of visible layer extent in overview canvas                                                                                              | Not reported                                             | `PR #50329 <https://github.com/qgis/QGIS/pull/50329>`__   | `PR #50336 <https://github.com/qgis/QGIS/pull/50336>`__   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties                                                  | `#50268 <https://github.com/qgis/QGIS/issues/50268>`__   | `PR #50326 <https://github.com/qgis/QGIS/pull/50326>`__   | Not suitable                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties                                                  | `#50268 <https://github.com/qgis/QGIS/issues/50268>`__   | `PR #50326 <https://github.com/qgis/QGIS/pull/50326>`__   | Not suitable                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Nyall Dawson <https://north-road.com/>`__

Feature: Bug fixes by Loïc Bartoletti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Bug Title                                                           | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                    | 3.22 backport commit (GitHub)                          |
+=====================================================================+==========================================================+========================================================+========================================================+
| Fix "Add Ring" tool doesn't consider all the overlapping features   | `#23113 <https://github.com/qgis/QGIS/issues/23113>`__   | `#50447 <https://github.com/qgis/QGIS/pull/50447>`__   | Not suitable - add new methods                         |
+---------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Fix wkbType cast from OGR 25D Type                                  | `#50218 <https://github.com/qgis/QGIS/issues/50218>`__   | `#50233 <https://github.com/qgis/QGIS/pull/50233>`__   | `#50251 <https://github.com/qgis/QGIS/pull/50251>`__   |
+---------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Loïc Bartoletti <https://oslandia.com/>`__

.. |image1| image:: images/projects/19a3cf4af4fcad7ecec62560b72067b903097054.png
   :class: img-responsive img-rounded center-block
.. |image3| image:: images/entries/8f0a6c8e4850886732633ab76d5873dffd7746c4.gif
   :class: img-responsive img-rounded
.. |image4| image:: images/entries/9bbc312e9b1362ae660a9719c910ab209d3e8a55.gif
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/8b43481bcab479b040b0a5ac5400ddc89c77dd0a.png
   :class: img-responsive img-rounded
.. |image6| image:: images/entries/f0c7217db5f0104999a3d87c2229010dcc62cb50.gif
   :class: img-responsive img-rounded
.. |image7| image:: images/entries/411b2d3b0f1b180857eda6d4e0c73144f1aeee57.gif
   :class: img-responsive img-rounded
.. |image8| image:: images/entries/3e749b405f10a24f95665cd0ad3e1ea0f199811b.png
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/b49f780e98b4276b76cf3022b34da26dd4ed9d1f.jpg
   :class: img-responsive img-rounded
.. |image10| image:: images/entries/b413c593933bc197886a97919ae015880e119aa7.png
   :class: img-responsive img-rounded
.. |image11| image:: images/entries/8bf480abed6701e5535110f8069ba1f63ecf2de4.gif
   :class: img-responsive img-rounded
.. |image12| image:: images/entries/996b020346252bc10d87279d9e0cac766802c1d4.png
   :class: img-responsive img-rounded
.. |image13| image:: images/entries/9b7102f1bbd9286c16285a43158904395e56c4bc.png
   :class: img-responsive img-rounded
.. |image14| image:: images/entries/99c16bf2efe3bdcf020a41ad088e29ec7437573e.png
   :class: img-responsive img-rounded
.. |image15| image:: images/entries/06cc045f6a69f9caaacde8f8b3ead9e89f02af22.png
   :class: img-responsive img-rounded
.. |image16| image:: images/entries/b9666dee9322ba767162310e6958503e639d1148.png
   :class: img-responsive img-rounded
.. |image17| image:: images/entries/f02946a8f1e45527366c30e6d0ea5a4947c7f86a.png
   :class: img-responsive img-rounded
.. |image18| image:: images/entries/bc2bbd8d26e2ebb4fd7dc02f0ce7ec6460f3a3bc.png
   :class: img-responsive img-rounded
.. |image19| image:: images/entries/e434b7356dc93f9c43fa3142c7f8f914a4aa5615.png
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/677952561ec24d417a74cf46842a6c52aec49587.png
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/17fc26636b3c1fe423ec8f715e69365495519add.png
   :class: img-responsive img-rounded
.. |image22| image:: images/entries/b2ef315dc1013852d3316023c62af5ff06626e93.png
   :class: img-responsive img-rounded
.. |image23| image:: images/entries/4b320e5bad078f1a0eb23fe958d86e330b08c10e.png
   :class: img-responsive img-rounded
.. |image24| image:: images/entries/e804b2accbcf155f4db2ea4024bd89ed5883097f.png
   :class: img-responsive img-rounded
.. |image25| image:: images/entries/26076b13de92a8ac2a1fea1511e03776c1aeae13.png
   :class: img-responsive img-rounded
.. |image26| image:: images/entries/78e9cb5b82c872604fc3616c2c7b3772e7d26bef.png
   :class: img-responsive img-rounded
.. |image27| image:: images/entries/7af6704f72373fec3c1e9c212366fd3d8cfa0218.png
   :class: img-responsive img-rounded
.. |image28| image:: images/entries/77e17395ccb70e466ad4c5a80675ad0ff8ec070e.gif
   :class: img-responsive img-rounded
.. |image29| image:: images/entries/11c3f493eff806b4eccbf9af27c96894ea3223a3.png
   :class: img-responsive img-rounded
.. |image30| image:: images/entries/7a0e8f73e24aa061244e30d6bf1b8154e5eebce4.gif
   :class: img-responsive img-rounded
.. |image31| image:: images/entries/c1c17d31db79a4beaab864daf13257e6e7ed0ba0.gif
   :class: img-responsive img-rounded
.. |image32| image:: images/entries/cc1f815593c28352dffaad020061004db91f8ded.png
   :class: img-responsive img-rounded
.. |Peek 2022-06-20 12-31| image:: https://user-images.githubusercontent.com/1829991/174514930-77887a1d-4679-49a2-9ff0-7c360bc0fc01.gif
.. |image34| image:: images/entries/2685710315d58fc03e1557e3381a41fdd8eb5a02.gif
   :class: img-responsive img-rounded
.. |image35| image:: images/entries/6a575714dfc905211f3518a4f5f3803c32e8afa9.png
   :class: img-responsive img-rounded
.. |image36| image:: images/entries/cebe844ae2c28045a8b6e2e89cb2b40cdbbd38c6.png
   :class: img-responsive img-rounded
