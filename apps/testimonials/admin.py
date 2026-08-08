from django.contrib import admin

from apps.testimonials.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "student_class", "rating", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("rating", "is_active")
    search_fields = ("parent_name", "student_name", "message")
