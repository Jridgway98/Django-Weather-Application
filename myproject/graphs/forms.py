from django import forms
from data.models import *

class CityChoiceField(forms.Form):
	cities = forms.ModelChoiceField(
		queryset=City.objects.all().order_by('name'))
