from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.sliders.views import AdmissionPopupSettingsView, BannerSlideViewSet

router = DefaultRouter()
router.register("banners", BannerSlideViewSet, basename="banner-slide")

urlpatterns = [
    path("admission-popup/", AdmissionPopupSettingsView.as_view(), name="admission-popup"),
]
urlpatterns += router.urls
