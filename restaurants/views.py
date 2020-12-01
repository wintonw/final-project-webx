from django.http import HttpResponse, JsonResponse
from django.http import response
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
from .util import calculatePrice, cartItems, ordersContent
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
            messages.info(request, 'Email or Password is INCORRECT')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('restaurants:login')


def menu(request):
    menu = Menu.objects.all()
    context = {'menu': menu,
               }
    return render(request, 'menu.html', context)


def menu_items(request, id):
    item = Menu.objects.get(pk=id)
    return HttpResponse(item)


@login_required(login_url='restaurants:login')
# @allowed_users(allowed_roles=['customer'])
def orders(request):
    # get all order by this customer
    account = Account.object.get(id=request.user.id)
    orderObjects = Order.objects.filter(customer=account).order_by('-time')

    ordersItems = ordersContent(orderObjects)
    print(ordersItems)
    # convert order_content to readable {'object':, cartItems}
    # => {'object':, {'count':, 'object':, 'subTotalPrice':}}

    context = {"orders": ordersItems,
               }
    return render(request, 'customer_orders.html', context)


@ensure_csrf_cookie
def cart(request):
    itemsList = request.COOKIES.get('itemsList', None)
    if itemsList is not None:
        total = calculatePrice(itemsList)
        items = cartItems(itemsList)  # {'count':, 'object':, 'subTotalPrice':}
        context = {'total': total,
                   'items': items}
        return render(request, 'cart.html', context)
        # check time, if close render CLOSED
    else:
        #
        nothing = True
        context = {'nothing': nothing, }
        return render(request, 'cart.html', context)


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
        # print(body)
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
                             comment='None'
                             )
        context = {'body': body}
        response = HttpResponse(context)
        response.delete_cookie('itemsList')
        return response

    return HttpResponse('Forbidden')


def ordersDetails(request, id):

    # if not logged in or , only show order detail
    if not request.user.is_authenticated:
        order = Order.objects.get(pk=id)
        context = {'order': order}
        return render(request, "order_less_details.html", context)
        # if logged it, more detail
    else:
        order = Order.objects.get(pk=id)
        if order.customer == request.user:

            items = cartItems(order.order_content)
            context = {'order': order,
                       'items': items}
            return render(request, "order_details.html", context)
        else:
            order = Order.objects.get(pk=id)
            context = {'order': order}
            return render(request, "order_less_details.html", context)
    # print(items)
    # return render(request, "order_details.html", context)


@login_required(login_url='restaurants:login')
@allowed_users(allowed_roles=['staff', 'manager'])
# @allowed_users(allowed_roles=['customer'])
def dashboard(request):
    # get all order by this customer
    if request.method == 'POST':
        updatedOrder = request.POST.get('orderID')
        newOrderStatus = request.POST.get('orderStatus')

        orderObjects = Order.objects.get(id=updatedOrder)
        orderObjects.status = newOrderStatus
        orderObjects.save()

    orderObjects = Order.objects.all().order_by('-time')
    ordersItems = ordersContent(orderObjects)
    # convert order_content to readable {'object':, cartItems}
    # => {'object':, {'count':, 'object':, 'subTotalPrice':}}

    context = {"orders": ordersItems,
               }
    return render(request, 'dashboard.html', context)
