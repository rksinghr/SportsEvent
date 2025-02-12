# forms.py
from django import forms
from .models import athleteRegistration

class AthRegForm(forms.ModelForm):
    class Meta:
        model = athleteRegistration
        exclude = ['eventName', 'email', 'mob', 'published_date']
