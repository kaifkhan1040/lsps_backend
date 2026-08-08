from django.db import models

from apps.core.base import OrderableModel


class Testimonial(OrderableModel):
    parent_name = models.CharField(max_length=150)
    student_name = models.CharField(max_length=150, blank=True)
    student_class = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5, help_text="Rating out of 5."
    )

    def __str__(self):
        return f"{self.parent_name} ({self.student_class})"

    def save(self, *args, **kwargs):
        # Get the existing database record before saving the new one
        if self.pk:
            try:
                old_instance = type(self).objects.get(pk=self.pk)

                # If a new file is uploaded, delete the old file
                if (
                    old_instance.photo
                    and old_instance.photo != self.photo
                ):
                    old_instance.photo.delete(save=False)

            except type(self).DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.photo:
            self.photo.delete(save=False)

        super().delete(*args, **kwargs)
