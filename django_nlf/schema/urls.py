from django.urls import path

from .views import schema_view


SCHEMA_URL_NAME = "nlf:schema"

app_name = "nlf"
urlpatterns = [path("<str:app>/<str:model>", schema_view, name="schema")]
