from django.urls import path,include
from cart import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cart', views.CartViewSet, base_name='cart')
# router.register('order', views.OrderViewSet, base_name='order')



urlpatterns = [

    path('', include(router.urls)),
]
