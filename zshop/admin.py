from django.contrib import admin
from .models import  *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','description','stock']
    list_filter = ['category']
    list_editable = ['price','stock']

admin.site.register(Product, ProductAdmin)



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'name']

admin.site.register(CustomUser, CustomUserAdmin)


