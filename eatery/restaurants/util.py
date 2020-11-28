from .models import Menu, Order
import json
from decimal import *
# query itemsList


# take in query to calculate price
def calculatePrice(itemsListStr):
    itemsList = json.loads(itemsListStr)
    total = 0
    for i in itemsList:
        total += Menu.objects.get(pk=i['itemID']).price*Decimal(i['count'])

    return total
