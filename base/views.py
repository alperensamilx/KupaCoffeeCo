from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# menus = [
#     {'id': 1, 'name': 'Drinks'},
#     {'id': 2, 'name': 'Food'},
#     {'id': 3, 'name': 'At Home Coffee'},
#     {'id': 4, 'name': 'Merchandise'},
# ]

def home(request):
    menus = Categories.objects.all()
    context = {'menus': menus}
    return render(request, 'base/home.html', context)


def menu(request, pk ):
    menu = Categories.objects.get(id=pk)
    context = {'menu': menu}

    return render(request, 'base/menu.html', context)


