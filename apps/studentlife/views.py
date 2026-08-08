from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.studentlife.models import ActivityCategory, ActivityPost
from apps.studentlife.serializers import (
    ActivityCategorySerializer, ActivityPostSerializer,
)


class ActivityCategoryViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = ActivityCategory.objects.all()
    serializer_class = ActivityCategorySerializer


class ActivityPostViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = ActivityPost.objects.all()
    serializer_class = ActivityPostSerializer
    filterset_fields = ["category"]
