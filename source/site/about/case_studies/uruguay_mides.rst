====================================================================
Use of QGIS at the Ministry of Social Development of Uruguay (MIDES)
====================================================================

Introduction
============

The Ministry of Social Development of Uruguay (`MIDES, <http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision>`_ , for its acronym in Spanish) is responsible for the
national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial
levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas
of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring (`DINEM <http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos>`_ ) is a section of MIDES that oversees the
monitoring and evaluation of plans, programs, actions, devices and social projects through the national
territory. DINEM also produces and manages necessary information to improve their design and
implementation.

The `Department of Geography of DINEM <http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia>`_ is responsible for the production, management and analysis of
geographical information,

QGIS at the Department of Geography of the DINEM
================================================

Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open
source software to fulfill our duties. In particular, the management of an extensive field work, consisting in
the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the
country. The objective was to conform a thorough georeferenced database of target households, in order to
improve social policies implementation. Particularly, data was collected to enhance the scope of monetary
transfer programs (`"Asignaciones Familiares – Plan de Equidad" <https://www.bps.gub.uy/3540/plan-de-equidad.html>`_
and `"Tarjeta Uruguay Social" <http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus>`_). The
survey form applied contemplates social, housing, and environmental aspects.

Logistics to viabilize such fieldwork involved using statistical packages to manage the database generated,
together with an intensive use of GIS to organize field trips and georeference relieved data.

.. figure:: ./images/uruguay_mides1.png
   :alt: QGIS at work
   :align: center

   QGIS at work: identifying houses on informal settlements to implement fieldwork

Although proprietary software was implemented when the working process started, the development of the
tasks themselves gradually demanded it to be converted to open source software. As the process as a whole
became more computerized -incorporating a workflow engine and a PostGIS geospatial database-, license
requirements and benefits offered by free and open source software (FOSS) options encouraged us to make
the change. In that way, as the QGIS project was refined (fewer bugs and more functionalities), we were able
to satisfy our needs using QGIS. PostGIS associated tools allowed the workgroup to rapidly coordinate the
tasks needed to viabilize daily field trips, together with subsequent analysis tasks on the same data fieldwork
generated, shortly after it was relieved and digitized.

.. figure:: ./images/uruguay_mides2.png
   :alt: QGIS at work
   :align: center

   QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)

In addition to information management and field work implementation, we constantly use QGIS typical
geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the
data that the fieldwork generates, as with other ministry programs information, and frequently even to aid
interinstitutional projects. With `"qgis2web" <https://plugins.qgis.org/plugins/qgis2web/>`_ we were able to produce interactive maps, which have become
the main way to communicate the results of such investigations. They allow human resources within other
programs and agencies to easily and effectively manage higher amounts of information than with a collection
of static maps, even when these resources are not used to reading spatial data.

Conclusion
==========

QGIS has become a fundamental software to the Department of Geography at DINEM. It presents an
excellent performance to work with heavy files and to interact with PostGIS and with our workflow engine.
This allows us to have an excellent management of geographic data, which also makes for the production of
basemaps and thematic cartographies of superior quality.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance,
the possibility of exporting "leaflet" map viewers, as well as incorporating high resolution satellite imagery
directly into the GIS work area through “OpenLayers” to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very
different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public
administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a
web map, offering general population much information about social issues (`SIG MIDES <https://mapas.mides.gub.uy/>`_, OpenLayers based
WEB GIS developed by the IT division).

Authors
=======

Guillermo D'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - Adviser in Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Ph.D. student in Social Sciences, Population Studies. Magister in Contemporary Studies of Latin America. Degree in Anthropological Sciences.

Martín Hahn - Adviser in Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Bach. currently coursing Geography Degree.

Despite the fact that the present article was written by the three above mentioned, there are more than a hundred people involved in the process described in it, so this work belongs mainly to them.

Contact: mapas@mides.gub.uy

