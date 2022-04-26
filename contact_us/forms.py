from django import forms
from . import models

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUsInfo
        fields = ('email', 'fullname', 'query')