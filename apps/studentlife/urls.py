from rest_framework.routers import DefaultRouter

from apps.studentlife.views import ActivityCategoryViewSet, ActivityPostViewSet

router = DefaultRouter()
router.register("categories", ActivityCategoryViewSet, basename="activity-category")
router.register("posts", ActivityPostViewSet, basename="activity-post")

urlpatterns = router.urls
