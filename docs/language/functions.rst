Available Functions
===================

Functions can be used in three ways: as a *field*, a *value* or a whole *expression*.

Date functions
**************

.. automodule:: django_nlf.functions.dates
    :members:

.. _custom-functions:

Writing your own function
*************************

To create your own custom function, you just need to register it. The first argument to :code:`nlf_function` will determine how the function can be referenced in *filter expressions*.

The arguments are passed as a strings as positional arguments, only quotes are removed. Additional context is available through key word arguments. Currently the :class:`Model class <django:django.db.models.Model>` being filtered is passed as :code:`model` and for value functions :code:`field_name` is passed as well.

If the function is used as a value, it can return anything appropriate for the field, but if it is used as and expression, it must return a :class:`Q object <django:django.db.models.Q>`.

Example #1
----------

.. literalinclude:: ../../django_nlf/functions/dates.py
  :language: python
  :emphasize-lines: 3,6
  :lines: 1-17
  :linenos:
