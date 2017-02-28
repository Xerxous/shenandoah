from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

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
    return render(request, 'index.html')

@login_required
def sign_out(request):
    logout(request)
    return redirect('home:login')
