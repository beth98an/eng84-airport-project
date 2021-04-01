# command to install: pip install SQLAlchemy

# Let's see the model of our project:

# Class:
# Airport
# Terminal
# Flight
# Aircraft (parent), Helicopter(child), Airplane(child)
# Person(parent) User(child), Staff(user)

# We will use this class for destinations and origins
class Airport:
    def __init__(self, name_airport):
        self.name_airport = name_airport

class Terminal:
    def __init__(self, name_terminal):
        self.name_terminal = name_terminal

class Flight:
    def __init__(self, origin, destination, duration, passenger_list):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.passenger_list = passenger_list

class Aircraft:
    def __init__(self, number_fly, place_land, fuel_up):
        self.number_fly = number_fly
        self.place_land = place_land
        self.fuel_up = fuel_up

class Helicopter(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model

class Planes(Aircraft):
    def __init__(self, model):
        super().__init__()
        self.model = model

class Person:
    def __init__(self, name, tax_number):
        self.name = name
        self.tax_number = tax_number

class User(Person):
    def __init__(self, passport):
        super().__init__()
        self.passport = passport

class Staff(Person):
    def __init__(self):
        super().__init__()

