from django.db.models import Q, Count, Sum, Subquery

from django_nlf.functions import nlf_function
from django_nlf.types import FunctionMeta, FunctionRole

from .models import Article, Publication


@nlf_function("totalViews", role=FunctionRole.FIELD, models=[Publication])
def total_views(*args, **kwargs):
    """Test function to be used as a field"""
    return {"total_views": Sum("articles__views")}


@nlf_function("hasBeenPublished", role=FunctionRole.EXPRESSION, models=[Article])
def has_been_published(*args, exclude=False, **kwargs):
    """Test function to be used as an expression"""
    if len(args) == 0:
        # just check if it has been published anywhere
        annotations = {"pub_count": Count("publications")}
        condition = Q(pub_count__gt=0)
    else:
        # check if article hase been published in given papers
        annotations = {}
        condition = Q(publications__title__in=args)

    return annotations, condition if not exclude else ~condition
