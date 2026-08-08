from django.db import models

from apps.core.base import OrderableModel, TimeStampedModel


class DownloadCategory(OrderableModel):
    """Admission Form, School Prospectus, Academic Documents,
    Circulars... admin can add/edit/delete/reorder categories."""
    name = models.CharField(max_length=150, unique=True)

    class Meta(OrderableModel.Meta):
        verbose_name = "Download Category"
        verbose_name_plural = "Download Categories"

    def __str__(self):
        return self.name


class DownloadDocument(TimeStampedModel):
    """A single uploadable/replaceable/deletable document within a
    category. Replacing simply means uploading a new file to the same
    row -- the old file is swapped out."""
    category = models.ForeignKey(
        DownloadCategory, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="downloads/")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category__order", "-created_at"]

    def __str__(self):
        return self.title
