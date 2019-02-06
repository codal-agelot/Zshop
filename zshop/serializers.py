from zshop import models
from rest_framework import serializers





class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id','name')


class ProductSerializer(serializers.ModelSerializer):



    class Meta:
        model = models.Product
        fields = ('category','name', 'price',
                  'description','stock')


#
# class UserDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.User
#         fields = ('first_name','last_name',
#                   'street_address','phone',
#                   'city','state','zip')