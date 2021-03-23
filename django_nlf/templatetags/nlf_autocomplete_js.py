from django import template


register = template.Library()


@register.inclusion_tag("django_nlf/nlf_autocomplete_js.html")
def nlf_autocomplete_js():
    pass
