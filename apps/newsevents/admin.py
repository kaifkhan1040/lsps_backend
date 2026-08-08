from django.contrib import admin

from apps.newsevents.models import (
    Announcement, Circular, Event, News, NoticeBoardItem,
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "content")
    date_hierarchy = "published_date"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "location", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    date_hierarchy = "event_date"


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_active")
    list_editable = ("is_active",)
    search_fields = ("title", "content")


@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):
    list_display = ("title", "class_category", "date", "is_active")
    list_editable = ("is_active",)
    list_filter = ("class_category", "is_active")
    search_fields = ("title",)
    date_hierarchy = "date"


@admin.register(NoticeBoardItem)
class NoticeBoardItemAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_pinned", "is_active")
    list_editable = ("is_pinned", "is_active")
    list_filter = ("is_pinned", "is_active")
    search_fields = ("title", "content")
    date_hierarchy = "date"
