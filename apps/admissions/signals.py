import logging

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.admissions.models import AdmissionEnquiry
from apps.core.models import NotificationRecipient

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AdmissionEnquiry)
def send_admission_popup_automailer(sender, instance, created, **kwargs):
    """
    Requirement: "After submission, an automailer send to the
    respective mail id which can be updated from the admin panel."

    Recipients live in apps.core.NotificationRecipient -- add/remove
    emails there any time, no code/deploy needed. Fires for every new
    enquiry regardless of source (popup, admissions page, or school
    visit) so no lead is missed; the source is included in the email
    so staff know where it came from.
    """
    if not created:
        return

    recipients = list(
        NotificationRecipient.objects.filter(is_active=True).values_list("email", flat=True)
    )
    if not recipients:
        logger.info("No active NotificationRecipient configured; skipping automailer.")
        return

    subject = f"New Admission Enquiry ({instance.get_source_display()}) - {instance.parent_name}"
    message = (
        f"A new admission enquiry has been submitted on the website.\n\n"
        f"Source: {instance.get_source_display()}\n"
        f"Parent Name: {instance.parent_name}\n"
        f"Student Name: {instance.student_name or '-'}\n"
        f"Class Applying For: {instance.class_applying_for or '-'}\n"
        f"Email: {instance.email}\n"
        f"Phone: {instance.phone}\n"
        f"Message: {instance.message or '-'}\n\n"
        f"Manage this enquiry in the Admin Panel under Admissions > Admission Enquiries."
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
        logger.exception("Failed to send admission enquiry automailer.")
