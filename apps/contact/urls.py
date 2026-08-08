from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.contact.views import ContactDetailView, ContactMessageViewSet

router = DefaultRouter()
router.register("messages", ContactMessageViewSet, basename="contact-message")

urlpatterns = [
    path("details/", ContactDetailView.as_view(), name="contact-details"),
]
urlpatterns += router.urls
