from django import template
from django.urls import reverse, NoReverseMatch

from django_nlf.schema.urls import SCHEMA_URL_NAME


register = template.Library()


@register.inclusion_tag("django_nlf/nlf_autocomplete_js.html")
def nlf_autocomplete_js():
    try:
        schema_root_url = reverse(SCHEMA_URL_NAME, kwargs={"app": "_", "model": "_"})[:-4]
    except NoReverseMatch:
        pass
    return {"init": {"schemaRootUrl": schema_root_url}}
