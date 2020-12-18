.. _configuration:

Configuration
=============

Here is a list of all available settings of django-nlf and their default values. All settings are prefixed with ``NLF_``.

NLF_EMPTY_VALUE
***************

Default: ``"EMPTY"``

The string that is translated to a lookup with the ``NULL`` database value.

NLF_FALSE_VALUES
****************

Default: ``("0", "f")``

Used in boolean coercion to determine the boolean value of a string. If the first character of the value coerced to boolean matches any listed character, the value is considered ``False``, otherwise ``True``.

NLF_FIELD_NAME_CONVERTER
************************

Default: ``None``

A function or an import path to a function that applies a conversion to the field name. Can be used to automatically convert between cases, e.g. *camelCase* to *snake_case*.

One such converter function is readily available as ``django_nlf.utils.camel_to_snake_case``.

NLF_FIELD_SHORTCUTS
*******************

Default: ``{}``

A simple mapping of models and field name shortcuts to full field path. The key must be a model identifier in a form of ``app.Model`` and its value is mapping of shortcut to full path. The special key ``__all__`` applies to all models, and has a lower precedence. For example if you would like to identify you users by their username in the language for your model ``Article``, and you have an ``author`` field on your model (pointing to the Primary Key of the users), you can do the following:

.. code-block:: python

  NLF_FIELD_SHORTCUTS = {
      "blog.Article": {"author": "author.username"},  # Do this for shortcuts for a specific model
      "__all__": {}                                   # Do this for generic shortcuts, applicable to all models
  }

.. _path-separator:

NLF_PATH_SEPARATOR
******************

Default: ``"."``

The character that separates path elements for fields. Used when applying filter following Foreign Key or Many-to-Many relations.

NLF_QUERY_PARAM
***************

Default: ``"q"``

This applies to the Django RESTFramework Backend. This parameter is used for extracting the filter expression from the ``GET`` query parameters.


  "PATH_SEPARATOR": ".",
  "QUERY_PARAM": "q",
