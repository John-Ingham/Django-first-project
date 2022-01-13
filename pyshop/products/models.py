from django.db import models  ## imports the models class information

# Create your models here.

class Product(models.Model):   # create a model class - inherits characteristics from imported
    name = models.CharField(max_length = 255)       ##characters  - limit prevents malicious inputs
    price = models.FloatField()                     ## floating num
    stock = models.IntegerField()                   ## whole num integer
    image_url = models.CharField(max_length = 2083) ## avg std max length of an URL


class Offer(models.Model):
    code = models.CharField(max_length = 8)          ## up to 8 character discount code
    description = models.CharField(max_length = 200) ## 200 char limit to describe discount - e.g. "20% off all products in this range"
    discount = models.FloatField()                   ## float used for a decimal discount to apply


class Simple_product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    stock= models.IntegerField()
## no image
