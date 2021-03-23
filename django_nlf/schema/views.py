import dataclasses
from http import HTTPStatus

from django.contrib.contenttypes.models import ContentType
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

from .django import NLFModelSchemaBuilder


class SchemaEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        return super().default(obj)


def schema_view(request, app, model):
    try:
        model = ContentType.objects.get(app_label=app, model=model).model_class()
    except ContentType.DoesNotExist:
        return JsonResponse({"details": "No such resource found"}, status=HTTPStatus.NOT_FOUND)

    builder = NLFModelSchemaBuilder()
    data = builder.get_schema_for(model)
    return JsonResponse(data, encoder=SchemaEncoder)
