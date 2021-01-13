from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet, PublicationViewSet

router = SimpleRouter()
router.register("articles", ArticleViewSet)
router.register("publications", PublicationViewSet)

schemapatterns = [
    path("", include("django_nlf.schema.urls")),
]

urlpatterns = router.urls + schemapatterns
