from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from products import views

api_router = routers.DefaultRouter()
api_router.register(r'products', views.ProductViewSet)

urlpatterns = [

    path('', views.index, name='home'),
    path('showcase/<str:user>', views.ProductListView.as_view(), name='showcase'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<pk>/', views.ProductDetailView.as_view(), name='product'),

    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/', include(api_router.urls)),

    url('', include('social_django.urls', namespace='social')),

]






