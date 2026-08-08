from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.core.models import FloatingButton, SiteSettings
from apps.core.serializers import FloatingButtonSerializer, SiteSettingsSerializer


class SiteSettingsView(APIView):
    """Single endpoint returning the site-wide settings singleton."""

    def get(self, request):
        settings_obj = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings_obj, context={"request": request})
        return Response(serializer.data)


class FloatingButtonViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = FloatingButton.objects.all()
    serializer_class = FloatingButtonSerializer
