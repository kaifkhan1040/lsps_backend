from rest_framework.routers import DefaultRouter

from apps.infrastructure.views import FacilityViewSet

router = DefaultRouter()
router.register("", FacilityViewSet, basename="facility")

urlpatterns = router.urls
