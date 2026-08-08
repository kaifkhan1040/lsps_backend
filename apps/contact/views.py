from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contact.models import ContactDetail, ContactMessage
from apps.contact.serializers import (
    ContactDetailSerializer, ContactMessageCreateSerializer,
)
from apps.core.mixins import PublicCreateOnlyViewSet


class ContactDetailView(APIView):
    def get(self, request):
        obj = ContactDetail.load()
        serializer = ContactDetailSerializer(obj, context={"request": request})
        return Response(serializer.data)


class ContactMessageViewSet(PublicCreateOnlyViewSet):
    """POST-only: the Contact Us page contact form."""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageCreateSerializer
