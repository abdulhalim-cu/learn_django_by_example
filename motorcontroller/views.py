from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpFrom


def index(request):
    return render(request, 'motorcontroller/index.html', {})


def signup(request):
    if request.method=='POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/controller/')
    else:
        form = SignUpFrom()
    return render(request, 'motorcontroller/signup.html', {'form': form})