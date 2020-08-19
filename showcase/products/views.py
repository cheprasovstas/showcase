from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#    def get_queryset(self):
#        event_id = self.kwargs['event_id']
#        return self.queryset.filter(event_id=event_id)

#    def perform_create(self, serializer):
#        event_id = self.kwargs['event_id']
#        serializer.save(event_id=event_id)

class ProductListView(ListView):

    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        queryset = queryset.filter(active=True)
        return queryset

class ProductDetailView(DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        product = super(ProductDetailView, self).get_object(*args, **kwargs)
        return product