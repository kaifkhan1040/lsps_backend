from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.newsevents.models import (
    Announcement, Circular, Event, News, NoticeBoardItem,
)
from apps.newsevents.serializers import (
    AnnouncementSerializer, CircularSerializer, EventSerializer,
    NewsSerializer, NoticeBoardItemSerializer,
)


class NewsViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class EventViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AnnouncementViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class CircularViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Circular.objects.all()
    serializer_class = CircularSerializer
    filterset_fields = ["class_category"]


class NoticeBoardItemViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = NoticeBoardItem.objects.all()
    serializer_class = NoticeBoardItemSerializer
