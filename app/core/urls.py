from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

from .views import HomeView, FlightListView

urlpatterns = [
        path('', HomeView.as_view(), name='index'),
        path('home/', HomeView.as_view(), name='index'),
        path('flights/', FlightListView.as_view(), name='flights'),
        path('passengers/', HomeView.as_view(), name='passengers'),
        ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
