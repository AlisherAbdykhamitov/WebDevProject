from rest_framework import serializers

from api.models import Category, Product

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProductsOfCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    category_id=serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(many = False,read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category_id')



class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'products')
