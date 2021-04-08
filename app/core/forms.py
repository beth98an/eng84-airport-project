from django import forms
from django.forms.models import ModelForm
# from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# from crispy_forms.layout import Submit, Layout, Div, Fieldset
from bootstrap_datepicker_plus import DateTimePickerInput, TimePickerInput, DatePickerInput

from .models import Flight, Aircraft, Passenger, Staff


class FlightsForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('origin', 'destination', 'departure_time', 'duration', 'aircraft_id', 'attendance', 'crew')

        widgets = {
                'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stansted'}),
                'destination': forms.TextInput(attrs={'class': 'form-control'}),
                'departure_time': DateTimePickerInput(),
                'duration': TimePickerInput(attrs={'class': 'form-control'}),
                'aircraft_id': forms.Select(attrs={'class': 'form-control'}),
                'attendance': forms.SelectMultiple(attrs={'class': 'form-control'}),
                'crew': forms.SelectMultiple(attrs={'class': 'form-control'})
                }


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('first_name', 'last_name', 'dob', 'passport_num')

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control', }),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'dob': DatePickerInput(attrs={'label': 'Date of Birth'}),
                'passport_num': forms.TextInput(attrs={'class': 'form-control'}),
                }
        labels = {
                'dob': _('Date of Birth'),
                'passport_num': _('Passport Number')
                }


class StaffForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Staff 
        fields = ('first_name', 'last_name', 'dob', 'email',  'role', 'password', 'password_confirm')


        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control', }),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                'dob': DatePickerInput(attrs={'label': 'Date of Birth'}),
                'role': forms.Select(attrs={'class': 'form-control'}),
                }

        labels = {
                'dob': _('Date of Birth'),
                }

    def clean(self, *args, **kwargs):
        data = super().clean()
        print()
        print(data)
        print()
        password1 = self.cleaned_data.get('password', None)
        password2 = self.cleaned_data.get('password_confirm', None)
        print(f'Got passwords: {password1} and {password2}')
        if password1 and password2:
            if password1 == password2:
                return data
            else:
                raise forms.ValidationError(_('Passwords do not match'))
            return data
        else:
            raise ValidationError(_('Password field is empty'))
        return None


# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff 
#         fields = ('first_name', 'last_name', 'dob', 'email', 'role', 'password')
# 
#         widgets = {
#                 'email': forms.EmailInput(attrs={'class': 'form-control'}),
#                 'password': forms.PasswordInput(attrs={'class': 'form-control'}),
#                 'first_name': forms.TextInput(attrs={'class': 'form-control', }),
#                 'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#                 'dob': DatePickerInput(),
#                 'role': forms.TextInput(attrs={'class': 'form-control'}),
# 
#                 }
# 
#         labels = {
#                 'dob': _('Date of Birth'),
#                 }
