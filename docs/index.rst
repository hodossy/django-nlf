.. Django Natural Language Filter documentation master file, created by
   sphinx-quickstart on Mon Nov 16 14:53:41 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Natural Language Filter's documentation!
==========================================================

Django NLF provides a simple and easy way to filter :class:`QuerySets <django.db.models.QuerySet>`. This natural language approach enables building nested complex queries quickly for your users, which are otherwise cumbersome with other libraries.

.. warning::

	This project is still in development, please use with this in mind!

Installation
************

Install using ``pip``,

.. code-block:: bash

  pip install django-nlf

Then you can use the ``DjangoNLFilter`` with a queryset and a string, containing the filter expression. Please see the :ref:`language-reference` for more details.

.. code-block:: python
  :linenos:

  from django_nlf import DjangoNLFilter
  from .models import Article

  nl_filter = DjangoNLFilter()
  qs = Article.objects.all()
  q = 'author.username is john or title ~ news'
  # equivalent to Article.objects.filter(Q(author__username="user") | Q(title__icontains="news"))
  articles = nl_filter.filter(qs, q)

  # Nested logical operators are also supported:
  q = 'author.username is john and (title ~ news or created_at <= 2020-06-05)'
  # equivalent to
  # Article.objects.filter(
  #   Q(author__username="user") & (Q(title__icontains="news") | Q(created_at__lte="2020-06-05"))
  # )
  articles = nl_filter.filter(qs, q)

Rest framework integration
**************************

You just need to simply add the natural language filter backend to your filter backends list.

.. code-block:: python

  REST_FRAMEWORK = {
    ...
    'DEFAULT_FILTER_BACKENDS': (
      'django_nlf.rest_framework.DjangoNLFilterBackend',
    ),
    ...
  }



.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :hidden:

   language.rst
   configuration.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
