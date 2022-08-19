
.. _addinggrasstools:

Adding GRASS Tools
==================

GRASS modules can be run from QGIS *GRASS Tools* if QGIS was started from a
GRASS shell or if a GRASS mapset was opened from QGIS. The modules work with
GRASS data only.

It is easy to modify the menu and add new modules because both the menu and the
modules are defined in XML configuration files. Below is described how to write
new modules and modify menu tree.


Module configuration
--------------------


Background
..........

The options of each module shown in module's_*Options_*tab are created according
to combination of definition in QGM (QGIS GRASS module) file and options
definition in GRASS module or GRASS script --- GMO (GRASS module options).
Because each option in QGM is linked to one (or more) GMO, it is often useful
if not necessary to see GMO. GMO are output by GRASS module if it is run
with _*--interface-description_* option, the output is in XML format, for example:


::

 r.to.vect --interface-description


Some GRASS modules have too many options which can be confusing for beginners.
In QGM it is possible to define only some of them and possibly set some default
values and/or hide some options with certain value. That means that more
QGIS-GRASS modules can be defined for each GRASS module. For example the module
r.to.vect was divided into three QGIS-GRASS modules with predefined "feature"
option. The QGM definition is written in XML format file with extension .qgm,
one for each QGIS-GRASS module. Configuration files are stored in
_*qgis/src/plugins/grass/modules*_ directory and installed in
_*share/qgis/grass/modules*_ directory. The name of the file should start with
GRASS module name + a word describing the specific task. For example, the module
which extracts vector lines from raster is called r.to.vect.line.qgm.

Here is an example of a configuration file:

::

  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE qgisgrassmodule SYSTEM "http://mrcc.com/qgisgrassmodule.dtd">
  <qgisgrassmodule label="Generate aspect map from DEM" module="r.slope.aspect">
         <option key="elevation" />
         <option key="aspect" />
  </qgisgrassmodule>


qgisgrassmodule tag attributes
..............................

* *label* --- description used in menu tree
* *module* --- name of GRASS module executable or script.

Option tags
...........

Each qgisgrassmodule tag can contain one or more option tags:

* *option* --- corresponds to GMO parameter tag, example:

::

  <option key="elevation" />

* *flag* --- corresponds to GMO flag tag, example:

::

  <flag key="o" answer="on" hidden="yes" />


* *field* --- for vector layers defines attribute field, the option is created
  as combobox with available fields. For example (v.to.db.qgm):

::

  <field key="column" layer="map" type="integer,double" label="Attribute field" />


* *selection* --- this is quite interesting and useful type of option. It allows
  to define list of GRASS vector categories using QGIS interface. Features (and
  their categories, GRASS feature ID equivalent) can be selected either with
  'Select Features' tool or in the attribute table. The list of categories is
  updated dynamically. Example (v.extract.list.qgm):

::

  <selection key="list" layerid="input" label="Cats" />

Common option/flag tag attributes
.................................

* *key* --- name of module option in GMO.
* *answer* --- default value (overwrites GMO default value); value "on" will
  switch on a flag.
* *hidden* --- the option will not appear in the dialog, but module will be run
  with this option (hidden="yes").
* *label* --- option label
* *advanced* --- "yes" or "no", default is "no". If set to "yes", the
  option/flag is add to initially hidden advanced options panel and "Show
  advanced options >>" button is shown under simple (basic,standard) options
* *version_min* --- minimum GRASS version for which this option/flag is valid
* *version_max* --- maximum GRASS version for which this option/flag is valid

Option tag specific attributes
..............................

* *typeoption* --- this option can be used with vector layer to define the name
  of vector input type option, when module is run, the type of selected vector
  layer will be used for that option. For example (v.overlay.or.qgm):

  ::

    <option key="ainput" typeoption="atype" layeroption="alayer" typemask="area,line" />

  It means that if a layer is selected from combobox of this option the
  _*atype*_ option is automaticaly set to the layer's type, and thus _*atype*_
  does not have to be added at all.

* *layeroption* --- equivalent of typeoption for layer.
* *typmask* --- for vector input option defines allowed types. Only the layers
  of one of defined type are displayed in input. See v.overlay.or.qgm for example.


Field tag specific attributes
.............................

* *layer* --- the key attribute of the option which defines the vector this
  field should depend on
* *type* --- defines types of attribute fields which should be added to the
  field combobox, for example

  ::

    <field key="column" layer="map" type="integer,double" label="Attribute field" />


  It means that only the attribute fields of type in integer and double precision
  will appear in combobox. See v.what.vect for example (2 different vectors).


Behind the scene
................

The idea QGIS-GRASS modules implementation is to use maximum information from
GMO and only simplify the interface. Here are described some rules how
information from GMO are used and in which order if not all of them are defined
in GMO.

* *label* --- if label attribute is defined in QGM it is used as option label,
  if it is not defined GMO option label tag is used and if it is not defined GMO
  option description tag is used
* *tooltip* --- (appeares on mouseover the option) if label is defined (either
  in QGM or GMO) and description is defined in GMO (thus label and description
  differ) the GMO description tag is used for tooltip
* *multiple values* label --- if an option is type multiple with defined list of
  possible values (like upload option of v.distance) and description tag is
  defined for value tag in GMO then it is used as checkbox label

Picture
.......

Each module must be represented also by a picture/icon which symbolizes the
modules functionality. The pictures are also stored in plugins/grass/modules as
SVG (*.svg) or PNG (*.png) files.

Currently there are supported 3 schemas for the picture:

* 1 picture
* 2 pictures --- QGIS will create icon: 1 -> 2
* 3 pictures --- QGIS will create icon: 1 + 2 -> 3

The name of the picture starts with QGIS-GRASS module name to which is appended
picture number, for example: v.overlay.and.1.svg, v.overlay.and.2.svg,
v.overlay.and.3.svg. It is possible to combine SVG and PNG pictures.

SVG and PNG pictures can be generated from QGIS using *Map Composer*. The size
of PNG images should be larger than the expected icon size, because it is
expected to be later used in automatically generated documentation, where
pictures will be used in larger size.

QGIS GRASS scripts
..................

Because it can take long time until a new script is added to stable GRASS
release and because some scripts can be useful only for QGIS GUI interface it is
possible to add a 'GRASS' script to QGIS. The scripts should follow general
requirements for GRASS scripts and they are located in qgis/src/plugins/grass/scripts.


Menu configuration
------------------

Once we have a new QGM configuration file, we can add the module to the list of
modules. The list is defined in qgis/src/plugins/grass/config/default.qgc file.
The sections in the file are organized hierarchically and represented in menu
as tree.

Here is an example of a record for r.to.vect.line.qgm module

::

   <section label="Convert raster to vector">
         <grass name="r.to.vect.line.qgm"/>
   </section>


For section/module it is possible to specify GRASS version for which it is valid
using version_min/version_max attributes:

* *version_min* --- minimum GRASS version for which this section/module is valid
* *version_max* --- maximum GRASS version for which this section/module is valid


General rules for new modules
-----------------------------

*GRASS Tools* are intended mostly for beginners and not very experienced users.
The basic rules are:

* Each module should have 3 or less options; if it seems to be necessary to add
  more options, it should be discussed beforehand
* Module definition should be robust so that it doesn't allow a user to run a
  module with wrong option. If there is not yet support for certain type of
  option the module should not be added to menu


Specific rules for module descriptions
--------------------------------------

* Avoid 3rd person for verbs, e.g. "Export raster" instead of "Exports raster"
* Avoid unnecessary "map", "layer" and "file", e.g. "Export raster" instead of
  "Export raster map layer"
* Avoid unnecessary "GRASS", e.g. "Export raster" instead of "Export GRASS raster"
* Avoid "a|an", e.g. "Export raster" instead of "Exports a raster"
* Avoid padding words, e.g. "Export raster" instead of "Allows the export of a raster"
* Avoid "Convert": use "Export" or "Import" instead. Convert should be used for
  internal GRASS conversions (e.g. from raster to vector)
* Acronyms should be upper case, e.g. ASCII instead of ascii
* In case of doubt, please check the existing similar plugins to maintain
  consistency


Options which cannot be currently used
--------------------------------------

Technically, any option can be used. Some kinds of options however are not yet
well supported, for example those which depend on other option. Here is a list
(probably incomplete) of options which are not yet well supported and so should
not be used at present:

* OGR input dsn/layer (v.in.ogr)


Modules which can be added
--------------------------

Most modules have been added. If you need additional ones, please write to the
qgis development mailing list, and list hereafter the modules you think are most
important to be added.

You should post the name of a new QGIS-GRASS module, the name of the GRASS
module and the options which you want to use. For example:

::

  r.to.vect.area: r.to.vect input output feature=area

See also here for discussion on 
`GRASS-QGIS relevant module list <http://grass.osgeo.org/wiki/GRASS-QGIS_relevant_module_list>`_.


Modules to be deprecated
------------------------

List hereafter the modules who should be removed, with a rationale for this
suggestion (e.g.: some modules related to projections are difficult to
understand, and of no general use). Please note: some modules have not been
thoroughly tested. Please test them, and if you find any issue report it to the
redmine (better still: fix it yourself and send the patch).
