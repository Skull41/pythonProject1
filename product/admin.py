from django.contrib import admin
from .models import Product,Offer,Order,OrderItem,Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','date_orderd', 'complete')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','order','date_added')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')



admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Offer, OfferAdmin)

