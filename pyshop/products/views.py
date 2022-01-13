from django.http import HttpResponse    
from django.shortcuts import render

# Create your views here.

# by default call the main page index

#URL = uniform resource locator (address)
# # Need to tell Django that the URL ending /products is our index

def index(request):
    return HttpResponse("Hello World!")


def new(request):
    return HttpResponse("New Products")

