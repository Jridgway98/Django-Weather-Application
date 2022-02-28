import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek(0)
	image_png = buffer.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffer.close()
	return graph


def get_plot(x,y):
	plt.switch_backend('Agg')
	plt.title('Levels of CO2')
	plt.bar(x, y, color='blue', width=0.45)
	plt.xticks(rotation=10)
	plt.xlabel('City')
	plt.ylabel('CO2')
	graph = get_graph()
	return graph

def get_pie_plot(x,y,cityName):
	plt.switch_backend('Agg')
	plt.title('Concentration of Pollutants in ' + cityName)
	plt.pie(y, labels=x)
	graph = get_graph()
	return graph

def get_hourly_PM25(x,y,cityName):
	plt.switch_backend('Agg')
	plt.title('Hourly Concentration of PM2.5 in ' + cityName)
	plt.plot(x,y)
	plt.xlabel('Hour')
	plt.ylabel('PM2.5')
	graph = get_graph()
	return graph

def get_yearly_PM25(y,cityName):
	plt.switch_backend('Agg')
	plt.title('Yearly Concentration of PM2.5 in ' + cityName)
	plt.boxplot(y)
	plt.xlabel('Year')
	plt.ylabel('PM2.5')
	graph = get_graph()
	return graph

def get_max_plot(x,y):
	plt.switch_backend('Agg')
	plt.title('Max Pollutants')
	plt.bar(x, y, color='blue', width=0.45)
	plt.xlabel('Pollutant')
	plt.ylabel('Amount')
	graph = get_graph()
	return graph

def get_vehicle_plot(x,y):
	plt.switch_backend('Agg')
	plt.title('PM2.5 in Vehicles')
	plt.bar(x, y, color='blue', width=0.45)
	plt.xlabel('Vehicle')
	plt.ylabel('PM2.5')
	graph = get_graph()
	return graph

def get_direction_plot(x,y,cityName):
	plt.switch_backend('Agg')
	plt.title('PM2.5 by Wind Direction')
	plt.bar(x, y, color='blue', width=0.45)
	plt.xlabel('Wind Direction in ' + cityName)
	plt.ylabel('PM2.5')
	graph = get_graph()
	return graph

