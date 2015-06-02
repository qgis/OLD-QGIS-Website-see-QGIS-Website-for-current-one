
============================================================
Using the processing toolbox to automate snow classification
============================================================

Snowy Hydro Limited (SHL) is a peak electricity generator based in the Snowy Mountains of New South Wales, Australia. Despite owning a variety of generation assets across the country, Snowy Hydro Limited is best known for the custodianship of an iconic piece of Australian infrastructure, the Snowy Mountains Hydro Electric Scheme. 


The Snowy Mountains Hydro Electric Scheme, is made possible by seasonal snow falls in the New South Wales alpine region. Water from the spring snow melt is used to generate electricity addressing peak demand in the national electricity market, while also diverting water to the drier inland areas of South Eastern Australia for irrigation and agriculture.


Classifying snow cover over the winter months allows SHL to monitor the life cycle of the snow covered area, archive coverage areas for historical records, and provide coverage statistics to the hydrographic services team for water yield and storage forecasts.

.. figure:: images/australia_snowyhydro1.jpg
   :height: 620
   :scale: 70
   :align: center
   :alt: Map 1.1 Snowy Water Catchment Map

   Map 1.1 Snowy Water Catchment Map

Background
----------

Each year during the winter months (1st June to the 31st October) SHL obtains as many cloud free images as possible from the MODIS Terra (EOS AM) satellite. These images are then ingested into an algorithm known as the Normalised Difference Snow Index (NDSI), which is used to indicate areas where snow is present. While this algorithm is not unique to any one particular sensor, the MODIS instrument was chosen due to its adequate spatial resolution and daily coverage of the project area (Map 1.1 Snowy Water Catchment).


Aim
---

The aim of this project is to automate the NDSI workflow as a model in the QGIS processing toolbox. The required output is a vector polygon showing the snow covered extent within the Snowy Water Catchment, along with attribution describing the total area covered in square kilometres.


Method
------

The NDSI algorithm itself is quite simple (show below in Formula 1.1 - Normalised Difference Snow Index (NDSI)) and the subsequent steps required to extract snow cover in a vector format also lends itself nicely to a processing toolbox model.


.. figure:: ./images/australia_snowyhydro8.png
   :scale: 100 %
   :alt: Formula 1.1 - Normalised Difference Snow Index (NDSI)

   Formula 1.1 - Normalised Difference Snow Index (NDSI)


This NDSI algorithm will return results between -1 and 1, with the threshold for snow typically being values greater than 0.4. An example of the NDSI output is shown below (Map 1.3 - NDSI output), alongside a natural colour image (Map 1.2 - MODIS true colour) for the 13th July 2014. As seen from these images the NDSI output is very good at discriminating snow covered areas from other land cover types and clouds. It can however misclassify portions of large water bodies as snow, caused by water having absorption characteristics in the Near Infrared part of the spectrum. This characteristic of the NDSI indicates the need to incorporate a water mask at some stage in the model.


.. figure:: ./images/australia_snowyhydro2.jpg
   :width: 300
   :align: left
   :alt: Map 1.2 - MODIS true colour

   Map 1.2 - MODIS true colour

.. figure:: ./images/australia_snowyhydro3.jpg
   :width: 300
   :align: center
   :alt: Map 1.3 - NDSI output

   Map 1.3 - NDSI output

.. figure:: ./images/australia_snowyhydro4.jpg
   :width: 300
   :align: left
   :alt: Map 1.4 - Recoded "Snow" vs "Non snow"

   Map 1.4 - Recoded "Snow" vs "Non snow"


The NDSI output is created with some very simple band map by using the GRASS module "r.mapcalculator". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting "Snow" and "Non snow" areas. To get that classification another GRASS module "r.recode" was used and produced the result shown above in Map 1.4 Recoded ‘Snow’ vs ‘Non Snow’.


The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment  (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.


.. figure:: ./images/australia_snowyhydro5.jpg
   :width: 300
   :align: left
   :alt: Map 1.5 - Extracted Snow

   Map 1.5 - Extracted Snow

.. figure:: ./images/australia_snowyhydro6.jpg
   :width: 300
   :align: center
   :alt: Map 1.6 - Snow inside the SWC

   Map 1.6 - Snow inside the SWC

.. figure:: ./images/australia_snowyhydro7.jpg
   :width: 300
   :align: left
   :alt: Map 1.7 - Final snow covered area

   Map 1.7 - Final snow covered area


The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in "Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model".


.. figure:: ./images/australia_snowyhydro.png
   :width: 600
   :align: center
   :alt: Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model

   Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model


Results/Conclusion
------------------

The QGIS processing toolbox is a powerful way to automate a workflow such as this snow classification. The model shown above successfully automates the snow classification process, and delivers a GIS dataset that can be used for visualisation and input into further statistical applications. It successfully removes subjective user error associated with previous methods used by SHL, while providing a repeatable and consistent classification tool. Some seasonal results can be viewed here.


Author
======

Andrew Jeffrey is a GIS Analyst with Snowy Hydro Limited based in Cooma NSW, Australia. He graduated from Charles Sturt University in Wagga Wagga with a Bachelor of Science (Bsc) majoring in Spatial Information Systems in 2004. While at Snowy Hydro Limited he has been able to provide spatial support to exciting projects such as the Cloud Seeding experiment, and day to day operations within the organisation.

