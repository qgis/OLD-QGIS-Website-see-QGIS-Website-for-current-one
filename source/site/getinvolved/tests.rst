.. _tests:

Tests
=====

Both QGIS and QGIS server are being tested via all kind of ways.

From build tests (github workflows) and code unit tests to OGC conformance testing.

Github workflows
................

.. image:: https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg
    :target: https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush

Docker
......

.. image:: https://img.shields.io/docker/automated/qgis/qgis.svg
    :target: https://hub.docker.com/r/qgis/qgis/tags

Unit tests
..........

See `Unit testing
<https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html>`_

OGC Conformance testing
.......................

See `OGC conformance testing <https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html>`_
for more information and how to run these tests yourself.

Recent tests output can be found here: http://test.qgis.org/ogc_cite. For latest
WMS 1.3.0 test see http://test.qgis.org/ogc_cite/wms_130/latest/report.html and
for WFS 1.1.0 see http://test.qgis.org/ogc_cite/wfs_110/latest/report.html.


