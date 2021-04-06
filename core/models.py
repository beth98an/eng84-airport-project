# command to install: pip install SQLAlchemy

# Let's see the model of our project:

# Class:
# Airport
# Terminal
# Flight
# Aircraft (parent), Helicopter(child), Airplane(child)
# Person(parent) User(child), Staff(user)

# NOT SURE IF WE WILL NEED THIS CLASS
# We will use this class for destinations and origins
#class Airport:
#    def __init__(self, name_airport):
#        self.name_airport = name_airport


class Terminal:
    def __init__(self, name_terminal):
        self.name_terminal = name_terminal


class Flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.passenger_list = {}

    def flight_attendees_list_report(self):
        return "Here is the list with the name and passport..."

    def add_passeneger(self):
        #self.passenger_list.
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
            def create_passenger(self):
        pass

    def create_flight_trip(self):
        pass

