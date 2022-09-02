from django.contrib import admin

#importing Product from model which is in current dir
from .models import Product

#Adding Product table in admin panel
# admin.site.register(Product)

#customize product table in admin panel
"""
- class name starts with table name and concatinate with Admin
- pass the model ModelAdmin from admin module

"""
class ProductAdmin(admin.ModelAdmin):
    #override the arrtibutes in ModelAdmin class
    list_display = ('name', 'price', 'stock')

#Register the Product table using new class ProductAdmin 
admin.site.register(Product, ProductAdmin)



