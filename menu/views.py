from django.shortcuts import render

# Create your views here.

menu = ['Drinks', 'Food', 'At Home Coffee', 'Merchandise']
def index(request, context):
    return render(request, 'menu/index.html')