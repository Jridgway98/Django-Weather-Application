import django_filters
from .models import City

class CityFilter(django_filters.FilterSet):

	class Meta:
		model = City
		fields = ('name', 'state', )