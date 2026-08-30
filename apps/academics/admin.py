from django.contrib import admin

from apps.academics.models import (
    AcademicCalendar, ClassCategory, ClassDownload, 
    # ClassGalleryImage,ClassVideo,
    Curriculum, HolidayHomework, SchoolTiming,
    UniformGuideline, Worksheet,
)


class BaseInline(admin.TabularInline):
    extra = 0
    show_change_link = True


class CurriculumInline(BaseInline):
    model = Curriculum
    fields = ("title", "description", "file", "order", "is_active")


class AcademicCalendarInline(BaseInline):
    model = AcademicCalendar
    fields = ("title", "academic_year", "file", "order", "is_active")


class SchoolTimingInline(BaseInline):
    model = SchoolTiming
    fields = ("title", "description", "order", "is_active")


class UniformGuidelineInline(BaseInline):
    model = UniformGuideline
    fields = ("title", "description", "image", "order", "is_active")


class HolidayHomeworkInline(BaseInline):
    model = HolidayHomework
    fields = ("title", "academic_year", "file", "order", "is_active")


class WorksheetInline(BaseInline):
    model = Worksheet
    fields = ("title", "subject", "file", "order", "is_active")


# class ClassGalleryImageInline(BaseInline):
#     model = ClassGalleryImage
#     fields = ("title", "image", "caption", "order", "is_active")


# class ClassVideoInline(BaseInline):
#     model = ClassVideo
#     fields = ("title", "video_url", "video_file", "order", "is_active")


class ClassDownloadInline(BaseInline):
    model = ClassDownload
    fields = ("title", "file", "order", "is_active")


@admin.register(ClassCategory)
class ClassCategoryAdmin(admin.ModelAdmin):
    """Manage a class (e.g. 'Grade II') and ALL of its content --
    curriculum, calendar, timings, uniform, homework, worksheets,
    gallery, videos and downloads -- from a single admin page."""
    list_display = ("name", "slug", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    inlines = [
        CurriculumInline, AcademicCalendarInline, SchoolTimingInline,
        UniformGuidelineInline, HolidayHomeworkInline, WorksheetInline,
        # ClassGalleryImageInline, ClassVideoInline, 
        ClassDownloadInline,
    ]


def _register_standalone(model, extra_list_fields=()):
    """Also register each content model on its own for quick
    bulk edits / filtering across classes, independent of the
    ClassCategory inline view above."""
    list_display = ("title", "class_category", *extra_list_fields, "order", "is_active")

    admin_class = type(
        f"{model.__name__}Admin",
        (admin.ModelAdmin,),
        {
            "list_display": list_display,
            "list_editable": ("order", "is_active"),
            "list_filter": ("class_category", "is_active"),
            "search_fields": ("title",),
        },
    )
    admin.site.register(model, admin_class)


_register_standalone(Curriculum)
_register_standalone(AcademicCalendar, ("academic_year",))
_register_standalone(SchoolTiming)
_register_standalone(UniformGuideline)
_register_standalone(HolidayHomework, ("academic_year",))
_register_standalone(Worksheet, ("subject",))
# _register_standalone(ClassGalleryImage)
# _register_standalone(ClassVideo)
_register_standalone(ClassDownload)
