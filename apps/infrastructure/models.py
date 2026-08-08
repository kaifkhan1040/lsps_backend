from django.db import models

from apps.core.base import OrderableModel


class Facility(OrderableModel):
    """Smart Classrooms, Computer Lab, Library, Sports Facilities,
    Medical Room, Transportation -- admin can add/edit/delete/reorder
    any facility under any category, images and all."""
    CATEGORY_CHOICES = [
        ("smart_classroom", "Smart Classrooms"),
        ("computer_lab", "Computer Lab"),
        ("library", "Library"),
        ("sports", "Sports Facilities"),
        ("medical", "Medical Room"),
        ("transport", "Transportation"),
        ("other", "Other"),
    ]
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="infrastructure/", blank=True, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"

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
