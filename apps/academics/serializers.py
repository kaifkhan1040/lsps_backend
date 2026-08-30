from rest_framework import serializers

from apps.academics.models import (
    AcademicCalendar, ClassCategory, ClassDownload, 
    # ClassGalleryImage,ClassVideo,
    Curriculum, HolidayHomework, SchoolTiming,
    UniformGuideline, Worksheet,
)


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ["id", "title", "description", "file", "order"]


class AcademicCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCalendar
        fields = ["id", "title", "academic_year", "file", "order"]


class SchoolTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolTiming
        fields = ["id", "title", "description", "order"]


class UniformGuidelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniformGuideline
        fields = ["id", "title", "description", "image", "order"]


class HolidayHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayHomework
        fields = ["id", "title", "academic_year", "file", "order"]


class WorksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worksheet
        fields = ["id", "title", "subject", "file", "order"]


# class ClassGalleryImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassGalleryImage
#         fields = ["id", "title", "image", "caption", "order"]


# class ClassVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassVideo
#         fields = ["id", "title", "video_url", "video_file", "order"]


class ClassDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDownload
        fields = ["id", "title", "file", "order"]


class ClassCategorySerializer(serializers.ModelSerializer):
    """Lightweight list serializer -- just the class names/slugs, used
    to build the Academics navigation (Pre-Nursery, Nursery, LKG...)."""
    class Meta:
        model = ClassCategory
        fields = ["id", "name", "slug", "description", "order"]


class ClassCategoryDetailSerializer(serializers.ModelSerializer):
    """Full payload for a single class: every content type in one
    call, so the React frontend can render a class page with one
    request instead of nine. Each block is filtered to is_active=True
    for the public API."""
    curriculum = serializers.SerializerMethodField()
    academic_calendar = serializers.SerializerMethodField()
    school_timings = serializers.SerializerMethodField()
    uniform_guidelines = serializers.SerializerMethodField()
    holiday_homework = serializers.SerializerMethodField()
    worksheets = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    downloads = serializers.SerializerMethodField()

    class Meta:
        model = ClassCategory
        fields = [
            "id", "name", "slug", "description",
            "curriculum", "academic_calendar", "school_timings",
            "uniform_guidelines", "holiday_homework", "worksheets",
            "gallery", "videos", "downloads",
        ]

    def get_curriculum(self, obj):
        return CurriculumSerializer(
            obj.curriculum_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_academic_calendar(self, obj):
        return AcademicCalendarSerializer(
            obj.academiccalendar_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_school_timings(self, obj):
        return SchoolTimingSerializer(
            obj.schooltiming_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_uniform_guidelines(self, obj):
        return UniformGuidelineSerializer(
            obj.uniformguideline_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_holiday_homework(self, obj):
        return HolidayHomeworkSerializer(
            obj.holidayhomework_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_worksheets(self, obj):
        return WorksheetSerializer(
            obj.worksheet_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_gallery(self, obj):
        return ClassGalleryImageSerializer(
            obj.classgalleryimage_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_videos(self, obj):
        return ClassVideoSerializer(
            obj.classvideo_set.filter(is_active=True), many=True, context=self.context
        ).data

    def get_downloads(self, obj):
        return ClassDownloadSerializer(
            obj.classdownload_set.filter(is_active=True), many=True, context=self.context
        ).data
