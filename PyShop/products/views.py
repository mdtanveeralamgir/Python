from django.shortcuts import render
from django.http import HttpResponse


#all function needs to have http request parameter

# /products -> index
def index(request):
    return HttpResponse("Hello world")

def new(request):
    return HttpResponse("New product")

