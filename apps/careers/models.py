from django.core.validators import FileExtensionValidator
from django.db import models

from apps.core.base import OrderableModel, TimeStampedModel
from apps.core.validators import mobile_validator


def validate_resume_size(file):
    max_size_mb = 5
    if file.size > max_size_mb * 1024 * 1024:
        from django.core.exceptions import ValidationError
        raise ValidationError(f"Resume file must be under {max_size_mb} MB.")


class JobPosition(OrderableModel):
    """
    'Apply for Position' dropdown options (Teacher / Accountant /
    Receptionist / Office Staff / Coordinator / Other, etc).

    Fully admin-managed so positions can be added/removed the moment
    hiring opens or closes for a role -- no code change needed. Seeded
    with the initial list via a data migration (0002_seed_positions).
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta(OrderableModel.Meta):
        verbose_name = "Job Position"
        verbose_name_plural = "Job Positions"

    def __str__(self):
        return self.name


class JobApplication(TimeStampedModel):
    """
    Captures the 'Apply for a Job' form on the Careers page. Public,
    anonymous submissions only -- reviewing and updating status happens
    in Django Admin. Triggers the automailer via a signal (see
    apps/careers/signals.py).
    """
    STATUS_CHOICES = [
        ("new", "New"),
        ("shortlisted", "Shortlisted"),
        ("interview", "Interview Scheduled"),
        ("hired", "Hired"),
        ("rejected", "Rejected"),
    ]

    full_name = models.CharField("Full Name", max_length=150)
    mobile_number = models.CharField(
        "Mobile Number", max_length=20, validators=[mobile_validator]
    )
    email = models.EmailField("Email ID")
    address = models.TextField("Address", blank=True)
    position = models.ForeignKey(
        JobPosition, on_delete=models.PROTECT,
        related_name="applications", verbose_name="Apply for Position",
    )
    qualification = models.CharField(
        "Qualification", max_length=500
    )
    experience=models.CharField(
        "Experience", max_length=500
    )
    resume = models.FileField(
        "Attach CV/Resume",
        upload_to="careers/resumes/",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"]),
            validate_resume_size,
        ],
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    admin_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.position} ({self.get_status_display()})"
