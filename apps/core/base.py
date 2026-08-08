from django.db import models


class TimeStampedModel(models.Model):
    """Adds created/updated timestamps to any model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderableModel(models.Model):
    """Adds a manual display-order field + active flag, used by every
    list-type content model (sliders, highlights, facilities, etc.) so
    admins can reorder and hide/show items without deleting them."""
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]
