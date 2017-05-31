from django.contrib import admin
from .models import Apartment, Landlord, Log

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Landlord)
admin.site.register(Log)
