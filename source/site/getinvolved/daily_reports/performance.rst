Performance
===========

At the moment, two tools are living together to test and generate performance
reports.

The first one is `MS-Perfs <https://github.com/camptocamp/ms_perfs>`_ which
allows to compare QGIS Server with other map servers (like GeoServer or
MapServer). Reports are generated weekly and available
`here <http://test.qgis.org/perf_test/ms_perf/>`_.

The second one is `Graffiti <https://github.com/pblottiere/graffiti>`_,
allowing to generate a performance report between several versions of QGIS
Server and/or specific project options (parallel rendering effect, trust
option, and so on). Reports are also generated daily and available
`in <http://test.qgis.org/perf_test/graffiti/>`_. Note that
`QGIS-Server-PerfSuite <http://github.com/Oslandia/QGIS-Server-PerfSuite>`_
project is the deployment infrastructure to run Graffiti in continuous
integration.
