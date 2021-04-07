from django.test import TestCase

from ..models import Passenger

# We will test if a Passenger was created
class PassengerTestCase(TestCase):
    def setUp(self):
        #Passenger.objects.create(first_name="Juan", last_name="Bond", tax_number=123, passport_num="dads34")
        #Passenger.objects.create(first_name="Mattie", last_name="Williams", tax_number=245, passport_num="asd123")
        #Passenger.objects.create(name="Juan")
        Passenger.first_name = "Juan"
        Passenger.last_name = "Bond"
        Passenger.tax_number = 123
        Passenger.passport_num = "dads34"

    def test_passenger_test(self):
        passenger1 = Passenger.objects.get(first_name="Juan")
        #passenger2 = Passenger.objects.get(first_name="Mattie", last_name="Williams", tax_number=245, passport_num="asd123")
        self.assertEqual(passenger1.first_name, "Juan")
        #self.assertEqual(passenger2, "Mattie")
        #new_passeneger = Passenger.objects.get(name="Juan")
        #self.assertEqual(new_passeneger.name, "Juan")
