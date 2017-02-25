

Plugin Development
===================

QGIS has a plugin infrastructure. You can add a lot of new functionality by
writing your own plugins. These plugins can either be written in C++ or in Python.

If you want to contribute to QGIS Project with your plugin, 
it's highly recommended to read :ref:`QGIS-Developers-Guide`


.. _QGIS-cpp-plugin-development:

Developing C++ Plugin
---------------------

Preparing the Environment and Setting up the Repo
.................................................

* Go to the QGIS repository in Github at https://github.com/qgis/QGIS/
* Make a Fork for yourself. Learn more about forking and keeping your repo in sync 
  with the main development repo at http://help.github.com/fork-a-repo/
* Clone your personal copy of the repository to your system, and 
  add upstream as mentioned in above provided link
* Read the https://github.com/qgis/QGIS/blob/master/INSTALL about setting up 
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


QGIS has a lot to offer for python developers too.

QGIS has python bindings so you can automate tasks in QGIS via python.

Interested in python plugin development, easiest way to start is using the Plugin Builder plugin in QGIS.
Search for 'Plugin Builder' in the plugin manager of QGIS, or read up here:
http://plugins.qgis.org/plugins/pluginbuilder/

You can also go to :ref:`QGIS-python-plugin-development`
or have a look into the Python Cookbook in our Documentation site: http://docs.qgis.org.

Looking for examples of python plugins, see http://plugins.qgis.org

You can find the QGIS-iface which you can use via python here:

http://qgis.org/api/classQgisInterface.html (for QGIS testing)

http://qgis.org/api/2.0/classQgisInterface.html (for QGIS 2.0)

http://qgis.org/api/1.8/classQgisInterface.html (for QGIS 1.8)



