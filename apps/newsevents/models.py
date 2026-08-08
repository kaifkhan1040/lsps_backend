from django.db import models

from apps.academics.models import ClassCategory
from apps.core.base import TimeStampedModel


class News(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    published_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Get the existing database record before saving the new one
        if self.pk:
            try:
                old_instance = type(self).objects.get(pk=self.pk)

                # If a new file is uploaded, delete the old file
                if (
                    old_instance.image
                    and old_instance.image != self.image
                ):
                    old_instance.image.delete(save=False)

            except type(self).DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.image:
            self.image.delete(save=False)

        super().delete(*args, **kwargs)


class Event(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    event_date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.image
                        and old_instance.image != self.image
                    ):
                        old_instance.image.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.image:
            self.image.delete(save=False)

        super().delete(*args, **kwargs)


class Announcement(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Circular(TimeStampedModel):
    """Shared between the general 'News & Events > Circulars' listing
    and the per-class 'Academics > Circulars' tab -- leave
    class_category blank for a school-wide circular, or set it to
    scope the circular to one class."""
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="circulars/")
    date = models.DateField()
    class_category = models.ForeignKey(
        ClassCategory, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="circulars",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.file
                        and old_instance.file != self.file
                    ):
                        old_instance.file.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.file:
            self.file.delete(save=False)

        super().delete(*args, **kwargs)


class NoticeBoardItem(TimeStampedModel):
    """The 'Dynamic Notice Board' -- short pinned/unpinned notices,
    optionally linking to an uploaded file."""
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to="notices/", blank=True, null=True)
    date = models.DateField()
    is_pinned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-is_pinned", "-date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Get the existing database record before saving the new one
        if self.pk:
            try:
                old_instance = type(self).objects.get(pk=self.pk)

                # If a new file is uploaded, delete the old file
                if (
                    old_instance.file
                    and old_instance.file != self.file
                ):
                    old_instance.file.delete(save=False)

            except type(self).DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.file:
            self.file.delete(save=False)

        super().delete(*args, **kwargs)
