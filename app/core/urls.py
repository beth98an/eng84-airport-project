from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
        path('', HomeView.as_view(), name='index'),
        path('/home', HomeView.as_view(), name='home'),
        path('/flights', HomeView.as_view(), name='flights'),
        path('/passengers', HomeView.as_view(), name='index'),
        ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

