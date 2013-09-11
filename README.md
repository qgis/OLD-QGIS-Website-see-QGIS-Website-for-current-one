QGIS-Website
============

QGIS-Website

To be able to run localisation targets you will need Sphinx 1.2b1 which comes with pip. 
Sphinx coming with most distro's is just 1.1.3. You will get an error with those.

Best to run the make file in a virtual env (http://www.virtualenv.org/):

So install sphinx 1.2b1:

    pip install sphinx

Sphinx bootstrap theme (http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html).
We use 0.3.0 currently.

    pip install sphinx_bootstrap_theme==0.2.8

Sphinx intl extention (https://pypi.python.org/pypi/sphinx-intl):

    pip install sphinx-intl

Then build:

    make clean html (to build the english languag)
    make clean LANG=nl html (to build the dutch version. Currently available: nl, es, zh_CN)

If you want add the QGIS-Documentation docs into the build, you need to manually copy the sources, resources and po files into the website project

TODO: do this via scripting or Makefile

    # from the QGIS-Documentation / source / docs directory, copy all subdirs into the QGIS-Website /source / docs directory
    # from the QGIS-Documentation / resources / en directory, copy all in to the QGIS-Website / resources / en directory
    # from the QGIS-Documentation / i18n / <your language> / LC_MESSAGES / docs directory, copy all subdirs in the  QGIS-Website / i18n / <your language> / LC_MESSAGES / docs

To gather all strings in a pot (.po) file:

    make gettext

To update or create strings:

    sphinx-intl update -p i18n/pot -c source/conf.py -l nl (es, zh_CN)

To create .mo files from the .po files then:

    sphinx-intl build -c source/conf.py

Then normal build

    make clean LANG=nl html
    
See it in action: http://new.qgis.org/html/en/site (to be moved)

qgis-style.css is based on Less (see http://lesscss.org/ )

To make changes to CSS on MacOsx
 
    download / install / open Less app (http://incident57.com/less/)
    in Finder navigate to themes/qgis-theme/static/
    drag qgis-style.less file to the Less app
    make changes in qgis-style.less
    on save it should automatically compile into qgis-style.css
    for advance usage read docs on Less CSS: http://lesscss.org/

    (if you have any questions ping yulka_plekhanova on Skype)

To make changes on cli Linux

    # install node-less and the compressor
    sudo apt-get install node-less yui-compressor
    # compile the less file to a normal css file:
    lessc qgis-style.less qgis-style.css
    # or
    lessc qgis-style.less > qgis-style.css
    # optional: compress the css
    yui-compressor -o qgis-style.css qgis-style.css
    
