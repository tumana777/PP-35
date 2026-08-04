from django.urls import path
# from .views import index, about, products, product_detail, add_product, update_product, delete_product
from .views import IndexView, AboutView, ProductsListView, ProductDetailView, \
      ProductCreateView, ProductUpdateView, ProductDeleteView, TechProductsView


app_name = 'store'

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    # path('about/', about, name='about'),
    path('about/', AboutView.as_view(), name='about'),
    # path('products/', products, name='products'),
    path('products/', ProductsListView.as_view(), name='products'),
    # path('products/<int:product_pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('add_product/', add_product, name='add_product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    # path('update_product/<int:product_pk>/', update_product, name='update_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    # path('delete_product/<int:product_pk>/', delete_product, name='delete_product'),
    path('delete_product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('tech_products/', TechProductsView.as_view(), name='tech_products')
]