from django import forms
from django.forms.models import ModelForm
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from .models import Flight, Aircraft, Passenger


class FlightsForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('origin', 'destination', 'departure_time', 'duration', 'aircraft_id', 'attendance')

        widgets= {
                'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stansted'}),
                'destination': forms.TextInput(attrs={'class': 'form-control'}),
                'departure_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
                'duration': forms.TimeInput(attrs={'class': 'form-control'}),
                'aircraft_id': forms.Select(attrs={'class': 'form-control'}),
                'attendance': forms.SelectMultiple(attrs={'class': 'form-control',}),
                }
