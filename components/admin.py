from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'state',
    )
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'selling_price',
        'discount_price',
        'brand',
        'category',
        'product_image'
    )
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'quantity',
    )
admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'quantity',
        'status',
    )
admin.site.register(OrderPlaced, OrderAdmin)