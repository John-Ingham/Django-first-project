from django.contrib import admin
from .models import Product  ## import my produt class
# Register your models here. These will be added to the admin superuser


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")



admin.site.register(Product, ProductAdmin) ## This will register the products app to the admin section of the webpage