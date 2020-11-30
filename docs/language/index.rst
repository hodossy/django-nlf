.. _language-reference:

Language Reference
==================

.. warning::

  This project is in development, please expect changes in the language syntax!

.. warning::

  Only the *a-z, A-Z, 0-9, '.', '_', '-', '/', ':'* characters are supported by the language right now.

Terminology
***********

The whole natural language expression, as a string, is referred to as *filter expression*. The atomic building blocks of the language are the *expressions* which can be composed via *operators* and grouped together to articulate the filtering criteria.

The most simple *expression* is of the following form:

  .. code-block:: python

    #<field name>  <lookup> <value>
    "title         contains science"

  .. note::

  	As a convenience, an expression targeting a boolean field can take the following form: :code:`"is archived"` or negated as :code:`"is not archived"`, where the last part is the field name.

Fields
------

All fields are available for a given model, including relationships as well. You can follow each path with the :ref:`path separator <path-separator>`, by default it looks like

  .. code-block:: python

    "author.username contains john"

Values
------

Values can be anything, but if you need whitespace in it, you must quote the value. For some *lookups*, a list of values can be defined as well. List of values are defined as a coma separated list within parenthesis. Regular expressions can be defined between two forward slashes.

  .. code-block:: python

    'title contains "science news"'
    "author.username is in (john, jane)"
    "payment_details matches /[\d]{4}(-[\d]{4}){3}/"

Complicating things
-------------------

These *expressions* can then be combined in any way with logical operators. The precedence of the operators are respected, i.e. *and* has higher precedence over *or*.

  .. code-block:: python

    "title contains science and published > 2020-01-01"

You can group these expressions as well:

  .. code-block:: python

    "title contains science and (author is john or published > 2020-01-01)"

  .. note::

    You can nest these groups as you like.

Advanced Use
------------

To express the most complicated filtering criteria, functions can be used in the language as an *expression* or a *value*.
On how to develop such functions, see the :ref:`Writing your own function Guide <custom-functions>`.

For example if we have an *articles* table for a science site, we could do the following, where :code:`hasBeenPeerReviewed()` hides a nasty join detail to check if a submitted paper has already been reviewed.

  .. code-block:: python

    "author is john and hasBeenPeerReviewed()"
    "published > startOfYear()"

See Also
--------

.. toctree::
   :maxdepth: 1

   lookups.rst
   operators.rst
   functions.rst
