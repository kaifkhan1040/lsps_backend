from rest_framework import serializers

from apps.sliders.models import AdmissionPopupSettings, BannerSlide,PopUpWindow


class BannerSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerSlide
        fields = [
            "id", "title", "subtitle", "file",
            "cta_type", "cta_text", "cta_link", "order",
        ]

class PopUpWindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopUpWindow
        fields = "__all__"


class AdmissionPopupSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionPopupSettings
        fields = ["is_active", "heading", "subtext", "image", "show_after_seconds"]
