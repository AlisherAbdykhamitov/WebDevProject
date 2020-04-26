from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import path

from api.views.views import сategory_list
from api.views.viewsCBV import ProductListAPIView, ProductDetailAPIView, CategoryProducts, CategoryList, \
    CategoryDetailAPIView, ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    path ('categories/', CategoryList.as_view()),
    path ('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path ('products', ProductList.as_view()),
    path ('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('categories/<int:category_id>/products/', CategoryProducts.as_view()),
]