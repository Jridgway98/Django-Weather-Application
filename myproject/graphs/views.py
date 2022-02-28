from django.shortcuts import render
from data.models import *
from .utils import *
from .forms import *
import random

def GraphView(request):
	return render(request, 'graphs.html')


def CityGraphView(request):
	#city1 = City.objects.all()
	city = City.objects.raw("SELECT * FROM Data_City WHERE (name='Bowling Green' AND state='KY')\
	 OR (name='Bowling Green' AND state='OH')\
	 OR (name='Chandler' AND state='AZ')\
	 OR (name='Albuquerque' AND state='NM')\
	 OR (name='Worcester' AND state='MA')")
	x = [x.name + ', ' + x.state for x in city]
	y = [y.SO2 for y in city]
	chart = get_plot(x, y)
	return render(request, 'citygraph.html', {'chart': chart})

def PollutantChartView(request):
	city = City.objects.raw("SELECT * FROM Data_City WHERE (name='Bowling Green' AND state='KY')")
	x = ['CO','SO2','PM10','NO2','O3_8','PM2.5',]
	y = [city[0].CO, city[0].SO2, city[0].PM10, city[0].NO2, city[0].O3_8, city[0].PM25]
	chart = get_pie_plot(x,y,city[0].name + ', ' + city[0].state)
	return render(request, 'pollutantchart.html', {'chart': chart})

def PM25HourlyChartView(request):
	city = City.objects.raw("SELECT * FROM Data_City WHERE (name='Bowling Green' AND state='KY')")
	yValue=city[0].PM25
	x = ['5 AM', '6 AM', '7 AM']
	y = [yValue, (yValue + random.randint(0, 20)), (yValue + random.randint(20, 40))]
	cityName = city[0].name + ', ' + city[0].state
	chart = get_hourly_PM25(x,y,cityName)
	return render(request, 'pm25hourlychart.html', {'chart': chart})
	
def PM25YearlyChartView(request):
	city = City.objects.raw("SELECT * FROM Data_City WHERE (name='Bowling Green' AND state='KY')")
	yValue=city[0].PM25
	y = [float(yValue), float(yValue + random.randint(0, 20)), float(yValue + random.randint(20, 40))]
	cityName = city[0].name + ', ' + city[0].state
	chart = get_yearly_PM25(y,cityName)
	return render(request, 'pm25yearlychart.html', {'chart': chart})

def HighestAmountsChartView(request):
	CO = City.objects.raw("SELECT id, MAX(CO) FROM Data_City")
	SO2 = City.objects.raw("SELECT id, MAX(SO2) FROM Data_City")
	PM10 = City.objects.raw("SELECT id, MAX(PM10) FROM Data_City")
	NO2 = City.objects.raw("SELECT id, MAX(NO2) FROM Data_City")
	O3_8 = City.objects.raw("SELECT id, MAX(O3_8) FROM Data_City")
	PM25 = City.objects.raw("SELECT id, MAX(PM25) FROM Data_City")
	x = ['CO', 'SO2', 'PM10', 'NO2', 'O3_8', 'PM2.5']
	y = [CO[0].CO, SO2[0].SO2, PM10[0].PM10, NO2[0].NO2, O3_8[0].O3_8, PM25[0].PM25]
	chart = get_max_plot(x,y)
	return render(request, 'highestamount.html', {'chart': chart})	

def VehicleChartView(request):
	vehicle = Vehicle.objects.raw("SELECT * FROM Data_Vehicle")
	x = [x.manufacturer + ' ' + x.name for x in vehicle]
	y = [y.PM25 for y in vehicle]
	chart = get_vehicle_plot(x,y)
	return render(request, 'vehiclechart.html', {'chart': chart})

def DirectionChartView(request):
	city = City.objects.raw("SELECT * FROM Data_City WHERE (name='Bowling Green' AND state='KY')")
	yValue = city[0].PM25
	cityName = city[0].name + ', ' + city[0].state
	x = ['N', 'E', 'S', 'W']
	y = [float(yValue), float(yValue + random.randint(0, 10)), float(yValue - random.randint(0, 5)), float(yValue + random.randint(0, 10))]
	chart = get_direction_plot(x,y,cityName)
	return render(request, 'directionchart.html', {'chart': chart})




