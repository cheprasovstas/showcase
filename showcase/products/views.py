from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return self.queryset.filter(event_id=event_id)

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        serializer.save(event_id=event_id)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
