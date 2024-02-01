from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('employee', 'Employee'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    cusr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_restaurants')
    name = models.CharField(max_length=255)
    # Add other fields

class Menu(models.Model):
    cusr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_menus')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=255)
    # Add other fields

class MenuItem(models.Model):
    cusr = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields

class Order(models.Model):
    cuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    payment_status = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])