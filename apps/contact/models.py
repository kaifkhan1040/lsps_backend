from django.db import models

from apps.core.base import OrderableModel, TimeStampedModel
from apps.core.models import SingletonModel


class ContactDetail(SingletonModel):
    """Single source of truth for address/email/timings/map/WhatsApp,
    used in the footer and the Contact Us page. Phone numbers and
    social links are separate repeatable models below."""
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    office_timings = models.CharField(max_length=200, blank=True, help_text="e.g. Mon-Sat, 8:00 AM - 3:00 PM")
    google_map_embed_url = models.URLField(
        blank=True, help_text="Google Maps embed src URL pointing at the school location."
    )
    whatsapp_number = models.CharField(
        max_length=20, blank=True, help_text="Digits only with country code, e.g. 919999999999"
    )

    class Meta:
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return "Contact Details"


class PhoneNumber(OrderableModel):
    label = models.CharField(max_length=50, blank=True, help_text="e.g. 'Front Office', 'Admissions'")
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.label}: {self.number}" if self.label else self.number


class SocialMediaLink(OrderableModel):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "YouTube"),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField(help_text="Direct link to the official profile/page.")

    def __str__(self):
        return self.get_platform_display()


class ContactMessage(TimeStampedModel):
    """'Contact Form' submissions from the Contact Us page."""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"
