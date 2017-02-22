from django.db import models

# Create your models here.
class Apartment(models.Model):
    agency = models.CharField(max_length=50, default='', blank=False)
    number = models.CharField(max_length=12, default='', blank=False) # Phone Number including dashes
    email = models.CharField(max_length=20, default='') #optional
    building = models.CharField(max_length=50, default='') #optional
    st_one = models.CharField(max_length=50, default='', blank=False)
    st_two = models.CharField(max_length=50, default='') #optional
    area = models.CharField(max_length=20, default='', blank=False)
    state = models.CharField(max_length=2, default='') #2 state acrynoym
    zipcode = models.CharField(max_length=5, default='', blank=False)
    low = models.IntegerField(default=0, blank=False)
    high = models.IntegerField(default=0, blank=False)
    cost_notes = models.CharField(max_length=50, default='') #optional
    rooms = models.BooleanField(default=False, blank=False)
    studio = models.BooleanField(default=False, blank=False)
    one_br = models.BooleanField(default=False, blank=False)
    two_br = models.BooleanField(default=False, blank=False)
    three_br = models.BooleanField(default=False, blank=False)
    notes = models.CharField(max_length=500, default='') #optional

    def __unicode__(self):
        return self.agency

    class Meta:
        verbose_name_plural = "Apartments"

class Landlord(models.Model):
    individual = models.CharField(max_length=50, default='', blank=False)
    number = models.CharField(max_length=12, default='', blank=False) # Phone Number including dashes
    email = models.CharField(max_length=20, default='') #optional
    building = models.CharField(max_length=50, default='') #optional
    st_one = models.CharField(max_length=50, default='') #optional
    st_two = models.CharField(max_length=50, default='') #optional
    city = models.CharField(max_length=20, default='')  #optional
    state = models.CharField(max_length=2, default='') #2 state acrynoym, optional
    zipcode = models.CharField(max_length=5, default='', blank=False)
    low = models.IntegerField(default=0, blank=False)
    high = models.IntegerField(default=0, blank=False)
    cost_notes = models.CharField(max_length=50, default='') #optional
    rooms = models.BooleanField(default=False, blank=False)
    studio = models.BooleanField(default=False, blank=False)
    one_br = models.BooleanField(default=False, blank=False)
    two_br = models.BooleanField(default=False, blank=False)
    three_br = models.BooleanField(default=False, blank=False)
    notes = models.CharField(max_length=500, default='') #optional

    def __unicode__(self):
        return self.indiidual + ': ' + self.st_one

    class Meta:
        verbose_name_plural = "Apartments"
