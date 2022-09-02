from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


#all function needs to have http request parameter

# /products -> index
def index(request):
    products = Product.objects.all() 
    return render(request, 'index.html')

def new(request):
    return HttpResponse("New product")

