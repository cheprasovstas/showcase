from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from products import views

api_router = routers.DefaultRouter()
api_router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('products/', views.index, name='index'),
    path('api/', include(api_router.urls)),
]






