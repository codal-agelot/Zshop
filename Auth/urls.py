from django.urls import include, path
from rest_framework import routers
from . import views

#
# router = routers.DefaultRouter()
# router.register('Users', views.UsersViewSet,'user')


urlpatterns = [
    path('users/', views.UsersViewSet),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]