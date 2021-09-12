import django_filters
from django_filters import CharFilter

from django import forms

from .models import *

class CatagoryFilter(django_filters.FilterSet):
	catagory = django_filters.ModelMultipleChoiceFilter(queryset=Catagory.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Catagory
		fields = ['catagory']