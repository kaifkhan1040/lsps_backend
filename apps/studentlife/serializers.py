from rest_framework import serializers

from apps.studentlife.models import ActivityCategory, ActivityPhoto, ActivityPost


class ActivityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPhoto
        fields = ["id", "image", "caption"]


class ActivityPostSerializer(serializers.ModelSerializer):
    photos = ActivityPhotoSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = ActivityPost
        fields = [
            "id", "category", "category_name", "title", "description",
            "date", "cover_image", "video_url", "photos",
        ]


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ["id", "name", "icon", "order"]
