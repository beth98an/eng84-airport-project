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


class User(Person):
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
# class Flight:
#     def __init__(self, origin, destination, duration, passenger_list):
#         self.origin = origin
#         self.destination = destination
#         self.duration = duration
#         self.passenger_list = passenger_list
# 
# 
# class Aircraft:
#     def __init__(self, number_fly, place_land, fuel_up):
#         self.number_fly = number_fly
#         self.place_land = place_land
#         self.fuel_up = fuel_up
# 
# 
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
