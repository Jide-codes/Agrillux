from django.contrib import admin
from .models import Product, Order, OrderItem, ShippingAddress,CustomerFeedBack

# Register your models here.
# admin.site.register(Customer)
admin.site.register(CustomerFeedBack)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)