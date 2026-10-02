from django.contrib import admin

from apps.sliders.models import AdmissionPopupSettings, BannerSlide,PopUpWindow


class SingletonpopAdminMixin:
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(BannerSlide)
class BannerSlideAdmin(admin.ModelAdmin):
    list_display = ("display_title", "cta_type",  "is_active")
    list_editable = ("is_active",)
    list_filter = ("cta_type", "is_active")
    search_fields = ("title", "subtitle")
    exclude = ("order",)
    # Custom method to handle empty titles
    def display_title(self, obj):
        if obj.title and obj.title.strip():
            return obj.title
        return f"Banner Slide Object ({obj.id})"
    
    # Keeps the column header named "TITLE" instead of "DISPLAY TITLE"
    display_title.short_description = "Title"

@admin.register(PopUpWindow)
class PopUpWindowAdmin(SingletonpopAdminMixin,admin.ModelAdmin):
    pass


# @admin.register(AdmissionPopupSettings)
# class AdmissionPopupSettingsAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not AdmissionPopupSettings.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         return False
