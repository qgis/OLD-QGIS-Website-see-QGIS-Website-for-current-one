
from paver.easy import *
from paver.setuputils import setup
from sys import platform as currentos

import os
import shutil
import distutils.core

setup(
    name="QGIS-Website",
    #packages=['mycool'],
    version="1.0",
    url="http://qgis.org/",
    author="Richard Duivenvoorde",
    author_email="richard@duif.net"
)


options(
    setupstatic=Bunch(
        lang='en',
    ),
    html=Bunch(
        sphinxbuildbin='sphinx-build',
        builder='html',
        builddir="build",
        sourcedir="source",
        resourcedir="resources",
        conf="source/conf.py"
    ),
    sphinxintl=Bunch(
        sphinxintlbin='sphinx-intl'
    ),
    virtualenv=Bunch(
        script_name="bootstrap.py",
        dest_dir="virtualenv",
        packages_to_install = [
            # Project dependencies
            'Jinja2==2.7.2',
            'MarkupSafe==0.18',
            'Pygments==1.6',
            'Sphinx==1.2',
            'argparse==1.2.1',
            'distribute==0.7.3',
            'docutils==0.11',
            'polib==1.0.3',
            'six==1.5.2',
            'sphinx-intl==0.9.4',
            # pip install transifex on Windows files because of py2exe problem
            # if you need id: pip install transifex-client==0.9
            #'transifex-client==0.9'
            ],
        paver_command_line="virtual_env_init",
    )
)


# from http://blog.carduner.net/tag/paver/
# to create bootstrap.py: 
#   paver paver.virtual.bootstrap

INSTRUCTIONS = """
To enter the virtual environment on Linux/Mac, run:
   $ source virtualenv/bin/activate
To exit the environment:
   $ deactivate

To enter the virtual environment on Windows, run:
   $ virtualenv\Scripts\activate
To exit the environment:
   $ deactivate
"""

@task
def virtual_env_init():
    """Initializing everything so you can start working
    by running: $ paver paver.virtual.bootstrap
    This will create a bootstrap.py file, which you can run with
    $ python bootstrap.py
    That will create a virtual environment to work in.
    """
    print "virtual environment successfully bootstrapped."
    print INSTRUCTIONS


# remove all resources from source/static directory
# copy english resources from resources/en to source/static directory
# IF we have a localized build (LANG != en) then
# overwrite with potentially available LANG resources  by
# copy LANG resources from resources/LANG to source/static directory
# TODO: check if LANG != en, for now: unnessecary copy for english
#   localizeresources: clean
#   	@echo
#   	@echo "Removing all static content from $(SOURCEDIR)/static."
#   	rm -rf $(SOURCEDIR)/static
#   	@echo "Copy 'en' (base) static content to $(SOURCEDIR)/static."
#   	mkdir $(SOURCEDIR)/static
#   	# historically the images for the docs sub project are not in a separate docs folder
#   	# that is why we copy site (to site) and docs/* into root in separate steps
#   	cp -r $(RESOURCEDIR)/en/site $(SOURCEDIR)/static
#   	@if [ -d "$(RESOURCEDIR)/en/docs" ]; then \
#   		cp -r $(RESOURCEDIR)/en/docs/* $(SOURCEDIR)/static; \
#   	fi
#   	@echo "Copy localized '$(LANG)' static content to $(SOURCEDIR)/static."
#   	@if [ -d "$(RESOURCEDIR)/$(LANG)/site" ]; then \
#   		cp -r $(RESOURCEDIR)/$(LANG)/site $(SOURCEDIR)/static; \
#   	fi
#   	@if [ -d "$(RESOURCEDIR)/$(LANG)/docs" ]; then \
#   		cp -r $(RESOURCEDIR)/$(LANG)/docs/* $(SOURCEDIR)/static; \
#   	fi


@task
@cmdopts([
    ('lang=', 'l', 'Optional language param (iso code, like "nl") to build for. If ommitted all languages in i18n dir will be build')
])
def setupstatic():
    """Setting up static resources (like images).
    Starting with the english version and overwriting with localized
    resources if available.
    """
    # remove static (images) from source/static dir
    staticdir = os.path.join(options.html.sourcedir, "static")
    if os.path.exists(staticdir):
        shutil.rmtree(staticdir)
    # create an empty static dir again
    os.mkdir(staticdir)
    # copy english resources in static dir
    english_site_resources = os.path.join(options.html.resourcedir, "en", "site")
    distutils.dir_util.copy_tree(english_site_resources, os.path.join(staticdir, "site"))
    # copy (optional) localized resource in static dir
    translated_site_resources = os.path.join(options.html.resourcedir, options.setupstatic.lang, "site")
    if os.path.exists(translated_site_resources):
        distutils.dir_util.copy_tree(translated_site_resources, os.path.join(staticdir, "site"))
    # historically the images for the docs sub project are not in a separate 'docs' folder
    # that is why we copy docs/* into root instead of docs to docs
    english_docs_resources = os.path.join(options.html.resourcedir, "en", "docs")
    if os.path.exists(english_docs_resources):
        distutils.dir_util.copy_tree(english_docs_resources, staticdir)
    translated_docs_resources = os.path.join(options.html.resourcedir, options.setupstatic.lang, "docs")
    if os.path.exists(translated_docs_resources):
        distutils.dir_util.copy_tree(translated_docs_resources, staticdir)

    # we also need to set the proper sphinx binaries
    if currentos == 'win32':
        options.sphinxintl.sphinxintlbin = 'virtualenv\Scripts\sphinx-intl.exe' 
        options.html.sphinxbuildbin = 'virtualenv\Scripts\sphinx-build.exe'



@task
@cmdopts([
    ('lang=', 'l', 'Optional language param (iso code, like "nl") to build for. If ommitted all languages in i18n dir will be build')
], share_with=['setupstatic'])
@needs(['setupstatic'])
@no_help
def sphinxintl(options):
    """Generate .mo files from .po files of this language."""
    # print "Running sphinx-intl build"
    # sphinx-intl uses 'locale-dir' from conf.py
    # -c = pointing to conf.py
    # -l = language
    sh('%s build -l %s -c %s' % (options.sphinxintl.sphinxintlbin, options.setupstatic.lang, options.html.conf))


@task
@needs(['sphinxintl'])
@cmdopts([
    ('lang=', 'l', 'Optional language param (defaults to "en") to build for.'),
    ('builder=', 'b', 'Sphinx builder to use (defaults to "html").')
], share_with=['setupstatic'])
def html(options):
    """Generate html in output dir."""
    #print "Running sphinx-build"
    # sphinx-build options used:
    # -b = build type (html, pdf etc)
    # -d = path for the cached environment and doctree files
    # -D = override a setting in configuration file
    # -A = pass a value into the templates, for HTML builder
    # sphinx-build -b html -d output/html/doctrees  -D language=en -A language=en source output/html/en
    sh('%s -b %s -d %s -D language=%s -A language=%s, %s %s' % ( \
        options.html.sphinxbuildbin,      \
        options.html.builder,             \
        os.path.join(options.html.builddir, options.html.builder, "doctrees"), \
        options.setupstatic.lang,         \
        options.setupstatic.lang,         \
        options.html.sourcedir,   \
        os.path.join(options.html.builddir, options.html.builder, options.setupstatic.lang) ))


