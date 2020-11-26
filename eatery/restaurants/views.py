from re import template
from django.http import request
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404, JsonResponse
import datetime
from time import gmtime, strftime
# Create your views here.


def index(request):
    return render(request, 'index.html')


class ContactMEView(TemplateView):
    template_name = 'contact.html'
