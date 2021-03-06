[![PyPi Version](https://img.shields.io/pypi/v/django-nlf)](https://pypi.org/project/django-nlf/)
[![PyPi Downloads](https://img.shields.io/pypi/dw/django-nlf)](https://pypi.org/project/django-nlf/)
![Tests](https://github.com/hodossy/django-nlf/workflows/Unit%20tests/badge.svg?branch=main)
![Weekly](https://github.com/hodossy/django-nlf/workflows/Weekly/badge.svg?branch=main)
[![Documentation](https://img.shields.io/readthedocs/django-nlf)](https://django-nlf.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/hodossy/django-nlf.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/hodossy/django-nlf/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/hodossy/django-nlf.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/hodossy/django-nlf/context:python)

# Django Natural Language Filter

Django NLF provides a simple and easy way to express complex filtering criteria with a filtering language as close to natural language as possible, while providing APIs to further customize the user experience.

## Installation

Install using `pip`,

```
pip install django-nlf
```

And add `django_nlf` to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    "django_nlf",
]
```

Then you can use the `DjangoNLFilter` with a queryset and a string, containing the filter expression. Please see the [Language Reference](https://django-nlf.readthedocs.io/en/stable/language/index.html) for more details.

```python
from django_nlf.filters import DjangoNLFilter
from .models import Article

nl_filter = DjangoNLFilter()
qs = Article.objects.all()
q = "author.username is john or title contains news"
# equivalent to Article.objects.filter(Q(author__username="john") | Q(title__icontains="news"))
articles = nl_filter.filter(qs, q)

# Nested logical operators are also supported:
q = "author.username is john and (title contains news or created_at <= 2020-06-05)"
# equivalent to
# Article.objects.filter(
#   Q(author__username="john") & (Q(title__icontains="news") | Q(created_at__lte="2020-06-05"))
# )
articles = nl_filter.filter(qs, q)
```

## Django REST framework integration

Simply add the natural language filter backend to your filter backends list.

```python
REST_FRAMEWORK = {
  "DEFAULT_FILTER_BACKENDS": (
    "django_nlf.rest_framework.DjangoNLFilterBackend",
  ),
}
```
