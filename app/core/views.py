from django.shortcuts import render

from django.views.generic import ListView

#
from .models import Person, Staff, User

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World")

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'queryset'

    # Overwrite default 'get_queryset' method to get all the objects in the database
    def get_queryset(self):
        # Write the queryset of each object as key-value pair and pass all of them as a dictionary object
        queryset = {
                'persons': Person.objects.all(),
                'staff': Staff.objects.all(),
                'users': User.objects.all(),
                }
        return queryset
