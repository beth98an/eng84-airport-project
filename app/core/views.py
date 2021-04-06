from django.shortcuts import render

from django.views.generic import ListView, DetailView

#
from .models import Person, Staff, Passenger, Flight

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World")

# Login Page
class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'queryset'

    # Overwrite default 'get_queryset' method to get all the objects in the database
    def get_queryset(self):
        # Write the queryset of each object as key-value pair and pass all of them as a dictionary object
        queryset = {
                'persons': Person.objects.all(),
                'staff': Staff.objects.all(),
                'passengers': Passenger.objects.all(),
                }
        return queryset


# Flights Page
class FlightListView(ListView):
    model = Flight
    template_name = 'flights.html'
    context_object_name = 'queryset'

# Passengers Page
class PassengerListView(ListView):
    model = Passenger
    template_name = 'passengers.html'
    context_object_name = 'queryset'


# Flights Detail Page
class FlightDetailView(DetailView):
    model = Flight

