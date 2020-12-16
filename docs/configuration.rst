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
