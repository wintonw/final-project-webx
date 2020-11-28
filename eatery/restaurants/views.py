from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreateUserForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Menu, Order
from .decorators import unauthenticated_user, allowed_users
# Create your views here.
User = get_user_model()


def index(request):
    return render(request, 'index.html')


@unauthenticated_user
def signUp(request):
    form = CustomCreateUserForm()
    if (request.method == 'POST'):
        form = CustomCreateUserForm(request.POST)
        if (form.is_valid()):

            user = form.save()
            email = form.cleaned_data.get('email')
            # register as customer
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account was created for " + email)

            return redirect('restaurants:login')

    context = {'form': form}
    return render(request, 'signUp.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # good exist
            login(request, user)
            return redirect('restaurants:index')
        else:
            messages.info(request, 'Username or Password is INCORRECT')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('restaurants:login')


@login_required(login_url='restaurants:login')
@allowed_users(allowed_roles=['customer'])
def orders(request):
    context = {}
    return render(request, 'customer_orders.html', context)


def menu(request):
    menu = Menu.objects.all()

    context = {'menu': menu,
               }
    return render(request, 'menu.html', context)


def cart(request):
    optionsOneToTen = list(range(1, 11))
    context = {}
    return render(request, 'cart.html', context)
