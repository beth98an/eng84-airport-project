from django.urls import path
from . import views

from .views import HomeView, FlightListView

urlpatterns = [
        path('', HomeView.as_view(), name='index'),
        path('home/', HomeView.as_view(), name='index'),
        path('flights/', FlightListView.as_view(), name='flights'),
        ]

