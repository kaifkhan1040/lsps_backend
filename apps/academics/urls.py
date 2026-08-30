from rest_framework.routers import DefaultRouter

from apps.academics.views import (
    AcademicCalendarViewSet, ClassCategoryViewSet, ClassDownloadViewSet,
    # ClassGalleryImageViewSet, ClassVideoViewSet,
    CurriculumViewSet,
    HolidayHomeworkViewSet, SchoolTimingViewSet, UniformGuidelineViewSet,
    WorksheetViewSet,
)

router = DefaultRouter()
router.register("classes", ClassCategoryViewSet, basename="class-category")
router.register("curriculum", CurriculumViewSet, basename="curriculum")
router.register("academic-calendar", AcademicCalendarViewSet, basename="academic-calendar")
router.register("school-timings", SchoolTimingViewSet, basename="school-timing")
router.register("uniform-guidelines", UniformGuidelineViewSet, basename="uniform-guideline")
router.register("holiday-homework", HolidayHomeworkViewSet, basename="holiday-homework")
router.register("worksheets", WorksheetViewSet, basename="worksheet")
# router.register("gallery", ClassGalleryImageViewSet, basename="class-gallery")
# router.register("videos", ClassVideoViewSet, basename="class-video")
router.register("downloads", ClassDownloadViewSet, basename="class-download")

urlpatterns = router.urls
