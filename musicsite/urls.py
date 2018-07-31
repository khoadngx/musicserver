from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('validate_usrname', views.validate_usrname, name='validate_usrname'),
    path('profile/<str:usrname>', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)