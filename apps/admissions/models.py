from django.db import models

from apps.academics.models import ClassCategory
from apps.core.base import OrderableModel, TimeStampedModel
from apps.core.validators import mobile_validator
from django_ckeditor_5.fields import CKEditor5Field

class AdmissionProcessStep(OrderableModel):
    """Step-by-step 'Admission Process' shown on the Admissions page."""
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    description = CKEditor5Field("Description", config_name="extends")

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
    # description = models.TextField(blank=True)
    description = CKEditor5Field("Description", config_name="extends")

    def __str__(self):
        return self.title


class AdmissionFormDownload(TimeStampedModel):
    """The downloadable Admission Form (PDF)."""
    title = models.CharField(max_length=150, default="Admission Form")
    file = models.FileField(upload_to="admissions/forms/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Admission Form"
        verbose_name_plural = "Admission Forms"
    
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
    Captures:
      - the 'Apply Now' form on the Admissions page (source='admissions_page'),
      - leads from the 'Admissions Open' Home page popup (source='popup'), and
      - (legacy) 'Book a School Visit' submissions (source='school_visit').
    Every submission is visible & manageable in the Admin Panel with a
    workflow status, and triggers the automailer via a signal
    (see apps/admissions/signals.py) for every source.

    `interested_in` / `preferred_visit_date` / `child_age` back the 'Apply
    Now' form fields; they're optional at the model level so the leaner
    popup/legacy submissions (which don't collect them) still validate.
    Per-endpoint required-ness is enforced in serializers.py instead.
    """
    INTERESTED_IN_CHOICES = [
        ("admission_enquiry", "Admission Enquiry"),
        ("school_visit", "School Visit"),
        ("both", "Both"),
    ]

    student_name = models.CharField("Child's Name", max_length=150, blank=True)
    student_age = models.PositiveSmallIntegerField(
        "Child Age", null=True, blank=True
    )
    parent_name = models.CharField("Parent/Guardian Name", max_length=150)
    phone = models.CharField(
        "Mobile Number", max_length=20, validators=[mobile_validator]
    )
    class_applying_for = models.ForeignKey(
        ClassCategory, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="admission_enquiries",
        verbose_name="Admission Required For Class",
    )
    interested_in = models.CharField(
        "I am Interested In", max_length=20,
        choices=INTERESTED_IN_CHOICES, blank=True,
        default="admission_enquiry",
    )
    preferred_visit_date = models.DateField(
        "Preferred Visit Date", null=True, blank=True,
        help_text="Required only when 'School Visit' or 'Both' is selected.",
    )
    message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Admission Enquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.parent_name}"

    @property
    def wants_visit(self):
        return self.interested_in in ("school_visit", "both")



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
