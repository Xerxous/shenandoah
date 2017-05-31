from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from itertools import chain
from .models import Apartment, Landlord, Log
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
def show_logs(request):
    return render(request, 'log.html', { 'logs': reversed(Log.objects.all()) })

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
    obj = Apartment.objects.filter(id=id).last()
    message = 'Deleted apartment object %s' % (obj.entity)
    Log.objects.create(account=request.user, activity=message)
    if obj:
        obj.delete()
    return redirect('home:index')

@login_required
def ll_delete(request, id):
    obj = Landlord.objects.filter(id=id).last()
    message = 'Deleted landlord object %s' % (obj.entity)
    Log.objects.create(account=request.user, activity=message)
    if obj:
        obj.delete()
    return redirect('home:index')

@login_required
def create(request):
    return render(request, 'form.html')

@login_required
def edit(request, cat, id):
    context = dict()
    if int(cat):
        context['nav'] = 'apt'
        context['obj'] = Apartment.objects.get(id=id)
    else:
        print('test')
        context['nav'] = 'll'
        context['obj'] = Landlord.objects.get(id=id)
    phone_number_slice = context['obj'].number.split('-')
    context['phone_one'] = phone_number_slice[0]
    context['phone_two'] = phone_number_slice[1]
    context['phone_three'] = phone_number_slice[2]
    return render(request, 'form.html', context)

@login_required
def create_apt(request):
    if request.method == 'POST':
        post = request.POST
        state = post['state']
        rooms = False
        studio = False
        one_br = False
        two_br = False
        three_br = False
        phone = '%s-%s-%s' % (post['phone1'], post['phone2'], post['phone3'])
        res_list = request.POST.getlist('res', False)
        for res in res_list:
            if res == 'rooms':
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
        else:
            low = post['low']
            high = post['high']

        message = 'Created apartment object %s' % (post['agency'])
        Log.objects.create(account=request.user, activity=message)

        Apartment.objects.create(
            entity=post['agency'], number=phone, email=post['email'],
            st_one=post['paddress'], st_two=post['saddress'], area=post['area'],
            state=state, zipcode=post['zip'], low=low,
            high=high, cost_notes=post['cost_notes'], rooms=rooms,
            studio=studio, one_br=one_br, two_br=two_br,
            three_br=three_br, notes=post['notes'])
    return redirect('home:index')

@login_required
def create_ll(request):
    if request.method == 'POST':
        post = request.POST
        state = post['state']
        rooms = False
        studio = False
        one_br = False
        two_br = False
        three_br = False
        phone = '%s-%s-%s' % (post['phone1'], post['phone2'], post['phone3'])
        for res in request.POST.getlist('res', False):
            if res == 'rooms':
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
        else:
            low = post['low']
            high = post['high']

        message = 'Created landlord object %s' % (post['agency'])
        Log.objects.create(account=request.user, activity=message)

        Landlord.objects.create(
            entity=post['name'], number=phone, email=post['email'],
            st_one=post['paddress'], st_two=post['saddress'], city=post['area'],
            state=state, zipcode=post['zip'], low=low,
            high=high, rooms=rooms, studio=studio,
            one_br=one_br, two_br=two_br, three_br=three_br,
            notes=post['notes'])
    return redirect('home:index')

def edit_apt(request, id):
    if request.method == 'POST':
        post = request.POST
        state = post['state']
        rooms = False
        studio = False
        one_br = False
        two_br = False
        three_br = False
        phone = '%s-%s-%s' % (post['phone1'], post['phone2'], post['phone3'])
        res_list = request.POST.getlist('res', False)
        for res in res_list:
            if res == 'rooms':
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
        else:
            low = post['low']
            high = post['high']

        message = 'Edited apartment object %s' % (post['agency'])
        Log.objects.create(account=request.user, activity=message)

        apartment = Apartment.objects.get(id=id)
        apartment.entity = post['agency']
        apartment.number = phone
        apartment.email = post['email']
        apartment.st_one = post['paddress']
        apartment.st_two = post['saddress']
        apartment.area = post['area']
        apartment.state = state
        apartment.zipcode = post['zip']
        apartment.low = low
        apartment.high = high
        apartment.cost_notes = post['cost_notes']
        apartment.rooms = rooms
        apartment.studio = studio
        apartment.one_br = one_br
        apartment.two_br = two_br
        apartment.three_br = three_br
        apartment.notes = post['notes']
        apartment.save()
    return redirect('home:index')

def edit_ll(request, id):
        if request.method == 'POST':
            post = request.POST
            state = post['state']
            rooms = False
            studio = False
            one_br = False
            two_br = False
            three_br = False
            phone = '%s-%s-%s' % (post['phone1'], post['phone2'], post['phone3'])
            for res in request.POST.getlist('res', False):
                if res == 'rooms':
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
            else:
                low = post['low']
                high = post['high']

            message = 'Edited landlord object %s' % (post['agency'])
            Log.objects.create(account=request.user, activity=message)

            landlord = landlord.objects.get(id=id)
            landlord.entity = post['name']
            landlord.number = phone
            landlord.email = post['email']
            landlord.st_one = post['paddress']
            landlord.st_two = post['saddress']
            landlord.city = post['area']
            landlord.state = state
            landlord.zipcode = post['zip']
            landlord.low = low
            landlord.high = high
            landlord.rooms = rooms
            landlord.studio = studio
            landlord.one_br = one_br
            landlord.two_br = two_br
            landlord.three_br = three_br
            landlord.notes = post['notes']
            landlord.save()
        return redirect('home:index')

@login_required
def sign_out(request):
    logout(request)
    return redirect('home:login')
