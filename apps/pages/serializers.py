from rest_framework import serializers

from apps.pages.models import (
    AboutUs, ChairmanMessage, HomeContent, PrincipalMessage,
    QuickLink, SchoolHighlight, WhyChooseUs,History,Infrastructure
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
        fields = ["name", "designation", "photo", "short_message", "full_message"]

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()
    infrastructure = serializers.SerializerMethodField()
    class Meta:
        model = AboutUs
        fields = [
            "introduction", "vision", "mission", "history",
            "infrastructure",
              "banner_image",
        ]
    def get_history(self, obj):
            return HistorySerializer(
                obj.history_set.filter(is_active=True), many=True, context=self.context
            ).data
    
    def get_infrastructure(self, obj):
                return InfrastructureSerializer(
                    obj.infrastructure_set.filter(is_active=True), many=True, context=self.context
                ).data


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
