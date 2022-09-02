from django.db import models


class Product(models.Model): #inherit Model from models
    name = models.CharField(max_length=255)
    price = models.FlotField()
    stock = models.integerField()
    image_url = models.CharField(max_length=2083)

