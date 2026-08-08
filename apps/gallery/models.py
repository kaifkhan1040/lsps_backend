from django.db import models

from apps.core.base import TimeStampedModel


class Album(TimeStampedModel):
    """Event-wise photo/video album. Admin creates an album, then
    uploads photos/videos into it."""
    title = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200, blank=True)
    date = models.DateField(blank=True, null=True)
    cover_image = models.ImageField(upload_to="gallery/covers/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Get the existing database record before saving the new one
        if self.pk:
            try:
                old_instance = type(self).objects.get(pk=self.pk)

                # If a new file is uploaded, delete the old file
                if (
                    old_instance.cover_image
                    and old_instance.cover_image != self.cover_image
                ):
                    old_instance.cover_image.delete(save=False)

            except type(self).DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
            # Delete the file from storage before deleting the database record
            if self.cover_image:
                self.cover_image.delete(save=False)
    
            super().delete(*args, **kwargs)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="gallery/photos/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Photo in {self.album.title}"

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


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="videos")
    video_url = models.URLField(blank=True, help_text="YouTube/Vimeo embed link.")
    video_file = models.FileField(upload_to="gallery/videos/", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Video in {self.album.title}"

    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.video_file
                        and old_instance.video_file != self.video_file
                    ):
                        old_instance.video_file.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.video_file:
            self.video_file.delete(save=False)

        super().delete(*args, **kwargs)
