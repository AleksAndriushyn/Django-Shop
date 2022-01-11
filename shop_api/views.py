from rest_framework import generics
from orders.models import OrderItem, Order
from shop.models import Category, Product
from shop_api.serializers import OrderSerializer, OrderItemSerializer
from .serializers import ProductSerializer, CategorySerializer


class GetListAllProducts(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class PostProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class GetListAllCategories(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class PostCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class GetListAllOrders(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()


class PostOrder(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()


class GetListAllOrderItems(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.all()


class PostOrderItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.all()
