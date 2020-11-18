from django.template import loader
from rest_framework.filters import BaseFilterBackend
from rest_framework import compat

from ..conf import settings as nlf_settings
from ..filters import DjangoNLFilter


class DjangoNLFilterBackend(BaseFilterBackend):
    filter_param = nlf_settings.QUERY_PARAM
    filter_class = DjangoNLFilter
    description = ""
    template = "django_nlf/rest_framework/form.html"

    def filter_queryset(self, request, queryset, view):
        nl_filter = self.get_filter(request, queryset, view)
        filter_expr = self.get_filter_expr(request)
        return nl_filter.filter(queryset, filter_expr) if filter_expr else queryset

    def get_filter(self, request, queryset, view):  # pylint: disable=unused-argument
        return self.filter_class()

    def get_filter_expr(self, request):
        return request.query_params.get(self.filter_param)

    def to_html(self, request, queryset, view):  # pylint: disable=unused-argument
        template = loader.get_template(self.template)
        context = {"param": self.filter_param, "expr": self.get_filter_expr(request)}
        return template.render(context, request)

    def get_schema_fields(self, view):
        super().get_schema_fields(view)
        return [
            compat.coreapi.Field(
                name=self.filter_param,
                required=False,
                location="query",
                schema=compat.coreschema.String(description=self.description),
            )
        ]

    def get_schema_operation_parameters(self, view):  # pylint: disable=unused-argument
        return [
            {
                "name": self.filter_param,
                "required": False,
                "in": "query",
                "description": self.description,
                "schema": {
                    "type": "string",
                },
            }
        ]