from .serializers import *
from rest_framework import viewsets
from .models import Cart
from rest_framework.permissions import IsAuthenticated

class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer
    queryset = Cart.objects.all()



# class CartPriceViewSet(viewsets.ModelViewSet):
#     model = Cart
#     serializer_class = CartPriceSerializer
#
#     def get_queryset(self,):
#         user = self.request.
#         return Cart.objects.filter(user=user)

    # def pre_save(self, obj):
    #     obj.user = self.request.user

# class OrderViewSet(viewsets.ModelViewSet):
#     model = Order
#     serializer_class = OrderSerializer
#
#     def get_queryset(self,):
#         return Order.objects.filter(cart_details__user = self.request.user).distinct()
#
#     def pre_save(self, obj):
#         obj.user = self.request.user
