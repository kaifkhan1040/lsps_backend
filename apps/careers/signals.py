import logging
import threading
import mimetypes
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from apps.careers.models import JobApplication
from apps.core.models import NotificationRecipient

logger = logging.getLogger(__name__)


def send_job_application_email(instance, recipients):
    """
    Send job application email with HTML template and resume attachment.
    """

    subject = (
        f"New Job Application - "
        f"{instance.position} - {instance.full_name}"
    )

    # Render HTML email template
    html_message = render_to_string(
        "emails/job_application.html",
        {
            "application": instance,
        }
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body=(
            f"A new job application has been submitted.\n\n"
            f"Name: {instance.full_name}\n"
            f"Position: {instance.position}\n"
            f"Email: {instance.email}"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
    )

    # Add HTML content
    email.attach_alternative(
        html_message,
        "text/html"
    )

    # Attach resume
    if instance.resume:
        try:
            filename = os.path.basename(instance.resume.name)

            # Detect content type from file extension
            content_type, _ = mimetypes.guess_type(filename)

            with instance.resume.open("rb") as resume_file:
                email.attach(
                    filename,
                    resume_file.read(),
                    content_type or "application/octet-stream",
                )

        except Exception:
            logger.exception(
                "Failed to attach resume for JobApplication %s",
                instance.pk,
            )

    try:
        email.send(fail_silently=False)

        logger.info(
            "Job application email sent successfully for application %s",
            instance.pk,
        )

    except Exception:
        logger.exception(
            "Failed to send job application email for application %s",
            instance.pk,
        )


@receiver(post_save, sender=JobApplication)
def send_job_application_automailer(
    sender,
    instance,
    created,
    **kwargs
):
    """
    Send email when a new job application is created.
    """

    if not created:
        return

    recipients = list(
        NotificationRecipient.objects
        .filter(is_active=True)
        .values_list("email", flat=True)
    )

    if not recipients:
        logger.info(
            "No active NotificationRecipient configured; "
            "skipping automailer."
        )
        return

    # Send email in background thread
    thread = threading.Thread(
        target=send_job_application_email,
        args=(instance, recipients),
        daemon=True,
    )

    thread.start()