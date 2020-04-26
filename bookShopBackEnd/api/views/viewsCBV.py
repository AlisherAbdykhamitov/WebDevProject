from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView


from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer, ProductsOfCategorySerializer, \
    CategoryWithProductsSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, )

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request,product_id):
        product =self.get_object(product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product =self.get_object(product_id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, product_id):
        product =self.get_object(product_id)
        product.delete()
        return Response({'deleted': True})


class CategoryProducts(APIView):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        serializer = CategoryWithProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryWithProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDetailAPIView(APIView):
    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, category_id):
        category =self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category =self.get_object(category_id)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})


    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()

        return Response({'deleted': True})