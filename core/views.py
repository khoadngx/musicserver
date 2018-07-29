from core.models import Song, User, Playlist, Detailpl, Follow
from core.serializers import SongSerializer, UserSerializer, PlaylistSerializer, DetailplSerializer, FollowSerializer
from rest_framework import viewsets, filters

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    ordering = ('usrname',)
    search_fields = ('name',)

class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    ordering = ('id',)
    search_fields = ('name',)


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (filters.OrderingFilter,filters.SearchFilter,)
    ordering = ('id',)
    search_fields = ('name',)

class DetailplViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Detailpl.objects.all()
    serializer_class = DetailplSerializer

class FollowViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer