from django.core.validators import RegexValidator

mobile_validator = RegexValidator(
    regex=r"^\+?91?\d{10}$",
    message="Enter a valid 10-digit mobile number (optionally prefixed with +91).",
)
