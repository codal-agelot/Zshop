from rest_framework import serializers
from .models import Cart,Order



class CartSerializer(serializers.ModelSerializer):

    totalprice = serializers.ReadOnlyField(source='total_price')
    price  = serializers.ReadOnlyField(source='pricee')


    class Meta:
        model = Cart
        fields = ( 'user', 'item','quantity','price','totalprice')

    def create(self, validated_data):
        guest, created = Cart.objects.get_or_create(
            user = validated_data['user'],
            item = validated_data['item'],
        )
        guest.quantity += validated_data.get('quantity')

        guest.save()
        return guest

class OrderSerializer(serializers.ModelSerializer):

    # productname = serializers.ReadOnlyField(source='product_name')
    # totalPrice = serializers.ReadOnlyField(source='total_cart_price')
    # final_cost = serializers.ReadOnlyField(source='total_cart_prize')

    class Meta:
        model = Order
        fields = ['id','cart_details','totalPrice']
        # depth = 1

    def create(self, validated_data):
        order_object,created = Order.objects.get_or_create(
            # id = validated_data['id']
            cart_details = validated_data
        )
        order_object.save()
        return order_object


    # def update(self, instance,validated_data):
    #     # id = Order.objects.get(id = validated_data['id'])
    #
    #     # if Order.objects.filter(id = id).exists():
    #     order_object = Order.objects.get_or_create(
    #             id = validated_data['id']
    #         )
    #
    #     instance.id = order_object
    #
    #     return instance

