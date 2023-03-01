<img src="https://github.com/qgis/QGIS/blob/master/images/README-md/main_logo.png" width="300" alt="Our full logo">

[![HTML Build](https://github.com/qgis/QGIS-Website/workflows/HTML%20build/badge.svg?branch=master)](https://github.com/qgis/QGIS-Website/actions?query=branch%3Amaster+workflow%3A%22HTML+build%22)

This repository is meant to manage the [Official website of QGIS](https://qgis.org),
a free and Open Source Geographic Information System (GIS) Software, under the
[Open Source Geospatial (OSGeo)](https://www.osgeo.org) foundation umbrella.


<!-- TOC generated with https://freelance-tech-writer.github.io/table-of-contents-generator/index.html -->

* [Development (Quick Start)](#development-quick-start)
* [Building the website using Docker](#building-the-website-using-docker)
* [Building the website using Make](#building-the-website-using-make)
   * [Build on macOS or Linux](#build-on-macos-or-linux)
   * [Build on Windows](#build-on-windows)
* [Translating](#translating)
* [Styling the website](#styling-the-website)
* [Publishing safely using rsync](#publishing-safely-using-rsync)
   * [Server configuration](#server-configuration)


QGIS Website is a static generated website using [Sphinx](http://sphinx-doc.org/),
based on [restructured text sources (rst)](http://docutils.sourceforge.net/rst.html)
and html (jinja2) templates.

Most sources are in source/site. Only front page and landing pages are in themes/qgis-theme.
Styling is in themes/qgis-theme.


> **Note:** The notes provided here are for manual setup, push and publish of the web site. As of QGIS Hackfest 24 in Florence, Italy, August 2022, we also have GitHub workflow automation. Please see the [./github/workflows](./github/workflows) folder for insight into the process used. Also see the [Publishing safely using rsync](#publishing-safely-using-rsync) section further down in this document for notes on how to set up the server to receive the docs.


##  Development (Quick Start)

```
# move into the dir of this repo:
cd QGIS-Website
# perform the actualy building of the html (using our 'qgis/sphinx_html_3' image)
docker run -t -i -v `pwd`:/QGIS-Website -w=/QGIS-Website --rm=true qgis/sphinx_html_3 make html
# now serve the output of the build on port 80 (usign nginx image) so you can view it in your browser
docker run -p 80:80 -v `pwd`/output/html:/usr/share/nginx/html nginx
# open it in your browser:
open http://localhost/en/site/
#  (make sure there is not another webserver running on port 80, if so change to another port in the nginx start above, eg 8000 and then use http://localhost:8000/en/site)
```

## Building the website using Docker

TLDR: `cd QGIS-Website && ./docker-run.sh html`

Note: you will use a QGIS docker image from hub.docker.com, created with the dockerfile from:

https://github.com/qgis/QGIS-Sysadmin/blob/master/docker/sphinx/Dockerfile-html

First: install Docker.

On Linux: use your package manager.

On Windows: install boot2docker from: https://boot2docker.io/
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
    rest_hostname = https://rest.api.transifex.com
    token = yourtransifextoken

Copy this file to the root of your repo. With me, that is /home/richard/dev/QGIS-Website. NOW you can run it using 'make full' and a LANG parameter like this:

    # french html (linux)
    docker run -t -i -v /home/richard/dev/QGIS-Website:/QGIS-Website -w=/QGIS-Website --rm=true qgis/sphinx_html_3 make full LANG=fr

Besides this, you can also have a look into the scripts docker-run.sh and docker-world.sh which are used on our own webservers.



## Building the website using Make

1. If not provided by your OS, you need to install:

   - [git](https://git-scm.com/download/)
   - and [Python3](https://www.python.org/downloads/)

   You can install both in default places and with default options.
1. [Clone the repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
1. Go into that directory and follow the next instructions depending on your OS.

The best way to build the website is within a Python Virtual Environment (venv).

### Build on macOS or Linux

1. You can create your own virtual env:
   ```
   # you NEED python >3.6. Depending on distro either use `python3` or `python`
   # common name is 'venv' but call it whatever you like

   python3 -m venv venv  # using the venv module, create a venv named 'venv'
   ```
1. Then activate the venv:
   ```
   source ./venv/bin/activate
   ```
   With 'activated' virtual environment, you should see 'venv' in the prompt.
1. Install the requirements via the REQUIREMENTS.txt:
   ```
   pip install -r REQUIREMENTS.txt
   ```
1. And run the build from within that venv:
   ```
   make html
   ```
   Want to build your own language? Note that you will use the translations from the .po files
   in the `i18n` folder within the repository! For example for 'nl' do:
   ```
   make LANG=nl html
   ```

### Build on Windows

1. Create a virtual environment called 'venv' in that directory (search the Internet for Python Virtual
   Env on Windows for more details), but in short: use the module 'venv' to create a virtual environment called 'venv'
   ```
   # in dos box:
   python -m venv venv
   ```
1. Then activate the venv:
   ```
   venv\Scripts\activate.bat
   ```
   With 'activated' virtualenv, you should see 'venv' in the prompt.
1. Install the requirements via the REQUIREMENTS.txt:
   ```
   pip install -r REQUIREMENTS.txt
   ```
1. And run the build from within that venv, using the make.bat script with the html argument to locally build the docs:
   ```
   make.bat html
   ```
   Want to build your own language? Note that you will use the translations from the .po files
   in the `i18n` folder within the repository! For example for 'nl' do:
   ```
   set SPHINXOPTS=-D language=nl
   make.bat html
   ```

## Translating

We rely on the [Transifex platform](https://transifex.com) to store and coordinate
our translation efforts. To be part of the translation team, please follow
[becoming a translator](https://www.qgis.org/en/site/getinvolved/translate.html#becoming-a-translator).

New English strings in the repository are automatically pushed and made available on Transifex platform
thanks to the [tx_push](.github/tx_push.yml) Github action.
This action also calls the [create_transifex_resources](scripts/create_transifex_resources.sh) script
ensuring that the Transifex [configuration file](.tx/config) is always up to date.

Translated strings are pulled from Transifex to our servers as part of the daily build process
(see [Makefile](Makefile) `full` rule).


Sometimes, the process may fail or you may want to build the site locally with new strings in translated language.
In this case, you need to manually pull the translations from Transifex to your local repository:

1. Checkout locally the repository and target branch in git
1. Prepare the environment
   ```
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r REQUIREMENTS.txt
   ```
1. Install [Transifex command line client](https://github.com/transifex/cli/)
   ```
   curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | bash
   ```
1. To gather new strings in a pot (.po) file for your language, and merge them with
   existing translations in the po files (**normally to be run by your language maintainer**):
    ```
    make pretranslate LANG=xx  # where xx is your language code
    ```
1. To add a new language (the scripts will need some directory structure):
    ```
    make createlang LANG=xx
    ```
1. Download the translated strings with commands in the Makefile.
   By default this pulls all the languages.
   ```
   # --minimum-perc=1 so only files which have at least 1% translation are pulled
   # -f to force, --skip to not stop with errors
   tx pull --minimum-perc=1 --skip -f
   ```
   To pull a specific language (e.g. italian), do
   ```
   tx pull --minimum-perc=1 --skip -f -l it
   ```

   IMPORTANT: to be able to pull from transifex.com, you will need a credentials file.
   This file should be named: ``.transifexrc`` and easiest is to put it in your home dir.
   The file should contain this:
   ```
   [https://www.transifex.com]
   rest_hostname = https://rest.api.transifex.com
   token = yourtransifextoken
   ```
1. Build the docs in your language
   ```
   make html LANG=yourlanguage
   ```
1. Share the changes by opening a pull-request, allowing us to integrate
   the new strings for the pulled language(s)


## Styling the website

Most javascript and css is in theme/qgis-style/ files.

theme/qgis-style/qgis-style.css is based on Less (see http://lesscss.org/ )

To make changes to CSS on MacOSX

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


## Publishing safely using rsync

In this section we describe how you can set up a small cloud server to receive the static content produced by sphinx, suitable for publishing on the internet.

### Server configuration

We use a CX11 Hetzner cloud machine configured with an external volume as per the image below:

![image](https://user-images.githubusercontent.com/178003/185931856-f3e9abef-cb4e-4df7-94f9-73fe810b8db6.png)

Using the external volume allows us to grow the disk without needing to upgrade the server itself.

The configuration of this server is simple: We set up a non-privaledged user that is only allowed to rsync files to a specific directory. In the steps below we show the process for doing this.

```
useradd runner -m -d /home/runner
su - runner
mkdir .ssh
chmod 0600 .ssh
cd .ssh/
rm id_rsa*
echo 'command="/usr/bin/rrsync -wo /mnt/HC_Volume_22264126" ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDAca8gta0y4esFE8Ro9nq9uOPWvd9+M7kK9DZ84tIxI runner@qgis' > authorized_keys
chmod 0600 authorized_keys
exit
chown runner /mnt/HC_Volume_22264126
```

Then the Github action worker is set up to upload files to /mnt/HC_Volume_22264126 - see the [./github/workflows](./github/workflows) for details.

Next we need to harden the server a little and set up NGINX to publish the files that are pushed to the HC_Volume_22264126 folder.

```
echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
systemctl restart sshd
# installed by default on newer ubuntu distro versions
apt install unattended-upgrades
apt install fail2ban
# Install crowdsec host protection
curl -s https://packagecloud.io/install/repositories/crowdsec/crowdsec/script.deb.sh | sudo bash
apt-get install crowdsec
apt install nginx
vim /etc/nginx/sites-enabled/default.conf
```

Now change the site root to use the volume directory.

```
root /mnt/HC_Volume_22264126;
```

Then restart nginx and push a little temp folder to test with:

```
systemctl restart nginx
su - runner -c "echo 'hi' > /mnt/HC_Volume_22264126/index.html"
```

Now in cloudflare create a DNS entry. For testing we create a new subdomain, but ultimately you should create it in the root domain:

![image](https://user-images.githubusercontent.com/178003/185939581-9f01123f-12ba-4b6c-8f41-305dc98b581f.png)

You will see our site is not yet secure:

![image](https://user-images.githubusercontent.com/178003/185940833-a242e75a-1d73-4d04-bb36-952d24c36b4a.png)

So we set up certbos:

Next get a Letsencrypt certificate for the site:
`
```
apt install snapd
snap install core; snap refresh core
snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```

Then open the site in your browser to test:

![image](https://user-images.githubusercontent.com/178003/185943941-86c3e444-ed49-4c58-bf42-5e39b8fe9e68.png)
