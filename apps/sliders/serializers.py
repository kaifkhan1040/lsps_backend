from rest_framework import serializers

from apps.sliders.models import AdmissionPopupSettings, BannerSlide


class BannerSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerSlide
        fields = [
            "id", "title", "subtitle", "image",
            "cta_type", "cta_text", "cta_link", "order",
        ]


class AdmissionPopupSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionPopupSettings
        fields = ["is_active", "heading", "subtext", "image", "show_after_seconds"]
