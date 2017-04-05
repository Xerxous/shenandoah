from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Apartment, Landlord

@login_required
def search(request):
    pass
