from rest_framework.routers import DefaultRouter

from apps.downloads.views import DownloadCategoryViewSet, DownloadDocumentViewSet

router = DefaultRouter()
router.register("categories", DownloadCategoryViewSet, basename="download-category")
router.register("documents", DownloadDocumentViewSet, basename="download-document")

urlpatterns = router.urls
