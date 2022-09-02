from django.contrib import admin

#importing Product from model which is in current dir
from .models import Product


#Adding Product table in admin panel
admin.site.register(Product)
