from .models import Menu, Order
import json
from decimal import *
# query itemsList


# take in query to calculate price
def calculatePrice(itemsListStr):
    total = Decimal(0.00)
    if (itemsListStr == None):
        return total

    itemsList = json.loads(itemsListStr)
    for i in itemsList:
        total += Menu.objects.get(pk=i['itemID']).price*Decimal(i['count'])

    return total


def subTotalPrice(count, itemPrice):
    return Decimal(count)*itemPrice


def cartItems(itemsListStr):
    # {'count':, 'object':, 'subTotalPrice':}
    itemsList = json.loads(itemsListStr)
    cart = []
    for i in itemsList:
        item = Menu.objects.get(pk=i['itemID'])
        cart.append({'count': i['count'], 'object': item,
                     'subTotalPrice': subTotalPrice(i['count'], item.price)})
    return cart


def ordersContent(orderObjects):
    # {'object':, cartItems}
    orders = []
    for order in orderObjects:
        itemsList = cartItems(order.order_content)
        orders.append({'object': order,
                       'cartItems': itemsList})
    return orders
