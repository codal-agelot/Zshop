from django.db import models
from zshop.models import User
from django.db.models import Sum

from zshop.models import Product



class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item  = models.ManyToManyField(Product, through='Through_table')
    quantity = models.IntegerField(default=1)



class Through_table(models.Model):
    cart  = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)



class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.Model)
    price = models.PositiveIntegerField()

