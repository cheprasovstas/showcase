from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from products.models import Product, Showcase, ShowcaseInfo
from products.serializers import ProductSerializer
from django.urls import reverse
from django_registration.backends.one_step.views import RegistrationView
from forms import ProductForm
from django.contrib import messages
from django.utils.translation import gettext as _


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


class ShowCaseView(ListView):

    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'showcase.html'

    def get_queryset(self):
        if 'user' in self.kwargs:
            return super(ShowCaseView, self).get_queryset().filter(owner__username=self.kwargs['user'],  active=True)
        return super(ShowCaseView, self).get_queryset().filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(ShowCaseView, self).get_context_data(**kwargs)
        showcase = Showcase.objects.filter(owner__username=self.kwargs['user']).first()
        context['showcase'] = showcase
#        showcaseinfo = ShowcaseInfo.objects.filter(showcase=showcase).order_by('order').all()
        showcaseinfo = ShowcaseInfo.objects.filter(owner__username=self.kwargs['user']).order_by('order').all()
        context['showcaseinfo'] = showcaseinfo
        return context


class ProductListView(ListView):

    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super(ProductListView, self).get_queryset().filter(owner=self.request.user,  active=True)
        return HttpResponseRedirect(reverse('login'))

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
#        showcase = Showcase.objects.filter(owner__username=self.kwargs['user']).first()
#        context['showcase'] = showcase
#        showcaseinfo = ShowcaseInfo.objects.filter(showcase=showcase).order_by('order').all()
#        showcaseinfo = ShowcaseInfo.objects.filter(owner__username=self.kwargs['user']).order_by('order').all()
#        context['showcaseinfo'] = showcaseinfo
        return context


class ProductDetailView(DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        product = super(ProductDetailView, self).get_object(*args, **kwargs)
        return product


class ProductEditView(FormView):

    form_class = ProductForm
    template_name = 'product_edit.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(ProductEditView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductEditView, self).get_context_data(**kwargs)
        # profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        # context['profile'] = profile
        return context

    # phone = PhoneNumberField(label='phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    # first_name = forms.CharField(label='First Name', required=False, max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}))
    # last_name = forms.CharField(label='Last Name', required=False, max_length=150, widget=forms.TextInput(attrs={'class': "form-control"}))

#    def get_initial(self):
#        initial = super(ProductEditView, self).get_initial()
#        if not self.request.user.is_authenticated:
#            raise PermissionDenied()
#        user = self.request.user
#        initial['phone'] = user.phone
#        initial['first_name'] = user.first_name
#        initial['last_name'] = user.last_name
#        return initial

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            raise PermissionDenied()
#        user = self.request.user
#        user.phone = form.cleaned_data['phone']
#        user.first_name = form.cleaned_data['first_name']
#        user.last_name = form.cleaned_data['last_name']
#        user.save()
        messages.add_message(self.request, messages.INFO, _("Product added"))
        return HttpResponseRedirect(reverse('products'))


# Сменить локализацию
def lang(request):
    return render(request, 'setlang.html')


class RegistrationViewCustom(RegistrationView):
    form_class = None
