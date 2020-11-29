from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreateUserForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Account, Menu, Order
from .decorators import unauthenticated_user, allowed_users
from .util import calculatePrice, cartItems
import json
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
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

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
# @allowed_users(allowed_roles=['customer'])
def orders(request):
    context = {}
    return render(request, 'customer_orders.html', context)


def menu(request):
    menu = Menu.objects.all()
    context = {'menu': menu,
               }
    return render(request, 'menu.html', context)


def menu_items(request, id):
    item = Menu.objects.get(pk=id)
    return HttpResponse(item)


@login_required(login_url='restaurants:login')
@ensure_csrf_cookie
def cart(request):
    itemsList = request.COOKIES.get('itemsList', None)
    if itemsList is not None:
        total = calculatePrice(itemsList)
        items = cartItems(itemsList)  # {'count':, 'object':, 'subTotalPrice':}
        context = {'total': total,
                   'items': items}
        return render(request, 'cart.html', context)

    return render(request, 'cart.html',)


def cartJSON(request):
    itemsList = request.COOKIES['itemsList']
    x = cartItems(itemsList)
    context = {}
    return HttpResponse(x)


def test(request):
    x = Account.object.get(id=request.user.id)
    return HttpResponse(x)


@csrf_exempt
def complete(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        # create the order
        account = Account.object.get(id=request.user.id)
        itemsList = request.COOKIES.get('itemsList', None)
        total = calculatePrice(itemsList)
        Order.objects.create(customer=account,
                             order_content=itemsList,
                             total_price=total,
                             status='A',
                             payment_id='null',
                             payer_id=body['payerID'],
                             comment=''
                             )
        return JsonResponse(body)

    return HttpResponse('Forbidden')
