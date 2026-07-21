from django.urls import path
from .views import index, about, products, product_detail

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('products/<int:product_pk>/', product_detail, name='product_detail'),
]