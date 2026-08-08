from rest_framework import serializers

from apps.core.models import FloatingButton, SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "school_name", "logo", "favicon", "tagline", "footer_about",
            "google_analytics_id", "default_meta_title", "default_meta_description",
            "maintenance_mode",
        ]


class FloatingButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = ["id", "button_type", "label", "link_or_number", "icon", "order"]
