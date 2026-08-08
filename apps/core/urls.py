from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.core.views import FloatingButtonViewSet, SiteSettingsView

router = DefaultRouter()
router.register("floating-buttons", FloatingButtonViewSet, basename="floating-button")

urlpatterns = [
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
]
urlpatterns += router.urls
