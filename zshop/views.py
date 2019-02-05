from zshop import models
from zshop import serializers
from rest_framework import viewsets, filters


class CatergoryViewSet(viewsets.ModelViewSet):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'available')

class UserDetailsViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer

