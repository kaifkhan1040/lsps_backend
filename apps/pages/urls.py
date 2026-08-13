from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.pages.views import (
    AboutUsView, ChairmanMessageView, HomeContentView,
    PrincipalMessageView, QuickLinkViewSet, SchoolHighlightViewSet,
    WhyChooseUsViewSet,
)

router = DefaultRouter()
router.register("highlights", SchoolHighlightViewSet, basename="school-highlight")
# router.register("home", HomeContentView, basename="school-homecontent")
router.register("why-choose-us", WhyChooseUsViewSet, basename="why-choose-us")
router.register("quick-links", QuickLinkViewSet, basename="quick-link")

urlpatterns = [
    path("home-content/", HomeContentView.as_view(), name="home-content"),
    path("chairman-message/", ChairmanMessageView.as_view(), name="chairman-message"),
    path("principal-message/", PrincipalMessageView.as_view(), name="principal-message"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
]
urlpatterns += router.urls
