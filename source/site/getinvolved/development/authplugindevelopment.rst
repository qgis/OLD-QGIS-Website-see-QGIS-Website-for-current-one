
.. _Authentication_Plugin_Development:

Authentication Plugin Development
=================================

User reference of the Authentication infrastructure can be read
in the `User Manual Auth overview </static/user_manual/auth_overview>`_

This chapter describes the way to create a plugin for the Authentication system
from a developer perspective.

.. _Authentication_Plugin_Development_glossary:

Glossary
--------
Here are some definition of the most common objects treated in this chapter.

.. glossary::

  Authentication Manager
    The QGIS component responsible to centralize and manage credential management
    for all protocols and providers that needs to have setup a secure connection.

  Master Password
    Password to allow access and decrypt credential stored in the QGIS
    Authentication DB

  Authentication Database
    A :term:`Master Password` crypted sqlite db ``<user home>/.qgis2/qgis-auth.db``
    where :term:`Authentication Configuration` are stored. e.g user/password,
    personal certificates and keys, Certificate Authorities

  Authentication DB
    :term:`Authentication Database`

  Authentication Configuration
    A set of authentication data depending on :term:`Authentication Method`.
    e.g Basic authentication method stores the couple of user/password.

  Authentication config
    :term:`Authentication Configuration`

  Authentication Method
    A specific method used to get authenticated. Each method has it's own
    protocol used to gain the authenticated level. Each method is implemented
    as shared library loaded dynamically during QGIS authentication
    infrastructure init.



.. _Create_a_new_HTTP_Auth_method:

Create a new HTTP Auth method
-----------------------------
There are many :term:`Authentication Method`\s and more will be developed. New
QGIS Auth methods can be developed to fulfill new ways to get authenticated. This
paragraph gives some hints on how to create a new QGIS Authentication plugin.
Authentication plugins are C++ plugins and can't be developed using Python.
The main reason is to avoid to dynamic override of auth methods that can introduce
security issues.

.. _Where_Auth_methods_are_located:

Where Auth methods are located
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All :term:`Authentication Method`\s are loaded dynamically during the
:term:`Authentication Manager` initialization at QGIS startup. A new build is not
necessary to add or remove a new Authentication method, they are shared library
(.so, dll) installed in the following paths:

* UNIX/Mac: :file:<installation path>/lib/qgis/plugins/
* Windows: :file:C:\OSGeo4W\apps\qgis\plugins

.. _Base_classes:

Base classes
^^^^^^^^^^^^
Any :term:`Authentication Method` is composed by two classes, `QgsAuthMethodEdit <https://qgis.org/api/classQgsAuthMethodEdit.html>`_
defining the Authentication parameters and how to edit them, and `QgsAuthMethod <https://qgis.org/api/classQgsAuthMethod.html>`_
that define how ``AuthCfg`` is managed during URI expansion.
Both classes define pure virtual methods that have to be implemented to produce
a complete and working Authentication method.

QgsAuthMethodEdit
"""""""""""""""""
Any new :term:`Authentication Method` must define the map or
:term:`Authentication Method` parameters in:

::

  QgsStringMap QgsAuthMethodEdit::configMap()

with the corresponding method to load from AuthDb:

::

  QgsAuthMethodEdit::loadConfig(const QgsStringMap &configmap)

It is possibile to define a method delegating the validation of the
:term:`Authentication Method` parameters in:

::

  bool QgsAuthMethodEdit::validateConfig()

These methods are called by ``QgsAuthManager`` to parse and save authentication
parameters in the :term:`Authentication DB`.

Usually any ``QgsAuthMethodEdit`` subclass is also derived from a UI class that
defines the UI used to edit authentication parameters in the QGIS interface.
The UI is loaded dynamically during authentication methods registrations by
calling https://qgis.org/api/qgsauthconfigedit_8cpp_source.html#l00119

QgsAuthMethod
^^^^^^^^^^^^^
This class define which providers are supported defining them in the:

::

  QStringList QgsAuthMethod::supportedDataProviders()

and what Expansions with enum in:

::

  QgsAuthMethod::Expansions QgsAuthMethod::supportedExpansions()

Depending on which expansion are allowed, corresponding update methods should
also be implemented

  * `bool updateNetworkRequest( QNetworkRequest &request, const QString &authcfg, const QString &dataprovider = QString() )`
  * `bool updateNetworkReply( QNetworkReply *reply, const QString &authcfg, const QString &dataprovider = QString() )`
  * `bool updateDataSourceUriItems( QStringList &connectionItems, const QString &authcfg, const QString &dataprovider = QString() )`

.. _Practical_examples:

Practical examples
^^^^^^^^^^^^^^^^^^
Practical examples can be find in some method implementations listed
`here <https://github.com/qgis/QGIS/tree/master/src/auth>`_
