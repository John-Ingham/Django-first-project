from django.contrib import admin
from . models import Product, Simple_product, Offer  ## import my product class

# Register your models here. These will be added to the admin superuser
# Models made here will then be accessible in the UI admin secton


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class Simple_ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "discount")

## The below lines denote how the items show and columns in the admin view table
admin.site.register(Simple_product, Simple_ProductAdmin)
admin.site.register(Product, ProductAdmin) ## This will register the products app to the admin section of the webpage
admin.site.register(Offer, OfferAdmin)