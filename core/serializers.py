from .models import Enter, Order, WorkerProduct
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Enter
        fields = ('id', 'name', 'qty', 'price', 'total_price', 'ndc_price', 'ndc', 'created_at')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'qty', 'total_price', 'price', 'created_at')


class WorkerProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = WorkerProduct
        fields = ('id', 'worker', 'product', 'qty', 'total', 'created_at')
