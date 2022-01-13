from django.urls import path
from . import views # period dot means from current folder




# Endpoints options:
# /products ------------main starting page
# /products/1/detail
# /products/new

urlpatterns = [
    path("", views.index),        ## tells django that this is the root URL
    path("new", views.new) 
]