from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django_registration.forms import RegistrationForm

User = get_user_model()

class RegistrationFormCustom(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        self.fields[email_field].required = False


class ProductForm(forms.Form):

    name = forms.CharField(label='name',  required=True, max_length=100, widget=forms.TextInput(attrs={'class': "form-control input_form", 'placeholder': "phone"}))
    description = forms.CharField(label='description', required=False, max_length=2000, widget=forms.Textarea(attrs={'class': "form-control input_form", 'placeholder': ""}))
    price = forms.DecimalField(label='price', required=False, max_digits=5, decimal_places=2, widget=forms.TextInput(attrs={'class': "form-control input_form", 'placeholder': "phone"}))
    unit_price = forms.CharField(label='unit price', required=False, max_length=20, widget=forms.TextInput(attrs={'class': "form-control input_form", 'placeholder': "phone"}))
    active = forms.BooleanField(label='active', initial=True, widget=forms.CheckboxInput())
    image = forms.ImageField(label='image', required=False)


