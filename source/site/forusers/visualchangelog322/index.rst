.. _changelog322:

Changelog for QGIS 3.22
=======================

|image1|

QGIS 3.22 Białowieża is aimed at celebrating the 100-year anniversary of `Białowieża National Park <https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_National_Park>`__, Poland, which was established in 1921. `Białowieża Forest <https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_Forest>`__ is one of the world’s last primary woodlands, located on the border between Poland and Belarus. It is one of the few natural old-growth forests in temperate lowland Europe and has been protected for over 600 years. The outstanding value of Białowieża Forest has been acknowledged by its recognition as a `UNESCO Natural World Heritage Site <https://whc.unesco.org/en/list/33>`__.

Białowieża Forest is named after the village Białowieża, which is located right in the middle of this woodland. It is one of the oldest settlements in the area, nowadays hosting numerous research and tourism activities. Today, there are three research institutions in the village: `Białowieża Geobotanical Station, University of Warsaw <https://bsg.bialowieza.pl/en/>`__, `The Mammal Research Institute, Polish Academy of Sciences <https://ibs.bialowieza.pl/en/>`__, and the `Forest Research Institute, Department of Natural Forests <https://www.ibles.pl/en/web/guest/home>`__. Additionally, a large number of scientists from Poland and abroad travel to Białowieża in order to carry out their studies, and as such, there are also other users of QGIS in the area, as well as additional projects which contribute to the Open Data and Open Source Software ecosystems, such as the `Open Forest Data <https://openforestdata.pl/>`__ project.

You can learn more about the project and this release of QGIS at the dedicated project website, https://qgisbialowieza.pl.

This feature-packed release includes a vast number of user experience enhancements and controls added to various advanced functionalities. In addition to a host of additional mesh functionality and operational improvements, QGIS Desktop now includes annotation tools and support for annotation layers, amongst much, much more. For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video at https://youtu.be/U-RHBt6WZi8

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to `QGIS.ORG <qgis.org>`__ and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our `donors list <https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors>`__. If you would like to become an official project sustaining member, please visit our `sustaining member page <https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships>`__ for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is free software and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision-making tools will result in a better society for all of humanity.

.. contents::
   :local:


Annotations
-----------

Feature: Annotation layer properties and effects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additional properties for annotation layers now include the following:

-  An annotation layer properties window, containing some basic information about the layer and options to set scale ranges, opacity, blend mode and draw effects for the layer
-  An option to view the main annotation layer's properties via the annotation toolbar (the main annotation layer is the hidden layer which is always present above all other map layers, so it's impossible to open it's property window via the layer tree)
-  Options to set an annotation layer's opacity/blend mode/paint effect in the layer styling dock for interactive changes

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Edit nodes in an annotation item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The modify annotation tool can now be used to edit nodes in an annotation item by clicking over an existing node and moving it. The user interactions follow the standard QGIS patterns as follows:

-  Left click to start the move
-  Second left click to apply changes
-  Right-click to cancel
-  Selecting a node and pressing delete will remove the node
-  Double clicking a segment will add a node

|image2|

This feature was funded by the Swiss QGIS user group.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Move selected annotation with cursor keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an annotation item is selected it can be moved by pressing the cursor keys.

This functionality includes the ability to use keyboard shortcuts in a manner that follows the same interaction pattern as used with layout items:

-  ``shift + cursor``: Big movement
-  ``alt + cursor``: 1px movement

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Create line/ polygon annotation item tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions for creating new line and polygon annotation items have been added to the annotation tools.

These support the same interactions as drawing vector features, such as snapping, tracing, cad dock, backspace to remove vertices, curve and stream digitizing modes, and others.

This feature was funded by QGIS Swiss User Group

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: New point text tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A framework has been created for map tools to create new annotation items, including the ability to create new point text annotation items.

|image3|

This feature was funded by the Swiss QGIS user group

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Annotations toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new annotations toolbar has been added which provides actions for the following:

-  Create a new empty annotation layer in the current project.
-  The "Modify Annotations" tool, which provides an interface for editing existing annotations.

The supported operations for the modify annotations feature include:

-  Clicking on an existing annotation to select it to shows its properties in the layer styling dock, including symbol, reference scale, z index, etc/
-  Left click on a selected annotation item to start moving it. A right click or escape cancels the move, while a second left click will confirm the move.
-  Pressing the delete key while an annotation is selected will delete that annotation

This feature was funded by the Swiss QGIS User group

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Map Tools
---------

Feature: Add a "measure bearing" map tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tool behaves similarly to the existing "measure angle" map tool, but requires the user only to click two points on the map and displays the bearing between these points.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

User Interface
--------------

Feature: Toggle editing on multiple selected layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The *toggle editing* action has been modified to support activation on all selected layers, making it easy to start and stop editing sessions across multiple layers simultaneously. Although the editing session status for all selected layers may not be the same, all selected layers will be toggled to an active or inactive state as the inverse of the current state of the currently active layer. This functionality is applied to the menu item *Layer > Toggle Editing*, the *Toggle Editing* button on the digitizing toolbar, and the *Toggle Editing* entry in the layers context menu.

This feature was developed by `Stefanos Natsis <https://github.com/uclaros>`__

Feature: Identify layer groups and all selected layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Whilst the identify features tool supported multiple selection modes, the "current layer" mode has been extended to support the selection of layer groups, and will identify features from all selected layers. Only features from visible layers within a layer group will be identified.

This feature was developed by `Stefanos Natsis <https://github.com/uclaros>`__

Feature: Add a 'Show in Files' action for all file items in browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Opens a file explorer window and directly selects the file

Also fixes the existing "File Properties" action so that it shows regardless of the file type, and doesn't show incorrectly in some circumstances.

|image4|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Symbology
---------

Feature: Custom units for geometry generator symbol layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Geometry generators now expose an option for users to select which units should be used for returning geometries in, rather than only supporting the units defined in the layer CRS. This is especially useful in situations where the symbol is not associated with a layer, such as when used in layout items.

The update provides the following unit choices:

-  Map units (the default, previous behavior)
-  Millimeters
-  Pixels
-  Inches
-  Points

When millimeters, pixels, inches or points are selected, then the @map\_geometry variable will be available for use within the expression, containing the feature geometry in the specified units (relative to the map frame), whilst the $geometry variable remains available within the expression in the layer CRS map units.

|image5|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Symbology reference scale for vector layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An option has been exposed that allows the configuration of reference scales for feature symbologies on vector layers.

In practice, this defines the relevant map scale at which the configured symbology and label sizes may be referenced with paper-based units, such as millimeters or points. These unit sizes will then be automatically scaled accordingly, based on the ratio of the relevant reference scale and the scale of the current map view.

For instance, where a line layer is configured to use a 2mm wide line using a reference scale of 1:2000, the feature would be rendered using 4mm wide lines at a map scale of 1:1000, or 1mm with a map scale of 1:4000.

This feature was funded by North Road, thanks to SLYR

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Invert colors filter option for raster rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is now possible to invert the colors of a raster being rendered via a new invert colors option. This can come in handy on a number of occasions. For example, a light raster base map can quickly be turned into a dark base map without the need to recreate a new raster dataset.

|image6|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Labelling
---------

Feature: Specify unit for data defined label rotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the angle unit for data defined label rotation

|image|

|Peek 2021-08-29 14-38|

This feature was developed by `Damiano Lombardi <https://github.com/domi4484>`__

Mesh
----

Feature: Create new mesh layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now supports the creation of new mesh layers.

The mesh creation supports the following creation formats:

-  New empty mesh layer
-  New mesh frame based on an existing mesh within the project
-  New mesh frame based on an existing mesh from a file

|image9|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Mesh frame editing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now supports mesh frame editing, which supports the ability to ensure mesh consistency and provides the ability to undo and redo edit operations.

This introduces the ``QgsMeshEditor`` class to the QGIS Python API, which allows for performing edit operations, and the QgsTopologicalMesh class which is not exposed to the Python API but is used for ensuring that edited mesh elements remain topologically correct and perform data modifications.

|image10|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Mesh frame editing lifecycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature has been introduced in the scope of `QEP 228 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228>`__ which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

Mesh frame editing now supports a complete set of functionalities for controlling the editing lifecycle operations, including start, commit, roll back, and cancel, similar to vector layers.

|image11|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Edit mesh map tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature has been introduced in the scope of `QEP 228 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228>`__ which outlines the introduction of Mesh Editing tools.

Mesh editing map tool now supports the following operations:

-  Add vertices/ faces
-  Select vertices/ faces
-  Remove vertices/ faces
-  Change the Z values of vertices
-  Move vertices
-  Interaction with edges
-  Split faces

|image12|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Advanced mesh editing enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature has been introduced in the scope of `QEP 228 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228>`__ which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

The QGIS User Interface provides delaunay triangulation and face refinement functions, which are accessible from the context menu in the map when vertices and/ or faces are selected from a mesh layer. These options may be migrated to buttons in the mesh toolbar once further functionality has been introduced.

|mapToolrefine|

The QGIS API has also been extended to support advanced editing for meshes, which is introduced by a new interface abstract class QgsMeshAdvancedEditing.
Derived classes of this class can be implemented to make some advanced editing on a mesh: generation of faces to add to the mesh, particular operation on many faces or vertices. The advanced editing is made by passing a QgsMeshAdvancedEditing instance to a QgsmeshEditor instance, and the editing is applied as other editing operations.

Two advanced editing functions are implemented within this feature:

-  Delaunay triangulation
-  Faces refinement

|image14|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Select editable mesh elements by polygon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can now select mesh elements within a digitized area when performing mesh editing. Each vertex of the polygon is digitized using a left click, whilst right clicking will complete and validate the polygon to select intersecting mesh elements (faces and vertices). Using the backspace key will allow the user to remove last vertex, and the Escape key will allow users to return to the normal digitizing mode.

This function supports two behavior modes with different selection predicates as follows:

-  Touching elements (default), or partially included/ intersecting elements will be selected (green rubber band).
-  Contained, or completely included elements will be selected (blue rubber band).

|image15|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Select mesh elements by existing geometries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two actions have been added for selecting mesh elements from geometries present in existing vector layers.

After selecting vector layer geometries, the user can use these tools to select mesh elements using the touching or containing predicates.

|image16|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Select mesh elements by expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An interface has been created for selecting mesh elements by expression during mesh editing. In addition, a contextual expression function ``$face_area`` has been added that returns the area of a mesh face.

|image17|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Transform single vertex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new editing mode for the mesh transform tool allows the user to import the coordinates of a single selected vertex.

The tool button on the top right of the Transform Mesh Vertices window toggles this mode, and each time a single vertex is selected it will automatically populate the available fields for the user to adjust the vertex coordinates accordingly.

|image18|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Reindex/ renumber mesh layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users are now able to reindex (or renumber) the vertices and faces of a mesh layer during editing. The renumbering is an optimization of the mesh with the Cuthill-McKee algorithm.

|image19|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Force mesh by polylines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When editing mesh features, users can now transform features by forcing them to conform to a surface defined by existing polylines, or break lines. Faces are forced to follow the break lines, that is, edges of encountered faces have to be on these lines. Users may select break line geometries and then use the dedicated button to transform intersecting mesh elements.

Options provided for the transform include:

-  Adding new vertices when the lines cut the internal edges
-  Interpolating the Z value of newly added vertices on the mesh or from the lines
-  Tolerance setting for shifting existing vertices into place and preventing the creation of new vertices along line within the specified distance

|forceByBreakLine|

Whilst the term "break lines" is typically used to refer to polylines that constrain a surface or TIN to the defined positions, these break lines are often components of the mesh itself, and additional operations would continue to constrain the surface to these lines. This functionality specifically transforms the surface in a static manner, so that future operations are not constrained to the lines used to transform the mesh elements.

|image21|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Mesh transform by expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User can perform geometrical transformations on a mesh using an expression to change the vertices' coordinates. All coordinates (X,Y,Z) of selected vertices can be calculated with an expression, allowing transformation of the mesh while the mesh is still valid.

With a valid expression, selecting the "Preview transform" option will calculate the new expression based mesh coordinates and identify whether the transform is valid and may be applied.

If the preview is green, the transformed mesh is valid and the user can apply the transformation.
If the preview is red, the transformed mesh is invalid and user cannot apply the transformation.

Once applied, users have the option to undo or redo the operation.

|image22|

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Rendering
---------

Feature: Allow using physical DPI for map canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new setting has been made available for correctly using the physical screen DPI instead of logical DPI, allowing symbols to be rendered equally on different attached devices (hi dpi and low dpi), and in mobile applications such as QField.

This setting is disabled by default to ensure that symbols are not scaled differently than they were in previous versions of QGIS.

This feature was developed by `Matthias Kuhn <https://github.com/m-kuhn>`__

Feature: Data defined raster layer opacity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new control has been exposed which allows the opacity of a raster to be data defined. This allows for the varied representation of a raster layer,
in various contexts, such as on different pages of an atlas, being dependent on the visibility of another layer, or adjusted by temporal variables etc.

Additionally, a "redraw layer only" temporal mode for raster layers has been added, which causes a raster layer to be redrawn on each new animation frame as in the equivalent functionality for vector layers. This may be useful in many contexts, such as when the layer uses time-based expression values like the data defined renderer opacity to fade in or out a raster layer from an animation.

|image23|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Print Layouts
-------------

Feature: Predefined scale support for point-driven atlases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Layout map items gained support for the predefined scale mode when controlled by point-driven atlases. This ensures the correct behavior is observed when atlas features are multipoint geometries with varying envelope areas.

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Indentation of legend groups and subgroups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two new entries have been added to the "Spacing" section of the Legend properties:

-  Indent of group items
-  Indent of subgroup items

Items belonging to groups or subgroups will be shifted right by the specified amount. When legend patches are added to the left of entries they will be indented as well.

|image24|

This feature was developed by `Jürnjakob Dugge <https://github.com/jdugge>`__

Expressions
-----------

Feature: Mesh expression functions for vertex\_as\_point and vertex\_z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Expressions have been added for interacting with mesh layers, with the following functions returning value related to the current vertex:

-  ``$vertex_as_point``: returns the current vertex as a geometry point
-  ``$vertex_z``: returns the Z value of the current vertex.

These two functions are contextual and need to be added in a ``QgsExpressionContext`` with ``QgsExpressionContextUtils::meshExpressionScope()`` for the creation of a specific ``QgsExpressionScope``.

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Expression function for $z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The z value for the current feature in an expression context can now be retrieved using ``$z``

This feature was funded by `Hydrotec <https://www.hydrotec.de/>`__

This feature was developed by `Lutra Consulting (Vincent Cloarec) <https://www.lutraconsulting.co.uk/>`__

Feature: Affine transform expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An affine\_transform function has been added to QGIS Expressions.

This feature was developed by `Antoine Facchini <https://github.com/Koyaani>`__

Feature: Straight distance2d expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A straight\_distance2d function is now available in QGIS expressions for retrieving the direct/ Euclidean distance between the first and last vertex of a curve geometry feature.

This feature was developed by `Antoine Facchini <https://github.com/Koyaani>`__

Feature: Add sinuosity expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sinuosity function has been added to QGIS expressions.

This feature was developed by `Loïc Bartoletti <https://github.com/lbartoletti>`__

Feature: New exif() and exif\_geotag() functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new pair of functions was added to the QGIS expression engine to read exif tags from image files. The two functions are:

-  exif(path, tag) : this function returns the value of a given tag string for the provided image file path; when the second optional parameter isn't provided, the function will return a map object containing *all* exif tags and their values.
-  exif\_geotag(path) : this function returns a point geometry from the exif geotags containing in the provided image file path.

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Digitising
----------

Feature: Geometry snapper algorithm optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The geometry snapper is now blazingly fast after benefiting from another round of optimization work. Small snapping distance values hanging QGIS forever is now a thing of the past.

This feature was funded by `SwissTierras Colombia <https://www.swisstierrascolombia.com/>`__

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Convert to curve with vertex tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to convert vertices to or from curved vertices is now supported with the Vertex tool, allowing users to convert vertices with the "C" and "O" keys.

Additionally, methods for ``convertVertex()`` have been introduced for the ``QgsGeometry`` and ``QgsCompoundCurve`` objects in the QGIS API.

|image25|

This feature was funded by `Swiss QGIS user group <https://qgis.ch/>`__

This feature was developed by `Olivier Dalang <https://github.com/olivierdalang>`__

Feature: Add Z/M support to Advanced Digitizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS Advanced Digitizing tools now support the entering of user-defined Z and M values, greatly improving the available control for newly digitized features such as components of 3D networks.

|image26|

This feature was funded by Métropole Européenne de Lille @Jean-Roc

This feature was developed by `Loïc Bartoletti <https://github.com/lbartoletti>`__

Data Management
---------------

Feature: Drag and Drop support for external storage file widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users may now use Drag and Drop support on an external resource widget when an external storage has been defined and configured appropriately.

|image27|

This feature was funded by `Lille Metropole <https://www.lillemetropole.fr/>`__

This feature was developed by `Julien Cabieces <https://github.com/troopa81>`__

Feature: File-based dataset size and last modified date in the layer properties dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The layer properties dialog's information panel now shows the size and last modified date of file-based datasets, removing the need to retrieve these details from a file manager. These additional details are also visible in the browser panel's information section. For datasets formed of more than a single file, the size will reflect the sum of all the auxiliary/ sidecar files forming the dataset.

|image28|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Rename files in QGIS Browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A rename action has been added to the manage submenu for files in the QGIS browser. If the renamed file corresponds to a spatial dataset with multiple auxiliary/ sidecar files, then these will be renamed accordingly.

Additionally, users are warned if the file is a layer which exists in the current project and are asked whether they want to automatically update all the layer paths accordingly.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Move GPS tools "add gpx layer" functionality to Data Source Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functionality from the GPS tools plugin to add GPX layers has been moved to a new "Add GPS Data" page in the data source manager.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Load projects from GPKG using drag and drop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Historically, when using drag and drop functionality with the GPKG format, only feature layers were represented to load into QGIS.

QGIS will now show projects embedded in a GPKG when the GPKG file is added to the QGIS canvas using the drag and drop functionality.

|image29|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: External Storage support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS now includes an External Storage API, in line with the proposal outlined in `QEP 196 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/196>`__.

The implementation includes the following features:

-  External storage API
-  Registry that contains all external storage backends
-  SimpleCopy external storage that stores the selected external resource on a specific location on disk
-  WebDAV support

In addition, a widget has been added to allow for the configuration and visualization of external storage backends and components. The storage mode (File or Directory) widget is not currently visible when an external storage is selected, and relative path settings are hidden as relative paths are not relevant to external storage data.

|image30|

This feature was funded by `Lille Metropole <https://www.lillemetropole.fr/>`__

This feature was developed by `Julien Cabieces <https://github.com/troopa81>`__

Forms and Widgets
-----------------

Feature: Drag & Drop designer form actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Layer actions are now available in forms using the drag and drop designer

|image31|

This feature was funded by `Kanton Solothurn, Amt für Geoinformation <https://geo.so.ch/>`__

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Layer Legend
------------

Feature: Use placeholder icon in legend for raster layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new feature has been added to allow the selection of a placeholder image which may be used in the legend item of a raster or vector layer. This is very useful in certain instances such as when using raster layers with QGIS server, preventing long lists of palleted values from GetLegendGraphic requests and instead returning a tailored result, among various other use cases.

|image32|

This feature was funded by `Canton of Glarus <https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808>`__

This feature was developed by `mhugent <https://github.com/mhugent>`__

Analysis Tools
--------------

Feature: Add if() function to raster calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A long awaited feature has been for QGIS to support simple if() statements in the raster calculator.

Although conditional statements have been supported in the raster calculator for a while, the syntax and structure of the expressions was often verbose and complex.

The raster calculator will now support simple conditional statements with the common syntax of ``if ( condition , option1 , option2 )`` whereby if the condition evaluates to true, the first option will be used, otherwise the second option will be used.

|image33|

This feature was developed by `Francesco Bursi <https://github.com/Franc-Brs>`__

Feature: Virtual raster support in raster calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Virtual raster data provider support has been added to the QGIS raster calculator, which now allows users to perform raster calculator operations without specifying an output file or writing the resulting raster to disk.

This option is enabled via the UI by checking the "Create on-the-fly raster instead of writing layer to disk" checkbox in the raster calculator, and is also supported via the PyQgis API.

Resulting raster layers may be used in further analysis operations and allow for user specified raster names. Where a name is not provided for the resulting raster, it will be named according to the formula used to generate it.

|image34|

This feature was developed by `Francesco Bursi <https://github.com/Franc-Brs>`__

Processing
----------

Feature: Annotation layer parameter type for processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An annotation layer parameter type has been added to the QGIS Processing Framework, which includes a new algorithm for converting main annotation layer items to secondary annotation layers. This is useful for moving items created in the main layer to a secondary layer, so that the item placement can be adjusted within the layer stack.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add a POST option to the FileDownloader processing algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a choice between performing GET or POST requests when downloading a file using the FileDownloader processing tool.

If the POST parameter is specified, some DATA can be added in the query.

This is useful in many contexts, such as for sending longer requests to the Overpass API using POST to download OSM data.

|image35|

This feature was funded by `3Liz <https://www.3liz.com>`__

This feature was developed by `Étienne Trimaille <https://github.com/Gustry>`__

Feature: Add new "Select within distance" and "Extract within distance" algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New algorithms have been provided which allow users to select or extract features from one layer which are within a certain distance of features from another reference layer.

The distance checking is heavily optimized, using spatial indices to restrict the number of features retrieved, and also automatically handling off the check to the database server for layers using the PostGIS provider.

Additionally, the distance parameter may be a data-defined. property

This feature was funded by QTIBIA Engineering

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Point cloud parameter for Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new point cloud parameter has been added to the QGIS Processing. Framework. this allows for the filtering of point cloud layers in the map layer and multiple layers parameters. This opens the door for native point cloud algorithms and improves point cloud support for 3rd party providers.

This feature was developed by `Alexander Bruy <https://github.com/alexbruy>`__

Feature: Remove the GPS importer plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The last of the GPS tools functionality has been ported to three new processing algorithms, namely:

-  Convert GPS data
-  Upload GPS data to device
-  Download GPS data from device

As a result, the GPS importer plugin has been made redundant and has been completely removed from QGIS.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Convert GPX feature type processing algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Convert GPX feature type tool has been ported from the GPS tools to a new processing algorithm, which uses the GPSBabel tool to convert GPX features from one type to another (e.g. converting all waypoint features to a route feature).

It is designed as a drop-in replacement for workflows which previously used this functionality from the GPS tools plugin, but with all the benefits and improvements that come automatically from being a part of of the QGIS Processing Framework.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Add incremental field with modulo option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This algorithm allows the user to add a column with an integer that will be incremented from START to the limit, with the possibility of grouping to resume at the value of START following the group.

An option called "modulo counter" is included which will reset the counter to the starting value if the modulo value is reached. Using a value of 0 for the modulo option will disable it.

This feature was developed by `Loïc Bartoletti <https://github.com/lbartoletti>`__

Feature: Duration parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A brand new duration parameter was added to the processing framework to facilitate the creation of temporal-related algorithms.

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Spatiotemporal ST-DBSCAN clustering algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS 3.22 ships with a brand new spatiotemporal ST-DBSCAN clustering algorithm which clusters point features based on a 2D implementation of spatiotemporal density-based clustering of applications with noise (ST-DBSCAN) algorithm.

For more details, please see the following papers:

-  Ester, M., H. P. Kriegel, J. Sander, and X. Xu, "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise". In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
-  Birant, Derya, and Alp Kut. "ST-DBSCAN: An algorithm for clustering spatial–temporal data." Data & Knowledge Engineering 60.1 (2007): 208-221.
-  Peca, I., Fuchs, G., Vrotsou, K., Andrienko, N. V., & Andrienko, G. L. (2012). Scalable Cluster Analysis of Spatial Events. In EuroVA@ EuroVis.

|image36|

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Feature: Move non-native processing providers into independent plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In line with the discussion in `QEP 226 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/226>`__, the SAGA, GRASS, and OTB providers have been separated into independent plugins.

This should prevent issues with the loading of the Processing plugin in cases where any one of these providers is broken. It will also make it easier to convert them into third-party plugins in the future.

The SAGA and GRASS plugins are enabled by default, leaving the UX unchanged. The OTB provider can be enabled in the Plugin Manager if necessary, however, the enabling or disabling of any of these providers is now performed via the Plugin Manager as with any other plugin.

This is mostly an internal change, with the only visible change on the part of end-users being that the Plugin Manager is used to activate or deactivate the SAGA, GRASS, and OTB providers.

This feature was developed by `Alexander Bruy <https://github.com/alexbruy>`__

Application and Project Options
-------------------------------

Feature: Export all keyboard shortcuts to XML or PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Historically, when exporting keyboard shortcuts to an XML file, QGIS would only export user-defined shortcuts. In instances where no customized shortcuts were found, an empty file would be created.

A new option has been provided to export all available keyboard shortcuts to the resulting XML file, or to generate a PDF output with a list of all defined QGIS shortcuts.

|image37|

This feature was developed by `Alexander Bruy <https://github.com/alexbruy>`__

Feature: Move GPS Tools GPSbabel device configuration widget to global settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GPS babel configuration settings has been moved from a settings page in the deprecated GPS Tools plugin, to a new page in the main settings dialog.

|image38|

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Set default path structure for new projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS Desktop historically supported the definition of whether a particular project used an absolute or relative structure from the project properties, however, the default setting for this functionality was always configured to use relative paths.

A new setting has been exposed which allows users to set the default path structure to use either absolute or relative for new projects under the program options. In much the same way the default project format may be configured to use qgz or qgs, this is made available as a global property specific to each user profile.

This feature was developed by `mhugent <https://github.com/mhugent>`__

Feature: Allow configuration of the max cache size from QGIS settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the ``qgis_global_settings.ini`` file, it's possible to set the max image cache size in bytes.

The cache is used for caching symbology and layout images,
If high resolution images are used for printing layout, then this value should be increased accordingly.

Default value is 100mb.

This feature was funded by `3Liz <https://www.3liz.com/>`__

This feature was developed by `David Marteau <https://github.com/dmarteau>`__

Browser
-------

Feature: Improved delete action for browser files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Th delete action used from the QGIS browser has been improved in various ways, including:

-  The action is more consistent and applied to all file type items
-  Multiple file deletion is now supported by selecting multiple file items in the browser which includes a confirmation prompt
-  Before deleting files, the current project is scanned to see if it is using any of the files. If so, a prompt is shown asking users if they want to cancel the deletion, or delete and remove layers, or delete and retain layers.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Connections API result widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a part of the ongoing efforts to port the table management functionalities from the DB Manager to the QGIS Browser, as detailed in `QEP 205 <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/205>`__, a new SQL dialog is available from the browser panel which provides the ability to execute queries and SQL statements for the following elements:

-  DB connections
-  Schema items
-  Table items

The implementation also supports the following advanced functionalities:

-  A multi-threaded implementation for both API token fetching and row fetching results in non-blocking GUI operations
-  Fully interruptible API
-  Support for progressive loading of features in the results view (fetchMore API)

|image39|

This feature was developed by `Alessandro Pasotti <https://github.com/elpaso>`__

Data Providers
--------------

Feature: Transactions in MSSQL provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Addition of transaction support to the MSSQL data provider.

There are no GUI-related changes, as users can enable transactional editing as with other providers. This is done by going to the Project Properties and checking "Automatically create transaction groups where possible" in the Data Sources tab.

By default, a running transaction in MSSQL will block other clients from accessing the same data. For example, if one client starts a transaction and adds or modifies a feature in a table, other clients will get blocked when trying to read any data from the table until the transaction is completed.

There is database-level configuration option, ``READ_COMMITTED_SNAPSHOT``, which is ``OFF`` by default.

Activating this will change the behavior to function in a similar fashion as other RDBMS systems such as PostgreSQL, in that transactions do not cause blocking and enables the database to support multiple versions of data. This is a database-level property configured by the administrator and can not be automatically set by QGIS when connecting to the database, however it may be activated using the following query:

``sql ALTER DATABASE my_db SET READ_COMMITTED_SNAPSHOT ON``

In most instances where transactions are desired, activating this option is likely recommended to prevent freezing in QGIS or other clients.

This feature was funded by `ms.GIS <http://www.msgis.com>`__

This feature was developed by `Lutra Consulting (Martin Dobias) <https://www.lutraconsulting.co.uk/>`__

Feature: Show system and internal tables in sublayer selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A check box has been added to the sublayer selection dialog to control whether system and internal tables should be shown. This will be turned off by default, but will be useful in instances where users have a particular need to load a system table into QGIS for viewing or manipulation purposes.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Automatically read and convert metadata from ESRI Personal Geodatabases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously this was supported for File Geodatabases and shp.xml metadata, but it is now also supported for ESRI personal geodatabases (.mdb files)

Requires GDAL 3.4+

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: Create a generic data item provider for all file based datasources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This provider uses the QgsProviderRegistry::querySublayers API to automatically create appropriate browser data items for all file based sources, regardless of the underlying provider whether it may be mdal, gdal, ogr, pdal, or ept.

This allows the merging of sources which can be handled by multiple different providers into single container items in the browser, which may be expanded to display all related or nested elements. It is common for many file types, such as GeoPDF or KML/KMZ files to may contain raster and vector layers, or .nc files which may be accessed as a mesh or raster depending on the data provider.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

QGIS Server
-----------

Feature: Enable multiple MetadataUrls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QGIS Server historically only supported the provision of a single metadata URL, but will now allow multiple metadata endpoints to be specified in the service definition.

|image40|

This feature was funded by `Ifremer <https://wwz.ifremer.fr/>`__

This feature was developed by `Étienne Trimaille <https://github.com/Gustry>`__

Feature: Add version to QGIS Server CLI tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's quite a common practice to have arguments like ``-v`` and ``--version`` for tools accessed via command line interfaces (CLIs), so new ``--version`` and it's alias ``-v`` have been added to identify QGIS version information for the following tools:

-  qgis\_process
-  qgis\_mapserv.fcgi
-  qgis\_mapserver

This feature was funded by `3Liz <https://www.3liz.com/>`__

This feature was developed by `Étienne Trimaille <https://github.com/Gustry>`__

Programmability
---------------

Feature: Expose scriptable vector tile encoder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An additional ``writeSingleTile`` method in ``QgsVectorTileWriter`` has been exposed to enable the encoding of a single vector tile to a memory buffer. This may support workflows for PyQgis and QGIS Server which include support for vector tiles.

This feature was developed by `David Marteau <https://github.com/dmarteau>`__

Feature: Encode and write vector tiles in different CRS than EPSG:3857
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QGIS API has been extended to support encoding and writing vector tiles in a different CRS than EPSG:3857.

Note that according to the Mapbox Vector Tile specification, a Vector Tile represents data based on a square extent within a projection. A Vector Tile should contain information about its bounds and projection. The file format assumes that the decoder knows the bounds and projection of a Vector Tile before decoding it.

This feature was funded by Ifremer

This feature was developed by `rldhont <https://github.com/rldhont>`__

Feature: DistanceWithin filter for QgsFeatureRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An option has been added to QgsFeatureRequest to request features within a certain distance of a reference geometry

This is made possible by the new enum Qgis::SpatialFilterType which has been added to reflect whether a request uses no spatial filter, a BoundingBox filter (via
setFilterRect), or the new DistanceWithin filter.

For example, the following request will retrieve all features within 50 map units of the provided linestring:

``QgsFeatureRequest().setDistanceWithin(QgsGeometry.fromWkt('LineString(0 0, 10 0, 12 1)'), 50)``

Distance within filters are treated like bounding box filters, in that they are independent of any attribute/id filters (such as feature ids or expressions).

Provider feature iterators can potentially delegate the distance within search to the backend. So, for example, the PostgreSQL data provider could use an ``ST_DWithin`` query for optimal index use.

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: API for preset combobox values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An API has been added to allow a string parameter to show as a combobox with preset choices in processing GUI tools.

In some circumstances, it is desirable to restrict the values available when a user is asked to enter a string parameter that should match a list of predetermined "valid" values, yet these values will vary installation by installation.

For example, a "printer name" parameter, where it may be desired that users may pick a name value from a list of printers installed on the system, but since the printer names will vary between installations, an enum parameter is not a suitable choice.

This is now supported by setting the "value\_hints" option in the widget wrapper metadata, as demonstrated below.

Whilst this provides a mechanism for guiding users to select from valid string values when running a Processing algorithm through the GUI, it does not place any limits on the string values accepted via PyQGIS codes or when running the algorithm via other means that do not use the GUI. Algorithms should gracefully handle other values accordingly.

``param = QgsProcessingParameterString( 'PRINTER_NAME', 'Printer name')     # show only printers which are available on the current system as options     # for the string input.     param.setMetadata( {'widget_wrapper':       { 'value_hints': ['Inkjet printer', 'Laser printer'] }     })``

This feature was developed by `Nyall Dawson <https://github.com/nyalldawson>`__

Feature: QgsExifTools class support for fetching tag values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QgsExifTools class can now retrieve individual exif tags from images using the readTag function.

E.g.: ``QgsExifTools.readTag('/my/photo/0997.JPG'), 'Exif.Image.DateTime')``

Known exif tags representing time values are automatically converted to Q{Date,Time,DateTime} objects. This makes working with those tags much easier and integrates well with other parts of the QGIS API.

This feature was developed by `Mathieu Pellerin <https://www.opengis.ch/>`__

Notable Fixes
-------------

Bug fixes by Even Rouault
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Bug Title                                                                                                                                        | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                          | 3.16 backport commit (GitHub)                             | Remark                 |
+==================================================================================================================================================+==========================================================+==============================================================+===========================================================+========================+
| WFS / GML parse issue, but QGIS loads GML as file fine?                                                                                          | `#45017 <https://github.com/qgis/QGIS/issues/45017>`__   |                                                              |                                                           | Not a bug              |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| POST request to modify timestamp does not respect defined format                                                                                 | `#44990 <https://github.com/qgis/QGIS/issues/44990>`__   |                                                              |                                                           | Wontfix / not a bug    |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Warning message 'Cannot create temporary SpatiaLite cache' when adding many WFS-layers                                                           | `#44971 <https://github.com/qgis/QGIS/issues/44971>`__   |                                                              |                                                           | Duplicate              |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| QGIS creates invalid filter for WFS GetFeature request                                                                                           | `#43957 <https://github.com/qgis/QGIS/issues/43957>`__   | `PR #45043 <https://github.com/qgis/QGIS/pull/45043>`__      | `PR #45053 <https://github.com/qgis/QGIS/pull/45053>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| WFS Layer is not rendered when requested CRS is not matching project CRS and "Only request features overlapping the view extent" option is set   | `#44054 <https://github.com/qgis/QGIS/issues/44054>`__   | `PR #45044 <https://github.com/qgis/QGIS/pull/45044>`__      | `PR #45047 <https://github.com/qgis/QGIS/pull/45047>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Adding a WFS layer with filter for non-existent attribute leads to broken layer                                                                  | `#43950 <https://github.com/qgis/QGIS/issues/43950>`__   | `PR #45045 <https://github.com/qgis/QGIS/pull/45045>`__      | `PR #45052 <https://github.com/qgis/QGIS/pull/45052>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| New Shapefile layer silently overwrite existing files                                                                                            | `#44299 <https://github.com/qgis/QGIS/issues/44299>`__   | `PR #45207 <https://github.com/qgis/QGIS/pull/45207>`__      | `PR #45240 <https://github.com/qgis/QGIS/pull/45240>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| QGIS on linux crashes when opening many geopackages at once                                                                                      | `#43620 <https://github.com/qgis/QGIS/issues/43620>`__   | `PR #45211 <https://github.com/qgis/QGIS/pull/45211>`__      | No                                                        |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Crash in QgsPointCloudLayerRenderer when closing while rendering still active                                                                    | `#44144 <https://github.com/qgis/QGIS/issues/44144>`__   | `PR #45227 <https://github.com/qgis/QGIS/pull/45227>`__      | `PR #45241 <https://github.com/qgis/QGIS/pull/45241>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Geoprocessing tools cause libgeos to throw SIGBUS                                                                                                | `#45226 <https://github.com/qgis/QGIS/issues/45226>`__   | `geos PR 481 <https://github.com/libgeos/geos/pull/481>`__   | N/A                                                       |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| QGIS crash after loading WMS layer via script and zooming in and out                                                                             | `#44095 <https://github.com/qgis/QGIS/issues/44095>`__   | `PR #45254 <https://github.com/qgis/QGIS/pull/45254>`__      | No                                                        | Mostly a usage issue   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Integer unexpectedly large in GeoPackage                                                                                                         | `#45178 <https://github.com/qgis/QGIS/issues/45178>`__   |                                                              |                                                           | Not a bug              |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file                                                                         | `#45139 <https://github.com/qgis/QGIS/issues/45139>`__   | `GDAL PR 4552 <https://github.com/OSGeo/gdal/pull/4552>`__   | N/A                                                       |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| WFS connection manager: GetCapabilities document's URLs not being used consistently                                                              | `#45242 <https://github.com/qgis/QGIS/issues/45242>`__   | `PR #45267 <https://github.com/qgis/QGIS/pull/45267>`__      | `PR #45273 <https://github.com/qgis/QGIS/pull/45273>`__   |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+
| QGIS crashes if network connexion is lost and a raster layer is loaded                                                                           | `#45293 <https://github.com/qgis/QGIS/issues/45293>`__   | `GDAL PR 4560 <https://github.com/OSGeo/gdal/pull/4560>`__   | N/A                                                       |                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------+------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Even Rouault <https://www.spatialys.com/>`__

Bug fixes by Alessandro Pasotti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Bug Title                                                                                                               | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.16 backport commit (GitHub)                             | Remark                                            |
+=========================================================================================================================+==========================================================+===========================================================+===========================================================+===================================================+
| Data Source Manager - ArcGIS REST Server - dialog/window closes when adding a layer                                     | `#45050 <https://github.com/qgis/QGIS/issues/45050>`__   | `PR #45059 <https://github.com/qgis/QGIS/pull/45059>`__   | n/a                                                       |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| "Display no data value as" option is not available in raster layer properties                                           | `#44949 <https://github.com/qgis/QGIS/issues/44949>`__   | `PR #45063 <https://github.com/qgis/QGIS/pull/45063>`__   | Not critical                                              |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Raster layer not rendering after data-source change when combined with certain layout element                           | `#44929 <https://github.com/qgis/QGIS/issues/44929>`__   | `PR #45074 <https://github.com/qgis/QGIS/pull/45074>`__   | `PR #45083 <https://github.com/qgis/QGIS/pull/45083>`__   |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Update selected feature ids before emitting featuresDeleted                                                             | `#44921 <https://github.com/qgis/QGIS/issues/44921>`__   | `PR #45078 <https://github.com/qgis/QGIS/pull/45078>`__   | Not critical                                              |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| sample() and identify() from QgsRasterDataProvider don't always provide the same value                                  | `#44902 <https://github.com/qgis/QGIS/issues/44902>`__   | `PR #45086 <https://github.com/qgis/QGIS/pull/45086>`__   | `PR #45145 <https://github.com/qgis/QGIS/pull/45145>`__   |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Copying objects containing multiline strings into another project does not work properly                                | `#44989 <https://github.com/qgis/QGIS/issues/44989>`__   | `PR #45129 <https://github.com/qgis/QGIS/pull/45129>`__   | Not critical                                              |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| projecting label coordinates for multiPoint geometry crashes QGIS                                                       | `#45148 <https://github.com/qgis/QGIS/issues/45148>`__   | `PR #45150 <https://github.com/qgis/QGIS/pull/45150>`__   | No                                                        |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Copy/paste style category "Form" is missing some settings                                                               | `#45146 <https://github.com/qgis/QGIS/issues/45146>`__   |                                                           |                                                           | Maybe won't fix, checking with m-kuhn and 3nids   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Adding a new point onto a memory multipoint layer kills QGIS                                                            | `#45152 <https://github.com/qgis/QGIS/issues/45152>`__   | `PR #45157 <https://github.com/qgis/QGIS/pull/45157>`__   |                                                           |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file                                                | `#45139 <https://github.com/qgis/QGIS/issues/45139>`__   | `PR #45174 <https://github.com/qgis/QGIS/pull/45174>`__   | No                                                        |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| WMS parent layer added via QGIS Browser doesn't use default style                                                       | `#45192 <https://github.com/qgis/QGIS/issues/45192>`__   | `PR #45209 <https://github.com/qgis/QGIS/pull/45209>`__   | No                                                        |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| "Display nodata as" color widget is not automatically updated in layer styling panel                                    | `#45132 <https://github.com/qgis/QGIS/issues/45132>`__   | `PR #45264 <https://github.com/qgis/QGIS/pull/45264>`__   | n/a                                                       |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| PostGIS error while changing attributes (field value and geometry): prepared statement "updatefeature" already exists   | `#45100 <https://github.com/qgis/QGIS/issues/45100>`__   | `PR #45266 <https://github.com/qgis/QGIS/pull/45266>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Attribute Table in Layout Manager Font Style Override Doesn't Show Fields                                               | `#45098 <https://github.com/qgis/QGIS/issues/45098>`__   | `PR #45269 <https://github.com/qgis/QGIS/pull/45269>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| WFS Layer from QGIS Server is not rendered because of an issue with coordinate axis order                               | `#45216 <https://github.com/qgis/QGIS/issues/45216>`__   | `PR #45270 <https://github.com/qgis/QGIS/pull/45270>`__   | Not critical                                              |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Not rendering with identity transform raster created with rasterio                                                      | `#45324 <https://github.com/qgis/QGIS/issues/45324>`__   |                                                           |                                                           | Checked out, probably not a bug                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| SQL query from DB Manager is executed twice                                                                             | `#45318 <https://github.com/qgis/QGIS/issues/45318>`__   | `PR #45351 <https://github.com/qgis/QGIS/pull/45351>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| can't use layers where name starts with number in virtual layer                                                         | `#45347 <https://github.com/qgis/QGIS/issues/45347>`__   | `PR #45354 <https://github.com/qgis/QGIS/pull/45354>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Show Feature Count counts null in zero category                                                                         | `#45280 <https://github.com/qgis/QGIS/issues/45280>`__   | `PR #45361 <https://github.com/qgis/QGIS/pull/45361>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Copying table by Drag&Drop in Browser (2) doesn't copy the table structure correctly                                    | `#45286 <https://github.com/qgis/QGIS/issues/45286>`__   | `PR #45375 <https://github.com/qgis/QGIS/pull/45375>`__   | No                                                        |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Wrong histogram plot if raster data type is byte                                                                        | `#45379 <https://github.com/qgis/QGIS/issues/45379>`__   | `PR #45400 <https://github.com/qgis/QGIS/pull/45400>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Inconsistency regarding pattern handling for QgsServerOgcApiHandler                                                     | `#45439 <https://github.com/qgis/QGIS/issues/45439>`__   | `PR #45450 <https://github.com/qgis/QGIS/pull/45450>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| QGIS Server - WMS Request GetPrint fails with ATLAS\_PK                                                                 | `#30817 <https://github.com/qgis/QGIS/issues/30817>`__   | `PR #45521 <https://github.com/qgis/QGIS/pull/45521>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| projectsInDatabase key is not stored to xml for PostGIS connections                                                     | `#45508 <https://github.com/qgis/QGIS/issues/45508>`__   | `PR #45523 <https://github.com/qgis/QGIS/pull/45523>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Changing values in Form mode of attribute table doesn't set active the Save button                                      | `#45527 <https://github.com/qgis/QGIS/issues/45527>`__   | `PR #45532 <https://github.com/qgis/QGIS/pull/45532>`__   | queued                                                    |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+
| Create spatialite trigger with DBManager do not work                                                                    | `#45420 <https://github.com/qgis/QGIS/issues/45420>`__   | `PR #45553 <https://github.com/qgis/QGIS/pull/45553>`__   | No                                                        |                                                   |
+-------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+---------------------------------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Alessandro Pasotti <https://www.qcooperative.net/>`__

Bug fixes by Peter Petrik
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| Bug Title                                                                                                           | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                                                                                                  | 3.16 backport commit (GitHub)      | Remark                                                                |
+=====================================================================================================================+==========================================================+======================================================================================================================================+====================================+=======================================================================+
| QGIS 3.20 on Mac crashes when certain Qt signals are emitted                                                        | `#44182 <https://github.com/qgis/QGIS/issues/44182>`__   | `QGIS-Mac-Packager Commit bf925f311 <https://github.com/qgis/QGIS-Mac-Packager/commit/bf925f3118a5d51080dfed46dddcb7cba3bbbc00>`__   | n/a                                |                                                                       |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| Unable to view LAS files written in WGS84 (EPSG:4326) coordinates                                                   | `#44755 <https://github.com/qgis/QGIS/issues/44755>`__   |                                                                                                                                      |                                    | duplicate of `#41765 <https://github.com/qgis/QGIS/issues/41765>`__   |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| macOS: Symbol not found: \_\_cg\_jpeg\_resync\_to\_restart when reprojecting raster layer with GDAL warp on macOS   | `#40164 <https://github.com/qgis/QGIS/issues/40164>`__   | no                                                                                                                                   | no                                 | Not an issue with the nightly (qgis-deps-0.9) anymore                 |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS                                           | `#43042 <https://github.com/qgis/QGIS/issues/43042>`__   | `PR #45322 <https://github.com/qgis/QGIS/pull/45322>`__                                                                              | queued                             |                                                                       |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| icons not visible in the Layer Notes                                                                                | `#44425 <https://github.com/qgis/QGIS/issues/44425>`__   | `PR #45332 <https://github.com/qgis/QGIS/pull/45332>`__                                                                              | n/a                                |                                                                       |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| unable to open any ascii FLO-2D files in Mesh Layer                                                                 | unreported                                               | `PR #45349 <https://github.com/qgis/QGIS/pull/45349>`__                                                                              | n/a                                |                                                                       |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| encoding issue when using GRASS processing tool on macOS                                                            | `#41870 <https://github.com/qgis/QGIS/issues/41870>`__   | `PR #45399 <https://github.com/qgis/QGIS/pull/45399>`__                                                                              | Not critical - workaround exists   |                                                                       |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+
| Matplotlib QT backend imports not working on MacOS                                                                  | `#45398 <https://github.com/qgis/QGIS/issues/45398>`__   |                                                                                                                                      |                                    | investigation                                                         |
+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+------------------------------------+-----------------------------------------------------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Lutra Consulting (Peter Petrik) <https://www.lutraconsulting.co.uk/>`__

Bug fixes by Sandro Santilli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Bug Title                                                            | URL issues.qgis.org (if reported)                                 | URL Commit (Github)                                                                                                 | 3.16 backport commit (GitHub)   | Remark                                                             |
+======================================================================+===================================================================+=====================================================================================================================+=================================+====================================================================+
| Make QgsGeos::prepareGeometry and QgsGeos::cacheGeos idempotent      | unreported                                                        | `PR #45147 <https://github.com/qgis/QGIS/pull/45147>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Add a distanceWithin method to the QgsGeometryEngine virtual class   | unreported                                                        | `PR #45057 <https://github.com/qgis/QGIS/pull/45057>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Allow calling testdata\_pg.sh from any directory                     | unreported                                                        | `PR #45378 <https://github.com/qgis/QGIS/pull/45378>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Make TestPyQgsPostgresProvider.testGeneratedColumns idempotent       | unreported                                                        | `PR #45415 <https://github.com/qgis/QGIS/pull/45415>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Improve PostgreSQL test DB setup documentation and script            | unreported                                                        | `PR #45413 <https://github.com/qgis/QGIS/pull/45413>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Add GEOS DistanceWithin API                                          | `GEOS Ticket #1124 <https://trac.osgeo.org/geos/ticket/1124>`__   | `GEOS commit #ba10ba4508a <https://trac.osgeo.org/geos/changeset/ba10ba4508af887a1a78bbc632ab45d89ce3242c/git>`__   |                                 | `GEOS Issue #472 <https://github.com/libgeos/geos/issues/472>`__   |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Make Postgres provider test idempotent                               | `#45417 <https://github.com/qgis/QGIS/issues/45417>`__            | `PR #45418 <https://github.com/qgis/QGIS/pull/45418>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Use GEOSDistanceWithin when available                                | unreported                                                        | `PR #45340 <https://github.com/qgis/QGIS/pull/45340>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| Reduce GEOS conversions and preparations of geometries               | unreported                                                        | `PR #45195 <https://github.com/qgis/QGIS/pull/45195>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+
| More heuristics to determine whether to iterate over target source   | unreported                                                        | `PR #45339 <https://github.com/qgis/QGIS/pull/45339>`__                                                             |                                 |                                                                    |
+----------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------+--------------------------------------------------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Sandro Santilli <https://strk.kbt.io/>`__

Bug fixes by Loïc Bartoletti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Bug Title                                                                                                     | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.16 backport commit (GitHub)                             | Remark                                                                                       |
+===============================================================================================================+==========================================================+===========================================================+===========================================================+==============================================================================================+
| More const in geometry                                                                                        | Not reported / performance                               | `PR #45217 <https://github.com/qgis/QGIS/pull/45217>`__   |                                                           |                                                                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| QgsFeature::setId improve documentation with a warning                                                        | `#44898 <https://github.com/qgis/QGIS/issues/44898>`__   | `PR #45189 <https://github.com/qgis/QGIS/pull/45189>`__   | `PR #45229 <https://github.com/qgis/QGIS/pull/45229>`__   |                                                                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Geometry Checker: Enlarge FeatureID                                                                           | `#44250 <https://github.com/qgis/QGIS/issues/44250>`__   | `PR #45191 <https://github.com/qgis/QGIS/pull/45191>`__   | `PR #45229 <https://github.com/qgis/QGIS/pull/45229>`__   |                                                                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VertexTool. Fixes move vertex on Z layer if CRS are differents (with Vincent Cloarec)                         | Not reported                                             | `PR #45020 <https://github.com/qgis/QGIS/pull/45020>`__   |                                                           | Not backported. Introduce new methods.                                                       |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Fix Z/M dimension URI via DB Manager.                                                                         | `#34894 <https://github.com/qgis/QGIS/issues/34894>`__   | `PR #45223 <https://github.com/qgis/QGIS/pull/45223>`__   | `PR #45304 <https://github.com/qgis/QGIS/pull/45304>`__   |                                                                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| [FIX] GeometryValidator init curve support                                                                    | Not reported                                             | `PR #45272 <https://github.com/qgis/QGIS/pull/45272>`__   |                                                           |                                                                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Compile fails, 'None' is not a member of 'QgsField::ConfigurationFlags'                                       | `#44681 <https://github.com/qgis/QGIS/issues/44681>`__   |                                                           |                                                           | Wontfix / not a bug                                                                          |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Union fails when using a point and a polygon layer                                                            | `#44801 <https://github.com/qgis/QGIS/issues/44801>`__   |                                                           |                                                           | Difference between GEOS 3.8 and 3.9                                                          |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Rings order in MultiPolygon WKT string may leave overlapping parts when deleting holes (native:deleteholes)   | `#44424 <https://github.com/qgis/QGIS/issues/44424>`__   |                                                           |                                                           | Wontfix for now. We can use Geos to fix the issue, but will remove Z/M and segmentize arc.   |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+----------------------------------------------------------------------------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Loïc Bartoletti <https://www.oslandia.com/>`__

Bug fixes by Denis Rouzaud
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+----------+
| Bug Title                                                                                | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.16 backport commit (GitHub)   | Remark   |
+==========================================================================================+==========================================================+===========================================================+=================================+==========+
| Regression: trying to run the multipart to singleparts algorithm throws a python error   | `#45331 <https://github.com/qgis/QGIS/issues/45331>`__   | `PR #45348 <https://github.com/qgis/QGIS/pull/45348>`__   |                                 |          |
+------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+---------------------------------+----------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Denis Rouzaud <https://www.opengis.ch/>`__

Bug fixes by Julien Cabieces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Bug Title                                                                                           | URL issues.qgis.org (if reported)                        | URL Commit (Github)                                       | 3.16 backport commit (GitHub)                             | Remark                                                                             |
+=====================================================================================================+==========================================================+===========================================================+===========================================================+====================================================================================+
| Styles in database not working for postgres provider and non-geometric layers                       | `#44749 <https://github.com/qgis/QGIS/issues/44749>`__   | `PR #45075 <https://github.com/qgis/QGIS/pull/45075>`__   | `PR #45102 <https://github.com/qgis/QGIS/pull/45102>`__   |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| "Layer notes" icon is not displayed when copy-pasting a style                                       | `#44692 <https://github.com/qgis/QGIS/issues/44692>`__   | `PR #45302 <https://github.com/qgis/QGIS/pull/45302>`__   | no need                                                   |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Ambiguous JSON errors                                                                               | `#42832 <https://github.com/qgis/QGIS/issues/42832>`__   |                                                           |                                                           | Failed to reproduce                                                                |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Attribute table: missing features when copying/pasting from scratch layer                           | `#42798 <https://github.com/qgis/QGIS/issues/42798>`__   |                                                           |                                                           | Can’t reproduce (Closed)                                                           |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Form view shows wrong image attachments when scrolling through features                             | `#42705 <https://github.com/qgis/QGIS/issues/42705>`__   |                                                           |                                                           | Already fixed                                                                      |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Build Virtual Raster tool creates an additional layer when selecting and reordering layers          | `#44270 <https://github.com/qgis/QGIS/issues/44270>`__   | `PR #45092 <https://github.com/qgis/QGIS/pull/45092>`__   | `PR #45102 <https://github.com/qgis/QGIS/pull/45102>`__   |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Attachment widget options are reset when you reopen the field widget properties                     | `#45089 <https://github.com/qgis/QGIS/issues/45089>`__   |                                                           |                                                           | Duplicate                                                                          |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| Cleared feature attributes not acting like they have been cleared, and preventing saving of layer   | `#39146 <https://github.com/qgis/QGIS/issues/39146>`__   | `PR #45176 <https://github.com/qgis/QGIS/pull/45176>`__   | `PR #45292 <https://github.com/qgis/QGIS/pull/45292>`__   |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| [Postgres] default value displayed instead of NULL                                                  | `#45198 <https://github.com/qgis/QGIS/issues/45198>`__   | `PR #45199 <https://github.com/qgis/QGIS/pull/45199>`__   | `PR #45291 <https://github.com/qgis/QGIS/pull/45291>`__   |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| a feature copy/paste sets a NULL field to its "default value" in a geopackage                       | `#44544 <https://github.com/qgis/QGIS/issues/44544>`__   |                                                           |                                                           | Question: Do we evaluate default value on NULL field when copy-pasting feature ?   |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+
| QGIS expression builder can not resolve PostgreSQL text arrays correctly                            | `#45290 <https://github.com/qgis/QGIS/issues/45290>`__   | `PR #45321 <https://github.com/qgis/QGIS/pull/45321>`__   |                                                           |                                                                                    |
+-----------------------------------------------------------------------------------------------------+----------------------------------------------------------+-----------------------------------------------------------+-----------------------------------------------------------+------------------------------------------------------------------------------------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Julien Cabieces <https://www.oslandia.com/>`__

Bug fixes by Nyall Dawson
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Bug Title                                                                                                                         | URL issues.qgis.org (if reported)                         | URL Commit (Github)                                                                                    | 3.16 backport commit (GitHub)                                                                         | Remark   |
+===================================================================================================================================+===========================================================+========================================================================================================+=======================================================================================================+==========+
| Don't reset mesh layer styling when changing data source for layer                                                                | `#45391 <https://github.com/qgis/QGIS/issues/45391>`__    | `PR #45392 <https://github.com/qgis/QGIS/pull/45392>`__                                                | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix crash when rendering clipped features and clipped shape results                                                               | `#45190 <https://github.com/qgis/QGIS/issues/45190>`__    | `Commit 6a4cdb36 <https://github.com/qgis/QGIS/commit/6a4cdb36c91085c5bb1544fb02da1f83467a29d7>`__     | `PR #45422 <https://github.com/qgis/QGIS/pull/45422>`__                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix crash when using map label tools with projects containing vector tile layers                                                  | `#44486 <https://github.com/qgis/QGIS/issues/44486>`__    | `PR #45311 <https://github.com/qgis/QGIS/pull/45311>`__                                                | `PR #45390 <https://github.com/qgis/QGIS/pull/45390>`__                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix symbol sizes in Meters at Scale cannot be negative                                                                            | `#45298 <https://github.com/qgis/QGIS/issues/45298>`__    | `Commit 360351a <https://github.com/qgis/QGIS/commit/360351a02704c370545fb8f92c0bdafbdfa35b2e>`__      | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix overwriting default style of geopackage layers                                                                                | `#42811 <https://github.com/qgis/QGIS/issues/42811>`__    | `Commit eef6939b96 <https://github.com/qgis/QGIS/commit/eef6939b96407b3d050988be4a0eeb692ffc5b68>`__   | `PR #45107 <https://github.com/qgis/QGIS/pull/45107>`__                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix hang when rendering lines with dash patterns with all 0 values                                                                | `#41994 <https://github.com/qgis/QGIS/issues/41994>`__    | `Commit f4e2e900 <https://github.com/qgis/QGIS/commit/f4e2e900eed16633ef0198f7b9a9152f395e173a>`__     | `PR #45107 <https://github.com/qgis/QGIS/pull/45107>`__                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Update default toolbar locations                                                                                                  | unreported                                                | `Commit 77be95feac <https://github.com/qgis/QGIS/commit/77be95feac7391e58f6bd487f30e09ed8ed63651>`__   | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Don't overwrite existing data defined property expressions when an interactive map tool is used to move/rotate/edit labels        | `PR #45279 <https://github.com/qgis/QGIS/pull/45279>`__   | `Commit b30c17f0 <https://github.com/qgis/QGIS/commit/b30c17f07d00850597d8bb1b2cfb1f454498b391>`__     | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix crash on exit with CAD dock open                                                                                              | unreported                                                | `Commit 1fb21f69f <https://github.com/qgis/QGIS/commit/1fb21f69fede05cabb8f1d27a8ad24564ae16f3d>`__    | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix rule based symbology doesn't work for columns with '-' in name                                                                | `#44379 <https://github.com/qgis/QGIS/issues/44379>`__    | `Commit 51fa9840 <https://github.com/qgis/QGIS/commit/51fa9840248135a7fe7ee181b7d645f3c591c9cc>`__     | `Commit 797367dde <https://github.com/qgis/QGIS/commit/797367dde65d6ab06f39f5c4636c2127c67aa9d1>`__   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Avoid hangs when drawing symbol icons using inappropriate sizes in map units                                                      | `#41149 <https://github.com/qgis/QGIS/issues/41149>`__    | `PR #45233 <https://github.com/qgis/QGIS/pull/45233>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix inappropriate display of z/m values in cad dock when non-z/m layer is selected                                                | unreported                                                | `Commit 55a76d1d <https://github.com/qgis/QGIS/commit/55a76d1d867c32f52ae4bd38ed671d44aa3ae92e>`__     | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Implement more responsive cancelation of map render for maps using complex effects                                                | `#41149 <https://github.com/qgis/QGIS/issues/41149>`__    | `PR #45212 <https://github.com/qgis/QGIS/pull/45212>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Allow CAD dock to be used for geographic CRS, but only allow the x/y/z/m constraints to be set                                    | unreported                                                | `PR #45185 <https://github.com/qgis/QGIS/pull/45185>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix crash when opening symbology properties of a layer set to embedded renderer which is not compatible with embedded renderers   | `#45159 <https://github.com/qgis/QGIS/issues/45159>`__    | `PR #45193 <https://github.com/qgis/QGIS/pull/45193>`__                                                | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix QgsMapToolCapture coordinates when associated with a non-vector layer where the layer CRS != canvas CRS                       | unreported                                                | `PR #45183 <https://github.com/qgis/QGIS/pull/45183>`__                                                | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix geometry generator rendering outside of vector layers                                                                         | `#39159 <https://github.com/qgis/QGIS/issues/39159>`__    | `PR #45165 <https://github.com/qgis/QGIS/pull/45165>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix color customisation is lost when configuring renderers using geometry generators                                              | `#38377 <https://github.com/qgis/QGIS/issues/38377>`__    | `PR #45166 <https://github.com/qgis/QGIS/pull/45166>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix rendering of interpolated line symbol layer outside of vector layers                                                          | `#45028 <https://github.com/qgis/QGIS/issues/45028>`__    | `PR #45164 <https://github.com/qgis/QGIS/pull/45164>`__                                                | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix QgsGeometry.fromPolygonXY docs                                                                                                | `#45099 <https://github.com/qgis/QGIS/issues/45099>`__    | `Commit 3d599fe4 <https://github.com/qgis/QGIS/commit/3d599fe4b5574e7c916133171e097163cae51e32>`__     | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix digitizing features using CAD dock when layer CRS != canvas CRS                                                               | unreported                                                | `PR #45108 <https://github.com/qgis/QGIS/pull/45108>`__                                                | N/A                                                                                                   |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix offset background when drawing rotated text                                                                                   | `#44907 <https://github.com/qgis/QGIS/issues/44907>`__    | `PR #45425 <https://github.com/qgis/QGIS/pull/45425>`__                                                | pending                                                                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Correctly escape complex source strings in processing history log                                                                 | `#45403 <https://github.com/qgis/QGIS/issues/45403>`__    | `PR #45426 <https://github.com/qgis/QGIS/pull/45426>`__                                                | pending                                                                                               |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+
| Fix handling of ADF files in browser                                                                                              | unreported                                                | `PR #45393 <https://github.com/qgis/QGIS/pull/45393>`__                                                | Not suitable for backport                                                                             |          |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------+

These bug fixes were funded by `QGIS.ORG (through donations and sustaining memberships) <https://www.qgis.org/>`__

Bugs fixed by `Nyall Dawson <https://north-road.com/>`__

.. |image1| image:: images/projects/badbeb89221e014ed31e7ea07919c9e734df39b2.png
.. |image2| image:: images/entries/4510afc65b63bab4ab46e0408a6c4c4207aff40f.gif
.. |image3| image:: images/entries/4822b0a64c8a57a049ae15acb8c77a27709172d5.gif
.. |image4| image:: images/entries/f80090adb3c2f85fa81b5689741afd936f8d5439.png
.. |image5| image:: images/entries/d1c6b0c69cf9dd8247d1dc0e370d0182b550f48a.png
.. |image6| image:: images/entries/0fc6bce9e9240b7e354b84d7477439798fd64a59.gif
.. |image| image:: images/entries/126294292-06c91bd5-83d2-4d6f-88a2-38fa2d303c86.png
.. |Peek 2021-08-29 14-38| image:: images/entries/131250678-52360214-31a9-4cf9-ad84-b10a4f78c431.gif
.. |image9| image:: images/entries/8ba4033bf4f8eea7e3776db420b34d6c51358859.gif
.. |image10| image:: images/entries/71bed70b1ced3fef5e3b8190cc613f3cb60f0fac.gif
.. |image11| image:: images/entries/9463f4559796ff4808fcd05d1ffbec3aa6d6bae4.gif
.. |image12| image:: images/entries/ce164b754aff6438bb6db52a4d5c2eb3e103af62.gif
.. |mapToolrefine| image:: images/entries/125721486-055c4cc3-5309-4455-bc5c-e00d6f349bc4.gif
.. |image14| image:: images/entries/a914bfb8a85bf2ab2232e8bfad6c3af3cdd751cb.gif
.. |image15| image:: images/entries/6a687b260a4d3a41c432360336393ee2746997c8.gif
.. |image16| image:: images/entries/4a918fc1feabd7e3c68282b1b6d052c8504d6013.gif
.. |image17| image:: images/entries/141acf32014c3ce387ff61e39cabf3e04c6d3896.gif
.. |image18| image:: images/entries/2148b3024a51a218bafafbbe26f74c30692222f6.gif
.. |image19| image:: images/entries/5da7e6705568488c08fbf7faaf311b2eca46c9da.gif
.. |forceByBreakLine| image:: images/entries/132239197-096d733b-b519-4aab-9384-79724fd84331.gif
.. |image21| image:: images/entries/704c731583ce48d963fe9878177bc40639ae3078.png
.. |image22| image:: images/entries/04937a2d9bba1e27712351f52e6b6f4d5fc0be4d.gif
.. |image23| image:: images/entries/881acd52afafba75698f1d7668794b80b594baef.gif
.. |image24| image:: images/entries/3792e9ae5124b81f1b4289cab220fdbb237851a8.png
.. |image25| image:: images/entries/fcc006352c7b09e37d6d8511ecb7fe2ae6a8be50.gif
.. |image26| image:: images/entries/287d041be909700393995e3018fba76f41e09a67.gif
.. |image27| image:: images/entries/038bb187a174a4c491f3f2db6ef03cec5b75e43d.gif
.. |image28| image:: images/entries/10c72ab958bb1e7a59f8f81afb81d33780ed0834.png
.. |image29| image:: images/entries/3672e8bb8d50bf1593252343da8fd8ff78a46535.png
.. |image30| image:: images/entries/c16663cabec529b113bb73919141bf50bf142c9e.gif
.. |image31| image:: images/entries/d8af279071ac38fdc63fbd3980077155db39bd0f.gif
.. |image32| image:: images/entries/f06524b9f422ee1ced55d9d79b816cabc5ea212d.jpg
.. |image33| image:: images/entries/c5d6968380879133ddb31ab2d0f755d6d2048402.gif
.. |image34| image:: images/entries/844b2b463a26d035fe25d43d7221a24a570ac615.gif
.. |image35| image:: images/entries/89bee20177cb03e453300ae291ae879649e963ab.png
.. |image36| image:: images/entries/10136b7563df169c40e2c20a96fe75b6ed93e16f.png
.. |image37| image:: images/entries/1822a5ace82d1e8030ed3d563c07f6b9b6fc3901.png
.. |image38| image:: images/entries/d61c12a455d85b290431d5ff461de15db0afb446.png
.. |image39| image:: images/entries/a4d260146fe4267a34d9db97495df2b244f5d7ff.gif
.. |image40| image:: images/entries/8e644bb4823b8da291e1e2b2dd1ca472d3d57246.png

