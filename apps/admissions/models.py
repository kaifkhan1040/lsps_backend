from django.db import models

from apps.academics.models import ClassCategory
from apps.core.base import OrderableModel, TimeStampedModel


class AdmissionProcessStep(OrderableModel):
    """Step-by-step 'Admission Process' shown on the Admissions page."""
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    class Meta(OrderableModel.Meta):
        ordering = ["step_number", "order"]

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class FeeStructure(models.Model):
    """Per-class fee breakdown, fully editable from Admin Panel."""
    class_category = models.ForeignKey(
        ClassCategory, on_delete=models.CASCADE, related_name="fee_structures"
    )
    academic_year = models.CharField(max_length=20, default="2026-27")
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tuition_fee_per_term = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    annual_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("class_category", "academic_year")
        ordering = ["class_category__order"]

    def __str__(self):
        return f"{self.class_category.name} Fee ({self.academic_year})"


class RequiredDocument(OrderableModel):
    """'Required Documents' checklist for admission."""
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class AdmissionFormDownload(TimeStampedModel):
    """The downloadable Admission Form (PDF)."""
    title = models.CharField(max_length=150, default="Admission Form")
    file = models.FileField(upload_to="admissions/forms/")
    is_active = models.BooleanField(default=True)

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


class AdmissionEnquiry(TimeStampedModel):
    """
    Captures BOTH:
      - the 'Online Admission Enquiry' form on the Admissions page, and
      - leads from the 'Admissions Open' Home page popup (source='popup')
    Every submission is visible & manageable in the Admin Panel with a
    workflow status, and triggers the popup automailer via a signal
    (see apps/admissions/signals.py) when source == 'popup'.
    """
    STATUS_CHOICES = [
        ("new", "New"),
        ("follow_up", "Follow-up"),
        ("admitted", "Admitted"),
        ("closed", "Closed"),
    ]
    SOURCE_CHOICES = [
        ("admissions_page", "Admissions Page Form"),
        ("popup", "Home Page Popup"),
        ("school_visit", "Book a School Visit"),
    ]

    student_name = models.CharField(max_length=150, blank=True)
    parent_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    class_applying_for = models.ForeignKey(
        ClassCategory, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="admission_enquiries",
    )
    message = models.TextField(blank=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="admissions_page")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    class Meta:
        verbose_name_plural = "Admission Enquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.parent_name} - {self.get_status_display()}"


class SchoolVisitBooking(TimeStampedModel):
    """'Book a School Visit' submissions."""
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_date = models.DateField()
    preferred_time = models.TimeField(blank=True, null=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.preferred_date}"
