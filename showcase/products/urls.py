from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from products import views
from products import forms

api_router = routers.DefaultRouter()
api_router.register(r'products', views.ProductViewSet)

urlpatterns = [

    path('', views.index, name='home'),
    path('showcase/<str:user>', views.ProductListView.as_view(), name='showcase'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<pk>/', views.ProductDetailView.as_view(), name='product'),

    path('accounts/register/',
         views.RegistrationView.as_view(success_url='/', form_class=forms.RegistrationFormCustom),
         name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('setlang/', views.lang, name='setlang'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    path('api/', include(api_router.urls)),

    url('', include('social_django.urls', namespace='social')),

]
