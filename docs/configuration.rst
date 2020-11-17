.. _configuration:

Configuration
=============

Here is a list of all available settings of django-nlf and their default values. All settings are prefixed with ``NLF_``.

NLF_QUERY_PARAM
***************

Default: ``"q"``

This applies to the Django RESTFramework Backend. This parameter is used for extracting the filter expression from the ``GET`` query parameters.

NLF_PATH_SEPARATOR
******************

Default: ``"."``

The character that separates path elements for fields. Used when applying filter following Foreign Key or Many-to-Many relations.

NLF_EMPTY_VALUE
***************

Default: ``"EMPTY"``

The string that is translated to a lookup with the ``NULL`` database value.
