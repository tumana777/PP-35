from django.urls import path
from api.views import category_list, product_list

app_name = 'api'

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
]