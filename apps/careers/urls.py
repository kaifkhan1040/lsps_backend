from rest_framework.routers import DefaultRouter

from apps.careers.views import JobApplicationViewSet, JobPositionViewSet

router = DefaultRouter()
router.register("positions", JobPositionViewSet, basename="job-position")
router.register("applications", JobApplicationViewSet, basename="job-application")

urlpatterns = router.urls

# Exposes, under api/careers/ (see config/urls.py):
#   GET  /api/careers/positions/      -> dropdown options
#   POST /api/careers/applications/   -> submit the 'Apply for a Job' form
