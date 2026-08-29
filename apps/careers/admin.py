from django.contrib import admin

from apps.careers.models import JobApplication, JobPosition


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    """HR's workflow tool: every application lands here with a status
    that can be updated as candidates move through the hiring pipeline."""
    list_display = (
        "full_name", "position", "mobile_number", "email",
        "status", "created_at",
    )
    # list_editable = ("status",)
    list_filter = ("status", "position", "created_at")
    search_fields = ("full_name", "email", "mobile_number")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
