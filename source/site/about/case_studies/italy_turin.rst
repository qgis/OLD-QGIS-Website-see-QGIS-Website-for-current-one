===================================================================================================
The Research Institute for Geo-hydrological Protection of Turin --- Aerial photo archive management
===================================================================================================

The Research Institute for Geo-hydrological Protection of Turin (IRPI), member of the Italian National Research Council (CNR), started its activities in 1970. The skills gathered since its foundation concern various following investigation sectors, e.g. the study of geological and hydrogeological features of the Alpine-Po river system (Northern Italy) or the monitoring, prediction and prevention of natural disasters. These tasks are carried out by the employment of a multidisciplinary approach including hearth sciences, engineering and geomatic.

In order to carry out exhaustive researches and studies, in addition to field survey, modelling and historical records analysis, aerial photograms are employed. Their use varies, from “simple” visual analyses to complex processing as stereoplotting or image segmentation.

The institute, for the explained purposes, keeps in its archive about 170000, recent and historical, photograms --- the oldest one dating back to 1920s (Figure 1) --- covering, in different years, the Po basin or part of it. Some photograms cover other basins in northern Italy. In addition the archives keeps flight plans of the described photograms (Figure 1).

.. figure:: ./images/italy_turin1.jpg
   :alt: 1929 photogram (left) and 1954 flight plan (right)
   :scale: 90%
   :align: left

   1929 photogram (left) and 1954 flight plan (right).

Archive management
==================

In order to cope with such amount of data a GIS approach was adopted. First each flight plan, showing photograms’ footprints, was scanned, georeferenced and digitized in shapefile format. Then photograms were scanned, at 600 DpI, and files were named according to a code including map sheet, year of acquisition, strip number, photogram’s serial number and code of property (IRPI’s or external).

Each footprint in digitized flight plan was provided, in its attributes, with the previous codes in order to link shapefile to scanned photograms, by the use of eVis plugin (Horning et al, 2009), and to allow a user friendly interface to search and refer to (Figure 2). Data concerning photogram code were stored in attribute table fields than, by field calculator, a “Link” field was created storing photograms’ file paths.

.. figure:: ./images/italy_turin2.jpg
   :alt: Photogram display (eVis Plugin)
   :scale: 90%
   :align: left

   Photogram display (eVis Plugin)

Moreover, due to the amount of searchable data a geographical search interface was developed. Thanks to the graphical modeler (in Processing, formerly SEXTANTE, plugin) capabilities, the developed tool, by different selection masks and input boxes, allows the user to select among three layers (administrative boundaries, map sheets and rivers), find a feature by querying its table and employ it to spatially query a digitized flight plan with the purpose of selecting photograms’ footprints intersecting the selected feature (Figure 3). With this procedure, is then possible to point out selected photogram and simply display them with the previously described tool or extract, by their filenames and path, photograms’ files for further processing.

.. figure:: ./images/italy_turin3.jpg
   :alt: Graphic modeler scheme used in the selection tool (in background: purple polygons-map sheets; labeled orange polygons-photogram footprints; brown polygons-municipalities administrative borders)
   :scale: 90%
   :align: left

   Graphic modeler scheme used in the selection tool (in background: purple polygons-map sheets; labeled orange polygons-photogram footprints; brown polygons-municipalities administrative borders)

The photogram collection is of great interest both in research (e.g. Godone et al, 2014) and professional environments (Figure 4). Now thanks to the described procedures and tools the collection is fully accessible and since 2009 the photograms were employed in several projects both internal and external to the Institute. QGIS features and plugins allowed developing tools and procedures to optimize photogram archive both in the implementation of its management and in its exploitation.


.. figure:: ./images/italy_turin4.jpg
   :alt: Pie chart showing different area of interest employing photograms in year 2013
   :scale: 90%
   :align: left

   Pie chart showing different area of interest employing photograms in year 2013


References
==========

* Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) “Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)”, Land use policy, ISSN: 0264-8377
* Horning N., Koy K., Ersts P. (2009) “eVis (v1.1.0) User's Guide. American Museum of Natural History, Center for Biodiversity and Conservation” Available from http://biodiversityinformatics.amnh.org/

Links
=====

* Aerial photo archive website: http://www.irpi.to.cnr.it/index_en.php?page=aerofototeca_en

Authors
=======

.. figure:: ./images/italy_turinaut1.jpg
   :alt: Danilo Godone
   :height: 120
   :align: left

   Danilo Godone

Danilo Godone is a Postdoc grant holder, at Turin University, studying geomatic contribution in landslide, glacier and, more generally, natural disasters monitoring. He is a member of NATRISK --- Research Centre on Natural Risks in Mountain and Hilly Environments, in the same University. He acts as a freelance consultant in the same topics, too.

.. figure:: ./images/italy_turinaut2.jpg
   :alt: Franco Godone
   :width: 120
   :align: left

   Franco Godone

Franco Godone is a specialized technician at Research Institute for Geo-hydrological Protection of Turin (IRPI-CNR) since 1972. He is involved in topographical and aerophotogrammetrical surveys and data analysis in the alpine regions.
