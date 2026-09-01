from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.serializers import (
    CategoryListSerializer, ProductListSerializer,
    ProductDetailSerializer, ProductCreateSerializer,
    ProductUpdateSerializer
)
from django.db.models import Count

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from store.models import Product, Category


# @api_view(['GET'])
# def product_list(request):
#     all_products = Product.objects.values()
#     return Response(all_products)

# @api_view(['GET'])
# def category_list(request):
#     all_categories = Category.objects.annotate(product_count=Count('product'))
#     serializer = CategoryListSerializer(all_categories, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def product_list(request):
#     all_products = Product.objects.select_related('category')
#     serializer = ProductListSerializer(all_products, many=True, context={'request': request})
#     return Response(serializer.data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.annotate(product_count=Count('product'))
    serializer_class = CategoryListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductListSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_pk'

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductUpdateSerializer

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.select_related('category')













