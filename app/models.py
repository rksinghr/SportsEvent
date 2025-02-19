from django.db import models
from django.utils import timezone

class athleteRegistration(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    eventName = models.CharField(max_length=50)
    # eventType = models.CharField(max_length=50)
    eventCategory = models.IntegerField(default=0)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mob = models.CharField(max_length=50)
    bibNumber = models.CharField(max_length=50, default="New")
    registratioDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.firstName

class raceMaster(models.Model):
    name = models.CharField(max_length=50)
    raceType = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    regStartDate = models.DateField(blank=True, null=True)
    regEndDate = models.DateField(blank=True, null=True)

    @property
    def is_Active(self):
        if self.regStartDate < timezone.now().date() and self.regEndDate > timezone.now().date():
            return 0
        elif self.regStartDate < timezone.now().date() and self.regEndDate < timezone.now().date():
            return 1
        else:
            return 2

    def __str__(self):
        return self.name
