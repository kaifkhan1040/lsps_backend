from django.db import models

from apps.core.base import OrderableModel
from apps.core.models import SingletonModel


class BannerSlide(OrderableModel):
    """Dynamic, auto-sliding Home page banner."""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    file = models.FileField(upload_to="sliders/banners/")

    CTA_CHOICES = [
        ("apply_now", "Apply Now"),
        ("book_visit", "Book a School Visit"),
        ("contact_us", "Contact Us"),
        ("custom", "Custom"),
    ]
    cta_type = models.CharField(max_length=20, choices=CTA_CHOICES, default="apply_now")
    cta_text = models.CharField(max_length=50, blank=True)
    cta_link = models.CharField(max_length=255, blank=True)

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


class AdmissionPopupSettings(SingletonModel):
    """Controls the 'Admissions Open – Apply Now' popup shown on
    first visit. The lead captured through this popup is stored as an
    AdmissionEnquiry (apps.admissions) with source='popup', which in
    turn triggers the automailer to every active NotificationRecipient
    (apps.core) -- addresses are editable from the Admin Panel with no
    code changes required."""
    is_active = models.BooleanField(default=True)
    heading = models.CharField(max_length=200, default="Admissions Open – Apply Now")
    subtext = models.TextField(blank=True)
    image = models.ImageField(upload_to="sliders/popup/", blank=True, null=True)
    show_after_seconds = models.PositiveIntegerField(
        default=2, help_text="Delay before the popup appears on first visit."
    )

    class Meta:
        verbose_name = "Admission Popup Settings"
        verbose_name_plural = "Admission Popup Settings"

    def __str__(self):
        return "Admission Popup Settings"

class PopUpWindow(SingletonModel):
    "pop-up window images"
    image = models.ImageField(upload_to="sliders/popup/", blank=True, null=True)

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

