from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.infrastructure.models import Facility
from apps.infrastructure.serializers import FacilitySerializer


class FacilityViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    filterset_fields = ["category"]
