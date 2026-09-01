from rest_framework import serializers
from store.models import Product, Category


# class CategoryListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     saxeli = serializers.CharField(source='name')
#     product_count = serializers.IntegerField()
#
# class ProductListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     quantity = serializers.IntegerField()
#     description = serializers.CharField()
#     category = serializers.CharField()
#     is_available = serializers.BooleanField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     image = serializers.ImageField()

class CategoryListSerializer(serializers.ModelSerializer):
    saxeli = serializers.CharField(source='name')
    # product_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ["id", "saxeli"]

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_total_price(self, obj):
        return obj.price * obj.quantity

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['is_available']

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'