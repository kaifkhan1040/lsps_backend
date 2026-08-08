from django.contrib import admin

from apps.gallery.models import Album, Photo, Video


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "event_name", "date", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "event_name")
    date_hierarchy = "date"
    inlines = [PhotoInline, VideoInline]
