QGIS-Website
============

QGIS-Website

To be able to run localisation targets you will need Sphinx 1.2b1 which comes with pip. 
Sphinx coming with most distro's is just 1.1.3. You will get an error with those.

Best to run the make file in a virtual env ( http://www.virtualenv.org/ ):

Move to a directory (~/myvirtualenvs/) and create a virtualenv enabled dir:

    virtualenv sphinx  # one time action, only to create the environment
    cd sphinx

And activate this virtualenv

    source bin/activate 
    # now you will see sphinx before your prompt:
    (sphinx)richard@mymachine

Now always activate your environment before building. To deactivate, you can do:

    deactivate

You can install all tools in on go via the REQUIREMENTS.txt here in root of this repo:

    pip install -r REQUIREMENTS.txt

Alternatively do it one by one:

Install sphinx 1.2b1 now in your virtual env:

    pip install sphinx==1.2b1
    
Sphinx bootstrap theme ( http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html ).
We use 0.3.0 currently.

    pip install sphinx_bootstrap_theme==0.3.0

Sphinx intl extention ( https://pypi.python.org/pypi/sphinx-intl ):

    pip install sphinx-intl

Then build:

    make html (to build the english languag)
    make LANG=nl html (to build the dutch version. Currently available: en, nl, es, zh_CN, de, it)

If you want add the QGIS-Documentation docs into the build, you need to manually copy the sources, resources and po files into the website project

    make fullhtml (english)
    make LANG=nl fullhtml

To gather new strings in a pot (.po) file for your language, and merge them with 
excisting translations in the po files (normally to be ran by your language maintainer):

    make LANG=xx pretranslate # where xx is your language code

To add a new language (the scripts will need some directory structure):

    make createlang

See it in action: http://new.qgis.org/html/en/site (to be moved)

Styling the website
-------------------

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
    
