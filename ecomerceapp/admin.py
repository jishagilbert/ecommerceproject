from django.contrib import admin

from ecomerceapp.models import Category, Product, Cart,Favourite

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)