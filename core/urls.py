from django.urls import path
from .views import Product, ProductDetail, OrderAPIView, OrderDetailAPIView, \
    WorkerProductAPIView, WorkerProductDetailAPIView, Order_to_SendAPIView, Order_to_SendDetailAPIView
app_name = 'core'

urlpatterns = [
    path('api/', Product.as_view()),
    path('api/<uuid:id>/', ProductDetail.as_view()),
    path('order/api/', OrderAPIView.as_view()),
    path('order/api/<uuid:id>/', OrderDetailAPIView.as_view()),
    path('worker-product/api/', WorkerProductAPIView.as_view()),
    path('worker-product/api/<uuid:id>/', WorkerProductDetailAPIView.as_view()),
    path('order-to-send/api/', Order_to_SendAPIView.as_view()),
    path('order-to-send/api/<uuid:id>/', Order_to_SendDetailAPIView.as_view()),

]
