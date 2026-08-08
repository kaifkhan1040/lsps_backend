from rest_framework import serializers

from apps.newsevents.models import (
    Announcement, Circular, Event, News, NoticeBoardItem,
)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "content", "image", "published_date"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "description", "image", "event_date", "location"]


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ["id", "title", "content", "created_at"]


class CircularSerializer(serializers.ModelSerializer):
    class_category_name = serializers.CharField(source="class_category.name", read_only=True)

    class Meta:
        model = Circular
        fields = ["id", "title", "file", "date", "class_category", "class_category_name"]


class NoticeBoardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoardItem
        fields = ["id", "title", "content", "file", "date", "is_pinned"]
