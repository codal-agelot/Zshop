from django.urls import path,include
from zshop import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('category', views.CatergoryViewSet,'category')
router.register('product', views.ProductViewSet, 'product')
router.register('userdetail',views.UserDetailsViewSet, 'userdetail')


urlpatterns = [

    path('', include(router.urls)),

]
