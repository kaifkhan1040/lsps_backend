from rest_framework import serializers

from apps.infrastructure.models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Facility
        fields = ["id", "category", "category_display", "title", "description", "image", "order"]
