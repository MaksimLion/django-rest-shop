from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as rest_filters 
from .models import Product, ProductCategory
from .pagination import ProductsResultSetPagination
from .serializers import ProductSerializer, ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsResultSetPagination
    
    filter_backends = (
        filters.SearchFilter, 
        rest_filters.DjangoFilterBackend
    )

    filterset_fields = (
        'category',
    )

    search_fields = (
        'title',
    )

    @action(detail=True, methods=['post'])
    def buy(self, request, *args, **kwargs):
        product = self.get_object()
        product.count -= 1
        if product.count == 0:
            product.in_stock = False

        product.save(update_fields=['count', 'in_stock'])
        return Response()


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
