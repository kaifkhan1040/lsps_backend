from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.pages.models import (
    AboutUs, ChairmanMessage, HomeContent, PrincipalMessage,
    QuickLink, SchoolHighlight, WhyChooseUs,
)
from apps.pages.serializers import (
    AboutUsSerializer, ChairmanMessageSerializer, HomeContentSerializer,
    PrincipalMessageSerializer, QuickLinkSerializer,
    SchoolHighlightSerializer, WhyChooseUsSerializer,
)


class _SingletonView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        obj = self.model.load()
        serializer = self.serializer_class(obj, context={"request": request})
        return Response(serializer.data)


class HomeContentView(_SingletonView):
    model = HomeContent
    serializer_class = HomeContentSerializer


class ChairmanMessageView(_SingletonView):
    model = ChairmanMessage
    serializer_class = ChairmanMessageSerializer


class PrincipalMessageView(_SingletonView):
    model = PrincipalMessage
    serializer_class = PrincipalMessageSerializer


class AboutUsView(_SingletonView):
    model = AboutUs
    serializer_class = AboutUsSerializer


class SchoolHighlightViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = SchoolHighlight.objects.all()
    serializer_class = SchoolHighlightSerializer


class WhyChooseUsViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer


class QuickLinkViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = QuickLink.objects.all()
    serializer_class = QuickLinkSerializer
