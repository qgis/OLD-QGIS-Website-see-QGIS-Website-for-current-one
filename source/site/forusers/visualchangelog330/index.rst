.. _changelog330:

Changelog for QGIS 3.30
=======================

|image1|

Release date: 2023-03-04

The 3.30 's-Hertogenbosch release of the groundbreaking QGIS project introduces a wide range of changes and optimizations from the QGIS developer community.

The splash screen features a fragment of the “Gemeentekaart”, or Municipality map, of 's-Hertogenbosch from 1867. It is part of a series of 1200 maps of all the communities in The Netherlands from that time, which were published in an atlas for each of the 11 regions. All maps were drawn in the same size, although for large municipalities a double format was used and scaled to match the page. The series was internationally rewarded because of its accuracy and completeness. The map was drawn by Jacob Kuyper (1821-1908), the most famous geographer and cartographer of his time in The Netherlands. Text and splash map image provided by `atlasandmap.com <https://atlasandmap.com>`__


The native GeoNode integration has also been migrated to an external plugin, leveraging the powerful extensions to the QGIS API for plugins implemented in recent releases.

Users can also look forward to new functionality and UX enhancements, including support for raster attribute tables, intelligent and configurable sorting for layer loading, improvements to GPS utilities, more dynamic form widgets, native rich media previews for attachments, better integration with cloud services, extensions to the QGIS metadata standards, and a host of other noteworthy additions.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at https://www.youtube.com/watch?v=q7O819lFKc4

:raw-html:`<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/q7O819lFKc4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>`

QGIS is a community effort, and we would like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to `QGIS.ORG <https://qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our `list of donors <https://qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our `sustaining member page <https://qgis.org/en/site/about/sustaining_members.html>`__ for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

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

Map Tools
---------

Feature: Raster MapTips
~~~~~~~~~~~~~~~~~~~~~~~

in previous releases, MapTips were only available for vector layers, but new API changes have made it possible to implement MapTips for other layer types.

Raster layers now support MapTips, and new expression utility functions have been added to extend the existing MapTips capabilities:

-  ``map_to_html_table``: converts a map (key-value pair data structure) to an HTML table
-  ``map_to_html_dl``: converts a map (key-value pair data structure) to an HTML definition list
-  ``raster_attributes``: creates a map with the fields names as keys and the raster attribute table values as values from the attribute table entry that matches the given raster value
-  a new "Map Layer Position" expression scope that defines a variable ``@layer_cursor_point`` with the layer coordinates (in the layer's CRS) under the mouse position

|image3|

This feature was funded by NOAA OCS Hydrography

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Identify on mouse move, no mouse click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new option allows for the use of the identify tool to be triggered on mouse movement, without needing to click on the canvas.

This option behaves almost identically to the default identify option, with the difference being that the user doesn't need to click or use a keyboard shortcut to trigger the identify action. This allows the identify tool to function similar to the MapTips utility, whilst providing users with the benefits of the identify tool such as support for multiple layer types and derived information.

The default trigger is a 300-millisecond timer which will execute the identify action, which is implemented to avoid performance issues when moving the mouse.

|image4|

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

User Interface
--------------

Feature: Constraint based functionality for attribute tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New constraint-based conditional styling and failing constraints feature filters have been exposed within the attribute table.

This functionality provides filtering options to view or hide features that have failing (hard or soft) constraints, and introduces a new conditional styling type that works alongside the pre-existing row and field types to highlight features which fail to meet the layer constraints.

|image5|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Additional GPS information panel and toolbar fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GPS information panel now includes the current total track length, and the distance from start of track. These features are also available as a (not-on-by-default) option which allows them to be shown in the GPS toolbar information label.

The GPS information panel also includes ellipsoidal altitude in the available GPS information values.

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: GPS Information Panel UX and Refactoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A substantial rework of the GPS information panel has been performed in order to simplify the user operation of GPS within QGIS and provide a more streamlined GPS experience.

Previously, **all** application-level GPS functionality was exposed through a single GPS "Information" panel interface, which included GPS connection settings, digitizing from GPS, and the actual display of GPS information. This interface became cluttered and difficult to use

GPS functionality has now been split up into distinct parts:

#. Application level, rarely changed GPS settings are present in the GPS tab of the Options menu within QGIS Settings.
#. A new floating "GPS Toolbar" has been added, which contains the most commonly used GPS-related operations.
#. The final action in the GPS Toolbar opens a "GPS settings" popup, that contains various settings that are expected to be modified mid-session and are expected to be more readily accessible.
#. The GPS information widget has been redesigned to show only GPS **information**. Specifically, only the "information" and "signal" tabs remain. The GPS information widget still contains a shortcut to the connect/disconnect action, and also a settings button that exposes the same GPS settings menu as is used in the GPS toolbar.

The GPS information widget class is now responsible ONLY for showing the GPS information in the panel, and new dedicated classes have been created for handling digitizing from GPS, the new GPS toolbar, and GPS settings accordingly.

|image6|

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Symbology
---------

Feature: Improved SLD Export Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new extension of the Styled Layer Descriptor (SLD) export API has been developed which exists in parallel with existing SLD export options, but provides additional functionality for the granular control of SLD exports.

This development includes the export of complex polygon layer styles as external graphic symbols which are stored alongside the exported SLD.

|image7|

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Rendering
---------

Feature: Global map terrain shading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users are now able to apply a global terrain shading effect to the map, which is based on the elevation of *all* the active layers that support elevation, including :

-  Raster layers (if "Represent elevation Surface" is checked in the layer properties)
-  Mesh layers
-  Point cloud layers.

The elevation value at any particular position for all the relevant layers are combined, and the considered elevation is chosen depending on one of two user defined methods:

-  The highest elevation is considered
-  The elevation on the topmost layer in the layer tree is considered

The implementation of shading methods are currently the Eye Dome Lighting and the hill-shade effect.

Elevation shading settings are exposed to the user interface in the following controls:

-  In project properties, in the same tab of the project elevation settings
-  In the layer styling panel, a new tab has been created for defining global terrain shading settings

|image8|

This feature was funded by `QGIS Community Crowdfunding Efforts <https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis>`__

This feature was developed by `Vincent Cloarec <https://github.com/vcloarec>`__

Feature: Add super and subscript support for text renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Text items in QGIS now support superscript and subscript.

This allows for:

-  ``<sup>superscript</sup>`` / ``<sub>subscript</sub>`` components in text, where the text will be vertically super or subscript aligned and automatically sized to 2/3rd of the parent font size. Users can also set a fixed font size for the super/subscript by including the relevant CSS rules in their HTML, e.g. ``<sup style="font-size:33pt">super</sup>``
-  ``vertical-align: super`` or ``vertical-align: sub`` CSS formatting rules in any other HTML element

|image9|

This feature was funded by OSGEO UK

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

3D Features
-----------

Feature: Limit 2D extent of 3D scene
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The rendered extent of a 3D scene can now be constrained to features that intersect a user-specified 2D extent.

The manner in which rendered features are limited is dependent on the source data layer type:

-  Flat, DEM, and Online Terrain are *clipped* at the specified extent
-  Point cloud layers *only load points within* the specified extent
-  Vector layers *only load features that intersect* the specified extent

Extent-based feature filtering on mesh layers is still currently in development.

|image10|

This feature was funded by `QGIS Community Crowdfunding Efforts <https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis>`__

This feature was developed by `Stefanos Natsis <https://github.com/uclaros>`__

Feature: Improved camera control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a couple of improvements that improve the user experience:

- Elevation range is taken into account when "Zoom full" is used (users should not end up "behind" their scene anymore)
- Move camera vertically using Ctrl + Shift + Left mouse button
- Allow wheel zooming while moving the mouse
- Continue right mouse button zooming when pointer exits the viewport

This feature was funded by `QGIS Community Crowdfunding Efforts <https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis>`__

This feature was developed by `Stefanos Natsis (Lutra Consulting) <https://www.lutraconsulting.co.uk/>`__

Print Layouts
-------------

Feature: Shortcuts manager in print layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The shortcut manager, accessible from the settings menu of the primary QGIS interface, allows users to configure and override existing keyboard shortcuts and supports user defined methods for executing QGIS Actions.

A similar keyboard manager configuration dialog has now been added to the Print Layout interface for enhanced productivity.

|image11|

This feature was developed by `Yoann Quenach de Quivillic <https://github.com/YoannQDQ>`__

Feature: Use text renderer in layout legends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This change allows the use of the full-text renderer capabilities for legend titles, subtitles, and item text.

It allows for the configuration of buffers, shadows, font spacing control, and other available options (including mixed HTML formatting) which are permitted for use in text formats.

This feature was funded by NIBIO

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Expressions
-----------

Feature: Add feature\_id() function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``feature_id($feature)`` expression function now allows for retrieving the feature ID of a feature object.

The function accepts one argument which must be a feature object. Accordingly, this function can be used with the results of any other function which returns feature objects, such as "get\_feature", "overlay\_\*", etc.

|image12|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: New is\_feature\_valid() and is\_attribute\_valid() functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New ``is_feature_valid()`` and ``is_attribute_valid()`` functions are provided in QGIS expressions. Both functions validate a feature or attribute, based on the constraints attached to fields for a given vector layer. This enables users to leverage the select-by-expression utility to locate features that have unmet constraints. In addition, users can now use the rule-based renderer to provide visual feedback through symbology indicating the constraint validity state of rendered features.

|image13|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Add x\_at, y\_at, z\_at, m\_at expression functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The available $functions are considered deprecated ($x\_at``and``\ $y\_at\`), and instead of operating on the current feature geometry the functions instead support a feature geometry as arguments.

The changes for these expressions include the creation of similar functions for other geometry measurements. These new functions include:

-  x\_at(geometry, i)
-  y\_at(geometry, i)
-  z\_at(geometry, i)
-  m\_at(geometry, i)

This feature was funded by `Métropole Européenne de Lille <https://www.lillemetropole.fr/>`__

This feature was developed by `Antoine Facchini <https://github.com/Koyaani>`__

Data Management
---------------

Feature: DateTime Field editing: segregation of display format and field value format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Efforts to improve the management of datetime field information include the explicit definition of localization formatting for the *display* of datetime fields, whilst ensuring that the editing, capture, and storage of the field values conforms with international time formatting standards.

This feature was funded by `3liz <https://3liz.com>`__

This feature was developed by `rldhont <https://github.com/rldhont>`__

Feature: Add option to directly log GPS points and tracks to a Geopackage or Spatialite db
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When activated in the GPS toolbar settings, the "Log to Geopackage/Spatialite" action will prompt the user to select an existing GPKG or SpatiaLite file, or enter a new file name. A "gps\_points" and "gps\_tracks" table will be created in the file with a predefined structure.

All incoming GPS messages will be logged to the gps\_points layer, along with speed/bearing/altitude/accuracy information from the GPS.

When the GPS is disconnected (or QGIS is closed), the entire recorded GPS track will be added to the gps\_tracks table, along with some calculated information like track length, and start and end times)

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add an explicit "Offset from UTC" option for storing GPS feature timestamps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This option allows users to manually enter a desired offset from UTC for storing GPS time stamps. This allows for full flexibility for users who need to account for daylight savings offsets or other complex time zone issues.

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Raster Attribute Tables (RAT) Suppport
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now includes extensive support for Raster Attribute Tables (RATs).

These updates provide a new RAT interface within the QGIS API, and support is provided for RATs managed by raster data providers (GDAL), as well as for generic value attribute table (VAT) files, provided that they are stored in an auxiliary DBF sidecar file.

Much of the functionality from the `Python RAT Plugin <https://github.com/noaa-ocs-hydrography/qgis-raster-attribute-table-plugin>`__ was ported into QGIS to provide native support for RATs, and a new set of GUI operations affords users the following advanced functionalities:

-  **Automatic raster styling**: If a RAT is available when adding a raster to the project and includes style information, QGIS will apply the relevant styles to the raster layer by default. Automatic loading works for both embedded RATs and sidecar VAT.DBF with same basename of the raster.
-  **RAT reclassification**: Reclassification of a raster can be performed by selecting a different column
-  **RAT Identify**: Values from the RAT row corresponding to the relevant pixel value are shown in the identify Map Tool
-  **RAT properties**: A new "Attribute Table" tab is available from the raster layers property window
-  **RAT editing**: RATs offer basic editing capabilities
-  **RAT creation from current classification**: RATs can be created from existing paletted or singleband pseudocolor styles

A gallery of these functionalities in action is `available on GitHub <https://github.com/qgis/QGIS/pull/50687>`__

|image14|

This feature was funded by NOAA OCS Hydrography

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Metadata and Metasearch
-----------------------

Feature: Add key dates to layer and project metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following fields have been added to the QGIS layer/project metadata standard:

-  Date created
-  Date published
-  Date revised
-  Date superseded

In previous releases, layer metadata had no date fields, whilst project metadata include only the created date field

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Forms and Widgets
-----------------

Feature: Audiovisual multimedia attribute attachments support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New functionality introduces multimedia support for the external resources widget, allowing users to playback audio and video media files in the attachments viewer.

This change includes additional configuration options for external resources, with two new items in the integrated viewer type combo box. The video type will take into consideration the height set by the user. If it's left to auto, the video widget will grow to fill available space.

This functionality includes the development of the ``QgsMediaWidget`` object into the QGIS API for extended multimedia support.

|image15|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Data defined editable state for form widgets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "Editable" checkbox status can now be controlled through an expression, the expression supports the "form" context, meaning that it can use ``current_value( '<field_name>' )`` to dynamically change the editable status according to changes to other fields in the form.

|image16|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Spacer widget for drag & drop attribute forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new spacer widget is provided, with the option to draw a horizontal line, affording users a greater degree of control for how forms are rendered for end users and extending functionality for improved UX with thematic breaks and improved alignment.

The widget renders as a blank space in the form, which creates a manual separation between other form objects.

When the "Draw line" option is set in the configuration it will fill the vacant space with a line in a manner similar to the horizontal rule, or ``<hr>`` tag in html.

|image17|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Dynamic text widgets with current\_value support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Text widgets now support dynamic configuration based on the values of fields present in the current form context by providing a ``current_value()`` function which may be evaluated within a ``QLabel`` object.

Using the ``current_value(  '<field_name>' )`` expression will evaluate and update the form when the form field value changes.

|image18|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Dynamic HTML widgets with current\_value support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTML widgets now support dynamic configuration based on the values of fields present in the current form context by providing a ``current_value`` function.

Using the ``current_value(  '<field_name>' )`` expression will evaluate and update the form when the form field value changes.

|image19|

This feature was funded by `Kanton Solothurn <https://geo.so.ch/>`__

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: Multiple selections with filtering in value relation widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Value Relation widget previously ignored "Use completer" option when "Allow multiple selections" was enabled. Now these two options work together and there is a search box present at the top of the table, allowing filtering of values. When "Use completer" option is not enabled, the search box is not shown as before.

|image20|

This feature was funded by `QGIS Norway <http://www.qgis.no/>`__

This feature was developed by `Stefanos Natsis (Lutra Consulting) <https://www.lutraconsulting.co.uk/>`__

Layer Legend
------------

Feature: New layer ordering improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New options for configurable layer tree insertion methods, and the automated sorting of layers added via drag and drop functions, are now available in QGIS.

The previous behavior was for QGIS to always load new layers above the currently active layer.

New options have been provided to allow for more control of how new layers are added to projects:

-  (Always) On top of the layer tree
-  Optimal index/position within the currently active layer's group

The optimal index will attempt to intelligently order layers by type (e.g. points on top of areas etc.) and provide a significantly improved experience for new users.

In addition, drag and drop added layers will be added to the layer index tree at the location of the cursor when released to ensure the layer is rendered in a predictable and intuitive manner.

|image21|

This feature was funded by `Funded by the QGIS user group Switzerland <https://www.qgis.ch/>`__

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Processing
----------

Feature: Additional options for XYZ Tile exports when using Leaflet html output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Three new optional advanced parameters have been exposed for the XYZ Tile generation algorithm:

-  Leaflet HTML output title
-  Leaflet HTML output attribution
-  Include OpenStreetMap basemap in Leaflet HTML output

|image22|

This feature was developed by `Björn Hinkeldey <https://github.com/pathmapper>`__

Feature: Support data defined parameter values when using qgis\_process tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While many processing algorithms supported data-defined parameter values, these were not possible to specify when using the qgis\_process tool (or when representing algorithm settings as JSON and qgis\_process commands), introducing limitations for utilizing QGIS within command line processing operations.

A new syntax is now provided to allow the specification of data-defined parameter values when running qgis\_process operations, and copying the algorithm settings from QGIS will now correctly handle data-defined values.

Command line arguments are specified with the ``expression:`` prefix within an encapsulated string, whilst the JSON definition is implemented using an expression object with a ``data_defined`` type definition. Note that special characters within the expression will need to use the appropriate escape characters relevant to the context in which they are used.

Considering the expression ``@variable*"field_name"*to_int('2')/100`` for the following examples, the command-line syntax would be:

::

    --PARAMETER='expression:@variable*"field_name"*to_int('\''2'\'')/100'

Whilst the JSON representation would be:

::

    "inputs": {
      "PARAMETER": {
        "expression": "@variable*\"field_name\"*to_int('2')/100",
        "type": "data_defined"
      },
      "OUTPUT": "TEMPORARY_OUTPUT"
    }

This feature was funded by the Research Institute for Nature and Forest, Flemish Govt

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: New "load\_layer" function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new ``load_layer`` expression function has been made available (exclusively for Processing expressions for the time being), which allows the loading of a map layer using a source string and provider name.

It is designed to allow the use of the expression functions which directly reference map layers (such as the aggregate functions) with a hardcoded layer path.

This permits the usage of these functions to be used outside of a project (such as via the qgis\_process tool) and perform operations such as utilizing complex aggregate functions in the refactor fields algorithm via the qgis\_process utility without creating a temporary project for data manipulation.

This feature was funded by the Research Institute for Nature and Forest, Flemish Govt

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add user interface for extent definition in GDAL Raster Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GDAL Raster Calculator now includes an interface for user-specified extent definition, so that users no longer have to specify the ``--extent`` criteria in advanced options.

This feature was developed by `Nicolas Godet <https://github.com/nicogodet>`__

Application and Project Options
-------------------------------

Feature: Add option to store selected GPS component in geometry M values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This new setting, available from the GPS settings panel, allows users to opt into creating geometries with M values from the inbuilt GPS logging tools. This applies to both features digitized from GPS logs, and from the new "Log to Geopackage/Spatialite" functionality.

Options include the storing of timestamps (as milliseconds since epoch), ground speed, altitudes, bearings, and accuracy components as m values.

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Make GPS track destination layer an explicit user choice, remember in project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In previous releases, the destination layer for newly created GPS digitized features always followed the current layer selection. This made it very tricky to design projects around GPS digitizing, as whenever a user started interacting with the project the captured GPS features would be placed unpredictably within the available layers.

The GPS feature destination layer is now an explicit choice made by the user. A user can set this layer, and then go ahead and interact with the rest of their project layers and be guaranteed that any time they hit the actions to create GPS features these features will be put into the correct layer. The destination layer is stored in the current project, so reopening a prior project will automatically restore the GPS destination layer (also making it easier for staff or scripts to create GPS digitizing projects in advance for other users and be confident that these will work correctly in the field).

Additional enhancements include:

-  GPS destination layer is now made automatically editable when a feature is created, and the user is notified accordingly. This follows the approach we use for the interactive labeling tools and avoids user frustration where the features were previously not saved without any guidance as to why.
-  The GPS toolbar actions now more intelligently follow the state of the project, GPS, and current GPS track, so that actions are only enabled when they make sense
-  UI improvements and better tooltips

|image23|

This feature was funded by NIWA

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Profile Plots
-------------

Feature: New elevation profile canvas item for QGIS Quick
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new elevation profile canvas item is available for `QGIS Quick <https://api.qgis.org/api/qgsquick.html>`__, allowing the elevation profile tools to be used in other cross platform and mobile QGIS applications.

|image24|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Elevation profile plots in print layouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is now possible to include profile plots in print layouts! There is a new "Add Elevation Profile" button in the toolbar which will initially create an empty plot. A plot can be initialized by clicking "Copy From Profile" button in the properties of the elevation profile item - this will use the active elevation profile from the main window of QGIS.

The elevation profile has wide configuration options - you can specify:

-  what layers to include
-  tolerance of the profile curve
-  chart ranges (minimum and maximum distance/elevation)
-  chart area borders and colors
-  distance and elevation axes properties - intervals of labels, grid lines appearance, fonts and more

|image25|

This feature was funded by `QGIS Community Crowdfunding Efforts <https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis>`__

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Browser
-------

Feature: Add dataset relationship editing and creation capabilities in browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This functionality allows for the creation of new embedded relationship definitions in database files for ESRI FileGeodatabases, GeoPackage, and sqlite databases.

Deleting and modification of existing relationships is also supported, however the available functionality may depend on the constraints of the actual database format.

|image26|

This feature was funded by Provincie Zuid-Holland

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Data Providers
--------------

Feature: Removal of Native GeoNode Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Native GeoNode Provider has been removed from QGIS and is now instead available as a `plugin <https://geonode.org/QGISGeoNodePlugin/>`__.

This change is due to the extension of plugin APIs to support the necessary functionalities, such as the data source manager, and was executed in line with `QEP 262 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/262>`__.

This feature was developed by `Giovanni Allegri <https://github.com/giohappy>`__

Feature: In data source manager, allow users to directly add an XYZ tile layer without having to create a connection first
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users may now directly add an XYZ tile layer in the data source manager, without having to first create a new connection.

This permits users to easily add ad-hoc XYZ layers to their map without polluting their lists of saved connections.

|image27|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: SQL Logging for OGR Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As GDAL now supports query logging callbacks for SQLite-based layers, QGIS leverages this functionality to allow for query logging in the QGIS debug tools.

This is available for OGR-based SQLite data sources (SpatiaLite/ GPKG).

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Feature: S3 Cloud Storage Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S3 compatible cloud storage, such as AWS S3 and MinIO, are now supported as a method for accessing and storing external files, made available by using the external storage UI for cloud storage of attachments.

A new QGIS Auth method named "AWS S3" has been provided to support connecting to services using the S3 protocol.

This feature was funded by Métropole Grand Lyon\*\*

This feature was developed by `Jacky Volpes <https://github.com/Djedouas>`__

Feature: Resolution aware WMTS layers with automatic upscaling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now allows for WMTS layers to take device screen resolution, or dots per inch (DPI), into account and scale up the tile resolution on high DPI screens.

A new combo box has been added in the new WMS and WMTS server dialog for configuration of the WMTS tile pixel ratio. This allows QGIS to automatically handle the scaling up and down of tiles retrieved from the service based on the rendered DPI.

Note that enabling smooth pixmap transform is recommended when automatic upscaling is active

|image28|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Drop unmaintained SAGA provider from QGIS installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This provider has not been maintained and does not work with newer SAGA versions. Users are encouraged to use the 3rd-party "Processing Saga NextGen" plugin instead.

After many many years of discussion, it's time for the inbuilt provider to go!

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Improve support of layers with unknown geometry type for WFS provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS WFS provider has been improved to look in the response to the GetCapabilities request (if using WFS 2.0) if the ``IsPoint``, ``IsCurve``, ``IsSurface`` extended filter functions are present. 

When such a layer is added to the project, a "Select Items to Add" dialog box is displayed.

This enables the user to select one or several layers among ones of ``NoGeometry``, ``MultiPoint``, ``MultiCurve``, ``MultiSurface``, ``GeometryCollection`` types.

|image32|

This feature was funded by `QGIS-DE user group <https://qgis.de>`__

This feature was developed by `Even Rouault  <https://github.com/rouault>`__

QGIS Server
-----------

Feature: QGIS\_APPLICATION\_FULL\_NAME environment variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This change defines the ``QgsApplication::applicationFullName()`` method for use with PostgreSQL ``application_name`` and QGIS Server Logging.

For QGIS Server, the ``QGIS_SERVER_APPLICATION_NAME`` can be specified instead and will take precedence over the ``QGIS_APPLICATION_FULL_NAME`` setting.

The value may also be specified in the ``/qgis/application_full_name`` variable in the QGIS Server config file.

By default, this value will be defined by the value of ``QgsApplication::applicationName()+' '+QgsApplication::platform()``.

This feature was funded by `3liz <https://3liz.com>`__

This feature was developed by `rldhont <https://github.com/rldhont>`__

Feature: GeoJSON support for WFS DescribeFeatureType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON support has been added as an output format for DescribeFeatureType requests to the QGIS Server WFS. Although not an explicit stipulation by the WFS specifications, this functionality allows for responses that match other WFS service providers such as GeoServer.

This feature was funded by `Kristianstads kommun <https://www.kristianstad.se/>`__

This feature was developed by `David Marteau <https://github.com/dmarteau>`__

Plugins
-------

Feature: Topology checker rules enabling/disabling and filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The topology checker plugin has been improved to provide functionality for better management of rules, as well as filtering on large error sets. Additional enhancements bring the UX more in line with later QGIS releases and allow productivity enhancement such as bulk deletions and rule disablement.

The topology checker rules dialog now features check boxes which are attached to individual rules, which allow for enabling/ disabling rules when running validity checks *without having to remove them*. This avoids scenarios when users don't want to lose rules but are only interested in validating a subset.

The topology checker panel also has a a new combo box below its toolbar to allow for quick filtering of errors to allow users to focus on a specific error type, although it will continue to display all error types by default.

|image29|

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Programmability
---------------

Feature: QgsExifTools Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New functionality has been added to the QgsExifTools class, including:

-  The ``readTag()`` and ``readTags()`` functions now support Xmp metadata tags
-  A new ``tagImage()`` function can be used to add individual metadata tags to a given image, which can be used in addition to the pre-existing ``geoTagImage()`` function

This feature was developed by `Mathieu Pellerin <https://github.com/nirvn>`__

Feature: Smart bracket autocomplete updates for Code Editors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous releases of QGIS included an ``autoCloseBracket`` setting for the Python Console, which had a number of limitations in its behavior, including being limited to use within the Python Console and Script Editor interfaces.

Updates to the autocomplete settings extend this functionality to other Code Editor interfaces, such as the Expression Editor, Project Macro Editor, and Script Editor. The ``autoCloseBracket`` behavior has also been adjusted to better mimic the behavior of modern IDEs, and an ``autoSurround`` setting has been added to surround selected text when using the following character sets:

-  braces/ curly brackets: ``{}``
-  square/ box brackets: ``[]``
-  parenthesis/ round brackets: ``()``
-  double quotation mark: ``"``
-  single quotation mark: ``'``
-  backticks: `````
-  asterisk: ``*``

With the exception of the backtick and asterisk characters, the autoCloseBracket functionality is available when encapsulating new data without an active text selection.

The autocompletion configuration is enabled by default for new releases, but a new settings interface is provided for granular control by users.

|image30|

This feature was developed by `Yoann Quenach de Quivillic <https://github.com/YoannQDQ>`__

Feature: Add "toggle comment" action to the integrated python console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The comment and uncomment actions of the embedded Python Editor have been replaced with a toggle comment action, which is now also available in the Processing Script Editor.

This brings the editor UX in line with other IDEs such as VSCode, which allow the ability to toggle comments.

The default shortcut for this action is set to ``Ctrl+:``

The toggle comment action is also available in **Project Macro** and **Expression Editors**, however this is only available using the ``Ctrl+:`` shortcut and oes not include the action button on the UI.

|image31|

This feature was developed by `Yoann Quenach de Quivillic <https://github.com/YoannQDQ>`__

Notable Fixes
-------------

Feature: Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Bug Title                                                                                                   | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                          | 3.28 backport commit (GitHub)                                |
+=============================================================================================================+==========================================================+==============================================================+==============================================================+
| Task: take into account GDT\_Int8                                                                           | `#50907 <https://github.com/qgis/QGIS/issues/50907>`__   | `PR #51586 <https://github.com/qgis/QGIS/pull/51586>`__      | `PR #51602 <https://github.com/qgis/QGIS/pull/51602>`__      |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Task: take into account GDT\_Int8                                                                           | `#50907 <https://github.com/qgis/QGIS/issues/50907>`__   | `PR #51587 <https://github.com/qgis/QGIS/pull/51587>`__      | N/A                                                          |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| MultiLineString from OpenFileGDB Disappears on Zoom                                                         | `#32534 <https://github.com/qgis/QGIS/issues/32534>`__   | `GDAL PR 7137 <https://github.com/OSGeo/gdal/pull/7137>`__   |                                                              |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| DATETIME: Wrong timezone for UTC in attribute table                                                         | `#48393 <https://github.com/qgis/QGIS/issues/48393>`__   | `PR #51625 <https://github.com/qgis/QGIS/pull/51625>`__      | `PR #51645 <https://github.com/qgis/QGIS/pull/51645>`__      |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| distutils is deprecated but still used                                                                      | `#51532 <https://github.com/qgis/QGIS/issues/51532>`__   | `PR #51630 <https://github.com/qgis/QGIS/pull/51630>`__      | `PR #51644 <https://github.com/qgis/QGIS/pull/51644>`__      |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Importing Data into a QGIS Created File Based Geodatabase                                                   | `#51435 <https://github.com/qgis/QGIS/issues/51435>`__   | https://github.com/nyalldawson/QGIS/pull/36                  | N/A                                                          |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Importing Data into a QGIS Created File Based Geodatabase                                                   | `#51435 <https://github.com/qgis/QGIS/issues/51435>`__   | `GDAL PR 7147 <https://github.com/OSGeo/gdal/pull/7147>`__   | `GDAL PR 7176 <https://github.com/OSGeo/gdal/pull/7176>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| OGCAPI Features url of collection with dot                                                                  | `#51663 <https://github.com/qgis/QGIS/issues/51663>`__   | `PR #51671 <https://github.com/qgis/QGIS/pull/51671>`__      | `PR #51987 <https://github.com/qgis/QGIS/pull/51987>`__      |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| CityGML Import not working with LoD2 files                                                                  | `#51647 <https://github.com/qgis/QGIS/issues/51647>`__   | `GDAL PR 7168 <https://github.com/OSGeo/gdal/pull/7168>`__   | N/A                                                          |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Broken layers when creating new table on GPKG created by third party                                        | `#51721 <https://github.com/qgis/QGIS/issues/51721>`__   | `GDAL PR 7174 <https://github.com/OSGeo/gdal/pull/7174>`__   | N/A                                                          |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| "Save Layer Edits" after "Add Polygon Feature" deletes added polygons when the objects have no attributes   | `#51247 <https://github.com/qgis/QGIS/issues/51247>`__   | `GDAL PR 7184 <https://github.com/OSGeo/gdal/pull/7184>`__   | `GDAL PR 7188 <https://github.com/OSGeo/gdal/pull/7188>`__   |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| gis transforming coordinates incorrectly                                                                    | `#51792 <https://github.com/qgis/QGIS/issues/51792>`__   | `proj PR 3621 <https://github.com/OSGeo/PROJ/pull/3621>`__   | N/A                                                          |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+
| Some versions of QGIS can't parse mixed-dtype-columns in GeoJSON                                            | `#51911 <https://github.com/qgis/QGIS/issues/51911>`__   | None: just investigation & preliminary fix attempt           |                                                              |
+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+--------------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Even Rouault <https://www.spatialys.com/>`__

Feature: Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                            | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                      | 3.28 backport commit (GitHub)                             |
+======================================================================================================================+==========================================================+==========================================================================================+===========================================================+
| Add Row does not work with postgres identity columns that have many characters                                       | `#51563 <https://github.com/qgis/QGIS/issues/51563>`__   | `PR #51641 <https://github.com/qgis/QGIS/pull/51641>`__                                  | `PR #52059 <https://github.com/qgis/QGIS/pull/52059>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| If some layers are not identifyable, QGIS Server WMS "GetFeatureInfo" returns LayerNotQueryable                      | `#51613 <https://github.com/qgis/QGIS/issues/51613>`__   | `PR #51646 <https://github.com/qgis/QGIS/pull/51646>`__ (tests only, cannot reproduce)   | N/A                                                       |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Research and diagnosys on: Bug or new behaviour on default fields values on QGIS 3.28.X                              | `#51543 <https://github.com/qgis/QGIS/issues/51543>`__   | Asked feedback to the original developer of the "feature"                                |                                                           |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| [ogr provider] Saving big CSV edit is very slow when the whole file has to be updated (such as adding a new field)   | `#51668 <https://github.com/qgis/QGIS/issues/51668>`__   | `PR #51686 <https://github.com/qgis/QGIS/pull/51686>`__                                  | `PR #51700 <https://github.com/qgis/QGIS/pull/51700>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Vector data - Graduated Symbology - Legend Format - Only use upper limit                                             | `#51691 <https://github.com/qgis/QGIS/issues/51691>`__   | `PR #51692 <https://github.com/qgis/QGIS/pull/51692>`__                                  | `PR #51696 <https://github.com/qgis/QGIS/pull/51696>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Weird interval QgsDoubleSpinbox behavior in graduated symbology with fixed interval                                  | `#51687 <https://github.com/qgis/QGIS/issues/51687>`__   | `PR #51714 <https://github.com/qgis/QGIS/pull/51714>`__                                  | No                                                        |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Project predefined scales are trimmed at thousand separator after project restart/reopening properties               | `#51735 <https://github.com/qgis/QGIS/issues/51735>`__   | `PR #51749 <https://github.com/qgis/QGIS/pull/51749>`__                                  | `PR #51766 <https://github.com/qgis/QGIS/pull/51766>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| wms getLegendGraphic call the group and not the layer when many style layers add from browser                        | `#51759 <https://github.com/qgis/QGIS/issues/51759>`__   | `PR #51765 <https://github.com/qgis/QGIS/pull/51765>`__                                  | No                                                        |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| overlay\_intersects' does not work with WFS-layer                                                                    | `#51492 <https://github.com/qgis/QGIS/issues/51492>`__   | `PR #51773 <https://github.com/qgis/QGIS/pull/51773>`__                                  | `PR #51793 <https://github.com/qgis/QGIS/pull/51793>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| multiedit in attribute table not working properly in version >=3.22                                                  | `#48077 <https://github.com/qgis/QGIS/issues/48077>`__   | `PR #51801 <https://github.com/qgis/QGIS/pull/51801>`__                                  | Risky?                                                    |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Key/Value expression constraint is not updated                                                                       | `#51791 <https://github.com/qgis/QGIS/issues/51791>`__   | `PR #51804 <https://github.com/qgis/QGIS/pull/51804>`__                                  | `PR #51811 <https://github.com/qgis/QGIS/pull/51811>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Float fields created in ArcGIS are converted into Real 12, 11 - Precision is too high                                | `#51849 <https://github.com/qgis/QGIS/issues/51849>`__   | Won't Fix                                                                                |                                                           |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| CSV datasource not converted from 3.16 to 3.22 correctly - projects not usable anymore                               | `#48587 <https://github.com/qgis/QGIS/issues/48587>`__   | `PR #51881 <https://github.com/qgis/QGIS/pull/51881>`__                                  | `PR #51950 <https://github.com/qgis/QGIS/pull/51950>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Changes on geometry get discarded on save edits when layer filter is enabled (gpkg layer)                            | `#51934 <https://github.com/qgis/QGIS/issues/51934>`__   | Works for me                                                                             |                                                           |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| If a widget default value is setup as NULL then it's not working as it's overriden by database column default        | `#51818 <https://github.com/qgis/QGIS/issues/51818>`__   | Won't Fix (probably: still debating)                                                     |                                                           |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Can't use raster Unique values symbolgogy for Integer rasters with a single value of 1                               | `#51822 <https://github.com/qgis/QGIS/issues/51822>`__   | `PR #51975 <https://github.com/qgis/QGIS/pull/51975>`__                                  | `PR #51979 <https://github.com/qgis/QGIS/pull/51979>`__   |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+
| PyQGIS QgsPolygon creation crashes                                                                                   | `#51978 <https://github.com/qgis/QGIS/issues/51978>`__   | `PR #52004 <https://github.com/qgis/QGIS/pull/52004>`__                                  | TODO                                                      |
+----------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Alessandro Pasotti <https://www.qcooperative.net/>`__

Feature: Bug fixes by Julien Cabieces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                  | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.28 backport commit (GitHub)                             |
+============================================================================================================+==========================================================+===========================================================+===========================================================+
| Area Simplify drops Z and M values                                                                         | `#50742 <https://github.com/qgis/QGIS/issues/50742>`__   | `PR #51695 <https://github.com/qgis/QGIS/pull/51695>`__   | `PR #51742 <https://github.com/qgis/QGIS/pull/51742>`__   |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| NULL Value is displayed as NULL html link in the File widget                                               | `#50892 <https://github.com/qgis/QGIS/issues/50892>`__   | `PR #51770 <https://github.com/qgis/QGIS/pull/51770>`__   | `PR #51775 <https://github.com/qgis/QGIS/pull/51775>`__   |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Vertex Editor table shows incorrect columns in QGIS 3.28                                                   | `#51433 <https://github.com/qgis/QGIS/issues/51433>`__   | `PR #51774 <https://github.com/qgis/QGIS/pull/51774>`__   | `PR #51986 <https://github.com/qgis/QGIS/pull/51986>`__   |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Copying fetures to PostgreSQL layer not copying same name attribute value                                  | `#51121 <https://github.com/qgis/QGIS/issues/51121>`__   | Won't Fix                                                 |                                                           |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Crash when switching style to point displacement from geometry generator                                   | `#51070 <https://github.com/qgis/QGIS/issues/51070>`__   | `PR #51784 <https://github.com/qgis/QGIS/pull/51784>`__   | TODO                                                      |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix trust parameter not saved and not read                                                                 | not reported                                             | `PR #51854 <https://github.com/qgis/QGIS/pull/51854>`__   | TODO                                                      |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| North Arrow Decoration: file selector for custom SVG does not work correctly                               | `#51850 <https://github.com/qgis/QGIS/issues/51850>`__   | `PR #51882 <https://github.com/qgis/QGIS/pull/51882>`__   | `PR #51949 <https://github.com/qgis/QGIS/pull/51949>`__   |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Filter dialog for vector layers in edit state can still be opened via the filter icon in the layers menu   | `#51816 <https://github.com/qgis/QGIS/issues/51816>`__   | `PR #51884 <https://github.com/qgis/QGIS/pull/51884>`__   | `PR #51990 <https://github.com/qgis/QGIS/pull/51990>`__   |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Julien Cabieces <https://oslandia.com/>`__

Feature: Bug fixes by Sandro Santilli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                     | URL issues.qgis.org (if reported)                                                              | URL Commit (Github)                                       | 3.28 backport commit (GitHub)                             |
+===============================================================+================================================================================================+===========================================================+===========================================================+
| CI fails upon touching src/test/qgistest.h                    | `#51917 <https://github.com/qgis/QGIS/issues/51917>`__                                         |                                                           |                                                           |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| TestQgsTileDownloadManager::testIdleThread is unstable        | `#48927 <https://github.com/qgis/QGIS/issues/48927>`__                                         | `PR #51916 <https://github.com/qgis/QGIS/pull/51916>`__   |                                                           |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Crash on exit with static ``QgsCoordinateReferenceSystem``    | `#51893 <https://github.com/qgis/QGIS/issues/51893>`__                                         | `PR #51891 <https://github.com/qgis/QGIS/pull/51891>`__   | `PR #51954 <https://github.com/qgis/QGIS/pull/51954>`__   |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Allow to skip PostgreSQL backend dependent tests at runtime   | `Discussion in PR #51891 <https://github.com/qgis/QGIS/pull/51891#discussion_r1109132667>`__   | `PR #51910 <https://github.com/qgis/QGIS/pull/51910>`__   | N/A                                                       |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Do not discard geometry attributes having no SRID             | `#49380 <https://github.com/qgis/QGIS/issues/49380#issuecomment-1282913470>`__                 | `PR #51885 <https://github.com/qgis/QGIS/pull/51885>`__   | `PR #51997 <https://github.com/qgis/QGIS/pull/51997>`__   |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Sandro Santilli (strk) <https://strk.kbt.io/>`__

Feature: Bug fixes by Jean Felder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                | URL issues.qgis.org (if reported)   | URL Commit (Github)                                       | 3.28 backport commit (GitHub)                             |
+==========================================================================+=====================================+===========================================================+===========================================================+
| wms getcapabilities crashes on dimensional data if there are no values   | not reporterd                       | `PR #51930 <https://github.com/qgis/QGIS/pull/51930>`__   | `PR #51933 <https://github.com/qgis/QGIS/pull/51933>`__   |
+--------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [3D] Fix Y-Z inversion in point3dsymbolwidget                            | not reporterd                       | `PR #51855 <https://github.com/qgis/QGIS/pull/51855>`__   | `PR #51938 <https://github.com/qgis/QGIS/pull/51938>`__   |
+--------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Jean Felder <https://oslandia.com/>`__

Feature: Bug fixes by Jacky Volpes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                           | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.28 backport commit (GitHub)   |
+=====================================================+==========================================================+===========================================================+=================================+
| Missing "Save style..." icon in Layer Style Panel   | `#51515 <https://github.com/qgis/QGIS/issues/51515>`__   | `PR #52037 <https://github.com/qgis/QGIS/pull/52037>`__   | Risky?                          |
+-----------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Jacky Volpes <https://oslandia.com/>`__

Feature: Bug fixes by Stefanos Natsis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                       | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.28 backport commit (GitHub)                             |
+=================================================================================================================+==========================================================+===========================================================+===========================================================+
| Drag and drop point clouds from the browser add the layer twice                                                 | not reporterd                                            | `PR #51685 <https://github.com/qgis/QGIS/pull/51685>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Opening more than 16 vector layers at once causes crash                                                         | not reporterd                                            | `PR #51782 <https://github.com/qgis/QGIS/pull/51782>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Crash when try to split line by point                                                                           | `#51501 <https://github.com/qgis/QGIS/issues/51501>`__   | `PR #51797 <https://github.com/qgis/QGIS/pull/51797>`__   | `PR #51951 <https://github.com/qgis/QGIS/pull/51951>`__   |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| QGIS 3.26 crashes when performing "split with line".                                                            | `#50948 <https://github.com/qgis/QGIS/issues/50948>`__   | `PR #51797 <https://github.com/qgis/QGIS/pull/51797>`__   | `PR #51951 <https://github.com/qgis/QGIS/pull/51951>`__   |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Cannot split line geometry at vertex if the geometry has Z dimension                                            | `#49403 <https://github.com/qgis/QGIS/issues/49403>`__   | `PR #51797 <https://github.com/qgis/QGIS/pull/51797>`__   | `PR #51951 <https://github.com/qgis/QGIS/pull/51951>`__   |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Current implementation of multiple-layer style paste doesn't work for the command menu "Layer / Paste Style".   | `#25214 <https://github.com/qgis/QGIS/issues/25214>`__   | `PR #51799 <https://github.com/qgis/QGIS/pull/51799>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Copy attribute / Copy feature attributes doesn't return value if value is URI                                   | `#26899 <https://github.com/qgis/QGIS/issues/26899>`__   | `PR #51803 <https://github.com/qgis/QGIS/pull/51803>`__   |                                                           |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Split tool tries to split even without any digitized points                                                     | not reported                                             | `PR #51831 <https://github.com/qgis/QGIS/pull/51831>`__   | `PR #51955 <https://github.com/qgis/QGIS/pull/51955>`__   |
+-----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Stefanos Natsis <https://www.lutraconsulting.co.uk/>`__

Feature: Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Bug Title                                                                                                           | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.28 backport commit (GitHub)                             |
+=====================================================================================================================+==========================================================+===========================================================+===========================================================+
| Fix using interpolated line symbol layer for polygon outlines                                                       | Unreported                                               | `PR #52030 <https://github.com/qgis/QGIS/pull/52030>`__   | `PR #52032 <https://github.com/qgis/QGIS/pull/52032>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [processing] Don't raise uncaught exceptions when trying to generate GDAL commands for invalid layers               | `#51958 <https://github.com/qgis/QGIS/issues/51958>`__   | `PR #51994 <https://github.com/qgis/QGIS/pull/51994>`__   | `PR #52001 <https://github.com/qgis/QGIS/pull/52001>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Don't use scientific notation when generating gdal\_translate command from georeferencer                            | `#51813 <https://github.com/qgis/QGIS/issues/51813>`__   | `PR #51993 <https://github.com/qgis/QGIS/pull/51993>`__   | `PR #52071 <https://github.com/qgis/QGIS/pull/52071>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Immediately apply color ramp label precision and suffix changes when auto apply is checked                          | Unreported                                               | `PR #51989 <https://github.com/qgis/QGIS/pull/51989>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [processing] Fix exception when setting output files in batch processing after removing rows                        | `#51664 <https://github.com/qgis/QGIS/issues/51664>`__   | `PR #51988 <https://github.com/qgis/QGIS/pull/51988>`__   | `PR #51998 <https://github.com/qgis/QGIS/pull/51998>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [processing] Gracefully handle algorithms with no provider set                                                      | `#51971 <https://github.com/qgis/QGIS/issues/51971>`__   | `PR #51985 <https://github.com/qgis/QGIS/pull/51985>`__   | `PR #51999 <https://github.com/qgis/QGIS/pull/51999>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Nan z values should not be clipped from rendered geometries                                                         | `#51796 <https://github.com/qgis/QGIS/issues/51796>`__   | `PR #51984 <https://github.com/qgis/QGIS/pull/51984>`__   | `PR #51996 <https://github.com/qgis/QGIS/pull/51996>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Don't try to download whole COG locally in order to determine open options                                          | Unreported                                               | `PR #51982 <https://github.com/qgis/QGIS/pull/51982>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix loss of first color for lineburst symbol layers in GUI                                                          | `#51942 <https://github.com/qgis/QGIS/issues/51942>`__   | `PR #51952 <https://github.com/qgis/QGIS/pull/51952>`__   | `PR #51968 <https://github.com/qgis/QGIS/pull/51968>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix inefficient vector iteration when no rule based rules match current map scale                                   | Unreported                                               | `PR #51904 <https://github.com/qgis/QGIS/pull/51904>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix logic for triggering a full model reset in attribute table after changing attributes                            | Unreported                                               | `PR #51890 <https://github.com/qgis/QGIS/pull/51890>`__   | `PR #51892 <https://github.com/qgis/QGIS/pull/51892>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix placement of perimeter labels with HTML formatting enabled                                                      | `#51829 <https://github.com/qgis/QGIS/issues/51829>`__   | `PR #51840 <https://github.com/qgis/QGIS/pull/51840>`__   | `PR #51868 <https://github.com/qgis/QGIS/pull/51868>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix data loss in secondary geometry columns when displaying in attribute form                                       | `#49380 <https://github.com/qgis/QGIS/issues/49380>`__   | `PR #51863 <https://github.com/qgis/QGIS/pull/51863>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix data loss when layers with secondary geometry columns are used in processing tools                              | `#49380 <https://github.com/qgis/QGIS/issues/49380>`__   | `PR #51846 <https://github.com/qgis/QGIS/pull/51846>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Correctly handle geometry value conversion for geometry fields                                                      | `#49380 <https://github.com/qgis/QGIS/issues/49380>`__   | `PR #51845 <https://github.com/qgis/QGIS/pull/51845>`__   | `PR #51859 <https://github.com/qgis/QGIS/pull/51859>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Show an icon for geometry fields                                                                                    | Unreported                                               | `PR #51844 <https://github.com/qgis/QGIS/pull/51844>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix geometry fields incorrectly show as "range" types in fields list                                                | Unreported                                               | `PR #51842 <https://github.com/qgis/QGIS/pull/51842>`__   | `PR #51860 <https://github.com/qgis/QGIS/pull/51860>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Ensure correct crs is available for QgsMapCanvas for slots connected to extentsChanged when canvas CRS is changed   | `#51833 <https://github.com/qgis/QGIS/issues/51833>`__   | `PR #51841 <https://github.com/qgis/QGIS/pull/51841>`__   | `PR #51873 <https://github.com/qgis/QGIS/pull/51873>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix array\_remove\_all behavior when removing null values from array                                                | `#51820 <https://github.com/qgis/QGIS/issues/51820>`__   | `PR #51838 <https://github.com/qgis/QGIS/pull/51838>`__   | `PR #51869 <https://github.com/qgis/QGIS/pull/51869>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Use a better approach to update virtual layer queries which doesn't lose all the layer's properties                 | `#51118 <https://github.com/qgis/QGIS/issues/51118>`__   | `PR #51780 <https://github.com/qgis/QGIS/pull/51780>`__   | `PR #51872 <https://github.com/qgis/QGIS/pull/51872>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [layouts] Use nicer number formatting for dynamic map scale labels                                                  | `#51764 <https://github.com/qgis/QGIS/issues/51764>`__   | `PR #51768 <https://github.com/qgis/QGIS/pull/51768>`__   | Not possible                                              |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Re-permit format\_number to omit group separators                                                                   | Unreported                                               | `PR #51761 <https://github.com/qgis/QGIS/pull/51761>`__   | `PR #51763 <https://github.com/qgis/QGIS/pull/51763>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Remember the collapsed state of the vector layer renderer group box                                                 | Unreported                                               | `PR #51719 <https://github.com/qgis/QGIS/pull/51719>`__   | Not appropriate                                           |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| When unchecking render layers as a group, ensure child layers don't have clipping blend modes                       | `#51358 <https://github.com/qgis/QGIS/issues/51358>`__   | `PR #51707 <https://github.com/qgis/QGIS/pull/51707>`__   | Too intrusive                                             |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix incorrect georeferencing of images                                                                              | `#51699 <https://github.com/qgis/QGIS/issues/51699>`__   | `PR #51705 <https://github.com/qgis/QGIS/pull/51705>`__   | `PR #51736 <https://github.com/qgis/QGIS/pull/51736>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix crash when showing tooltips for invalid layers                                                                  | Unreported                                               | `PR #51703 <https://github.com/qgis/QGIS/pull/51703>`__   | `PR #51708 <https://github.com/qgis/QGIS/pull/51708>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix map tips do not show for vector layers where the HTML map tip option isn't used                                 | Unreported                                               | `PR #51702 <https://github.com/qgis/QGIS/pull/51702>`__   | Unaffected                                                |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix creation of GeoPDF with exported themes containing slashes                                                      | `#51480 <https://github.com/qgis/QGIS/issues/51480>`__   | `PR #51633 <https://github.com/qgis/QGIS/pull/51633>`__   | `PR #51677 <https://github.com/qgis/QGIS/pull/51677>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Avoid redo-ing the legend symbol hit test for legend edits which won't affect the legend symbols visible in a map   | `#51455 <https://github.com/qgis/QGIS/issues/51455>`__   | `PR #51681 <https://github.com/qgis/QGIS/pull/51681>`__   | `PR #51738 <https://github.com/qgis/QGIS/pull/51738>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Optimise legend filter by map/expression calculations                                                               | `#51233 <https://github.com/qgis/QGIS/issues/51233>`__   | `PR #51675 <https://github.com/qgis/QGIS/pull/51675>`__   | Too risky                                                 |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| [georeferencer] Fix warning about missing output file name doesn't show in all circumstances                        | Unreported                                               | `PR #51673 <https://github.com/qgis/QGIS/pull/51673>`__   | `PR #51739 <https://github.com/qgis/QGIS/pull/51739>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Ensure using @geometry/@feature variables trigger geometry fetching in expression calculation                       | `#50791 <https://github.com/qgis/QGIS/issues/50791>`__   | `PR #51655 <https://github.com/qgis/QGIS/pull/51655>`__   | `PR #51678 <https://github.com/qgis/QGIS/pull/51678>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix generation of raster elevation profiles for exactly horizontal/vertical lines                                   | `#51196 <https://github.com/qgis/QGIS/issues/51196>`__   | `PR #51637 <https://github.com/qgis/QGIS/pull/51637>`__   | `PR #52072 <https://github.com/qgis/QGIS/pull/52072>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Percent encode text values when creating/updating fields on ArcGIS feature services                                 | `#51509 <https://github.com/qgis/QGIS/issues/51509>`__   | `PR #51636 <https://github.com/qgis/QGIS/pull/51636>`__   | `PR #51654 <https://github.com/qgis/QGIS/pull/51654>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Fix drag and drop to GDB results in columns shifted by on                                                           | `#51435 <https://github.com/qgis/QGIS/issues/51435>`__   | `PR #51634 <https://github.com/qgis/QGIS/pull/51634>`__   | `PR #51969 <https://github.com/qgis/QGIS/pull/51969>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+
| Expose option for irregular time steps when exporting map animations                                                | `#51546 <https://github.com/qgis/QGIS/issues/51546>`__   | `PR #51632 <https://github.com/qgis/QGIS/pull/51632>`__   | `PR #51638 <https://github.com/qgis/QGIS/pull/51638>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `Nyall Dawson <https://north-road.com/>`__

Feature: Bug fixes by David Signer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Bug Title                                                                       | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.28 backport commit (GitHub)   |
+=================================================================================+==========================================================+===========================================================+=================================+
| WMS legend symbol missing for "Meters at Scale" symbology and projected CRS     | `#50366 <https://github.com/qgis/QGIS/issues/50366>`__   | `PR #52015 <https://github.com/qgis/QGIS/pull/52015>`__   |                                 |
+---------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Attribute table form view looses index when a layer depending on changed        | `#43902 <https://github.com/qgis/QGIS/issues/43902>`__   | `PR #52046 <https://github.com/qgis/QGIS/pull/52046>`__   |                                 |
+---------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Attribute table form view looses index when the "yellow" selection is changed   | unreported                                               | `PR #52045 <https://github.com/qgis/QGIS/pull/52045>`__   |                                 |
+---------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+
| Features in Relation Editor are not selectable anymore                          | unreported                                               | `PR #51914 <https://github.com/qgis/QGIS/pull/51914>`__   | Unaffected                      |
+---------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+

This feature was funded by `QGIS.ORG (through donations and sustaining memberships) <https://qgis.org/>`__

This feature was developed by `David Signer <https://opengis.ch/>`__

.. |image1| image:: images/projects/af9e5405a8329d7de8959238a3d499da780c1598.png
   :class: img-responsive img-rounded center-block
.. |image3| image:: images/entries/7cc33f0191d7461c103eef9eb792495d4b298dd6.png
   :class: img-responsive img-rounded
.. |image4| image:: images/entries/36bfbae2b85c46b304ea84c05ce819fd69a66d38.gif
   :class: img-responsive img-rounded
.. |image5| image:: images/entries/4ad89600c1e78bca863927f30581319b86afe6f1.png
   :class: img-responsive img-rounded
.. |image6| image:: images/entries/206ae34a728a37cae967f60887b5a7f2bbd94c0f.png
   :class: img-responsive img-rounded
.. |image7| image:: images/entries/cce332a4adc8cc7a24ead53acd8924431f1085f2.png
   :class: img-responsive img-rounded
.. |image8| image:: images/entries/e75c69fb42f1916ceaf4b30f589154dc47881c6f.png
   :class: img-responsive img-rounded
.. |image9| image:: images/entries/24e510e32b919b373d09e5fe8536cfc0dfd0d66e.png
   :class: img-responsive img-rounded
.. |image10| image:: images/entries/a8135c9cfcaa91fdc540512f36cf276a2cdb4f02.png
   :class: img-responsive img-rounded
.. |image11| image:: images/entries/ce065abd5dfe0a678e461a12e0efef92c5acaae3.gif
   :class: img-responsive img-rounded
.. |image12| image:: images/entries/6536913b10d68dded9a54bc58ba003b821b100f6.png
   :class: img-responsive img-rounded
.. |image13| image:: images/entries/f6a73012edcc84033d40e91bc6216365fd4f5ae6.png
   :class: img-responsive img-rounded
.. |image14| image:: images/entries/4406611cee132d2bfae92d9ba01681464f333928.gif
   :class: img-responsive img-rounded
.. |image15| image:: images/entries/75fcba5750d9ce4bb1b7ad41089dd39fd11ae827.png
   :class: img-responsive img-rounded
.. |image16| image:: images/entries/ce2bc7938c4c5f28d3f0d872e9045c856ef79ef1.gif
   :class: img-responsive img-rounded
.. |image17| image:: images/entries/72c262227fb339abd30833edc712ead25d943044.png
   :class: img-responsive img-rounded
.. |image18| image:: images/entries/6de3cc5d5a6d002fd014717e57f251ec9b0147d9.gif
   :class: img-responsive img-rounded
.. |image19| image:: images/entries/f04157ac77cf00862595f8b75707c8126e121ce4.gif
   :class: img-responsive img-rounded
.. |image20| image:: images/entries/3ec355e558ca705d17be8f21c79c613d1022630a.gif
   :class: img-responsive img-rounded
.. |image21| image:: images/entries/a2f44bdf5df6e8b33dc71c975cbb9c01cfa4845c.png
   :class: img-responsive img-rounded
.. |image22| image:: images/entries/a96f4972c9664c8887220b0a218103c053050e71.png
   :class: img-responsive img-rounded
.. |image23| image:: images/entries/9563911d7eeb4412cd32f237969579aa1ed6aa90.gif
   :class: img-responsive img-rounded
.. |image24| image:: images/entries/f870a9112a3577742c6f8c6a98b142b23145d525.png
   :class: img-responsive img-rounded
.. |image25| image:: images/entries/ca6f01c1c76d7cff23ff8d27492734c74b8c3973.png
   :class: img-responsive img-rounded
.. |image26| image:: images/entries/2e902df01faff7f71bdfe3854c5b1a38e013e8d8.gif
   :class: img-responsive img-rounded
.. |image27| image:: images/entries/1e5a07f058db3b16265d94f6e535ac7c79664bcd.gif
   :class: img-responsive img-rounded
.. |image28| image:: images/entries/a921de87af46b4774b94bd632e704527f840ea55.png
   :class: img-responsive img-rounded
.. |image29| image:: images/entries/52e54d9f31a12f024d3c452ecbc77fb3278c18e4.png
   :class: img-responsive img-rounded
.. |image30| image:: images/entries/2ed531d2789b12d258d1503c8fb74e396f06e63d.png
   :class: img-responsive img-rounded
.. |image31| image:: images/entries/fb255d60095471377459f1c6907df83e6f54bea4.gif
   :class: img-responsive img-rounded
.. |image32| image:: images/entries/2068734219e240ca90b22435ca1381f3c8e4b9ef.png
   :class: img-responsive img-rounded

