from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
class User(AbstractBaseUser):
    email = models.EmailField(('email address'), unique=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.PositiveIntegerField(default=1)
    phone = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = ('users')




class Category(models.Model):

    name = models.CharField(max_length=120, db_index=True, unique=True)


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

