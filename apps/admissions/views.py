from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.admissions.models import (
    AdmissionEnquiry, AdmissionFormDownload, AdmissionProcessStep,
    FeeStructure, RequiredDocument, SchoolVisitBooking,
)
from apps.admissions.serializers import (
    AdmissionEnquiryCreateSerializer, AdmissionFormDownloadSerializer,
    AdmissionProcessStepSerializer, FeeStructureSerializer,
    RequiredDocumentSerializer, SchoolVisitBookingCreateSerializer,
)
from apps.core.mixins import ActiveOnlyReadOnlyViewSet, PublicCreateOnlyViewSet


class AdmissionProcessStepViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = AdmissionProcessStep.objects.all()
    serializer_class = AdmissionProcessStepSerializer


class FeeStructureViewSet(ReadOnlyModelViewSet):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    filterset_fields = ["class_category", "academic_year"]


class RequiredDocumentViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = RequiredDocument.objects.all()
    serializer_class = RequiredDocumentSerializer


class AdmissionFormDownloadViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = AdmissionFormDownload.objects.all()
    serializer_class = AdmissionFormDownloadSerializer


class AdmissionEnquiryViewSet(PublicCreateOnlyViewSet):
    """POST-only: the Admissions page 'Online Admission Enquiry' form."""
    queryset = AdmissionEnquiry.objects.all()
    serializer_class = AdmissionEnquiryCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(source="admissions_page")


class AdmissionPopupEnquiryViewSet(PublicCreateOnlyViewSet):
    """POST-only: leads captured from the Home page 'Admissions Open'
    popup. Triggers the automailer (see apps/admissions/signals.py)."""
    queryset = AdmissionEnquiry.objects.all()
    serializer_class = AdmissionEnquiryCreateSerializer



class SchoolVisitBookingViewSet(PublicCreateOnlyViewSet):
    """POST-only: 'Book a School Visit' form."""
    queryset = SchoolVisitBooking.objects.all()
    serializer_class = SchoolVisitBookingCreateSerializer
