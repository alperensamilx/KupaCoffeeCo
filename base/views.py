from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


products = [
    {'id': 1, 'name': 'Drinks'},
    {'id': 2, 'name': 'Food'},
    {'id': 3, 'name': 'At Home Coffee'},
    {'id': 4, 'name': 'Merchandise'},

]


def home(request):
    context = {'products': products}
    return render(request, 'home.html', context)


def menu(request):
    return render(request, 'menu.html')


