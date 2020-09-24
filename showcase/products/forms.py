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
