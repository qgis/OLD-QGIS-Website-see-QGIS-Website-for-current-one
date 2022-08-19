
=================================================
Lynx habitat analysis in the Southern Carpathians
=================================================

A case study to promote basic understanding of wildlife habitat modeling for students based on open source data.

Introduction
------------

Challenged with the task of GIS based modeling for the first time, a working group
of undergraduate forestry students of the University for Sustainable Development 
Eberswalde (HNEE) conducted literature research for habitat suitability and behavior
of the Eurasian Lynx (*Lynx lynx*). In the module ‘Applied GIS in Natural Resource Management’,
under the guidance of Prof. Mund, the students quickly discovered the subject’s complexity, 
especially within regard to the adaptability of species to changing environments. 
With limited research published in English about lynx habitat on the Romanian side,
we continued the project based on only freely available data sets and open-source software, 
aiming to establish conceptual knowledge of habitat modeling, strengthening skills 
on widely applied QGIS tools and to create a **basic expert model** in the process.


Methodology
-----------

All collected data was processed with QGIS 2.6 and 2.8, projected into 
ETRS89 / ETRS-LAEA and stored according to the INSPIRE directive to meet EU standards. 
An overall **discrete index of weights** was defined and applied to all input data. 

.. figure:: ./images/europe_lynx1.png
   :scale: 100 %
   :alt: Figure 1: Workflow - Lynx habitat expert model

   Figure 1: Workflow - Lynx habitat expert model


**Workflow description**

* Area of Interest [Step I – II]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box [α] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools [β] were applied to all additional data as an initial preparation step (Figure 2)

* Land Cover Suitability Model [Step IX]: [γ] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values.  Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Note: Land cover classes were grouped by possible lynx occurrence and human activity. Although technically of older origin, information related to forest cover values were integrated in order to indicate habitat improvement and as a general example for joining spatial data sets*

* Habitat Suitability Model [Step X]: [δ] An Elevation Suitability Index was derived from the AsterDEM 2.0 [VI] and together with a Population Density Index [V] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

::

 Cover Suitability Model * Population Density Index * Elevation Suitability Index

*Note:Defining forest (>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*

* Potential Hunter Accessibility Model [Step XI]: Applying the #Terrain analysis tool [ε], a slope layer was extracted from the DEM data and combined [η] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

::

 .
                       Slopelayer
 Road distance * ( 1 + ----------- )
                          100

* Conservation Value Model [Step XII]: Is the result of the #Raster calculator function: (Figure 4)

::

 (Habitat Suitability Model * Hunter Accessibility Model)
 --------------------------------------------------------
                        2

*Note: The Hunter Accessibility Model shall indicate the decreasing likelihood of hunters accessing the area by further distance to roads and increasing slope*

.. figure:: ./images/europe_lynx2.png
   :scale: 100 %
   :alt: Figure 2, 3 and 4

   Figure 2, 3 and 4

Conclusion
----------

Looking at the final output (Figure 3), a plausible first potential habitat analysis
appeared to be successful, yet more importantly, basic modeling itself turned out 
to be less difficult than initially expected. Our choice to add a sub-model for 
hunter accessibility allowed us to implement another dimension in terms of habitat 
risk assessment, which can be simply nested into the already existing scenario and 
used to determine protection necessities under aspects of e.g. infrastructure 
development. However, some crucial habitat information, such as forest structure
(our highest habitat suitability) cannot be derived by available data sets and 
in combination with the complex species behavior, the result must therefore be 
understood as basic and incomplete. Additional factors not implemented at 
this stage are road mortality, terrain roughness and detailed prey occurrence.

Besides its open source, free available character, QGIS software has been the
subject of major developments in recent years. We made very positive experience
with the integration of the tool box, allowing the use of various GRASS and SAGA
tools, even for inexperienced users. No compatibility issues occurred despite
changing frequently between different versions and the general absence of
administrative restrictions can be a powerful advantage when working intuitively
with data sets. We are looking forward seeing further improvements, especially
in regards to the integrated model builder.

References
----------

* Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
* Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
* Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.  
* Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97–110.
* Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

Authors
=======

Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe and
David Winger are fourth semester students of the study program International
Forest Ecosystem Management B.Sc., Anne Gnilke respectively German Forestry and
Henri Hiltunen is an exchange student from Mikkeli University of Applied
Sciences, Finland. Prof. Mund is lecturing GIS and Remote Sensing at HNE
Eberswalde since 2010 and provided guidance and technical support to the
project.

Please contact Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, or
Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de for further information.
