from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tax_number = models.IntegerField()

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

class Flight(models.Model):
    """
    Class that defines the model for a flight
    """
    # self.origin = origin
    # self.destination = destination
    # self.duration = duration
    # self.passenger_list = passenger_list
    flight_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departure_time = models.DateTimeField('Departure Time')
    duration = models.TimeField('Duration')
    aircraft_id = models.ForeignKey('Aircraft', on_delete=models.CASCADE)
    attendance = models.ManyToManyField(Passenger)

    def __str__(self):
        return f'Flight from {self.origin} to {self.destination}'


class Aircraft(models.Model):
    pass
    # def __init__(self, number_fly, place_land, fuel_up):
    #     self.number_fly = number_fly
    #     self.place_land = place_land
    #     self.fuel_up = fuel_up


# class Helicopter(Aircraft):
#     def __init__(self, model):
#         super().__init__()
#         self.model = model
# 
# 
# class Planes(Aircraft):
#     def __init__(self, model):
#         super().__init__()
#         self.model = model
# 
# 
# class Person:
#     def __init__(self, name, tax_number):
#         self.name = name
#         self.tax_number = tax_number
# 
# 
# class User(Person):
#     def __init__(self, passport):
#         super().__init__()
#         self.passport = passport
# 
# 
# class Staff(Person):
#     def __init__(self):
#         super().__init__()
# 
# # Create your models here.

'''
# Let's see the model of our project:

# Class:
# Login
# Flight
# Aircraft (parent), Helicopter(child), Airplane(child)
# Person(parent) User(child), Staff(user)

class Flight:
    def __init__(self, origin, destination, departure_date, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.departure_date = departure_date
        self.passenger_list = {}

    # As an airport assistant, I want to be able to generate a flight_attendees_list_report that lists passengers' names and passports to check identity.
    def flight_attendees_list_report(self):
        pass

    #  As an airport assistant, I want to be able to add passengers to a flight so I can sell tickets to them
    def add_passeneger(self, User):
        #self.passenger_list.
        pass

    # As an airport assistant, I want to be able to assign or change flight destinations or departure dates with user passwords.
    def change_flight_destination(self, destination):
        pass

    def change_flight_departure_date(self, departure_date):
        pass


class Aircraft:
    def __init__(self, fuel, flight_capacity):
        self.fuel = fuel
        self.flight_capacity = flight_capacity

    def fly_trip(self):
        #return "Let's go..."
        pass

    def land_trip(self):
        #return "Arriving..."
        pass

    def fuel_up(self):
        pass
        #return "Let's fuel up..."


class Helicopter(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model


class Planes(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model


class Person:
    def __init__(self, first_name, last_name, tax_number):
        self.first_name = first_name
        self.last_name = last_name
        self.tax_number = tax_number


class User(Person):
    def __init__(self, passport):
        super().__init__()
        self.passport = passport


class Staff(Person):
    def __init__(self):
        super().__init__()

    #  As an airport assistant, I want to be to create passengers with name AND passport number, so that I can add them flight.
    def create_passenger(self, first_name, last_name, passport):
        pass

    #As an airport assistant, I want to create a flight trip with a specific destination.
    def create_flight_trip(self, origin, duration, departure_date, destination):
        pass

class Login():
    pass
'''