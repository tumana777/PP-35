from django.urls import path
from api.views import (
    CategoryListAPIView, ProductListAPIView,
    ProductDetailAPIView, ProductCreateAPIView,
    ProductUpdateAPIView, ProductDeleteAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
)

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    # path('products/<int:product_pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    # path('products/', ProductListAPIView.as_view(), name='product_list'),
    # path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    # path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product_delete'),
    path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
]