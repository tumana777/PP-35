from django.urls import path
from .views import index, about, products, product_detail, add_product, update_product, delete_product

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('products/<int:product_pk>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_pk>/', update_product, name='update_product'),
    path('delete_product/<int:product_pk>/', delete_product, name='delete_product'),
]