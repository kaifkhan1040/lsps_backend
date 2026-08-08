from rest_framework.routers import DefaultRouter

from apps.newsevents.views import (
    AnnouncementViewSet, CircularViewSet, EventViewSet, NewsViewSet,
    NoticeBoardItemViewSet,
)

router = DefaultRouter()
router.register("news", NewsViewSet, basename="news")
router.register("events", EventViewSet, basename="event")
router.register("announcements", AnnouncementViewSet, basename="announcement")
router.register("circulars", CircularViewSet, basename="circular")
router.register("notice-board", NoticeBoardItemViewSet, basename="notice-board")

urlpatterns = router.urls
