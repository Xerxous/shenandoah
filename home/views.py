from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from itertools import chain
from .models import Apartment, Landlord
from .search import search, verify

def auth(request):
    if request.method == 'POST':
        name = request.POST['username'].lower()
        user = authenticate(username=name, password=request.POST['password'])
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login.html', {'invalid': 'Invalid username or password.'})

    if request.user.is_authenticated():
        return redirect('home:index')
    return render(request, 'login.html')

@login_required
def landing(request):
    context = dict()
    apt = Apartment.objects.all()
    ll = Landlord.objects.all()
    if request.method == 'GET':
        context['apt'] = apt.all()
        context['ll'] = ll.all()
    elif request.method == 'POST':
        print(request.POST)
        error_msg = verify(request.POST)
        if error_msg:
            context['error_msg'] = error_msg
        else:
            #FIELDS: zip, low, high, name, room[], area
            apt_results = search(apt, request.POST, 'apt')
            context['apt'] = apt_results['queryset']
            context['ll'] = search(ll, request.POST, 'll')['queryset']
            context['feedback'] = apt_results['feedback']
    return render(request, 'index.html', context)

@login_required
def detail(request, id):
    return render(request, 'details.html')


@login_required
def sign_out(request):
    logout(request)
    return redirect('home:login')
