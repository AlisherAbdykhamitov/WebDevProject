from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def сategory_list(request):
    if request.method =='GET':
        categories= Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def company_vacancies(request, category_id):
    try:
        products = Product.objects.filter(category_id=category_id)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        products.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def vacancy_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, category_id):
    try:
      category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})
        # raise Http404
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})