from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    # ticket_number = models.IntegerField((), unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Staff(Person):
    employee_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Note: Renamed from User to avoid conflicts
class Passenger(Person):
    """
    Class that defines the passenger users.
    """
    passport_num = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("passenger_detail", args=[str(self.pk)])


class Flight(models.Model):
    """
    Class that defines the model for a flight
    """
    flight_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departure_time = models.DateTimeField('Departure Time')
    duration = models.TimeField('Duration')
    aircraft_id = models.ForeignKey('Aircraft', on_delete=models.CASCADE)
    attendance = models.ManyToManyField(Passenger, blank=True)

    # Method that finds the url of a particular flight, given its id
    def get_absolute_url(self):
        return reverse('flight_detail', args=[str(self.flight_id)])

    # Method that makes the flight look pretty when printed (made into string)
    def __str__(self):
        return f'Flight from {self.origin} to {self.destination}'


class Aircraft(models.Model):
    """
    Class that holds the type of aircraft
    """
    aircraft_id = models.AutoField(primary_key=True, null=False, blank=False)
    model = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.model} no{self.aircraft_id} by {self.manufacturer}'

    def get_absolute_url(self):
        return reverse("aircraft_details", args=[str(self.aircraft_id)])


# class Airport:
#     def __init__(self, name_airport):
#         self.name_airport = name_airport
# 
# 
# class Terminal:
#     def __init__(self, name_terminal):
#         self.name_terminal = name_terminal
# 
# 

