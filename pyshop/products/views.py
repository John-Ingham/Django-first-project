from django.http import HttpResponse    
from django.shortcuts import render
from . models import Product ## from current folder get Product class

# Create your views here.

# by default call the main page index (index.html will be linked to it)

#URL = uniform resource locator (address)
# # Need to tell Django that the URL ending /products is our index

def index(request):
    products = Product.objects.all() ## Gets all products from database, saves as a variable
    ##other useful methods .get to get one record, .filter to filter results
    ##return HttpResponse("Hello World! Products Page")
    
    return render(request, "index.html", {"products" : products})


def new(request):
    return HttpResponse("New Products")

