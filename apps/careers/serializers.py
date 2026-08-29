from rest_framework import serializers

from apps.careers.models import JobApplication, JobPosition


class JobPositionSerializer(serializers.ModelSerializer):
    """Read-only: powers the 'Apply for Position' dropdown on the frontend."""
    class Meta:
        model = JobPosition
        fields = ["id", "name"]


class JobApplicationCreateSerializer(serializers.ModelSerializer):
    """
    Public-facing serializer for the 'Apply for a Job' form.

    Field mapping to the form spec:
      Full Name*                 -> full_name
      Mobile Number*              -> mobile_number
      Email ID*                   -> email
      Address                     -> address (optional)
      Apply for Position*         -> position
      Qualification & Experience* -> qualification_experience
      Attach CV/Resume*           -> resume (PDF/DOC/DOCX, validated in the model)

    `status` and `admin_notes` are never accepted from the client --
    status starts at its model default ('new') and notes are added later
    from Django Admin.
    """
    position = serializers.PrimaryKeyRelatedField(
        queryset=JobPosition.objects.filter(is_active=True),
        required=True, label="Apply for Position",
    )

    class Meta:
        model = JobApplication
        fields = [
            "id", "full_name", "mobile_number", "email", "address",
            "position", "qualification','experience", "resume",
        ]
