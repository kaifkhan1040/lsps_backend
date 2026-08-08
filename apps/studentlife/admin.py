from django.contrib import admin

from apps.studentlife.models import ActivityCategory, ActivityPhoto, ActivityPost


class ActivityPhotoInline(admin.TabularInline):
    model = ActivityPhoto
    extra = 0


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(ActivityPost)
class ActivityPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "is_active")
    list_editable = ("is_active",)
    list_filter = ("category", "is_active")
    search_fields = ("title", "description")
    date_hierarchy = "date"
    inlines = [ActivityPhotoInline]
