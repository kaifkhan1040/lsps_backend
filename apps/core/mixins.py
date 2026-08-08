from rest_framework import mixins, viewsets


class PublicCreateOnlyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Used for anonymous-facing forms (admission enquiry, school-visit
    booking, contact message, admission-popup lead). The public can
    only POST/create; listing, retrieving, updating and deleting is
    intentionally left out of the public API and handled through
    Django Admin instead.
    """
    pass


class ActiveOnlyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only viewset that automatically filters to is_active=True
    for the public API, when the model defines that field.
    """
    def get_queryset(self):
        qs = super().get_queryset()
        if hasattr(qs.model, "is_active"):
            qs = qs.filter(is_active=True)
        return qs
