from django.contrib import admin

from apps.contact.models import (
    ContactDetail, ContactMessage, PhoneNumber, SocialMediaLink,
)


@admin.register(ContactDetail)
class ContactDetailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactDetail.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("number", "label", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "subject", "is_read", "created_at")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
