from .models import Enter, Order
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Enter
        fields = ('id', 'name', 'qty', 'price', 'date', 'category', 'total_price', 'ndc_price', 'ndc')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'qty', 'total_price', 'price')