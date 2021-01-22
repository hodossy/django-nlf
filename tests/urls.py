from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet, PublicationViewSet

router = SimpleRouter()
router.register("articles", ArticleViewSet)
router.register("publications", PublicationViewSet)

schemapatterns = [
    path("schemas/", include("django_nlf.schema.urls")),
]

demopatterns = [
    path("", TemplateView.as_view(template_name="demo.html")),
]

urlpatterns = router.urls + schemapatterns + demopatterns
