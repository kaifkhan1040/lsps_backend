from rest_framework import serializers

from apps.pages.models import (
    AboutUs, ChairmanMessage, HomeContent, PrincipalMessage,
    QuickLink, SchoolHighlight, WhyChooseUs,
)


class HomeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContent
        fields = ["welcome_title", "welcome_text", "welcome_image"]


class ChairmanMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairmanMessage
        fields = ["name", "designation", "photo", "short_message", "full_message"]


class PrincipalMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalMessage
        fields = ["name", "designation", "photo", "message"]


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
            "introduction", "vision", "mission", "history",
            "infrastructure_summary", "banner_image",
        ]


class SchoolHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolHighlight
        fields = ["id", "icon", "title", "description", "order"]


class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = ["id", "icon", "title", "description", "order"]


class QuickLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickLink
        fields = ["id", "title", "url", "icon", "order"]
