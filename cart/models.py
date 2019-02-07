from django.db import models
from django.contrib.auth.models import User


from zshop.models import Product



class Cart(models.Model):
    item  = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        permissions = (

        )
    @property

    def totalCost(self,):
        price = Product.objects.values_list('price').filter(name = self.item.name)
        price = [int(i[0]) for i in price]
        price = price[0]
        quantity = self.quantity
        totalcost = price * quantity

        return totalcost






class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    @property

    def cost(self):
