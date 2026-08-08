from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.academics.models import (
    AcademicCalendar, ClassCategory, ClassDownload, ClassGalleryImage,
    ClassVideo, Curriculum, HolidayHomework, SchoolTiming,
    UniformGuideline, Worksheet,
)
from apps.academics.serializers import (
    AcademicCalendarSerializer, ClassCategoryDetailSerializer,
    ClassCategorySerializer, ClassDownloadSerializer,
    ClassGalleryImageSerializer, ClassVideoSerializer,
    CurriculumSerializer, HolidayHomeworkSerializer,
    SchoolTimingSerializer, UniformGuidelineSerializer, WorksheetSerializer,
)


class ClassCategoryViewSet(ReadOnlyModelViewSet):
    """
    /api/academics/classes/            -> list of classes (nav)
    /api/academics/classes/{slug}/      -> full class page (everything nested)
    """
    queryset = ClassCategory.objects.filter(is_active=True)
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ClassCategoryDetailSerializer
        return ClassCategorySerializer


class _ClassFilteredReadOnlyViewSet(ReadOnlyModelViewSet):
    """Common behaviour for each per-class content type: active-only,
    filterable by ?class=<slug> or ?class_category=<id>."""
    filterset_fields = ["class_category"]

    def get_queryset(self):
        qs = self.queryset_model.objects.filter(is_active=True)
        class_slug = self.request.query_params.get("class")
        if class_slug:
            qs = qs.filter(class_category__slug=class_slug)
        return qs


class CurriculumViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = Curriculum
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


class AcademicCalendarViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = AcademicCalendar
    queryset = AcademicCalendar.objects.all()
    serializer_class = AcademicCalendarSerializer


class SchoolTimingViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = SchoolTiming
    queryset = SchoolTiming.objects.all()
    serializer_class = SchoolTimingSerializer


class UniformGuidelineViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = UniformGuideline
    queryset = UniformGuideline.objects.all()
    serializer_class = UniformGuidelineSerializer


class HolidayHomeworkViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = HolidayHomework
    queryset = HolidayHomework.objects.all()
    serializer_class = HolidayHomeworkSerializer


class WorksheetViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = Worksheet
    queryset = Worksheet.objects.all()
    serializer_class = WorksheetSerializer


class ClassGalleryImageViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = ClassGalleryImage
    queryset = ClassGalleryImage.objects.all()
    serializer_class = ClassGalleryImageSerializer


class ClassVideoViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = ClassVideo
    queryset = ClassVideo.objects.all()
    serializer_class = ClassVideoSerializer


class ClassDownloadViewSet(_ClassFilteredReadOnlyViewSet):
    queryset_model = ClassDownload
    queryset = ClassDownload.objects.all()
    serializer_class = ClassDownloadSerializer
