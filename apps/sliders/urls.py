from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.sliders.views import AdmissionPopupSettingsView, BannerSlideViewSet,PopUpWindowViewSet

router = DefaultRouter()
router.register("banners", BannerSlideViewSet, basename="banner-slide")
router.register("popup", PopUpWindowViewSet, basename="PopUp-Window")

urlpatterns = [
    path("admission-popup/", AdmissionPopupSettingsView.as_view(), name="admission-popup"),
]
urlpatterns += router.urls
