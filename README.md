QGIS-Website
============

[![HTML Build](https://github.com/qgis/QGIS-Website/workflows/HTML%20build/badge.svg?branch=master)](https://github.com/qgis/QGIS-Website/actions?query=branch%3Amaster+workflow%3A%22HTML+build%22)
[![Build Status](https://travis-ci.org/qgis/QGIS-Website.svg?branch=master)](https://travis-ci.org/qgis/QGIS-Website)

Website is a static generated website using Sphinx (http://sphinx-doc.org/), 
based on restructured text sources (rst: http://docutils.sourceforge.net/rst.html)
and html (jinja2) templates.

Most sources are in source/site. Only frontpage and landing pages are in theme/qgis-theme

Styling is in theme/qgis-theme. This theme is used for website and documentation builds. 
The Website version is the canonical one.


Building the website using Docker
---------------------------------

TLDR: `cd QGIS-Website && ./docker-run.sh html `

Note: you will use a QGIS docker image from hub.docker.com, created with the dockerfile from: 

https://github.com/qgis/QGIS-Sysadmin/blob/master/docker/sphinx/Dockerfile-html

First: install Docker.

On Linux: use your package manager.

On Windows: install boot2docker from: http://boot2docker.io/
Some notes: you need admin rights to do this: the install script will generate some keys, just accept all defaults.
If it does not work the first time, check if you need to 'enable virtualization' in your BIOS (eg Lenovo disables it by default).

Start a command box (on Windows: double click the boot2docker icon on desktop, you will get a terminal):

Verify that Docker/Boot2docker is working by typing:

    docker run hello-world
  
If all goes ok, it will download a small Docker image and you will have an output like this:

    richard@kwik~$ docker run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from hello-world
    ....
    Hello from Docker.
    This message shows that your installation appears to be working correctly.

Now we are going to create a working directory and pull the sources from github,
either your own fork or the original QGIS repo like here:

    # cd to your home dir
    cd
    # create a dev dir and move into it
    mkdir dev
    cd dev
    # clone/copy the sources into it and go into the dir
    git clone git@github.com:qgis/QGIS-Website.git
    cd QGIS-Website
    # check your current path
    pwd
    # ^^^ that shows your current path, with me on Linux it is:
    /home/richard/dev/QGIS-Website
    # on Win7 and Win8 I had:
    /c/Users/richard/dev/QGIS-Website
 
We are now going to use that QGIS-Website directory as the source and output directory for the 
Docker 'virtual machine' that will build the site.
We will start this Docker container with a command line like below:

    docker run -t -i -v /home/richard/dev/QGIS-Website:/QGIS-Website -w=/QGIS-Website --rm=true qgis/sphinx_html_3 make html
 
Where "docker run -t -i qgis/sphinx_html_3 make html" means: "run a Docker container/process based on the qgis/sphinx_html_3 image available online, call make in the working directory of the container, with parameter 'html', meaning: only build english html"

"-v /home/richard/dev/QGIS-Website:/QGIS-Website" means: use the directory "/home/richard/dev/QGIS-Website" as a virtual directory in the container and name it '/QGIS-Website'
  
"-w=/QGIS-Website" means that it is to be used as the working dir of Docker

"--rm=true" means remove the container after the build

Now the actual command lines:

On linux (use your own repo path here!):

    # english html
    docker run -t -i -v /home/richard/dev/QGIS-Website:/QGIS-Website -w=/QGIS-Website --rm=true qgis/sphinx_html_3 make html

On windows (tested on Win7 and Win8), use your own repo path here!

IMPORTANT you need 2x a double // in the command !!!   Without it you will get an error message about a wrong working directory:

    docker run -t -i -v //c/Users/richard/dev/QGIS-Website:/QGIS-Website -w=//QGIS-Website --rm=true qgis/sphinx_html_3 make html

Note: only the first time it will pull the qgis/sphinx_html_3 image (>300Mb) from the online repository https://hub.docker.com/u/qgis/

Now if you want to build a translated website, there is some more work to do. We have to pull the translations from transifex etc. You need your own transifex credentials to do this. So first get an account/password at www.transifex.com and then create a so-called '.transifexrc' file which is used to authorize you at transifex.
The contents of this file should be like this:

    [https://www.transifex.com]
    hostname = https://www.transifex.com
    password = yourpasswordhere
    token = 
    username = yourusernamehere

Copy this file to the root of your repo. With me, that is /home/richard/dev/QGIS-Website. NOW you can run it using 'make full' and a LANG parameter like this:

    # french html (linux)
    docker run -t -i -v /home/richard/dev/QGIS-Website:/QGIS-Website -w=/QGIS-Website --rm=true qgis/sphinx_html_3 make full LANG=fr

Besides this, you can also have a look into the scripts docker-run.sh and docker-world.sh which are used on our own webservers.

Building the website using Make
-------------------------------

Building is only tested on Linux systems using make, on windows we now started a Paver setup (see below)

To be able to run localisation targets you will need Sphinx 1.2 which comes with pip. 
Sphinx coming with most distro's is just 1.1.3. You will get a gettext error with those.

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

You can install all tools on go via the REQUIREMENTS.txt here at the root of this repo:

    pip install -r REQUIREMENTS.txt

Alternatively, do it one by one:

Install sphinx 1.2 now in your virtual env:

    pip install sphinx==1.2

Sphinx-intl extension ( https://pypi.python.org/pypi/sphinx-intl ):

    pip install sphinx-intl

Then build:

    make html (to build the english language)
    make LANG=nl html (to build the dutch version)

If you want add the QGIS-Documentation docs into the build, you either need to manually copy the sources, resources 
and po files into the website project. Or use the fullhtml target of make (which will checkout the 2.0 branch):

    # to build english:
    make fullhtml
    # to build eg dutch:
    make LANG=nl fullhtml

To gather new strings in a pot (.po) file for your language, and merge them with 
excisting translations in the po files (normally to be ran by your language maintainer):

    make pretranslate LANG=xx  # where xx is your language code

To add a new language (the scripts will need some directory structure):

    make createlang LANG=xx

See the website in action: http://www.qgis.org


Building the website using Paver
--------------------------------

Paver is a python based Make-like tool (http://paver.github.io/paver/)

Paver can be used on Linux and Windows (somebody can test on OSX?)

There are two scripts available:

- bootstrap.py (for setting up the python related stuff)
- pavement.py (the config file for Paver)

General use:

    # first let bootstrap.py install all stuff    
    python bootstrap.py
    
    # if the script is complaining about easysetup missing:
    # download: https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    # and install that first:
    python ez_setup.py

    # after succesfull running of bootstrap.py you have all wheels on place, the script has created a virtual
    environment (called "virtualenv") with all Sphinx related python machinery. Now, each time you want to build,
    you just need to:
    # 1) activate a virtual environment with all Sphinx related python machinery
    # 2) run the actual script to build the website
    
    # to go into the virtual environment:
    # on Windows:
    virtualenv\Scripts\activate
    # on Linux:
    source virtualenv/bin/activate
    
    # now build (only website, no included Documentation yet):
    # eg english only:
    paver html

To be able to build localized versions of the Website with paver the
'Transifex-client (tx)' is needed.

On linux, install with::

	# note that we use a slightly older version of tx
	pip install transifex-client==0.9
	
On Windows, you should download it from: http://files.transifex.com/transifex-client/0.10/tx.exe
see http://support.transifex.com/customer/portal/articles/998120-client-on-windows	

To make tx.exe usable in the paver script, either put it IN this directory next to the pavement.py file, OR add it to your PATH

IMPORTANT: to be able to pull from transifex.com, you will need a credentials file. 
This file should be named: ``.transifexrc`` and easiest is to put it in your home dir C:/users/you. 
Another option is to put it in the root of this project, but be carefull to not put your credentials in Github :-)

The file should contain this::

	[https://www.transifex.com]
	hostname = https://www.transifex.com
	password = yourtransifexpassword
	token = 
	username = yourtransifexusername

With a working tx and a .transifexrc, you should be able to build for example the german version of docs via::	

    # german:
    paver html -l de
    
During the build you will see this command::

	tx pull --minimum-perc=1 --skip -f -l de
	
This will pull all german po files from transifex (based on the .tx/config file in the root of this project)




Styling the website
-------------------

Most javascript and css is in theme/qgis-style/ files.

theme/qgis-style/qgis-style.css is based on Less (see http://lesscss.org/ )

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
    
