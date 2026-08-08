from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.testimonials.models import Testimonial
from apps.testimonials.serializers import TestimonialSerializer


class TestimonialViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
