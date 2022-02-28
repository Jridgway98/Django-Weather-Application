from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import City, Vehicle, Powerplant
from .filters import CityFilter

class CityList(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'cities.html'

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context['filter'] = CityFilter(self.request.GET, queryset=self.get_queryset())
    	return context

def city_vehicle(request, pk):
	city = get_object_or_404(City, pk=pk)
	vehicles = city.vehicles.order_by('time_created')
	return render(request, 'city_vehicle.html', {'city': city, 'vehicles': vehicles})

class VehicleList(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'vehicles.html'

def get_queryset(self):
	queryset = super().get_queryset()
	return queryset.filter(created_by=self.request.user)

class PowerplantList(ListView):
    model = Powerplant
    context_object_name = 'powerplants'
    template_name = 'powerplants.html'

def get_queryset(self):
	queryset = super().get_queryset()
	return queryset.filter(created_by=self.request.user)