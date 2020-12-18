"""Log API url definitions"""
from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet, PublicationViewSet

router = SimpleRouter()
router.register("articles", ArticleViewSet)
router.register("publications", PublicationViewSet)

urlpatterns = router.urls
