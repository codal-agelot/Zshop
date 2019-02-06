from django.db import models



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
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,null=True)
    stock = models.PositiveIntegerField(default=1)


    class Meta:
        ordering = ('name',)
        index_together = ('id',)

    def __str__(self):
        return self.name


