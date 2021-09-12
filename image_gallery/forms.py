from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Image, Catagory
import datetime


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['catagory', 'description', 'price', 'photo']
        