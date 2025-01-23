from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .utils import logout_required

# message
from django.contrib import messages


# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


@logout_required
def user_signup(request):
    # if request.user.is_authenticated: #####if not use custom @logout_required decorator
    #     return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', context={'form': form})


def user_login(request):
    # @logout_required  #####if not use request.user.is_authenticated:
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            print(form.errors)
            messages.warning(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')


@login_required
def change_password(request):
    user = request.user
    form = PasswordChangeForm(user)
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('change_password')
    return render(request, 'change_password.html', context={'form': form})
