from zshop import models
from zshop import serializers
from rest_framework import viewsets, filters
from rest_framework import generics

class CatergoryViewSet(viewsets.ModelViewSet):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'available')


class CustomUserViewSet(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
