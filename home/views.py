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
def apt_detail(request, id):
    context = dict()
    context['obj'] = Apartment.objects.get(id=id)
    context['obj_type'] = 1
    return render(request, 'details.html', context)

@login_required
def ll_detail(request, id):
    context = dict()
    context['obj'] = Landlord.objects.get(id=id)
    context['obj_type'] = 0
    return render(request, 'details.html', context)

@login_required
def apt_delete(request, id):
    Apartment.objects.get(id=id).delete()
    return redirect('home:index')

@login_required
def ll_delete(request, id):
    Landlord.objects.get(id=id).delete()
    return redirect('home:index')

@login_required
def create(request):
    return render(request, 'form.html')

def create_apt(request):
    post = request.POST
    state = 'MD'
    low = post['low']
    high = post['high']
    rooms = False
    studio = False
    one_br = False
    two_br = False
    three_br = False
    for res in request.POST.getlist('res', False):
        if res == 'room':
            rooms = True
        elif res == 'studio':
            studio = True
        elif res == 'one_br':
            one_br = True
        elif res == 'two_br':
            two_br = True
        elif res == 'three_br':
            three_br = True

    if post['cost_notes']:
        low = 0
        high = 0
    Apartment.objects.create(entity=post['agency'], number=post['phone'], email=post['email'],
                             st_one=post['paddress'], st_two=post['saddress'], area=post['area'],
                             state=state, zipcode=post['zip'], low=low,
                             high=high, cost_notes=post['cost_notes'], rooms=rooms,
                             studio=studio, one_br=one_br, two_br=two_br,
                             three_br=three_br, notes=post['notes'])
    return redirect('home:index')

def create_ll(request):
    post = request.POST
    state = 'MD'
    low = post['low']
    high = post['high']
    rooms = False
    studio = False
    one_br = False
    two_br = False
    three_br = False
    for res in request.POST.getlist('res', False):
        if res == 'room':
            rooms = True
        elif res == 'studio':
            studio = True
        elif res == 'one_br':
            one_br = True
        elif res == 'two_br':
            two_br = True
        elif res == 'three_br':
            three_br = True

    if post['cost_notes']:
        low = 0
        high = 0
    Landlord.objects.create(entity=post['agency'], number=post['phone'], email=post['email'],
                             st_one=post['paddress'], st_two=post['saddress'], city=post['area'],
                             state=state, zipcode=post['zip'], low=low,
                             high=high, rooms=rooms, studio=studio,
                             one_br=one_br, two_br=two_br, three_br=three_br,
                             notes=post['notes'])
    return redirect('home:index')


@login_required
def sign_out(request):
    logout(request)
    return redirect('home:login')
