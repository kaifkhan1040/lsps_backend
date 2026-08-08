from rest_framework.routers import DefaultRouter

from apps.admissions.views import (
    AdmissionEnquiryViewSet, AdmissionFormDownloadViewSet,
    AdmissionPopupEnquiryViewSet, AdmissionProcessStepViewSet,
    FeeStructureViewSet, RequiredDocumentViewSet, SchoolVisitBookingViewSet,
)

router = DefaultRouter()
router.register("process-steps", AdmissionProcessStepViewSet, basename="admission-process-step")
router.register("fee-structure", FeeStructureViewSet, basename="fee-structure")
router.register("required-documents", RequiredDocumentViewSet, basename="required-document")
router.register("form-download", AdmissionFormDownloadViewSet, basename="admission-form-download")
router.register("enquiry", AdmissionEnquiryViewSet, basename="admission-enquiry")
router.register("popup-enquiry", AdmissionPopupEnquiryViewSet, basename="admission-popup-enquiry")
router.register("school-visit", SchoolVisitBookingViewSet, basename="school-visit-booking")

urlpatterns = router.urls
