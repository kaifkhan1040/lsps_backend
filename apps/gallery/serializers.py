from rest_framework import serializers

from apps.gallery.models import Album, Photo, Video


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "image", "caption", "order"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video_url", "video_file", "caption", "order"]


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            "id", "title", "event_name", "date", "cover_image",
            "photos", "videos",
        ]


class AlbumListSerializer(serializers.ModelSerializer):
    """Lightweight version for the gallery landing grid (no nested
    photos/videos -- fetch the full album via retrieve when opened)."""
    photo_count = serializers.IntegerField(source="photos.count", read_only=True)
    video_count = serializers.IntegerField(source="videos.count", read_only=True)

    class Meta:
        model = Album
        fields = [
            "id", "title", "event_name", "date", "cover_image",
            "photo_count", "video_count",
        ]
