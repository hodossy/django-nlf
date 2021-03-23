Converting field names
======================

You may not like the snake case convention widely used in Python to be used in the filtering expressions your users write. Therefore you can use one of the built-in case converters or write your own.

Built in converters
*******************

.. autofunction:: django_nlf.utils.camel_to_snake_case

Custom converter
****************

To support automatic case conversion, a custom implementation can be provided.

.. code-block:: python

  # app/utils.py
  def my_converter(field_name: str) -> str:
      # do something with field_name
      return field_name

and in ``settings.py``:

.. code-block:: python

  NLF_FIELD_NAME_CONVERTER = "app.utils.my_converter"
