from django.shortcuts import render

# Create your views here.
import stripe
from .models import Restaurant, Menu, MenuItem
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer,OrderSerializer, OrderItemSerializer
from .permissions import IsOwnerGroup,IsEmployeeGroup
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,generics, permissions
from .models import Order, OrderItem,MenuItem


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

class PaymentProcessView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerGroup]

    def post(self, request, *args, **kwargs):
        try:
            order_id = request.data.get('order_id')
            order = Order.objects.get(id=order_id, user=request.user, payment_status=False)
        except Order.DoesNotExist:
            return Response({'error': 'Invalid order ID or payment already processed.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a payment intent using Stripe
        intent = stripe.PaymentIntent.create(
            amount=int(order.total_price * 100),  # Amount in cents
            currency='usd',
        )

        return Response({'client_secret': intent.client_secret})
    

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        # Extract menu item data from request and create order items
        order_items_data = self.request.data.get('items', [])
        order_items = []
        for item_data in order_items_data:
            menu_item_id = item_data.get('menu_item')
            quantity = item_data.get('quantity', 1)
            menu_item = MenuItem.objects.get(id=menu_item_id)
            order_items.append(OrderItem(menu_item=menu_item, quantity=quantity, price=menu_item.price))

        # Save the order and related order items
        serializer.save(user=self.request.user, items=order_items)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        # Extract menu item data from request and create order items
        order_items_data = self.request.data.get('items', [])
        order_items = []
        for item_data in order_items_data:
            menu_item_id = item_data.get('menu_item')
            quantity = item_data.get('quantity', 1)
            menu_item = MenuItem.objects.get(id=menu_item_id)
            order_items.append(OrderItem(menu_item=menu_item, quantity=quantity, price=menu_item.price))

        # Save the order and related order items
        serializer.save(user=self.request.user, items=order_items)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployeeGroup]

    def perform_create(self, serializer):
        # Extract menu item data from request and create order items
        order_items_data = self.request.data.get('items', [])
        order_items = []
        for item_data in order_items_data:
            menu_item_id = item_data.get('menu_item')
            quantity = item_data.get('quantity', 1)
            menu_item = MenuItem.objects.get(id=menu_item_id)
            order_items.append(OrderItem(menu_item=menu_item, quantity=quantity, price=menu_item.price))

        # Save the order and related order items
        serializer.save(user=self.request.user, items=order_items)