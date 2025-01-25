from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    eMail = models.EmailField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mobNumber = models.CharField(max_length=15, blank=True, null=True)
    altMobNumber = models.CharField(max_length=15, blank=True, null=True)
    addressLine1 = models.TextField(blank=True, null=True)
    addressLine2 = models.TextField(blank=True, null=True)
    pin = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    academy = models.CharField(max_length=100, blank=True, null=True)
    aadhar = models.CharField(max_length=100, blank=True, null=True)
    sport = models.CharField(max_length=100, blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

class otpBank(models.Model):
    key_user = models.CharField(max_length=100)
    otp_secret_key = models.CharField(max_length=50)
    otp_valid_date = models.DateTimeField()
    
    def __str__(self):
        return self.key_user