from rest_framework import serializers

from apps.admissions.models import (
    AdmissionEnquiry, AdmissionFormDownload, AdmissionProcessStep,
    FeeStructure, RequiredDocument, SchoolVisitBooking,
)


class AdmissionProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionProcessStep
        fields = ["id", "step_number", "title", "description"]


class FeeStructureSerializer(serializers.ModelSerializer):
    class_category_name = serializers.CharField(source="class_category.name", read_only=True)

    class Meta:
        model = FeeStructure
        fields = [
            "id", "class_category", "class_category_name", "academic_year",
            "admission_fee", "tuition_fee_per_term", "annual_fee",
            "other_charges", "notes",
        ]


class RequiredDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocument
        fields = ["id", "title", "description"]


class AdmissionFormDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionFormDownload
        fields = ["id", "title", "file"]


class AdmissionEnquiryCreateSerializer(serializers.ModelSerializer):
    """
    Public-facing serializer used by BOTH the Admissions page enquiry
    form and the Home page popup. `source` and `status` are never
    accepted from the client -- the view sets `source` explicitly per
    endpoint, and `status` always starts at its model default ('new').
    """
    class Meta:
        model = AdmissionEnquiry
        fields ="__all__"


class SchoolVisitBookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolVisitBooking
        fields = [
            "id", "name", "email", "phone",
            "preferred_date", "preferred_time", "message",
        ]
