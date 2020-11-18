Supported Lookups
=================

  .. note::

    The lookups are all case insensitive.

  .. note::

    Custom lookups are not supported currently.

Equals
******

Can be expressed as :code:`is`, :code:`equals` or :code:`=`, and means a case insensitive equality check. Can be negated as :code:`is not`, :code:`not equals` or :code:`!=` respectively.

Contains
********

Can be expressed as :code:`contains`, and means a case insensitive check. Can be negated as :code:`do(es) not contain`.

Regex
*****

Can be expressed as :code:`matches`, and means a case insensitive regular expression match. Can be negated as :code:`do(es) not match`.

In
***

Can be expressed as :code:`in`, and means a case sensitive equality check against the given list of values. Can be negated as :code:`not in`.

Greater than (or equal)
***********************

Can be expressed as :code:`>` and :code:`>=`, and means a comparison against the given value.

Lower than (or equal)
***********************

Can be expressed as :code:`<` and :code:`<=`, and means a comparison against the given value.
