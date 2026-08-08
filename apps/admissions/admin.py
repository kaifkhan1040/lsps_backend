from django.contrib import admin

from apps.admissions.models import (
    AdmissionEnquiry, AdmissionFormDownload, AdmissionProcessStep,
    FeeStructure, RequiredDocument, SchoolVisitBooking,
)


@admin.register(AdmissionProcessStep)
class AdmissionProcessStepAdmin(admin.ModelAdmin):
    list_display = ("step_number", "title", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering = ("step_number",)


@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = (
        "class_category", "academic_year", "admission_fee",
        "tuition_fee_per_term", "annual_fee", "other_charges",
    )
    list_filter = ("academic_year", "class_category")


@admin.register(RequiredDocument)
class RequiredDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(AdmissionFormDownload)
class AdmissionFormDownloadAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "updated_at")
    list_editable = ("is_active",)


@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    """The core admissions workflow tool: every enquiry (from the
    Admissions page form, the Home page popup, or school-visit
    booking) lands here with a status the office staff can update."""
    list_display = (
        "parent_name", "student_name", "class_applying_for",
        "phone", "email", "source", "status", "created_at",
    )
    list_editable = ("status",)
    list_filter = ("status", "source", "class_applying_for", "created_at")
    search_fields = ("parent_name", "student_name", "email", "phone")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(SchoolVisitBooking)
class SchoolVisitBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "preferred_date", "preferred_time", "status")
    list_editable = ("status",)
    list_filter = ("status", "preferred_date")
    search_fields = ("name", "email", "phone")
    date_hierarchy = "preferred_date"
