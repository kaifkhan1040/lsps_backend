from django.contrib import admin

from apps.pages.models import (
    AboutUs, ChairmanMessage, HomeContent, PrincipalMessage,
    QuickLink, SchoolHighlight, WhyChooseUs,History,Infrastructure
)

class BaseInline(admin.TabularInline):
    extra = 0
    show_change_link = True


class HistoryInline(BaseInline):
    model = History
    fields = ("year", "title", "description")

class InfrastructureInline(BaseInline):
    model = Infrastructure
    fields = ("image", "title", "description")

class SingletonAdminMixin:
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(HomeContent)
class HomeContentAdmin(SingletonAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ChairmanMessage)
class ChairmanMessageAdmin(SingletonAdminMixin, admin.ModelAdmin):
    pass


@admin.register(PrincipalMessage)
class PrincipalMessageAdmin(SingletonAdminMixin, admin.ModelAdmin):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    inlines = [
            HistoryInline,InfrastructureInline
        ]


@admin.register(SchoolHighlight)
class SchoolHighlightAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)


# @admin.register(QuickLink)
# class QuickLinkAdmin(admin.ModelAdmin):
#     list_display = ("title", "url", "order", "is_active")
#     list_editable = ("order", "is_active")
#     search_fields = ("title",)
