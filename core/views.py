from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer, OrderSerializer, WorkerProductSerializer
from core.models import Enter, Order, WorkerProduct


class Product(APIView):
    def get(self, request):
        product = Enter.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get(self, request, id,  *args, **kwargs):
        product = get_object_or_404(Enter, id=id)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, reqeust, id, *args, **kwargs):
        product = get_object_or_404(Enter, id=id)
        serializer = ProductSerializer(instance=product, data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            product = get_object_or_404(Enter, id=id)
        except:
            return Response(data={'errors': 'Product not found'})
        else:
            product.delete()
            return Response(data={'message': 'Product successfully deleted'})


class OrderAPIView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            order = get_object_or_404(Order, id=id)
        except:
            return Response(data={'error': 'Order Not Fount'})

        else:
            order.delete()
            return Response(data={'success': 'Order successfully deleted'})


class WorkerProductAPIView(APIView):
    def get(self, request):
        order = WorkerProduct.objects.all()
        serializer = WorkerProductSerializer(order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WorkerProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerProductDetailAPIView(APIView):
    def get(self, request, id):
        order = get_object_or_404(WorkerProduct, id=id)
        serializer = WorkerProductSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        order = get_object_or_404(WorkerProduct, id=id)
        serializer = WorkerProductSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            order = get_object_or_404(WorkerProduct, id=id)
        except:
            return Response(data={'error': 'Order Not Fount'})

        else:
            order.delete()
            return Response(data={'success': 'Order successfully deleted'})