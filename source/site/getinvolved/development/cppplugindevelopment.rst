
.. _QGIS-cpp-plugin-development:

Developing C++ plugins
----------------------

Preparing the Environment and Setting up the Repo

Go to the QGIS repository in Github at https://github.com/qgis/QGIS/
Make a Fork for yourself. Learn more about forking and keeping your repo in sync with the main development repo at http://help.github.com/fork-a-repo/
Clone your personal copy of the repository to your system, and add upstream as mentioned in above provided link
Read the https://github.com/qgis/QGIS/blob/master/INSTALL about setting up the installation environment and make a compilation with ccache enabled.

Setting up the Plugin Directory

Inside the QGIS folder::

 cd src/plugins/
 python plugin_builder.py


Now follow the instructions in the screen wizard to create a folder for your plugin. 
After the required input is given, a folder for the plugin is created. 
Read the README inside the plugin folder to create a plugin.

Building QGIS now will also build your plugin. After starting QGIS enable the plugin to see it and show it's dialog.
