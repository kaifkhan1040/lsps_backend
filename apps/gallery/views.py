from apps.core.mixins import ActiveOnlyReadOnlyViewSet
from apps.gallery.models import Album
from apps.gallery.serializers import AlbumListSerializer, AlbumSerializer


class AlbumViewSet(ActiveOnlyReadOnlyViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AlbumSerializer
        return AlbumListSerializer
