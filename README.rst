core_module_chemical_composition_simple_app
===========================================

Chemical composition simple module for the parser core project.

Quick start
===========

1. Add "core_module_chemical_composition_simple_app" to your INSTALLED_APPS setting
-----------------------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_module_chemical_composition_simple_app',
    ]


2. Include the core_module_chemical_composition_simple_app URLconf in your project urls.py
------------------------------------------------------------------------------------------

.. code:: python

    url(r'^', include('core_module_chemical_composition_simple_app.urls')),