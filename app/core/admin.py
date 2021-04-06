from django.contrib import admin
from .models import Person, User, Staff


admin.site.register(Person)
admin.site.register(User)
admin.site.register(Staff)
