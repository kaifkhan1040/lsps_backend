from django.contrib import admin

from apps.core.models import FloatingButton, NotificationRecipient, SiteSettings


# @admin.register(SiteSettings)
# class SiteSettingsAdmin(admin.ModelAdmin):
#     """Only one row ever exists -- disable 'add' once it's created,
#     and disable 'delete' entirely, so admins can't lose the settings."""

#     def has_add_permission(self, request):
#         return not SiteSettings.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         return False


# @admin.register(FloatingButton)
# class FloatingButtonAdmin(admin.ModelAdmin):
#     list_display = ("label", "button_type", "link_or_number", "order", "is_active")
#     list_editable = ("order", "is_active")
#     list_filter = ("button_type", "is_active")
#     search_fields = ("label", "link_or_number")


@admin.register(NotificationRecipient)
class NotificationRecipientAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "is_active", "created_at")
    list_editable = ("is_active",)
    search_fields = ("email", "name")
