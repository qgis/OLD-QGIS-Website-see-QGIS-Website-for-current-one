.. _coding_standards:

QGIS Coding Standards
=====================


These standards should be followed by all QGIS developers.

Classes
-------


Names
.....

Class in QGIS begin with Qgs and are formed using camel case.

Examples:

* ``QgsPoint``
* ``QgsMapCanvas``
* ``QgsRasterLayer``


Members
.......


Class member names begin with a lower case m and are formed using mixed
case.

* ``mMapCanvas``
* ``mCurrentExtent``

All class members should be private.
Public class members are STRONGLY discouraged


Accessor Functions
..................


Class member values should be obtained through accesssor functions. The
function should be named without a get prefix. Accessor functions for the
two private members above would be:

* ``mapCanvas()``
* ``currentExtent()``


Functions
.........


Function names begin with a lowercase letter and are formed using mixed case.
The function name should convey something about the purpose of the function.

* ``updateMapExtent()``
* ``setUserOptions()``

Qt Designer
-----------

Generated Classes
.................

QGIS classes that are generated from Qt Designer (ui) files should have a
Base suffix. This identifies the class as a generated base class.

Examples:

* ``QgsPluginManagerBase``
* ``QgsUserOptionsBase``


Dialogs
.......

All dialogs should implement the following:

* Tooltip help for all toolbar icons and other relevant widgets
* WhatsThis help for all widgets on the dialog
* An optional (though highly recommended) context sensitive Help button
   that directs the user to the appropriate help page by launching their web
   browser

C++ Files
---------

Names
.....

C++ implementation and header files should have a .cpp and .h extension
respectively. Filename should be all lowercase and, in the case of classes,
match the class name.

Example:
Class ``QgsFeatureAttribute`` source files are
``qgsfeatureattribute.cpp`` and ``qgsfeatureattribute.h``

.. note:: In case it is not clear from the statement above, for a filename
  to match a class name it implicitly means that each class should be declared
  and implemented in its own file. This makes it much easier for newcomers to
  identify where the code is relating to specific class.


Standard Header and License
...........................

Each source file should contain a header section patterned after the following
example:

.. code-block:: cpp

  /***************************************************************************
    qgsfield.cpp - Describes a field in a layer or table
    --------------------------------------
    Date : 01-Jan-2004
    Copyright: (C) 2004 by Gary E.Sherman
    Email: sherman at mrcc.com
  /***************************************************************************
   *
   * This program is free software; you can redistribute it and/or modify
   * it under the terms of the GNU General Public License as published by
   * the Free Software Foundation; either version 2 of the License, or
   * (at your option) any later version.
   *
   ***************************************************************************/

.. note:: There is a template for Qt Creator in git. To use it, copy it from
  ``doc/qt_creator_license_template`` to a local location, adjust the
  mail address and - if required - the name and configure QtCreator to use it:
  ``Tools`` -> ``Options`` -> ``C++`` -> ``File Naming``.

Keyword Substitution
....................

In the days of SVN we used to require that each source file should contain the
``$Id$`` keyword. Keyword substitution is not supported by GIT and so should no
longer be used.

Variable Names
--------------

Variable names begin with a lower case letter and are formed using mixed case.

Examples:

* ``mapCanvas``
* ``currentExtent``


Enumerated Types
----------------

Enumerated types should be named in CamelCase with a leading capital e.g.:

.. code-block:: cpp

  enum UnitType
  {
    Meters,
    Feet,
    Degrees,
    UnknownUnit
  };

Do not use generic type names that will conflict with other types. e.g. use
``UnkownUnit`` rather than ``Unknown``

Global Constants & Macros
--------------------------

Global constants and macros should be written in upper case underscore separated e.g.:

.. code-block:: cpp

  const long GEOCRS_ID = 3344;

Editing
-------

Any text editor/IDE can be used to edit QGIS code, providing the following
requirements are met.

Tabs
....

Set your editor to emulate tabs with spaces. Tab spacing should be set to 2
spaces.

.. note:: In vim this is done with ``set expandtab ts=2``

Indentation
...........

Source code should be indented to improve readability. There is a
``scripts/prepare-commit.sh`` that looks up the changed files and reindents them
using astyle. This should be run before committing. You can also use
``scripts/astyle.sh`` to indent individual files.

As newer versions of astyle indent differently than the version used to do a
complete reindentation of the source, the script uses an old astyle version,
that we include in our repository (enable WITH_ASTYLE in cmake to include it in
the build).

Braces
......

Braces should start on the line following the expression:

.. code-block:: cpp

  if(foo == 1)
  {
    // do stuff
    ...
  }
  else
  {
    // do something else
    ...
  }

API Compatibility
-----------------

There is `API documentation <http://qgis.org/api/>`_ for C++.

We try to keep the API stable and backwards compatible. Cleanups to the API
should be done in a manner similar to the Trolltech developers e.g.

.. code-block:: cpp

  class Foo
  {
    public:
      /** This method will be deprecated, you are encouraged to use
       *  doSomethingBetter() rather.
       *  @deprecated doSomethingBetter()
       */
      Q_DECL_DEPRECATED bool doSomething();

      /** Does something a better way.
       *  @note added in 1.1
       */
      bool doSomethingBetter();

    signals:
      /** This signal will be deprecated, you are encouraged to
       *  connect to somethingHappenedBetter() rather.
       * @deprecated use somethingHappenedBetter()
       */
  #ifndef Q_MOC_RUN
      Q_DECL_DEPRECATED
  #endif
      bool somethingHappened();

      /** Something happened
       *  @note added in 1.1
       */
      bool somethingHappenedBetter();
  }

Coding Style
------------


Here are described some programming hints and tips that will hopefully reduce
errors, development time and maintenance.


Where-ever Possible Generalize Code
...................................


If you are cut-n-pasting code, or otherwise writing the same thing more than
once, consider consolidating the code into a single function.

This will:

- allow changes to be made in one location instead of in multiple places
- help prevent code bloat
- make it more difficult for multiple copies to evolve differences over time,
  thus making it harder to understand and maintain for others


Prefer Having Constants First in Predicates
...........................................

Prefer to put constants first in predicates.

``0 == value`` instead of ``value == 0``

This will help prevent programmers from accidentally using ``=`` when they meant
to use ``==``, which can introduce very subtle logic bugs.The compiler will
generate an error if you accidentally use ``=`` instead of ``==`` for comparisons
since constants inherently cannot be assigned values.

Whitespace Can Be Your Friend
.............................

Adding spaces between operators, statements, and functions makes it easier for
humans to parse code.

Which is easier to read, this:

.. code-block:: cpp

  if (!a&&b)

or this:

.. code-block:: cpp

  if ( ! a && b )

.. note:: ``scripts/prepare-commit.sh`` will take care of this.


Use Braces Even for Single Line Statements
..........................................

Using braces for code in if/then blocks or similar code structures even for
single line statements means that adding another statement is less likely to
generate broken code.

Consider:

.. code-block:: cpp

  if (foo)
    bar();
  else
    baz();

Adding code after bar() or baz() without adding enclosing braces would create
broken code. Though most programmers would naturally do that, some may forget
to do so in haste.

So, prefer this:

.. code-block:: cpp

  if (foo)
  {
    bar();
  }
  else
  {
    baz();
  }


Book recommendations
....................


- `Effective C++ <http://www.awprofessional.com/title/0321334876>`_, Scott Meyers
- `More Effective C++ <http://www.awprofessional.com/bookstore/product.asp?isbn=020163371X&rl=1>`_, Scott Meyers
- `Effective STL <http://www.awprofessional.com/title/0201749629>`_, Scott Meyers
- `Design Patterns <http://www.awprofessional.com/title/0201634988>`_, GoF

You should also really read this article from Qt Quarterly on
`designing Qt style (APIs) <http://doc.trolltech.com/qq/qq13-apis.html>`_


Credits for contributions
-------------------------

Contributors of new functions are encouraged to let people know about their contribution by:

* adding a note to the changelog for the first version where 
  the code has been incorporated, of the type::

    This feature was funded by: Olmiomland http://olmiomland.ol
    This feature was developed by: Chuck Norris http://chucknorris.kr

* writing an article about the new feature on a blog, 
  and add it to the QGIS planet http://plugins.qgis.org/planet/
* adding their name to:

  * https://github.com/qgis/QGIS/blob/master/doc/CONTRIBUTORS
  * https://github.com/qgis/QGIS/blob/master/doc/AUTHORS
  * https://github.com/qgis/QGIS/blob/master/doc/contributors.json
  
  
