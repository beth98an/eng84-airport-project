from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView

#
from .models import Person, Staff, Passenger, Flight, Aircraft
from .forms import FlightsForm

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
    template_name = 'flight_detail.html'
    context_object_name = 'queryset'


class FlightCreateView(CreateView):
    model = Flight
    template_name = 'flight_create.html'
    form_class = FlightsForm

class FlightUpdateView(UpdateView):
    model = Flight
    template_name = 'flight_update.html'
    form_class = FlightsForm

class AircraftListView(ListView):
    model = Aircraft
    template_name = 'aircrafts.html'
    context_object_name = 'queryset'

class AircraftCreateView(CreateView):
    model = Aircraft 
    template_name = 'aircraft_create.html'
    fields = '__all__'

# class PassengerCreateView(CreateView):
#     model = Passenger
#     fields = '__all__'
#     template_name = 'passenger_create.html'
# 
