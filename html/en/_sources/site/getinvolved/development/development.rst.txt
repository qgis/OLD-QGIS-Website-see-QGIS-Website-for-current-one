
.. _developing_qgis:

*********************
 Development in QGIS
*********************

Core Development
=================

QGIS is an Open Source Geographic Information System that currently runs on
most Unix platforms (macOS/OS X included) and Windows. Developed using the Qt
toolkit (https://www.qt.io), it's mainly written in C++ and Python languages.
This means that QGIS feels snappy to use and has a pleasing, easy to use
graphical user interface.

QGIS source code is available at https://github.com/qgis/QGIS.
If you wish to help on bug fixing or adding new features to the application,
you are most welcome and can freely contribute via pull requests. You can also
get in touch with the other developers through their mailing list at
https://lists.osgeo.org/mailman/listinfo/qgis-developer.

Beside this, we've written a short **QGIS Developers Guide** to help you in
QGIS coding. It provides rules, tools and steps to easily and efficiently
contribute to QGIS code and is available at https://docs.qgis.org.
You are warmly encouraged to read it.

Plugin Development
===================

QGIS has a plugin infrastructure. You can add a lot of new functionality by
writing your own plugins. These plugins can either be written in C++ or in Python.

If you want to contribute to QGIS Project with your plugin, it's highly
recommended to read the **QGIS Developers Guide** at our documentation
website: https://docs.qgis.org


.. _QGIS-cpp-plugin-development:

Developing C++ Plugin
---------------------

Preparing the Environment and Setting up the Repo
.................................................

#. Go to the QGIS repository in GitHub at https://github.com/qgis/QGIS/
#. Make a Fork for yourself. Learn more about forking and keeping your repo in sync 
   with the main development repo at http://help.github.com/fork-a-repo/
#. Clone your personal copy of the repository to your system, and 
   add upstream as mentioned in above provided link
#. Read the https://github.com/qgis/QGIS/blob/master/INSTALL.md about setting up
   the installation environment and make a compilation with ccache enabled.

Setting up the Plugin Directory
...............................

Inside the QGIS folder::

 cd src/plugins/
 python plugin_builder.py


Now follow the instructions in the screen wizard to create a folder for your plugin. 
After the required input is given, a folder for the plugin is created. 
Read the README inside the plugin folder to create a plugin.

Building QGIS now will also build your plugin. After starting QGIS 
enable the plugin to see it and show its dialog.


.. _QGIS-python-plugin-development:

Developing Python plugin
------------------------

QGIS has a lot to offer to python developers too.

QGIS has python bindings so you can automate tasks in QGIS via python.
We provide a documentation for QGIS API at
https://qgis.org/pyqgis/

You can also have a look into the **Python Cookbook** in our Documentation site:
https://docs.qgis.org/

Particularly interested in python plugin development, you can find some instructions
at https://docs.qgis.org/latest/en/docs/pyqgis_developer_cookbook/plugins/index.html

Looking for examples of python plugins, see https://plugins.qgis.org

