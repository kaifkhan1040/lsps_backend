from apps.careers.models import JobApplication, JobPosition
from apps.careers.serializers import (
    JobApplicationCreateSerializer, JobPositionSerializer,
)
from apps.core.mixins import ActiveOnlyReadOnlyViewSet, PublicCreateOnlyViewSet


class JobPositionViewSet(ActiveOnlyReadOnlyViewSet):
    """Read-only: the 'Apply for Position' dropdown options, editable
    from Admin so HR can add/remove roles as hiring opens/closes."""
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobApplicationViewSet(PublicCreateOnlyViewSet):
    """POST-only: the Careers page 'Apply for a Job' form."""
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationCreateSerializer
