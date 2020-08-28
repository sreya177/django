from django import forms
from .models import Contact
from django.forms import ModelForm


class AddForm(ModelForm):
   class Meta:
      model = Contact
      fields = ('name', 'relation', 'phone', 'email',)
