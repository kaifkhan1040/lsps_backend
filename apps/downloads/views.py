from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.downloads.models import DownloadCategory, DownloadDocument
from apps.downloads.serializers import (
    DownloadCategorySerializer, DownloadDocumentSerializer,
)


class DownloadCategoryViewSet(ActiveOnlyReadOnlyViewSet):
    """Nested view: each category with its active documents inline."""
    queryset = DownloadCategory.objects.all()
    serializer_class = DownloadCategorySerializer


class DownloadDocumentViewSet(ActiveOnlyReadOnlyViewSet):
    """Flat view: all documents, filterable by ?category=<id>."""
    queryset = DownloadDocument.objects.all()
    serializer_class = DownloadDocumentSerializer
    filterset_fields = ["category"]
