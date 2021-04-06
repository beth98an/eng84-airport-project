from django.contrib import admin
from .models import Person, Staff, Passenger


admin.site.register(Person)
admin.site.register(Passenger)
admin.site.register(Staff)
