from django.urls import path

from .views import schema_view

from .const import SCHEMA_APP_NAME, SCHEMA_VIEW_NAME


app_name = SCHEMA_APP_NAME
urlpatterns = [path("<str:app>/<str:model>", schema_view, name=SCHEMA_VIEW_NAME)]
