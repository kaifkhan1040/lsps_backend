from django.contrib import admin

from apps.sliders.models import AdmissionPopupSettings, BannerSlide,PopUpWindow


class SingletonpopAdminMixin:
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(BannerSlide)
class BannerSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "cta_type",  "is_active")
    list_editable = ( "is_active",)
    list_filter = ("cta_type", "is_active")
    search_fields = ("title", "subtitle")

@admin.register(PopUpWindow)
class PopUpWindowAdmin(SingletonpopAdminMixin,admin.ModelAdmin):
    pass


# @admin.register(AdmissionPopupSettings)
# class AdmissionPopupSettingsAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return not AdmissionPopupSettings.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         return False
