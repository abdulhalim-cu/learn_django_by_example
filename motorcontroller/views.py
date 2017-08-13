from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import SignUpFrom, UserProfileForm, DeviceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url='motorcontroller:login')
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


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/controller/')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'motorcontroller/profile.html', {'form': form})


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password successfully updated')
            return redirect('/controller/login/')
        else:
            messages.error(request, 'please correct the error below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'motorcontroller/password_change.html', {'form':form})


@login_required
def register_device(request):
    if request.POST:
        form = DeviceForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            register.user = request.user
            register.save()
            messages.success(request, 'Registered Successfully')
            return redirect('motorcontroller:register_device')
        else:
            messages.error(request, 'Please Enter a valid device_id')
    else:
        form = DeviceForm()
    return render(request, 'motorcontroller/register_device.html', {'form':form})
