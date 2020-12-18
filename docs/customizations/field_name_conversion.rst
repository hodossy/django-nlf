Converting field names
======================

To support automatic case conversion, a custom implementation can be provided.

.. code-block:: python

  # app/utils.py
  def my_converter(field_name: str) -> str:
      # do something with field_name
      return field_name

and in ``settings.py``:

.. code-block:: python

  NLF_FIELD_NAME_CONVERTER = "app.utils.my_converter"
