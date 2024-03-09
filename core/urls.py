from django.urls import path
from .views import Product, ProductDetail, OrderAPIView, OrderDetailAPIView
app_name = 'core'

urlpatterns = [
    path('api/', Product.as_view()),
    path('api/<uuid:id>/', ProductDetail.as_view()),
    path('order/api/', OrderAPIView.as_view(), name='orders'),
    path('order/api/<uuid:id>/', OrderDetailAPIView.as_view())
]