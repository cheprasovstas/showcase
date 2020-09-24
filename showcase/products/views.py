from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Product
from products.serializers import ProductSerializer
from django.urls import reverse
from django_registration.backends.one_step.views import RegistrationView


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('showcase', kwargs={'user': request.user.username}))
    else:
        return HttpResponseRedirect(reverse('login'))


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
        if 'user' in self.kwargs:
            return super(ProductListView, self).get_queryset().filter(owner__username=self.kwargs['user'],  active=True)
        return super(ProductListView, self).get_queryset().filter(active=True)


class ProductDetailView(DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        product = super(ProductDetailView, self).get_object(*args, **kwargs)
        return product


# Сменить локализацию
def lang(request):
    return render(request, 'setlang.html')


class RegistrationViewCustom(RegistrationView):
    form_class = None
