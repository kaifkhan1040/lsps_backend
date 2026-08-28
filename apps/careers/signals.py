import logging

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.careers.models import JobApplication
from apps.core.models import NotificationRecipient

logger = logging.getLogger(__name__)


@receiver(post_save, sender=JobApplication)
def send_job_application_automailer(sender, instance, created, **kwargs):
    """
    Notifies staff whenever a new job application comes in via the
    Careers page. Reuses the same admin-managed recipient list as the
    admissions automailer (apps.core.NotificationRecipient) so there's
    one place to manage notification emails; split this into its own
    recipient list later if HR needs a different distribution list.
    """
    if not created:
        return

    recipients = list(
        NotificationRecipient.objects.filter(is_active=True).values_list("email", flat=True)
    )
    if not recipients:
        logger.info("No active NotificationRecipient configured; skipping automailer.")
        return

    subject = f"New Job Application - {instance.position} - {instance.full_name}"
    message = (
        f"A new job application has been submitted on the website.\n\n"
        f"Position: {instance.position}\n"
        f"Full Name: {instance.full_name}\n"
        f"Mobile Number: {instance.mobile_number}\n"
        f"Email: {instance.email}\n"
        f"Address: {instance.address or '-'}\n"
        f"Qualification & Experience: {instance.qualification_experience}\n"
        f"Resume: {instance.resume.url if instance.resume else '-'}\n\n"
        f"Manage this application in the Admin Panel under Careers > Job Applications."
    )

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=True,
        )
    except Exception:
        logger.exception("Failed to send job application automailer.")
