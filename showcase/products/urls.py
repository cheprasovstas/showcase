from django.urls import path
from django.conf.urls import include, url

from . import views
from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register(r'products', views.ProductsViewSet)

urlpatterns = [
    path('products/', views.index, name='index'),
    path('api/',include(api_router.urls)),
]






