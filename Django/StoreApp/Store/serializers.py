from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'is_active', 'created_at', 'updated_at']

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField()
    class Meta:
        model = Order
        fields = ['order_id','user', 'status', 'created_at', 'updated_at']
    