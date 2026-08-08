from django.db import models
from django.utils.text import slugify

from apps.core.base import OrderableModel, TimeStampedModel


class ClassCategory(OrderableModel):
    """Dynamic class categories: Pre-Nursery, Nursery, LKG, UKG,
    Grade I-V ... Admin can add/edit/delete/reorder freely."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta(OrderableModel.Meta):
        verbose_name = "Class Category"
        verbose_name_plural = "Class Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ClassContentBase(TimeStampedModel):
    """Shared shape for every per-class content type: always tied to
    a ClassCategory, always has a title, always orderable/active."""
    class_category = models.ForeignKey(
        ClassCategory, on_delete=models.CASCADE, related_name="%(class)s_set"
    )
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.class_category.name} - {self.title}"


class Curriculum(ClassContentBase):
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="academics/curriculum/", blank=True, null=True)


class AcademicCalendar(ClassContentBase):
    academic_year = models.CharField(max_length=20, blank=True, help_text="e.g. 2026-27")
    file = models.FileField(upload_to="academics/calendar/", blank=True, null=True)


class SchoolTiming(ClassContentBase):
    description = models.TextField(help_text="e.g. 8:00 AM - 1:30 PM, Mon-Sat")


class UniformGuideline(ClassContentBase):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="academics/uniform/", blank=True, null=True)


class HolidayHomework(ClassContentBase):
    academic_year = models.CharField(max_length=20, blank=True)
    file = models.FileField(upload_to="academics/holiday_homework/", blank=True, null=True)


class Worksheet(ClassContentBase):
    subject = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to="academics/worksheets/", blank=True, null=True)


class ClassGalleryImage(ClassContentBase):
    image = models.ImageField(upload_to="academics/gallery/")
    caption = models.CharField(max_length=200, blank=True)


class ClassVideo(ClassContentBase):
    video_url = models.URLField(blank=True, help_text="YouTube/Vimeo embed link.")
    video_file = models.FileField(upload_to="academics/videos/", blank=True, null=True)


class ClassDownload(ClassContentBase):
    """Generic per-class PDF/download not covered by a more specific
    model above (e.g. syllabus overview, book list)."""
    file = models.FileField(upload_to="academics/downloads/")
