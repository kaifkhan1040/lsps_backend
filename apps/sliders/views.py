from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.sliders.models import AdmissionPopupSettings, BannerSlide
from apps.sliders.serializers import (
    AdmissionPopupSettingsSerializer, BannerSlideSerializer,
)


class BannerSlideViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = BannerSlide.objects.all()
    serializer_class = BannerSlideSerializer


class AdmissionPopupSettingsView(APIView):
    def get(self, request):
        obj = AdmissionPopupSettings.load()
        serializer = AdmissionPopupSettingsSerializer(obj, context={"request": request})
        return Response(serializer.data)
