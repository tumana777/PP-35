from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.serializers import CategoryListSerializer, ProductListSerializer
from django.db.models import Count

from store.models import Product, Category


# @api_view(['GET'])
# def product_list(request):
#     all_products = Product.objects.values()
#     return Response(all_products)

@api_view(['GET'])
def category_list(request):
    all_categories = Category.objects.annotate(product_count=Count('product'))
    serializer = CategoryListSerializer(all_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    all_products = Product.objects.select_related('category')
    serializer = ProductListSerializer(all_products, many=True, context={'request': request})
    return Response(serializer.data)