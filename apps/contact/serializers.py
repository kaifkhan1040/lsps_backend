from rest_framework import serializers

from apps.contact.models import (
    ContactDetail, ContactMessage, PhoneNumber, SocialMediaLink,
)


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ["id", "label", "number"]


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = ["id", "platform", "url"]


class ContactDetailSerializer(serializers.ModelSerializer):
    phone_numbers = serializers.SerializerMethodField()
    social_links = serializers.SerializerMethodField()

    class Meta:
        model = ContactDetail
        fields = [
            "address", "email", "office_timings", "google_map_embed_url",
            "whatsapp_number", "phone_numbers", "social_links",
        ]

    def get_phone_numbers(self, obj):
        return PhoneNumberSerializer(
            PhoneNumber.objects.filter(is_active=True), many=True, context=self.context
        ).data

    def get_social_links(self, obj):
        return SocialMediaLinkSerializer(
            SocialMediaLink.objects.filter(is_active=True), many=True, context=self.context
        ).data


class ContactMessageCreateSerializer(serializers.ModelSerializer):
    """Public-facing: `is_read` is never accepted from the client."""
    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "phone", "subject", "message"]
