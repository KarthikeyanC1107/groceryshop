from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'items', 'payment_method', 'pickup_time', 'timestamp')
    search_fields = ('name', 'phone', 'items')
