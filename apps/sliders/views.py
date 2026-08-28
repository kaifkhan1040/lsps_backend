from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.sliders.models import AdmissionPopupSettings, BannerSlide,PopUpWindow
from apps.sliders.serializers import (
    AdmissionPopupSettingsSerializer, BannerSlideSerializer,PopUpWindowSerializer
)


class BannerSlideViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = BannerSlide.objects.all()
    serializer_class = BannerSlideSerializer

class PopUpWindowViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = PopUpWindow.objects.all()
    serializer_class = PopUpWindowSerializer


class AdmissionPopupSettingsView(APIView):
    def get(self, request):
        obj = AdmissionPopupSettings.load()
        serializer = AdmissionPopupSettingsSerializer(obj, context={"request": request})
        return Response(serializer.data)
