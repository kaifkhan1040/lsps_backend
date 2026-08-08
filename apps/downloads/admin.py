from django.contrib import admin

from apps.downloads.models import DownloadCategory, DownloadDocument


class DownloadDocumentInline(admin.TabularInline):
    model = DownloadDocument
    extra = 0
    fields = ("title", "file", "is_active")


@admin.register(DownloadCategory)
class DownloadCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    inlines = [DownloadDocumentInline]


@admin.register(DownloadDocument)
class DownloadDocumentAdmin(admin.ModelAdmin):
    """Standalone view too, for quickly uploading/replacing a single
    document without opening the whole category page."""
    list_display = ("title", "category", "is_active", "updated_at")
    list_editable = ("is_active",)
    list_filter = ("category", "is_active")
    search_fields = ("title",)
