from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.PositiveIntegerField(default=1)
    phone = models.CharField(max_length=10)




class Category(models.Model):

    name = models.CharField(max_length=120, db_index=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,null=True)
    stock = models.PositiveIntegerField(default=1)


    class Meta:
        ordering = ('name',)
        index_together = ('id',)

    def __str__(self):
        return self.name

