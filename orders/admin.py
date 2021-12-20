from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid']
    list_filter = ['created', 'paid']
    list_editable = ['paid']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity']
    list_filter = ['quantity']
    list_editable = ['price', 'quantity']