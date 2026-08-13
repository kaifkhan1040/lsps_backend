from django.contrib import admin

from apps.infrastructure.models import Facility


# @admin.register(Facility)
# class FacilityAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "order", "is_active")
#     list_editable = ("order", "is_active")
#     list_filter = ("category", "is_active")
#     search_fields = ("title", "description")
