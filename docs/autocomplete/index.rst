.. _autocomplete-guide:

Autocomplete Guide
==================

.. note::

  There is a demo/test app, where you can play around with the autocomplete feature. Just run
  ``python manage.py runserver`` after checking out this repository and go to
  ``http://localhost:8000``.

Setup
-----

Two things are required for the autocomplete functionality. First make sure, that the schema views
are added to your ``urls.py`` file.

.. code-block:: python
  :linenos:

  # urls.py
  urlpatterns = [
    path("schemas/", include("django_nlf.schema.urls")),
  ]

And then you need the client functionality, which you can get multiple ways depending on what you need.

Template tags
_____________

There are two template tags available, one to add an input with the autocomplete functionality and
one to include the Javascript files only.

.. autofunction:: django_nlf.templatetags.nlf_autocomplete.nlf_autocomplete

.. autofunction:: django_nlf.templatetags.nlf_autocomplete_js.nlf_autocomplete_js


.. _spa-integration:

SPA integration
_______________


See also
--------

.. toctree::
   :maxdepth: 1

   customization.rst
