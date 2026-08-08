from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Little Star Public School — Admin"
admin.site.site_title = "LSPS Admin"
admin.site.index_title = "Website Content Management"

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/core/", include("apps.core.urls")),
    path("api/pages/", include("apps.pages.urls")),
    path("api/sliders/", include("apps.sliders.urls")),
    path("api/testimonials/", include("apps.testimonials.urls")),
    path("api/academics/", include("apps.academics.urls")),
    path("api/admissions/", include("apps.admissions.urls")),
    path("api/infrastructure/", include("apps.infrastructure.urls")),
    path("api/student-life/", include("apps.studentlife.urls")),
    path("api/news-events/", include("apps.newsevents.urls")),
    path("api/gallery/", include("apps.gallery.urls")),
    path("api/downloads/", include("apps.downloads.urls")),
    path("api/contact/", include("apps.contact.urls")),

    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
