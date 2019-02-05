from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from zshop.models import Product



class Cart(models.Model):

    user = models.ForeignKey(User, related_name="carts",on_delete=models.CASCADE)
    item  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    @property
    def total_price(self):
        product_price = self.item.price * self.quantity
        return product_price


    def pricee(self):
        price = self.item.price
        return price


class Order(models.Model):

    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cart_details = models.ManyToManyField(Cart)

    @property
    def total_cart_price(self):
        total_price = Cart.item.objects.aggregate(Sum('price')).get('price__sum')
        total_quantity = Cart.objects.aggregate(Sum('quantity')).get('quantity__sum')

        total_price  = total_price*total_quantity

        return total_price