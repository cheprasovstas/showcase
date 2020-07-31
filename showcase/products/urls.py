from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from products import views

api_router = routers.DefaultRouter()
api_router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<pk>/', views.ProductDetailView.as_view(), name='product'),

    path('api/', include(api_router.urls)),
]






