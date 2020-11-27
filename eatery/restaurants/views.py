from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signUp(request):
    form = CreateUserForm()
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)

            form.save()
            return redirect('/login/')

    context = {'form': form}
    return render(request, 'signUp.html', context)


def login(request):

    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')
    context = {}
    return render(request, 'login.html', context)
