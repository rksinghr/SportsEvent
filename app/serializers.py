# myapp/serializers.py

from rest_framework import serializers
from .models import athleteRegistration

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = athleteRegistration
        fields = ['firstName', 'lastName', 'dob', 'eventName', 'gender', 'email', 'mob']
