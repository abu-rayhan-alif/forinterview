from django.contrib import admin
from .models import CustomUser,Restaurant,Menu,MenuItem,Order,OrderItem

# Register your models here.
@admin.register(CustomUser)
class CustomUserADmin(admin.ModelAdmin):
    list_display=[
        'role'
    ]
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=[
        
        'name',
    ]
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=[
        
        'name',
        'restaurant',
    ]
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=[
    
    'menu',
    'name',
    'price',
    ]
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    'items',
    'total_price',
    'payment_status',
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=[
    'order',
    'menu_item', 
    'quantity',
    'price',
    ]