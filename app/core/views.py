from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

#
from .models import Person, Staff, Passenger, Flight, Aircraft
from .forms import FlightsForm, PassengerForm, StaffForm

"""
           HOME-LOGIN
"""
# Login Page


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'queryset'

    # Overwrite default 'get_queryset' method to get all the objects in the database
    def get_queryset(self):
        # Write the queryset of each object as key-value pair and pass all of them as a dictionary object
        queryset = {
                'flights': Flight.objects.all(),
                }
        return queryset


class AirportAppLoginView(LoginView):
    template_name = 'login.html'


"""
            PASSENGERS
"""


# Passengers Page
class PassengerListView(ListView):
    model = Passenger
    template_name = 'passengers.html'
    context_object_name = 'queryset'


class PassengerView(CreateView):
    model = Passenger
    template_name = "add_passenger.html"
    form_class = PassengerForm


class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passenger_detail.html'
    context_object_name = 'queryset'


"""
            FLIGHTS
"""


# Flights Page
class FlightListView(ListView):
    model = Flight
    template_name = 'flights.html'
    context_object_name = 'queryset'


# Flights Detail Page
class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight_detail.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Count available seats
        full_capacity = self.object.aircraft_id.capacity
        seats_taken = len(self.object.attendance.all())
        available = full_capacity - seats_taken

        # Add to context
        context.update({'available': available})
        print(context)

        return context


class FlightCreateView(CreateView):
    model = Flight
    template_name = 'flight_create.html'
    form_class = FlightsForm


class FlightUpdateView(UpdateView):
    model = Flight
    template_name = 'flight_update.html'
    form_class = FlightsForm


"""
           AIRCRAFT
"""


class AircraftListView(ListView):
    model = Aircraft
    template_name = 'aircrafts.html'
    context_object_name = 'queryset'


class AircraftCreateView(CreateView):
    model = Aircraft
    template_name = 'aircraft_create.html'
    fields = '__all__'


class AircraftDetailView(DetailView):
    model = Aircraft
    template_name = 'aircraft_details.html'
    context_object_name = 'queryset'


"""
           STAFF
"""


class StaffListView(ListView):
    model = Staff
    template_name = 'staff_list.html'
    context_object_name = 'queryset'


class StaffCreateView(CreateView):
    model = Staff
    template_name = "staff_create.html"
    form_class = StaffForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.request.email
        self.object.save()



class StaffUpdateView(UpdateView):
    model = Staff
    template_name = "staff_update.html"
    form_class = StaffForm


class StaffDetailView(DetailView):
    model = Staff 
    template_name = 'staff_detail.html'
    context_object_name = 'queryset'

