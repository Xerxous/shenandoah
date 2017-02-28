import os, sys, django
DJANGO_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

#Django setup to import models
sys.path.append(DJANGO_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'plase.settings'
django.setup()
from apps.search.models import Apartment, Landlord
