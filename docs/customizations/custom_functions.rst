.. _custom-functions:

Writing your own function
=========================

To create your own custom function, you just need to register it. The first argument to :func:`nlf_function <functions.factory.nlf_function>` will determine how the function can be referenced in *filter expressions*, the role parameters determines where the function can be used, while the model parameter can be used to restrict usability to certain models.

See the following example:

.. code-block:: python

  from django_nlf.functions import nlf_function

  @nlf_function("myFunction")
  def my_function(*args, **kwargs):
    pass

The arguments are passed as strings as positional arguments, only quotes are removed. Additional context is available through key word arguments.

Currently the :class:`Model class <django:django.db.models.Model>` being filtered, the :class:`Request <drf:rest_framework.Request>` and the :class:`View <drf:rest_framework.views.View>` are passed as :code:`model`, :code:`request` and :code:`view` respectively.

Value functions
***************

If the function is used as a value, it can return anything appropriate for the field.

Field functions
***************

If the function is used as a field, it must return a dictionary with a single key, the field name, and an annotation. This can be an :class:`F object <django:django.db.models.F>`, :class:`Aggragation <django:django.db.models.Aggregate>`, :class:`Subquery <django:django.db.models.Subquery>` or even a :class:`Window <django:django.db.models.Window>`.

.. warning::

  Annotations are applied **BEFORE** all other filtering is done, therefore if you need to filter on a group, that must be handled as an expression function with a :class:`Subquery <django:django.db.models.Subquery>`.

Expression functions
********************

Expression functions are passed an additional keyword argument :code:`exclude` to specify if the function has been negated (:code:`exclude=True`) or not (:code:`exclude=False`). It must return a tuple of a dictionary holding annotations as for field functions and a :class:`Q object <django:django.db.models.Q>`.

.. warning::

  Annotations are applied **BEFORE** all other filtering is done, therefore if you need to filter on a group, that must be handled as an expression function with a :class:`Subquery <django:django.db.models.Subquery>`.
