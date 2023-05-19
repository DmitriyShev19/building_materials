from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['avatar', 'first_name', 'last_name', 'email',
                  'phone_numbers', 'city', 'street', 'house_number']
