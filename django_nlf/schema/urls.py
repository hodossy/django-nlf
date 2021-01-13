from django.urls import path

from .views import schema_view


urlpatterns = [
    path("schemas/<str:app>/<str:model>", schema_view, name="nlf-schema")
]
