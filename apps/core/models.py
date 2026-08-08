from django.db import models

from apps.core.base import OrderableModel, TimeStampedModel


class SingletonModel(models.Model):
    """Base class for models that should only ever have one row
    (e.g. global site settings). Always saves to pk=1."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # singleton rows are never deleted

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    """Global, site-wide settings editable from one place in the
    Admin Panel: school name/logo, contact snippets used in the
    header/footer, analytics id, and SSL/SEO toggles."""
    school_name = models.CharField(max_length=200, default="Little Star Public School")
    logo = models.ImageField(upload_to="core/logo/", blank=True, null=True)
    favicon = models.ImageField(upload_to="core/favicon/", blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True)

    footer_about = models.TextField(blank=True)

    google_analytics_id = models.CharField(max_length=50, blank=True)
    default_meta_title = models.CharField(max_length=200, blank=True)
    default_meta_description = models.TextField(blank=True)

    maintenance_mode = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"


class FloatingButton(OrderableModel):
    """The 'Apply Now / WhatsApp / Call Now' floating action buttons
    required on every page."""
    BUTTON_TYPES = [
        ("apply_now", "Apply Now"),
        ("whatsapp", "WhatsApp"),
        ("call_now", "Call Now"),
        ("custom", "Custom"),
    ]
    button_type = models.CharField(max_length=20, choices=BUTTON_TYPES)
    label = models.CharField(max_length=50)
    link_or_number = models.CharField(
        max_length=255,
        help_text="URL for Apply Now/Custom, phone number for Call Now, "
                   "WhatsApp number (with country code, digits only) for WhatsApp.",
    )
    icon = models.CharField(
        max_length=50, blank=True,
        help_text="Optional icon name/class used by the frontend, e.g. 'phone', 'whatsapp'.",
    )

    def __str__(self):
        return f"{self.get_button_type_display()} - {self.label}"


class NotificationRecipient(TimeStampedModel):
    """Email addresses that receive the automailer whenever someone
    submits the 'Admissions Open' popup form. Fully editable from the
    Admin Panel -- no code changes needed to add/remove recipients."""
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Notification Recipient"
        verbose_name_plural = "Notification Recipients (Popup Automailer)"

    def __str__(self):
        return self.email
