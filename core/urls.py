from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'detailpls', views.DetailplViewSet)
router.register(r'follows', views.FollowViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]