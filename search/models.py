from django.db import models

# Create your models here.
class Apartment(models.Model):
    agency = models.CharField(max_length=50, default='')
    individual = models.CharField(max_length=30, default='')
    number = models.CharField(max_length=12, default='') # Phone Number including dashes
    email = models.CharField(max_length=20, default='') #optional
    building = models.CharField(max_length=50, default='')
    st_one = models.CharField(max_length=50, default='')
    st_two = models.CharField(max_length=50, default='') #optional
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=2, default='') #2 state acrynoym
    low = models.IntegerField(default=0)
    high = models.IntegerField(default=0)
    rooms = models.BooleanField(default=False)
    studio = models.BooleanField(default=False)
    one_br = models.BooleanField(default=False)
    two_br = models.BooleanField(default=False)
    three_br = models.BooleanField(default=False)
    notes = models.CharField(max_length=500, default='') #optional

class Landlord(models.Model):
    pass
